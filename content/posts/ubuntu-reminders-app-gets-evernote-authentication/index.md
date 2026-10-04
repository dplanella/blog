---
title: "Ubuntu Reminders app gets Evernote authentication"
slug: "ubuntu-reminders-app-gets-evernote-authentication"
date: 2013-11-22T00:40:57.000Z
tags: ["ubuntu", "evernote", "core-apps", "reminders", "app-development"]
images: ["/content/images/2021/07/Ubuntu-heart-evernote.jpg"]
---

![Ubuntu loves Evernote](/wp-content/uploads/2013/11/Ubuntu-heart-evernote.jpg)

We've been making good progress with [Reminders](https://wiki.ubuntu.com/Touch/CoreApps/RemindersApp), the Ubuntu app powered by Evernote. While our team of developers have been busy working on the UI, a set of other equally awesome individuals have been working in parallel to implement the backend pieces.

Today, I'm thrilled to announce that **the Evernote Online Accounts provider is now available for Ubuntu** as a preview. This plugin enables secure login to Evernote via OAuth, and handles the authentication process via the standard Ubuntu platform APIs, so that the Reminders app does not even have to care about the logic.

Big thanks to [Alberto Mardegan](http://blog.mardy.it/) and [Chris Wayne](http://chrismwayne.com/) for making this possible.

## For developers only

At this point, the authentication plugin is provided for the purpose of developing the Reminders app only, and it will intentionally not work with regular Evernote accounts. Support for regular Evernote accounts will be enabled when the Reminders app reaches the stable release status.

The plugin talks to the Evernote sandbox service, so before using it you'll need to create a developer account there first. [Create a free Evernote developer account ›](https://sandbox.evernote.com/Registration.action)

### Installing the Evernote account provider

As the required packages have not yet landed in the archive, we'll need to install them from the core apps repository. You can open a terminal and run these commands to do the installation, either on the phone or on the desktop:

On the phone, before you can install a package [you will need to switch to RW mode](http://askubuntu.com/q/380258/9781)

    sudo add-apt-repository ppa:ubuntu-touch-coreapps-drivers/daily
    sudo apt-get update
    sudo apt-get install account-plugin-evernote signon-plugin-oauth2

### Logging into the Evernote sandbox

![Evernote Account](/wp-content/uploads/2013/11/Evernote-Account.jpg)

The next step in using the plugin is to log into the Evernote sandbox. The Evernote login process, as for any other Ubuntu online account, takes place in the System Settings app. Once the plugin is installed, you'll be able to add new Evernote accounts from the New Account screen. While the screenshots above show how to do it on the phone, this works equally well on the desktop.

### Using the Evernote account provider

To enable Evernote account support in QML apps, you'll only require an instance of the Ubuntu Online Accounts [AccountServiceModel](http://developer.ubuntu.com/api/qml/sdk-1.0/Ubuntu.OnlineAccounts.AccountServiceModel/). You should check out the online API reference for more information, but in essence, an adapted version of the snippet from the documentation will do the trick:

    Item {
        AccountServiceModel {
            id: accounts
            // Use the Evernote service
            service: "evernote"
        }
        ListView {
            model: accounts
            delegate: Rectangle {
                id: rect
                Text { text: rect.model.displayName }
                AccountService {
                    id: accountService
                    objectHandle: rect.model.accountServiceHandle
                    // Print the access token on the console
                    onAuthenticated: { console.log("Access token is " + reply.AccessToken) }
                    onAuthenticationError: { console.log("Authentication failed, code " + error.code) }
                }
                MouseArea {
                    anchors.fill: parent
                    onClicked: accountService.authenticate()
                }
            }
        }
    }

With this code, you'll get your Evernote account listed in the UI. Clicking on it, and upon successful authentication you'll obtain an Evernote **authentication token**, that can then be passed to the Evernote API to access the [NoteStore](http://dev.evernote.com/doc/articles/core_concepts.php#services) and manage notes for the account associated to that token.

This is however the first step, as you'll need a working backend to pass that token to and to talk to the Evernote API before you can manage any notes. Read on to learn more on this.

## Setting up the Evernote API Taskforce

The next phase in the project is now to focus on the creation a QML plugin that will talk to the Evernote service. This is a key piece of the infrastructure that will enable performing the essential operations of fetching, modifying and updating notes while online.

The unstoppable [Michael Zanetti](http://notyetthere.org/) has been helping us bootstrapping the process, and he's already put together an Evernote API QML plugin that performs the basic communication with the Evernote servers.

Taking this work as a foundation, we want to extend the plugin to perform all necessary operations to cover the needs of the Reminders app. With this goal in mind, we're putting together **the Evernote API taskforce**: a team of developers tightly focused in developing the Evernote API QML plugin and working very closely with the Reminders app developers to ensure backend and UI perfectly fit.

So if you've got Qt and C++ experience, this is a call for you: **join the team of core developers who bring Evernote support to Ubuntu and millions of users**!

If you're interested in participating, **let us know in the comments** or or [drop us an e-mail on the Core Apps mailing list](https://launchpad.net/~ubuntu-touch-coreapps/). Looking forward to welcoming new developers to the team, and stay tuned for more updates!
