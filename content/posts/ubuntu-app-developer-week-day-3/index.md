---
title: "Ubuntu App Developer Week - Day 3"
slug: "ubuntu-app-developer-week-day-3"
date: 2011-04-14T23:14:37.000Z
tags: ["appdeveloperweek", "d-bus", "development", "launchpad", "qml", "qt", "summary", "translations", "ubuntu", "ubuntu-one"]
---

## Ubuntu App Developer Week - Day 3 Summary

Right into the middle of the week and still delivering the most diverse set of sessions from the most interesting technologies. QML, Cloud, D-Bus, Multitouch, Unity, Bazaar... Wednesday had a bit of everything. Most importantly, this sessions are for you all, so I was really glad to hear feedback on how people liked the content of App Developer Week! So here's a new summary for all of those who couldn't attend.

### Qt Quick: QML the Language

*By Jürgen Bocklage-Ryannel*

In his first session, Jürgen gave a short intro to Qt Quick's QML language and how to use it. The first steps were to install Qt and Qt Creator, followed by a description of what Qt Quick is and how developers came up with a declarative way, similar to CSS or JSON to write in the language. All that clear, he then started with the Qt Quick tutorial and code examples that could be run with qmlviewer, the qml interpreter. Onto the second part, he focused on the QML languate, and going into the detail on how to create custom QML components. There were also lots of pointers to the excellent Qt documentation.

*Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1104/QML).*

### Make your applications work in the cloud with Ubuntu One

*By [Stuart Langridge](https://launchpad.net/%7Esil "LaunchpadHome")*

Stuart gave a great overview on how to add the cloud to existing apps and how to make new apps for the cloud, letting Ubuntu One do all the hard work for you: from managing identities, password renewal to sharing data between applications. And all that on the web, the desktop, mobile... all your stuff everywhere! He then showed us some simple code to sync playlists on the cloud, ready for streaming. File sync is also an important Ubuntu One feature apps can make use of for sharing, and he also went through a couple of the many cool ways you can use it. The last mention was on API documentation, something Stuart is working on in this cycle.

*Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1104/UbuntuOneCloudApps).*

### Take control of your desktop easily with DBus

*By [Alejandro J. Cura](https://launchpad.net/%7Ealecu "LaunchpadHome")*

In this session Alejandro showed us in a hands-on and easy to follow way different bits and pieces of D-Bus, and how applications in the desktop can communicate through it. He went through real life examples to show how to do simple tasks and explained how they can be achieved with D-Bus.

*Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1104/DBus).*

### Touchégg: Bringing Multitouch Gestures to your Desktop

