---
title: "Get the Ubuntu Online Tour on your LoCo site"
slug: "get-the-ubuntu-online-tour-on-your-loco-site"
date: 2012-04-25T20:00:41.000Z
tags: ["ubuntu", "loco", "translations", "12-04"]
---

I'm thrilled to announce the availability of the **Ubuntu 12.04 Online Tour** for local community teams to localize and use on their websites.

![Ubuntu Online Tour](/content/images/2012/04/ubuntuonlinetour2.png)

The tour has been the result of the stunning work done by Ant Dillon from the Canonical Web Design Team and should provide a web-based first impression of Ubuntu to new users, now in their language.

It's a great opportunity to showcase Ubuntu to your local community to celebrate release day tomorrow.

## Where is it?

- [Go to the Ubuntu Online Tour  on Launchpad ›](https://launchpad.net/ubuntu-online-tour)
- [Translate the Ubuntu Online Tour rsaquo;](https://translations.launchpad.net/ubuntu-online-tour)

## How can I use it for my LoCo website?

First of all, you'll need to get set up with the right tools before you start.

### Getting set up

- **Bazaar** revision control system. [Install bzr ›](http://apt.ubuntu.com/p/bzr)
- **Polib** library. [Install polib ›](http://apt.ubuntu.com/p/python-polib)
- **Terminal**. You'll need to run the commands below on a terminal. Simply press `Ctrl+Alt+T` to fire up a new terminal console.

### Building the tour

If you've already translated the tour in Launchpad, you can build a localized version in 3 easy steps:

1.  Get the code:

<!-- -->

    bzr branch lp:ubuntu-online-tour/12.04

2.  Build the localized tour:

<!-- -->

    cd 12.04
    cd translate-html/bin
    ./translate-html -t

3.  Deploy the tour:

- This will vary depending on your setup, so simply make sure you copy the `chromeless`, `css`, `img`, `js`, `pie` and `videos` folders along with the `videoplayer.swf` file to your site. In addition, you will need the `en` folder and the folder for your language created in the previous step.

If you haven't finished the translation for your language in Launchpad, you will need to complete the corresponding PO file before you run step 2. Just ask on the ✉ [Ubuntu translators mailing list](https://wiki.ubuntu.com/Translations/Contact) or [on Launchpad](https://answers.launchpad.net/ubuntu-translations/+addquestion) in case you need help or are not familiar with PO files.

For any issues, suggestions or enhancement, use the [Online Tour's Launchpad project](https://launchpad.net/ubuntu-online-tour) to report bugs or submit improvements.

Enjoy!
