---
title: "Ubuntu App Developer Week - Day 4"
slug: "ubuntu-app-developer-week-day-4"
date: 2011-04-15T20:04:04.000Z
tags: ["app-review-process", "appdeveloperweek", "development", "indicators", "launchpad", "qml", "qt", "qt-quick", "quickly", "rapid-prototyping", "summary", "translations", "ubuntu", "unity"]
---

## Ubuntu App Developer Week - Day 4 Summary

Ramping up to the end of the week we had another full app development goodness day, and one where the session topics fitted together in a nice workflow as well: creating bling, creating apps with Rapid Prototyping, getting them into Ubuntu, adding indicator support and translating them. Here's the report of yesterday's app development journey:

### Qt Quick: Elements/Animations/States

*By Jürgen Bocklage-Ryannel*

The next Qt Quick session was all about creating attractive and usable user interfaces. Jürgen went through the QML tutorial documentation and code examples, showing us how to position elements with anchors, columns, rows and grids. Then onto states and transitions: describing the changes in an element's properties and how to switch between them. To finalize, the most impressive stuff: QML animations, in which he teached us the different types of animations and how to use them.

Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1104/QmlElementsActionsStates).

### Qt Quick: Rapid Prototyping

By Jürgen Bocklage-Ryannel

In Jürgen's words, Qt Quick was designed to bridge the gap between designers and developers, letting both groups to work with the same technologies and code base. He explained how Qt Creator provides a design mode which allows easy dragging and dropping of UI elements, and separation between code and interface. All through a natural and agile prototyping workflow.\

*Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1104/QtQuickRad).*

### Rapid App Development with Quickly

By [Michael Terry](https://launchpad.net/%7Emterry "LaunchpadHome")

Michael started introducing what Quickly at the heart is: a robust yet simple system of templates with boilerplate code and commands. The available templates are ubuntu-application, ubuntu-cli, ubuntu-pygame and ubuntu-flash-game, and on the Natty version, Quickly will feature the 'submitubuntu' command to help getting applications into the Software Center. All that being set straight, he then showed how to use Quickly and what it can do: from creating the first example application, to modifying the UI with 'quickly design' and Glade, into debugging and finally packaging.

*Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1104/QuicklyRad).*

### Getting Your App in the Distro: the Application Review Process

By [Allison Randal](https://launchpad.net/%7Eallison "LaunchpadHome")

Linking from the previous session on how to create an app, Allison explained in a very clear way how to get your applications into Ubuntu, so that they make their way into the OS in a matter of weeks instead of having to wait until the next release. The first step is to submit a ticket to the App Review Board, giving them the essential details for the proposal. They'll then do the initial review, in which one of the reviewers will volunteer to walk you through the process and help you with suggestions or improvements, to bring the app to a state ready for the final review. There the board will vote in a meeting for the inclusion of the application. After the process description she answered the questions from the audience and wrapped up with some useful tips to application submitters.

*Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1104/AppReviewProcess).*

### Adding Indicator Support to your Apps

By [Ted Gould](https://launchpad.net/%7Eted "LaunchpadHome")

Ted kicked off with an explanation of what indicators are and their intended use: they should not be used just because they are available - rather as a feature for long running applications, those that are more services to users, to expose that functionality. The next step was to describe how to create indicators through libappindicator, with any language supported by GObject Introspection, such as Python or Javascript, and how to add more features to a basic indicator: accessible labels and attention state. After that he described fallbacks, and how platforms not using Unity can nevertheless use indicators. The final minutes were dedicated to the future of indicators, that for now will focus on API cleanup and stabilization, and introspection improvements.

*Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1104/AppIndicators).*

### Using Launchpad to get your application translated -