In the second multitouch session of the week, app developer José Expósito started showcasing Touchégg, how it works and its features: recognizing multitouch gestures and getting the most of multitouch devices. He then went on describing which gestures it supports, such as tap, drag, pinch or tap & hold, and the different actions that can be associated to gestures, showing us a really [cool video of Touchégg in action](http://www.youtube.com/watch?v=1Ek4QaFQ1qo). The second part of the talk focused on describing the technologies used to develop Touchégg: uTouch-GEIS, through its simplified interface, and Qt.

*By [José Expósito](https://launchpad.net/%7Ejose-exposito89 "LaunchpadHome")*

*Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1104/Touchegg).*

### Unity: Integrating with Launcher and Places

*By [Mikkel Kamstrup Erlandsen](https://launchpad.net/%7Ekamstrup "LaunchpadHome")*

Mikkel used the intro of the talk to set a couple of things straight: "Places" are going to be called "Lenses" in the next cycle, and libunity does not yet guarantee API or ABI stability. He then followed with the Unity Launcher integration, and how applications can use static quicklists, and more advanced features such as count, progress bar, window flashing and dynamic quicklists. The second part were Places: remote databases that provide data for Unity to render. Through a Python code example he showed us in detail all the aspects of creating a Unity Place.

*Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1104/UnityAPI).*

### Tracking Source Code History with Bazaar

*By [Jelmer Vernooij](https://launchpad.net/%7Ejelmer "LaunchpadHome")*

Jelmer, in his experience of seasoned Bazaar hacker started off introducing what bzr is: a modern distributed version control system. He then went on with the basics with a hands-on example, going through the creation of a branch, the first commit, and describing several of the most handy bzr commands. As a wrap-up, he showcased more advanced features such as source recipes: scripts that combine branches and build daily Debian packages from them.

*Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1104/Bazaar).*

## The Day Ahead: Upcoming Sessions for Day 4

We're featuring a Qt Quick Marathon today: 2 sessions in a row. Following that, how to do RAD with yet another framework: Quickly, how to get your applications in Ubuntu, and how to get them translated in Launchpad. Enjoy!

[16:00 UTC](http://www.timeanddate.com/worldclock/fixedtime.html?month=4&day=14&year=2011&hour=16&min=0&sec=0&p1=0)\
**Qt Quick: Elements/Animations/States** - Jürgen Bocklage-Ryannel\
Another day and more featured Qt content: this time Jürgen will take us through different elements/animations and states Qt Quick provides, and will show us through examples how to make use of them.

[17:00 UTC](http://www.timeanddate.com/worldclock/fixedtime.html?month=4&day=14&year=2011&hour=17&min=0&sec=0&p1=0)\
**Qt Quick: Rapid Prototyping** - Jürgen Bocklage-Ryannel\
If one session weren't enough, here's the continuation: more Qt goodness, this time a hands-on session to develop a small application from start to finish and experience the whole process from the front row.

[18:00 UTC](http://www.timeanddate.com/worldclock/fixedtime.html?month=4&day=14&year=2011&hour=18&min=0&sec=0&p1=0)\
**Rapid App Development with Quickly** - [Michael Terry](https://launchpad.net/%7Emterry "LaunchpadHome")\
Mike will show you how to write applications in no time with the power of Python and Quickly: bringing back the fun in programming.

[19:00 UTC](http://www.timeanddate.com/worldclock/fixedtime.html?month=4&day=14&year=2011&hour=19&min=0&sec=0&p1=0)\
**Getting Your App in the Distro: the Application Review Process** - [Allison Randal](https://launchpad.net/%7Eallison "LaunchpadHome")\
A while back we created an easy process defining how to get applications into Ubuntu, so in order to be able to add them in a matter of weeks, rather than waiting for the next release. Allison, in her Ubuntu Technical Architect and Application Review Board member hat, will walk you through the [Application Review Process](https://wiki.ubuntu.com/PostReleaseApps/Process)

[20:00 UTC](http://www.timeanddate.com/worldclock/fixedtime.html?month=4&day=14&year=2011&hour=20&min=0&sec=0&p1=0)\
**Adding Indicator Support to your Apps** - [Ted Gould](https://launchpad.net/%7Eted "LaunchpadHome")\
Join the man who knows most about indicators in a session that will teach you how to integrate your application even more into Ubuntu. They're slick, robust and consistent: bringing indicator support to your apps.

[21:00 UTC](http://www.timeanddate.com/worldclock/fixedtime.html?month=4&day=14&year=2011&hour=21&min=0&sec=0&p1=0)\
**Using Launchpad to get your application translated** - [Henning Eggers](https://launchpad.net/%7Ehenninge "LaunchpadHome")\
One of the coolest features of Launchpad is that it helps growing a translation community around your project. You can make your application translatable in Launchpad and be able to deliver it into almost any language. Henning will teach you how to do this, picking up where the [previous session on translations](http://davidplanella.wordpress.com/2011/04/12/off-to-a-great-start-ubuntu-app-developer-week-day-1/) left.

Looking forward to seeing you all there!

[<img src="/wp-content/uploads/2011/04/rect3827.png" title="Join Ubuntu App Developer Week" class="aligncenter" width="154" height="42" />](http://webchat.freenode.net/?channels=ubuntu-classroom)
