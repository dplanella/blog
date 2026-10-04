---
title: "Ubuntu App Developer Week Day 5 and Wrap-up"
slug: "ubuntu-app-developer-week-day-5-and-wrap-up"
date: 2011-04-19T15:59:25.000Z
tags: ["appdeveloperweek", "development", "phonon", "qt", "qt-quick", "summary", "ubuntu", "unity"]
---

[<img src="/wp-content/uploads/2011/04/appdeveloperweek.png" title="App Developer Week" class="aligncenter size-full wp-image-1126" width="480" height="259" alt="App Developer Week" />](https://wiki.ubuntu.com/UbuntuAppDeveloperWeek/)

What an awesome week for application developers. Ubuntu App Developer Week was a week of great speakers, great sessions, great participation, Multitouch, Unity, GObject, Introspection, PyGI, Qt, Qt Quick, QML, Internationalization, KDE, Phonon, Multimedia, Touchegg, Plasma Widgets, Python, Testing, Rapid Prototyping, Thunderbird, GStreamer, Zeitgeist, D-Bus, Ubuntu One, Bazaar, Lenses, Launcher API, Indicators, Launchpad, Translations, Application Review Process, Packaging, pkgme, the Sound Menu, and much much more.

Here's a recap of the whole week:

- [Day 1 Summary](http://davidplanella.wordpress.com/2011/04/12/off-to-a-great-start-ubuntu-app-developer-week-day-1/)
- [Day 2 Summary](http://davidplanella.wordpress.com/2011/04/13/ubuntu-app-developer-week-day-2/)
- [Day 3 Summary](http://davidplanella.wordpress.com/2011/04/14/ubuntu-app-developer-week-day-3/)
- [Day 4 Summary](http://davidplanella.wordpress.com/2011/04/15/ubuntu-app-developer-week-day-4/)

If you happened to miss any of the sessions, simply head to the [Ubuntu App Developer Week page](https://wiki.ubuntu.com/UbuntuAppDeveloperWeek/) where you'll find the logs for all of them.

## Ubuntu App Developer Week - Day 5 Summary

Here comes the last of the summaries for your reading pleasure. Enjoy!

### Qt Quick: Extend with C++

*By Jürgen Bocklage-Ryannel*

In this session Jürgen did another brief intro to Qt Quick: a declarative language to creat user interfaces on top of Qt C++. The subject was to extend it using the C++ language, and for this he introduced QtDeclarative, a UI runtime provided in a Qt module Qt Quick is based on. After this, he walked us through code examples: the first step - include QtDeclarative in the project in order to be able to use it in a C++ main.cpp file. Starting with basic tasks such as changing properties such as the colour of a rectangle from the C++ side, he went into more advanced ones, such as create a new qm element. Even more advanced tasks, such ad creating own elements, were left as a reading exercise with a pointer to the exhaustive Qt Quick documentation and tutorials.

Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1104/QtQuickCpp).

### Phonon: Multimedia in Qt

*By [Harald Sitter](https://launchpad.net/%7Eapachelogger "LaunchpadHome")*

For the third time this week, Harald rocked the house with an entertaining and enlightening session: Phonon, a multimedia abstraction library. First, he showed how to get the environment set up and tools installed; next: an intro to Phonon - an abstraction layer between multimedia apps and a multimedia library backend in the form of a plugin. And next up some coding: the famous 3-line example to create a Phonon-based video player with C++. He showed us how to write a simple audio player, to which then video was progressively added. As a finale he pointed to a way to create a video player with no code at all!

Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1104/Phonon).

### Integrating music applications with the Sound Menu

*By [Conor Curran](https://launchpad.net/%7Ecjcurran "LaunchpadHome")*

Conor started off explaining that sound menu integration in the next cycle will be made much easier through libunity, and talked a bit about the sound menu spec and the resources for contributors. He then explained that this cycle he concentrated on settling the architecture, making it easier for clients to provide integration. The only thing for a client to care about is to raise an MPRIS interface with a desktop entry, which will then allow it to be shown in the sound menu, and if available, any D-Bus menu items with it. He wrapped up with a description of some of the new features this cycle and an outlook on the next.

Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1104/SoundMenu).

### pkgme: Automating The Packaging Of Your Project

*By [James Westby](https://launchpad.net/%7Ejames-w "LaunchpadHome")*

On to packaging: James introduced pkgme, an almost magic tool to package your application to be distributed to users. Assuming your project uses a standard layout and pkgme has heard of it, it will use one of its backend to create the packaging structure tailored to your layout and toolset. New backends can be created upon request. As the finale, a recursive example: he showed us how to use pkgme to package pkgme itself!

Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1104/PkgMe).

### Unity Technical Q&A

*By [Jason Smith](https://launchpad.net/%7Ejassmith "LaunchpadHome") and [Jorge Castro](https://launchpad.net/%7Ejorge "LaunchpadHome")*

Jason and Jorge started off this exciting session with an introduction to the cool things you can do in Unity: Lenses - bits of pluggable UI to mash up websites and applications in the dash, the Launcher API. After that questions started to kick in: What's dee? Can you add multiple progress bars to the launcher? What's the status of progress bars, badges and counters in the launcher? What search backend does the dash use? ... if want to know the answer to these and more questions check out the session log :)

Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1104/UnityQ%26A).

### Lightning Talks

*By [Stefano Palazzo](https://launchpad.net/%7Estefano-palazzo), [David Callé](https://launchpad.net/%7Edavidc3), [Dustin Kirkland](https://launchpad.net/%7Ekirkland), MeanEye, Christian Muehlhaeuser, [Nathan Handler](https://launchpad.net/~nhandler)*

As the grand finale for a week packed with great sessions, even more concentraded content on a set of lightning talks to showcase cool projects created using the technologies available in Ubuntu: *StackExchange App* - a Unity Lens designed to work with Ask Ubuntu; *Unity Book Lens* - a Unity Lens to search through free online libraries; *Bikeshed* - a breeding ground for new/interesting/even-trivial-but-helpful scripts and programs; *Sunflower FM* - a twin-panel file GTK+ manager; *Tomahawk* - a social music player written in C++ and Qt; *ClassBot* - an IRC bot to help with running classroom sessions in \#ubuntu-classroom

Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1104/LightningTalks).

## Thanks! 

I'd like to thank all session leaders for taking the time to prepare awesome content and deliver the sessions, and all participants for their attention and their interesting questions. You all made Ubuntu App Developer Week possible, and a success!

We'll be back in 6 months time with a newer and cooler App Developer Week edition for you. See you then!

\

\
