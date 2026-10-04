---
title: "Installing Gollum with SSL authentication and Disqus comments on Ubuntu"
slug: "gollum-wiki-installation"
date: 2017-10-15T06:51:00.000Z
description: "A guide to install and self-host Gollum, the wiki engine that powers GitHub's and GitLab's wikis."
tags: ["open-source", "gollum"]
images: ["/content/images/2021/06/ilya-pavlov-87438-cropped.jpg"]
---

> ⚠️ This article is several years old by now. If you're planning to self-host a wiki, you might want to look at more modern, containerized, and better maintained alternatives than Gollum.

[Gollum](https://github.com/gollum/gollum) is a simple wiki that uses git for revision control and markdown syntax for editing. It is also the engine that powers Github's and GitLab's wikis. It can be easily set up for either a collaborative or personal wiki.

After following this guide you will be able to get Gollum running on an Ubuntu or Debian server with secure OAuth authentication and a commenting system with Disqus.

> 💡 You can also run this setup for a personal wiki on your laptop or desktop instead of a server on the net, in which case you might want to skip the *Omnigollum* and *Disqus* sections. To make it even simpler, you can also skip the *Nginx* configuration section.

## Installing Gollum

We're assuming an Ubuntu 16.04 or later system. Debian should work too.\
We're not installing from source, but rather via Ruby gems

``` sh
sudo apt install ruby ruby-dev make zlib1g-dev libicu-dev build-essential git
sudo gem install gollum
```

## Updating Gollum

When a new version of gollum is released, you can easily upgrade your installation with the `gem` command:

``` sh
sudo gem update gollum
sudo gem update gollum-lib
```

ℹ️ Other useful commands are `gem list` and `gem outdated`, to list installed and outdated gems, respectively.

ℹ️ See the [Troubleshooting section](#troubleshooting) if you've got issues upgrading on your VPS provider.

## Basic setup

After the initial installation, Gollum requires a git repository to be pointed at to work. We'll create that and add a dedicated user to access that repository.

### Setting up the repository

``` sh
# Add the 'gollum' user to the system
sudo adduser --shell /bin/bash --gecos 'Gollum application' gollum

# Switch user in the shell to gollum
sudo su - gollum

# You can optionally set your personal name and e-mail to
# assign all commits to yourself. Particularly useful if you
# need to do manual commits as 'gollum' to revert pages,
# which cannot be done in the UI
git config --global user.name "David Planella"
git config --global user.email "david.planella@example.com"

# Create a folder to contain the repository to be used for the wiki
# This will be at /home/gollum/wiki
mkdir wiki
cd wiki
git init .
exit
```

### Configuring Gollum

You can pass a set of command line parameters to Gollum whenever you start it to modify and adapt its behaviour to your needs. You can also define these parameters in a configuration file that Gollum reads, to the same result.

I prefer the second approach, as it's self-documenting and it allows you to keep the configuration file under source control. The file itself is called `config.rb` by convention, and it's a regular Ruby source file. The Ruby configuration variables you can specify as Gollum parameters map one to one with the startup command line parameters.

Let's start by creating the file and putting it in a standard location:

``` sh
sudo mkdir -p /usr/local/etc/gollum
sudo vim /usr/local/etc/gollum/config.rb
```

File contents:

``` ruby
# Define the wiki options
wiki_options = {
  :h1_title => true,
  :user_icons => 'gravatar',
  :live_preview => false,
  :allow_uploads => true,
  :per_page_uploads => true,
  :allow_editing => true,
  :css => false,
  :js => false,
  :mathjax => true,
  :emoji => true,
  :show_all => true
}

# Send the wiki options to the Gollum app
Precious::App.set(:wiki_options, wiki_options)
```

As you can see, all we're doing is to assigning the values of the configuration parameters to variables in Ruby syntax, and then passing the array where they are stored to the Gollum app programmatically.

In the next section, we'll be telling the system how to start gollum and pass it the location of our `config.rb` file.

ℹ️ While there isn't a canonical list of configuration variables, you can infer their names and what they do from the [Gollum configuration parameters list](https://github.com/gollum/gollum#configuration).

ℹ️ Another reason for using a configuration file is so that you can [modify the supported markdown formats and extenstions](https://github.com/gollum/gollum/wiki/Formats-and-extensions). As a brief example, you can limit the list of supported syntax flavors on the editor to only Markdown:

``` ruby
# If present, undefine the :FORMAT_NAMES constant to avoid the 
# "already initialized constant FORMAT_NAMES" warning
Gollum::Page.send :remove_const, :FORMAT_NAMES if defined? Gollum::Page::FORMAT_NAMES
# Redefine the :FORMAT_NAMES constant to limit the available
# formats on the editor to only markdown
Gollum::Page::FORMAT_NAMES = { :markdown  => "Markdown" }
```

### Starting Gollum

We'll be setting up Gollum to start as a service when the server starts, using [systemd](https://en.wikipedia.org/wiki/Systemd). This will allow us to control its start/stop/restart actions when we need to shut it down (e.g. on upgrades).

``` sh
sudo vim /lib/systemd/system/gollum.service
```

File contents:

``` ini
[Unit]
Description=Gollum wiki server
After=network.target

[Service]
Type=simple
User=gollum
Group=gollum
WorkingDirectory=/home/gollum/wiki
ExecStart=/usr/local/bin/gollum --config "/usr/local/etc/gollum/config.rb" --host localhost
Restart=on-abort

[Install]
WantedBy=multi-user.target
```

ℹ️ Note that we're passing the path to the configuration file (`config.rb`) upon launch. All required configuration parameters are then contained in that file.

ℹ️ Note we also do not need to pass the path to the git repository being served. If not specified, gollum defaults to using the `WorkingDirectory` we've defined on the `gollum.service` file.

ℹ️ Note that we're passing the `--host` parameter for Gollum to accept connections from the same host (`localhost`). By default Gollum listens to connections from every available network interface (`0.0.0.0`).

### Exposing Gollum

Next we want to expose Gollum to the web. This describes a basic web server set up to give you some guidance and get you up and running. For critical sites, you'll probably want to have a more robust and scalable setup, which is outside the scope of this guide.

Essentially, we'll be configuring a web server that acts as a front-end and more efficiently deals with client requests than the Gollum app's web server ([WEBrick](https://en.wikipedia.org/wiki/WEBrick)).

The web server will be set up as a reverse proxy that forwards the requests to Gollum's own web server. We're chosing Nginx as one of the most popular, efficient and easy to configure web servers.

It's assumed you're familiar with Nginx and it's already installed on the server. Delving into Nginx's config and installation is outside the scope of this guide, but for the most basic setup, you'll at least need to install it from the Ubuntu archive:

``` sh
sudo apt install nginx
```

We will start by creating an Nginx virtual host that listens to port 80, and sets up the reverse proxy that forwards the client requests to Gollum's web server. Let's define it in the usual Nginx way:

``` sh
sudo vim /etc/nginx/sites-available/example.com.conf
```

File contents:

``` nginx
upstream gollum_app_webrick_server {
    server localhost:4567;
}

server {
    listen 80;

    server_name $YOUR_SERVER_NAME_OR_IP;

    location / {
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Scheme $scheme;
        proxy_redirect off;

        proxy_pass http://gollum_app_webrick_server;
    }
}
```

Finally, we simply need to enable the configured site. Again, in the usual Nginx way:

``` sh
sudo ln -s /etc/nginx/sites-enabled/example.com /etc/nginx/sites-available/example.com.conf
```

It's recommended to test and validate your configuration files:

``` sh
sudo nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

And at this point, you might just restart (or reload) Nginx for it to reload its configuration files with your new site.

``` sh
sudo service nginx restart
```

## Adding Disqus comments

Disqus relies on a snippet of JavaScript code that is loaded on every page that needs comments. That code takes care of dynamically generating the comments feed. It is called the **Disqus embed code**.

Gollum relies on [Mustache](https://mustache.github.io/) templates to dynamically render HTML for each page upon request. To modify the content that will be shown on every page (i.e. to add comment support), **we will modify the template generates each page** to inject the Disqus embed code. It's called `page.mustache`.

> ℹ️ In these steps, we'll do a simple modification to the Gollum templates to add Disqus comments. If you want to broaden the scope and learn more about extending the stock templates, you can jump to the [Customizing views section](#customizing-gollum-wiki-s-appearance_customizing-views).

To keep things modular and simple, we'll be adding the code on a separate template file (`comments.mustache`) that will be loaded by `page.mustache`. In Mustache terminology, **the page template will be loading the *partial* comments template**.

To recap, we'll be:

- adding a mustache partial template named `comments.mustache` that contains the Disqus embed code
- modifying the `page.mustache` template to reference (and include) the partial template

Step by step:

1.  Copy all stock templates to a new location where you can edit them without modifying the originals. We'll be using `/usr/local/share/gollum/` as a [standard FHS location](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard#cite_note-9).

``` sh
sudo mkdir -p /usr/local/share/gollum/
cp -R /var/lib/gems/2.3.0/gems/gollum-`gollum --version | awk '{print $2}'`/lib/gollum/templates \
  /usr/local/share/gollum/templates
sudo chown -R $USER:$USER /usr/local/share/gollum/templates
```

1.  Create a new `comments.mustache` file in the new location and add the contents from the [Disqus universal embed code](https://disqus.com/admin/install/platforms/universalcode/) snippet.
2.  Edit the `page.mustache` file in the new location to add the `{{>comments}}` line right after the end of the body div:

``` html
    <div class="markdown-body">
      {{{content}}}
    </div>
  </div>
  {{>comments}}
```

1.  Point gollum to the location of your new templates directory via the `template-dir` option: add `:template_dir => 'YOUR_TEMPLATES_LOCATION'` to the `wiki_options` array in your `config.rb` file.

ℹ️ Be aware of Gollum's [issue 1221](https://github.com/gollum/gollum/issues/1221) and [issue 1222](https://github.com/gollum/gollum/issues/1222).

## Adding secure authentication

Unfortunately Gollum does not offer any means of access control or authentication, meaning that anyone will be able to edit your wiki in its most basic setup.

[Omnigollum](https://github.com/arr2036/omnigollum) is a third-party library that builds on top of the [Omniauth](https://github.com/omniauth/omniauth) multi-provider authentication library to provide OAuth access control to Gollum.

With Omnigollum you'll be able to restrict access to your wiki via login through a given OAuth provider from the extensive [set of providers supported by Omniauth](https://github.com/omniauth/omniauth/wiki/List-of-Strategies).

:warning: Although Omnigollum seems to be the only way to provide secure access control to Gollum, a few words of caution:

- Omnigollum does not seem to be regularly maintained
- Omnigollum offers a very basic set of permissions
- The login/logout functionality is also very basic -i.e. you can log into your wiki via a 3rd-party OAuth provider, but you can neither see your status after login or actually log out

### Enabling SSL

In order to be able to communicate with the SSL protocol for secure authentication on your server, the first step will be to install a set of certificates, that will be tied to the domain(s) Gollum is being served from.

For this, we'll be using [Let's Encrypt](https://letsencrypt.org/) a free and open Certificate Authority. The process of fetching, generating and installing the certificates is automated by the [Certbot](https://certbot.eff.org) client.

The next sections describe how to install and operate the Certbot client to generate and install the required certificates.

#### Installing Certbot

The Certbot team maintains a PPA (Personal Package Archive) that contains the latest versions of the software. There it is updated more often than in the Ubuntu archives.

The first step is to install it:

``` sh
$ sudo apt-get update
$ sudo apt-get install software-properties-common
$ sudo add-apt-repository ppa:certbot/certbot
$ sudo apt-get update
$ sudo apt-get install python-certbot-nginx 
```

#### Getting an SSL certificate

Before obtaining the certificate, we'll need to do a small change to the Nginx configuration.

Certbot will create some files under `$root/.well-known` and will try to access them from the Internet, so we'll have to make sure that we've set the `root` variable and allowed access to that location.

``` sh
sudo vim /etc/nginx/sites-available/example.com.conf
```

Add this bit to the Nginx config file:

``` nginx
root /srv/www

location ~ /.well-known {
        allow all;
}
```

Then check if the Nginx configuration file still looks good, and if so restart Nginx

``` sh
sudo nginx -t
sudo service nginx restart
```

You can test it by placing a text file there and trying to access the file's URL via your browser.

Finally obtain the certificate, specifying the domain it is for. You can specify multiple domains with the `-d` option, but note that they must at least be defined in a virtual host in your Nginx configuration files:

``` sh
sudo certbot --nginx -d example.com -d www.example.com
```

The certificates will expire after a set time. To renew them:

``` sh
sudo certbot renew
```

You can also set this command to be executed on a cron job. You can learn more about it on:

- [Certbot documentation](https://certbot.eff.org/#ubuntuxenial-nginx)
- [Letsencrypt tutorial on Digitalocean.com](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-16-04)

### Installing Omnigollum

Omnigollum requires an *Omniauth provider* to work. In our case, we'll use Github to handle authentication in our wiki, via the `omniauth-github` package:

``` sh
sudo gem install omnigollum
sudo gem install omniauth-github
```

### Configuring Omnigollum

These are the bits you'll need to add to Gollum's config.rb configuration file:

``` ruby
# [...]

## Omni Auth
require 'omnigollum'
require 'omniauth/strategies/github'

# [...]

options = {
  # OmniAuth::Builder block is passed as a proc
  :providers => Proc.new do
    # Found https://github.com/settings/applications/
    provider :github, 'Client ID', 'Client Secret'
  end,
  :dummy_auth => false,
  # If you want to make pages private:
  #:protected_routes => ['/private*'],

  # Specify committer name as just the user name
  :author_format => Proc.new { |user| user.name },
  # Specify committer e-mail as just the user e-mail
  :author_email => Proc.new { |user| user.email },

  # Authorized users
  :authorized_users => ["your_email@example.com"],
}


## :omnigollum options *must* be set before the Omnigollum extension is registered
Precious::App.set(:omnigollum, options)
Precious::App.register Omnigollum::Sinatra
```

### Setting up Github as the OAuth provider

We'll be using Github as the OAuth provider to control access to the wiki. This is a very condensed set of instructions from [Github's Basics of authentication](https://developer.github.com/guides/basics-of-authentication).

#### Register your app at Github

1.  [Register your app at Github](https://github.com/settings/applications/new) to get an OAuth Client ID and Client Secret
2.  Fill in the details, and set the Authorization callback URL to your site.
3.  Click Register application. You're nearly done.

![](https://projects.davidplanella.org/open-source/gollum-wiki-installation/GithubGollum.png)

#### Configure user authorization on the server

1.  Go to your [registered OAuth applications page](https://github.com/settings/developers) at Github and simply click on your newly registered Gollum app
2.  Copy the Client ID and Client Secret from there
3.  Add `github` to the `providers` option in Gollum's `config.rb` file and paste the Client ID and Client Secret as shown:

``` ruby
options = {
:providers => Proc.new do
    # Found https://github.com/settings/applications/
    provider :github, 'your-client-id-goes-here', 'your-client-secret-goes-here'
  end,

# [...]
```

Ensure gollum is running (`sudo service gollum status` or `sudo service gollum start`) before the next step.

#### Authorize the Gollum app at Github

1.  Navigate to your site in your browser (e.g. <https://wiki.davidplanella.org>)
2.  Authorize the application in the Github prompt that appears on the browser.

![](https://projects.davidplanella.org/open-source/gollum-wiki-installation/oauth_prompt-(1).png)

That's it!

### Making a wiki private

Optionally, you can make your wiki or part of it private. You can achieve this by specifying the path of your wiki you want to make inaccessible in the `:protected_routes` variable in `config.rb`.

As an example, the following values will not allow unauthenticated visitors to:

- See any subpages you create under the `private` namespace in your wiki
- Revert, create, edit, rename, upload or delete pages
- See individual page history or latest changes globally
- They will still be able to access (i.e. view) the open parts of your wiki, that is, those outside of the private namespace.

They will still be able to access (i.e. view) the open parts of your wiki, that is, those outside of the `private` namespace.

``` ruby
:protected_routes => [
    '/private/*',
    '/private',
    '/revert/*',
    '/revert',
    '/create/*',
    '/create',
    '/edit/*',
    '/edit',
    '/history/*',
    '/history',
    '/latest_changes',
    '/rename/*',
    '/rename/',
    '/upload/*',
    '/upload/',
    '/delete/*',
    '/delete'],
```

:warning: Be aware of [Omnigollum's issue \#44](https://github.com/arr2036/omnigollum/issues/44) and [issue \#45](https://github.com/arr2036/omnigollum/issues/45) before you do this.

:warning: You might want to set the `:authorized_users` variable in the `config.rb` file to restrict which authenticated users have access.

## Customizing Gollum wiki's appearance

![](https://i.imgur.com/4ocwhdc.gif%7Cheight=200px)

### Customizing styles

You can add your own styles to augment or modify the stock Gollum theme by creating a `custom.css` file and placing it in the root of your wiki's git repository. To enable its use, you'll need to either set `:css => true` in the wiki options of the [`config.rb` file](#basic-setup_configuring-gollum) or start gollum with the `--css` command line option.

ℹ️ You'll need to have committed the `custom.css` file on your git repository for custom styles to be taken into account.

### Code injection

You can also inject your own JavaScript code styles to augment or modify the stock Gollum theme by creating a `custom.js` file and placing it in the root of your wiki's git repository. To enable its use, you'll need to either set `:js => true` in the wiki options of the [`config.rb` file](#basic-setup_configuring-gollum) or start gollum with the `--js` command line option.

ℹ️ You'll need to have committed the `custom.js` file on your git repository for your custom code to be used by Gollum.

### Customizing views

If you've followed the [Adding Disqus comments section](#adding-disqus-comments), you will know that Gollum renders its wiki pages based on a set of [Mustache](https://mustache.github.io/) templates. In plain terms, it is a set of files with the `.mustache` extension, with a combination of HTML markup and Mustache syntax that you can modify to your own needs. The file hierarchy looks like this:

``` sh
/var/lib/gems/2.3.0/gems/gollum-4.1.2/lib/gollum/templates/
├── compare.mustache
├── create.mustache
├── edit.mustache
├── editor.mustache
├── error.mustache
├── file_view.mustache
├── history_authors
│   ├── gravatar.mustache
│   ├── identicon.mustache
│   └── none.mustache
├── history.mustache
├── latest_changes.mustache
├── layout.mustache
├── livepreview.mustache
├── page.mustache
├── pages.mustache
├── searchbar.mustache
└── search.mustache
```

The two perhaps most important files you'll want to modify are:

- `layout.page`: this is the template that defines the basic layout of all pages. As such, it defines the HTML5 doctype, which CSS files and JS files will be loaded and in which order. It also defines the `<body>` tag and the most basic CSS styling.
- `page.mustache`: most of the content on your wiki will be viewed as pages. This template defines the layout of each single page. It can be used, for instance, to [add Disqus comments to each page](#adding-disqus-comments).

This makes it a modular and versatile system for extension and modification. You can create your own views or modifying existing ones by simply adding (and including) new `.mustache` files, or modifying the stock files. In theory, you could also create your own full theme, but I have found that currently the core gollum JavaScript code and CSS classes are not decoupled enough from the view generation in order to be able to do this cleanly. It *can* be done, though.

Here's a suggestion on how to customize the Gollum views to your own needs:

1.  If you haven't done it already, copy all stock templates to a new location where you can edit them without modifying the originals. We'll be using `/usr/local/share/gollum/` as a [standard FHS location](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard#cite_note-9).

``` sh
sudo mkdir -p /usr/local/share/gollum/
cp -R /var/lib/gems/2.3.0/gems/gollum-`gollum --version | awk '{print $2}'`/lib/gollum/templates \
  /usr/local/share/gollum/templates
sudo chown -R $USER:$USER /usr/local/share/gollum/templates
```

1.  Also, only if you haven't done it already, append the `:template_dir => '/usr/local/share/gollum/templates'` line in the `wiki_options` array inside your `config.rb` [configuration file](#basic-setup_configuring-gollum)
2.  If you've changed the `config.rb` file, restart gollum: `sudo service gollum restart`
3.  Now open the template files you need to modify and hack away :)

## Troubleshooting

### Cannot allocate memory when updating Gollum gems on Digitalocean

ℹ️ In some cases some gems cannot be updated, returning a *Cannot allocate memory* message. This seems to happen on Digitalocean servers, where due to their SSD storage, swap is not enabled. A workaround is to [temporarily create a swap file](https://www.digitalocean.com/community/tutorials/how-to-add-swap-on-ubuntu-14-04), do the update and then delete the swap. In a nutshell:

``` sh
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
sudo gem update gollum
sudo swapoff -a
sudo rm /swapfile
```
