---
title: "Off to a Great Start: Ubuntu App Developer Week - Day 1"
slug: "off-to-a-great-start-ubuntu-app-developer-week-day-1"
date: 2011-04-12T16:55:55.000Z
tags: ["appdeveloperweek", "development", "summary", "ubuntu"]
---

## Ubuntu App Developer Week - Day 1 Summary

A great start for a great week. Looking at the lots of participation and questions during the first day shows that developing applications in Ubuntu is a hot topic. Here is a small summary from yesterday's schedule.

### Enabling Multitouch and Gestures Using uTouch

*By [Chase Douglas](https://launchpad.net/%7Echasedouglas "LaunchpadHome") and [Stephen Webb](https://launchpad.net/%7Ebregma "LaunchpadHome")*

Chase and Stephen delivered an overview on the whole stack of touch technologies focusing on two main aspects: gestures/uTouch and multitouch. On gestures, they showed us how there is a difference between general-purpose stroke gestures and defined gestures primitives, such as "drag", "pinch/expand", "rotate", "tap", and "touch", which enable the possibility of defining a gesture language. A [high-level overview of uTouch](https://docs.google.com/drawings/edit?id=1isTrkSWDH7OWKLi_aialasw9xjb0pziK9yjKUR1yt9c&hl=en&authkey=CLiA9fEG&pli=1) followed, with a description of the API and a couple of [code examples](http://pastebin.com/ju1Tgq4N) showing how to integrate applications with it. To wrap up the session, they explained how Ubuntu will be the first distro to bring multitouch in 11.04 and how this was made possible, such as extending xorg's XInput to version 2.1 to add multitouch support and. On the app developer side of multitouch, they announced a pre-release addition to the Qt framework that will support multitouch.

Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1104/Multitouch).

### GObject Introspection: The New Way For Developing GNOME Apps in Python, JavaScript and Others

*By* *[Tomeu Vizoso](https://launchpad.net/%7Etomeu "LaunchpadHome")*[](https://launchpad.net/%7Etomeu "LaunchpadHome")

On this session we saw the initial problem GNOME developers were facing in the past to provide and maintain bindings in multiple programming languages, and how introspection came to the rescue. The reason for having several bindings had always been to enable interaction with the GNOME platform using other languages than C. With introspection, there is no need for external bindings, as the C API itself contains all the required information. Not only that, but this information is also available at runtime without a considerable performance cost. He then went on to describe the workflow changes, the new typelibs and .gir files, and describing what annotations are. Following that, the changes required for library and, most especially application writers, sharing some tips on how to [port applications](http://live.gnome.org/PyGObject/IntrospectionPorting) to use GObject Introspection. He finished the session with a few pointers on where to go from here and to the resources to get more info about introspection.

Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1104/GObjectIntrospection).

### From English to any language: internationalizing your apps

*By [David Planella](https://launchpad.net/%7Edpm "LaunchpadHome")*

The session started of with the description of some of the main players in the internationalization game: gettext, intltool, Launchpad, followed by a bit more insight on the gettext concepts and terminology. The idea was to deliver a hands-on session that could be nevertheless used generically to provide i18n support to any application in any programming language. The second part of the session focused on making a choice of a programming language and framework to showcase a practical example on how to internationalize an app. So Python and Quickly were used as an easy way to develop an internationalized application in a matter of minutes. From [that example](http://bazaar.launchpad.net/~dpm/+junk/awesometranslations/files) the session then focused on describing the main bits to provide native language support.*\*

Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1104/InternationalizingApps).

### Widgetcraft: The Art of Creating Plasma Widgets

***By [Harald Sitter](https://launchpad.net/%7Eapachelogger "LaunchpadHome")***

On this session packed with code examples, Harald started with the description of the technologies involved in developing widgets for Plasma, otherwise known as the KDE desktop or the KDE workspace, and how Plasma comes in several different flavours for different form factors. Next were Plasmoids, the name by which Plasma widgets go, which can be written in Javascript, C++ (both always available), Python,  and Ruby*. He then moved on to hacking, creating an easy-to-follow, bare setup for a Plasmoid, mentioning how the* plasmoidviewer tool can be used to test them prior to deployment. The next steps involved extending the Plasmoid, adding UI functionality such as buttons and other visual elements. All the code is available [here](http://people.ubuntu.com/~apachelogger/uadw/04.11/dont-blink/).

Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1104/PlasmaWidgetcraft).

### Rock solid Python development with unittest/doctest

*By [Barry Warsaw](https://launchpad.net/%7Ebarry "LaunchpadHome")*

Barry delivered a great overview to unit- and doc- testing Python applications, and how to hook these into Debian packages as well. After briefly pointing out to resources for background reading on testing, he then delved into the [coding example](http://bazaar.launchpad.net/~barry/+junk/adw/files) he had set up to as an aid to the session. Starting with unittesting, he showed us the tests were set up in the code and how to run them, as well as what a failing test looks like. Next on the list were doctests, emphasizing that they are testable documentation, written in restructured text (.rst), and that they do not replace, but rather are a complement to unittests. Again, he showed us how they were written and run. He wrapped up explaining in detail how to integrate them all in setup.py and to a Debian package.

Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1104/RockSolidPython).

## The Day Ahead: Upcoming Sessions for Day 2

Well, you thought that was all? Lots of additional app developer goodness are waiting for you today. Let's have a look at what's in store for day 2:

[16.00 UTC](http://www.timeanddate.com/worldclock/fixedtime.html?month=4&day=12&year=2011&hour=16&min=0&sec=0&p1=0)\
***PyGTK is dead, long live PyGI! Using gobject-introspection in Python*** - [Martin Pitt](https://launchpad.net/%7Epitti "LaunchpadHome")\
PyGTK might be dead, but only to be succeeded by the power of introspection. Join Martin to learn all you ever wanted to know about using the new cool stuff in the Python/GTK world: PyGI. He [tells us](http://www.piware.de/2011/04/pygtk-is-dead-long-live-pygi-app-developer-week-talk/) about the focus of his talk: "*\[...\] how to use the GI typelibs in Python, and how to port PyGTK2 applications to PyGI. For the most part these sessions are distribution neutral (we don’t have any special sauce for this in Debian/Ubuntu, it all happened right upstream ![:-)](http://www.piware.de/wp/wp-includes/images/smilies/icon_smile.gif) ); only a very small fraction of it (where I explain package names, etc.) will be specific to Debian/Ubuntu, but shouldn’t be hard to apply to other distributions as well.*"

[17:00 UTC](http://www.timeanddate.com/worldclock/fixedtime.html?month=4&day=12&year=2011&hour=17&min=0&sec=0&p1=0)\
***Zeitgeist API & Zeitgeist Application Integration*** - [Manish Sinha (मनीष सिन्हा)](https://launchpad.net/%7Emanishsinha "LaunchpadHome") and [Seif Lotfy](https://launchpad.net/%7Eseif "LaunchpadHome")\
The [Zeitgeist Project](http://zeitgeist-project.com/about/) is taking many important projects and distributions by storm. It's all about seamlessly tracking user data and events in a way that is revolutionizing the way they interact with their desktop. Do you want to know more about Zeitgest? Or even better: do you want to use Zeitgeist features in your application? Project leader Seif Lotfy and developer Manish Sinha will tell you all about it and be willing to hear your questions

[18:00 UTC](http://www.timeanddate.com/worldclock/fixedtime.html?month=4&day=12&year=2011&hour=18&min=0&sec=0&p1=0)\
***GStreamer+Python: Multimedia Swiss Army Machete*** - [Jason DeRose](https://launchpad.net/%7Ejderose "LaunchpadHome")\
When you hear [GStreamer](http://gstreamer.freedesktop.org/) and [Python](http://python.org/) in the same sentence you know for sure that you're up for something awesome. Join the power of Rapid Application Development with Python with the most popular multimedia framework in Free Software, and you'll end up with a versatile tool to tackle all your multimedia needs. Jason knows well what he's talking about

[19:00 UTC](http://www.timeanddate.com/worldclock/fixedtime.html?month=4&day=12&year=2011&hour=19&min=0&sec=0&p1=0)\
***Creating a KDE app with KAppTemplate*** - [Jonathan Thomas](https://launchpad.net/%7Eechidnaman "LaunchpadHome")\
Second day in and we get the luxury of having the second KDE/Kubuntu ninja delivering content straight from the source. Do you know how easy is to create full featured KDE applications with [KAppTemplate](http://www.kde.org/applications/development/kapptemplate/)? Put on your developer hat and join Jonathan on a hands-on session where you'll learn to write beautiful KDE apps in a matter of minutes.

[20:00 UTC](http://www.timeanddate.com/worldclock/fixedtime.html?month=4&day=12&year=2011&hour=20&min=0&sec=0&p1=0)\
***Thunderbird + Unity = Awesome, and how JSCtypes lets you get to the candy*** - [Mike Conley](https://launchpad.net/%7Emconley "LaunchpadHome")\
We're seeing more and more major upstreams providing integration with the new way of interacting with computers: Unity. The story of [integrating Thunderbird and Unity](http://mikeconley.ca/blog/2011/03/15/my-campaign-to-get-thunderbird-integrated-into-ubuntu-natty-narwhal-continues/) is full of awesome, and Mike will be on a quest to tell you all about it and hear your questions.

[21:00 UTC](http://www.timeanddate.com/worldclock/fixedtime.html?month=4&day=12&year=2011&hour=21&min=0&sec=0&p1=0)\
***STORY: Unity, hacking on a real-world app*** - [Marco Trevisan](https://launchpad.net/%7E3v1n0 "LaunchpadHome")\
Would you like to become the next Unity rockstar? How would you get started? In this session Marco will tell us his journey on how he got involved in hacking on Unity, from the day he found the itch to scratch until his branch fixing it was landed. I'm personally very much looking forward to this session, as I believe it will be inspiring not only to prospective Unity contributors, but for developers in general who want to know how to start hacking on a particular application.

Looking forward to seeing you all there in a few hours!

[<img src="/wp-content/uploads/2011/04/rect3827.png" title="Join Ubuntu App Developer Week" class="aligncenter" width="154" height="42" />](http://webchat.freenode.net/?channels=ubuntu-classroom)
