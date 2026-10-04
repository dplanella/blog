---
title: "Ubuntu App Developer Week - Day 2"
slug: "ubuntu-app-developer-week-day-2"
date: 2011-04-13T17:59:32.000Z
tags: ["appdeveloperweek", "development", "gobject", "gstreamer", "introspection", "kde", "pygi", "pygtk", "python", "qt-quick", "summary", "ubuntu", "unity", "zeitgeist"]
---

## Ubuntu App Developer Week - Day 2 Summary

Wow, what a great follow-up to the first day! The second [Ubuntu App Developer Week](https://wiki.ubuntu.com/UbuntuAppDeveloperWeek) brought lots of awesome: great speakers and sessions, great participation, improvisation, Python, GTK, KDE, Qt, PyGI, Zeitgeist, Gstreamer, Introspection, Thunderbird, Unity, API Integration, hacking, fun... all the buzzwords you can associate when developing in your favourite Free Software Platform.

### PyGTK is dead, long live PyGI! Using gobject-introspection in Python

*By [Martin Pitt](https://launchpad.net/%7Epitti "LaunchpadHome")*

Martin's complementary session to the [GObject Introspection (GI) one on Monday](http://davidplanella.wordpress.com/2011/04/12/off-to-a-great-start-ubuntu-app-developer-week-day-1/) was very popular. He started off with a recap of what GI is and the importance of the availability of several programming language bindings in any modern development platform. He provided an overview on how GI works in practice, and then delved into how it actually works in Python through the use of Pygobject and the gi.repository module, with lots of coding examples and comparison with traditiona GTK+ C code. After that he described other API differences, in particular the caveats with contructoirs, passing arrays, output arguments, GDestroyNotify and what to do with non-introspectable functions or methods. The next topic where overrides: how to provide custom code to override the introspected library's objects. The second part of the session focused on explaining in detail how to migrate old PyGtk code to GTK3 and PyGI, in a series of easy guidelines: renaming, checking and repeating, and packaging changes. He wrapped up with a series of pointers on how to learn more and a Q+A session with lots of interesting questions from the audience.

*Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1104/PyGI).*

### Zeitgeist API & Zeitgeist Application Integration

*By [Manish Sinha (मनीष सिन्हा)](https://launchpad.net/%7Emanishsinha "LaunchpadHome") and [Seif Lotfy](https://launchpad.net/%7Eseif "LaunchpadHome")*

For this session we had the luxury of having two key members of the Zeitgeist project to explain us all the details on how to integrate it to your own projects.  Manish, one of the Zeitgest developers, kicked off with an introduction on what Zeitgeist is: an automatic event logger which logs the events that happen on your computer. He then went on through the details of the Zeitgest terminology (events, manifestations, actors, timestamps...), architecture, and its interaction with D-Bus, with an overview of the API interface and the existing bindings: Python, C/Vala and C#. The session went on with examples of how real world applications and data providers use Zeitgeist, such as EOG plugins or Tomboy. Seif then chipped in with an example of  how Zeitgeist support was integrated into a GEdit plugin. Throughout the session lots of interesting questions were raised by the audience.

*Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1104/Zeitgeist).*

### GStreamer+Python: Multimedia Swiss Army Machete

*By [Jason DeRose](https://launchpad.net/%7Ejderose "LaunchpadHome")*

A very intersesting session indeed. In it, Jason explained all the points why GStreamer is *the* multimedia framework due to its economy of scale and why Python is the perfect complement with its simplicity and language clarity. According to him, together they provide the ultimative multimedia development tool, and this was why he chose to use them in hos own project: [Novacut](http://novacut.com/), the distributed video editor. From this point on, it was "Learning by doing", and he then walked thorugh the [code examples](http://bazaar.launchpad.net/~jderose/+junk/machete/files) he'd set up for the session, showcasing how simple it is to work with multimedia streams with his swiss army machete :)

*Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1104/GstreamerPython).*

### KDE Development Intro: Q+A

*By [Harald Sitter](https://launchpad.net/%7Eapachelogger "LaunchpadHome") and [Jonathan Riddell](https://launchpad.net/%7Ejr "LaunchpadHome")*

I'd especially like to mention this session due to a change of schedule. The original speaker, KDE/Kubuntu ninja Joathan Thomas could not make if due to last-minute commitments. But no worries, KDE/Kubuntu friends are always there to lend a hand, and in no time Harald and Jonathan stepped up to fill the gap and do an impromptu KDE Development Intro and Q+A session. In there they gave an overview on the essentials every prospective KDE developer should know and answered in detail the questions in the audience. All in all a great insight on how to get started developing KDE apps.

*Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1104/KdeDevQ%26A).*

### Thunderbird + Unity = Awesome, and how JSCtypes lets you get to the candy

*By [Mike Conley](https://launchpad.net/%7Emconley "LaunchpadHome")*

Mike has been working over the last 3 months at Mozilla on ways in which Thunderbird can integrate nicely into Ubuntu, in particular with Unity. He started explaining the main points he's been focusing on: the messaging menu, the Unity launcher adn Ubuntu One, and for the rest of the session he covered the first two. Going straight to the subject, the next topic was to explain what a Thunderbird extension is, and how they are written using a mixture of Javascript, the XUL mark-up language and CSS, all executed by the Gecko engine. He then introduced JS-CTypes, which allow developers to access C libraries directly from Chrome-level Javascript code. and how he used them to write a Unity launcher add-on. the resto of the session focused on this subject, with plenty of code examples.

*Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1104/ThunderbirdUnity).*

### STORY: Unity, hacking on a real-world app

*By [Marco Trevisan](https://launchpad.net/%7E3v1n0 "LaunchpadHome")*

The last session of the day was one of my favourite ones: an inspiring personal story. Marco is a community contributor to Unity who told us about his journey since he found an application itch to scratch and until his own feature was landed. He started with a very easy to understand overview of the Unity architecture and how all the pieces fit together, following with the story on how he found something that needed improvement and how he went about fixing it: indicator-sound not being precise when setting the volume with the mouse wheel. Do read it, as it is going to be a great help to all of you who are looking on how to get started contributing to Ubuntu development.

*Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1104/UnityHacking).*

## The Day Ahead: Upcoming Sessions for Day 3

A quick look at today's session lineup for your development pleasure:

[16:00 UTC](http://www.timeanddate.com/worldclock/fixedtime.html?month=4&day=13&year=2011&hour=16&min=0&sec=0&p1=0)\
***Qt Quick: QML the Language*** - Jürgen Bocklage-Ryannel\
Here's a special treat for anyone interested in [Qt](http://qt.nokia.com/) development: Jürgen Bocklage-Ryannel, from Nokia, the maker of Qt, will be introducing Qt Quick and QML as the language used in Qt Quick. He'll be showing some elements of the UI and the general process, and tell you the right places to go to to get more information.

[17:00 UTC](http://www.timeanddate.com/worldclock/fixedtime.html?month=4&day=13&year=2011&hour=17&min=0&sec=0&p1=0)\
***Make your applications work in the cloud with Ubuntu One*** - [Stuart Langridge](https://launchpad.net/%7Esil "LaunchpadHome")\
Who else than the [Ubuntu One](https://one.ubuntu.com/) mastermind himself could tell you better about supercharging your apps with cloud functionality? Join Stuart in this talk where he'll be describing how to integrate Ubuntu One into your applications and bring your users to cloud 9 ;)

[18:00 UTC](http://www.timeanddate.com/worldclock/fixedtime.html?month=4&day=13&year=2011&hour=18&min=0&sec=0&p1=0)\
***Take control of your desktop easily with DBus*** - [Alejandro J. Cura](https://launchpad.net/%7Ealecu "LaunchpadHome")\
[D-Bus](http://www.freedesktop.org/wiki/Software/dbus), the cross-desktop message bus system, is becoming more and more ubiquitous in any Free Software distribution. You can bring your applications to a whole new level letting them talk to other ones in a desktop session, and Alejandro can tell you exactly how to do that.

[19:00 UTC](http://www.timeanddate.com/worldclock/fixedtime.html?month=4&day=13&year=2011&hour=19&min=0&sec=0&p1=0)\
***Touchégg: Bringing Multitouch Gestures to your Desktop*** - [José Expósito](https://launchpad.net/%7Ejose-exposito89 "LaunchpadHome")\
It's always great to see real-world examples of how the newest and coolest technologies are being used. José will be showcasing his multitouch-based application, Touchégg, introducing its features, describing how to add new multitouch gestures, the technologies used to develop it, and how it uses the uTouch-GEIS API. Check out the [summary](http://davidplanella.wordpress.com/2011/04/12/off-to-a-great-start-ubuntu-app-developer-week-day-1/) and the logs from the other Multitouch session on Monday to learn more.

[20:00 UTC](http://www.timeanddate.com/worldclock/fixedtime.html?month=4&day=13&year=2011&hour=20&min=0&sec=0&p1=0)\
***Unity: Integrating with Launcher and Places*** - [Mikkel Kamstrup Erlandsen](https://launchpad.net/%7Ekamstrup "LaunchpadHome")\
Do you want your application to seamlessly blend into the new Ubuntu user interface experience? Do you want it to provide all interaction capabilities that [Unity](http://unity.ubuntu.com/) provides? Then join Unity developer Mikkel Kamstrup in his walkthrough with examples on how to plug your app into the Launcher and Places API.

[21:00 UTC](http://www.timeanddate.com/worldclock/fixedtime.html?month=4&day=13&year=2011&hour=21&min=0&sec=0&p1=0)\
***Tracking Source Code History with Bazaar*** - [Jelmer Vernooij](https://launchpad.net/%7Ejelmer "LaunchpadHome")\
Learn how to control the history of your source code with a distributed and modern revision control system. [Bazaar](http://bazaar.canonical.com/) is powerful, fast, and most importantly, easy and fun to use. Jelmer has had a lot to do in developing Bazaar, so he knows well what he's talking about. Join him in this session where he'll tell you the basics and more sophisticated uses of the revision control system used to develop Ubuntu and thousands of other projects in [Launchpad](https://launchpad.net/).

Looking forward to seeing you all there in a few hours!

[<img src="/wp-content/uploads/2011/04/rect3827.png" title="Join Ubuntu App Developer Week" class="aligncenter" width="154" height="42" />](http://webchat.freenode.net/?channels=ubuntu-classroom)