By [Henning Eggers](https://launchpad.net/%7Ehenninge "LaunchpadHome")

As a follow up to the talk on how to [add native language support to your applications](https://wiki.ubuntu.com/MeetingLogs/appdevweek1104/InternationalizingApps) on Monday, Henning described the next step: how to make them translatable in Launchpad and grow a translation community around them. In the first part he showed how to set up a demo project using Launchpad's staging server, and shared some recommendations on how to make sure the application is correctly set up for translations, followed by an overview on some Gettext concepts Launchpad relies upon. From there, it was straight into business: setting up a translatable project in Launchpad, getting translatable templates imported and exposed to translators, creating a translation community for your project and the workflow for translation. A very detailed overview to get your application to talk any language.

*Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1104/LaunchpadTranslations).*

## The Day Ahead: Upcoming Sessions for Day 5

The last day and the quality and variety of the sessions is still going strong. Check out the great content we've prepared for you today:

[16:00 UTC](http://www.timeanddate.com/worldclock/fixedtime.html?month=4&day=15&year=2011&hour=16&min=0&sec=0&p1=0)\
**Qt Quick: Extend with C++** - Jürgen Bocklage-Ryannel\
Sometimes you would like to extend Qt Quick with your own native extension. Jürgen will show you some ways how to do it.

[17:00 UTC](http://www.timeanddate.com/worldclock/fixedtime.html?month=4&day=15&year=2011&hour=17&min=0&sec=0&p1=0)\
**Phonon: Multimedia in Qt -** [Harald Sitter](https://launchpad.net/%7Eapachelogger "LaunchpadHome")\
Harald, as the lead developer of the Qt/KDE multimedia library Phoon will tell you about the awesomeness that Phonon provides and how it achieves ultimate portability, so that it can even run on vending machines. He'll also tell you hos to create a video player with 3 lines of code (or in 30 seconds without any code) and much more.

[18:00 UTC](http://www.timeanddate.com/worldclock/fixedtime.html?month=4&day=15&year=2011&hour=18&min=0&sec=0&p1=0)\
**Integrating music applications with the Sound Menu -** [Conor Curran](https://launchpad.net/%7Ecjcurran "LaunchpadHome")\
So you've seen the slick sound menu in Ubuntu, and you're developing a multimedia application, right? You're then wondering how to seamlessly integrate it into Ubuntu and use all the nice features from the menu as well? Wonder no more, for Conor is the man behind the sound menu and he'll be delighted to teach you how.

[19:00 UTC](http://www.timeanddate.com/worldclock/fixedtime.html?month=4&day=15&year=2011&hour=19&min=0&sec=0&p1=0)\
**pkgme: Automating The Packaging Of Your Project -** [James Westby](https://launchpad.net/%7Ejames-w "LaunchpadHome")\
Once you've developed a cool application you'll want to package it and distribute it to users so that they can easily install it in their favourite platform. James will show you how this can be both easy and fun letting pkgme do all the work for you.

[20:00 UTC](http://www.timeanddate.com/worldclock/fixedtime.html?month=4&day=15&year=2011&hour=20&min=0&sec=0&p1=0)\
**Unity Technical Q&A -** [Jason Smith](https://launchpad.net/%7Ejassmith "LaunchpadHome") and [Jorge Castro](https://launchpad.net/%7Ejorge "LaunchpadHome")\
You've heard about Unity, the new UI concept which is going to improve several orders of magnitude how you interact with your computer in Ubuntu. You are probably using it already, and you'll surely have questions and will want to learn more about the coolness it brings. Jason Smith, from the Unity development team, and Jorge Castro, from the Community team know all about Unity and they'll be here to chat with you.

[21:00 UTC](http://www.timeanddate.com/worldclock/fixedtime.html?month=4&day=15&year=2011&hour=21&min=0&sec=0&p1=0)\
**Lightning Talks -** [Nigel Babu](https://launchpad.net/%7Enigelbabu "LaunchpadHome")\
As the final treat to close the week, Nigel has organized a series of lightning talks to showcase a medley of cool applications: *CLI Companio*n, *[Unity Book Lens](https://launchpad.net/unity-books-lens)*, *Bikeshed*, *circleoffriends*, *[Algorithm School](https://launchpad.net/as)*, *[Sunflower FM](http://code.google.com/p/sunflower-fm/)*, *[Tomahawk Player](http://tomahawk-player.org/)*, *Classbot* - your app could be in this list next time, do check them out!

Looking forward to seeing you all there!

[<img src="/wp-content/uploads/2011/04/rect3827.png" title="Join Ubuntu App Developer Week" class="aligncenter" width="154" height="42" />](http://webchat.freenode.net/?channels=ubuntu-classroom)
