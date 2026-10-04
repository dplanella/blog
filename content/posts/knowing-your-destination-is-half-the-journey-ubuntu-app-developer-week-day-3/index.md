---
title: "Knowing Your Destination Is Half The Journey: Ubuntu App Developer Week - Day 3"
slug: "knowing-your-destination-is-half-the-journey-ubuntu-app-developer-week-day-3"
date: 2011-09-08T16:33:57.000Z
tags: ["appdeveloperweek", "apps-tag", "launchpad", "ppa", "summary", "ubuntu", "ubuntu-one", "unity", "vala"]
---

## Ubuntu App Developer Week - Day 3 Summary

Time flies and we're already halfway through UADW, but there is still much to come! Here's yesterday report for your reading pleasure:

### Unity Mail: Webmail Notification on Your Desktop

*By [Dmitry Shachnev](https://launchpad.net/%7Emitya57 "LaunchpadHome")*

<img src="/wp-content/uploads/2011/09/mitya1.jpg" title="Dmitry Shachnev" class="alignleft" width="64" height="64" />Starting off with a description of the features of [Unity Mail](https://launchpad.net/unity-mail), such as displaying webmail unread message count, notifications and mail subjects, we then learned more about how it was developed and the technologies that were used to create it. It's written in Python, using GObject introspection (PyGI) and integrates with Ubuntu through the Unity, Notify and Indicate modules. After describing each one in more detail, Dmitry continued talking about how the app can be translated using Launchpad, and how he uses the Bazaar  source revision control system to work with code history. Wrapping up, he went through the plans for the future: more configuration options, marking all messages as read and the need for a new icon. Any takers? ;)

Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1109/UnityMailWebMailNotification).

### Launchpad Daily Builds and Rapid Feedback: Writing Recipe Builds

*By [Jelmer Vernooij](https://launchpad.net/%7Ejelmer "LaunchpadHome")*

<img src="/wp-content/uploads/2011/09/jelmervernooij.jpg" title="Jelmer Vernooij" class="alignleft" width="64" height="64" />Assuming some previous knowledge on Debian packaging, in his session Jelmer walked the audience through a practical example of a basic recipe build for a small project: pydoctor. Drawing the cooking recipe analogy, package recipes are a description of the ingredients (source code branches) and how to put them together, ending up with a delicious Debian package for users to enjoy. Launchpad can build packages from recipes once or automatically on a daily basis provided the code has changed, conveniently placing the result in a [PPA](https://launchpad.net/ubuntu/+ppas). In the last part of the session, he described in detail the contents of an existing recipe and added some notes on best practices when building from a recipe.

Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1109/LaunchpadDailyBuildsRapidFeedback).

### Using the Ubuntu One APIs for Your Apps: An Overview

*By [Stuart Langridge](https://launchpad.net/%7Esil "LaunchpadHome")*

[<img src="/wp-content/uploads/2011/09/stuartlangridge.jpg" title="Stuart Langridge" class="alignleft" width="64" height="64" />](/wp-content/uploads/2011/09/stuartlangridge.jpg)The idea bahind the Ubuntu One developer programme is to make it easy to add the cloud to your apps and make new apps for the cloud. With this opening line, Stuart delivered a talk about a high-level overview on the cool things you can do as an app developer adding Ubuntu One support. One aspect it data: for example building applications that work on the desktop, on mobile phones and on the web, securely sharing data among users. Another is music: streaming, streaming music and sharing playlists on the desktop, on mobile and from the web, all through a simple REST HTTP API. He also mentioned some examples of cloud enabled applications: Shutter and Deja-Dup, and many other interesting ways to use Ubuntu One to do exciting thigs with data. And you can get started already using the [available documentation](https://one.ubuntu.com/developer).

Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1109/UsingUbuntuOneApis).

### Supercharging Your Apps with Unity Launcher Integration

*By [Jason Smith](https://launchpad.net/%7Ejassmith "LaunchpadHome")*

[<img src="/wp-content/uploads/2011/09/jasonsmith.jpg" title="Jason Smith" class="alignleft" width="64" height="64" />](/wp-content/uploads/2011/09/jasonsmith.jpg)In his talk, Jason first went through the terminology that covers the elements related to the Unity Launcher, and the bachground behind the Launcher API, implemented in the libunity library. Libunity can be used in many programming languages: Python, C, Vala and others supported by GObject Introspection. Going through what you can do with the Launcher (marking/unmarking apps as urgent, setting object counts, setting progress on objects and adding quicklist menu items to the object), he used Vala snippets to illustrate each feature with code.

Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1109/UnityLauncherIntegration).

### Hello Vala: An Introduction to the Vala Language

*By [Luca Bruno](http://lethalman.blogspot.com/)*

[<img src="/wp-content/uploads/2011/09/lucabruno.png" title="Luca Bruno" class="alignleft" width="64" height="64" />](/wp-content/uploads/2011/09/lucabruno.png)[Vala](http://live.gnome.org/Vala), a new programming language with C#-like syntax that compiles to C and targets the GObject type system: with a clear statement of what Vala is and what it can do, Luca, a contributor to the project introduced one by one the mostkey features of the language through his "Hello world" example: namespaces, types, classes, properties, keywords and more. As a highlight he mentioned Vala's automatic memory management using reference counting, andits interoperability with other languages, most notably C, but it can also work with many others supported by GObject Introspection. Other cool featuresto note were also error handling on top of GError, support for async operations, closures and DBus client/server, on each of which he elaborated before finishing the session.

Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1109/HelloValaIntroduction).

## The Day Ahead: Upcoming Sessions for Day 3

Another day, another awesome set of sessions coming up:

[16.00 UTC](http://www.timeanddate.com/worldclock/fixedtime.html?month=9&day=8&year=2011&hour=16&min=0&sec=0&p1=0) - **Creating an App Developer Website: developer.ubuntu.com**

<img src="/wp-content/uploads/2011/09/johnoxton.jpeg" title="John Oxton" class="alignleft size-full wp-image-1269" width="64" height="64" /><img src="/wp-content/uploads/2011/09/468171231f740a6eaf57b763b726594f.jpeg" title="David Planella" class="alignleft" width="64" height="64" /> Ubuntu 11.10 will not only bring new features to the OS itself. In time for the release we'll be launching the new Ubuntu App Developer site, a place for developers to find all the infromation and the resources they need to get started creating, submitting and publishing their apps in Ubuntu. [John Oxton](https://launchpad.net/~johnoxton), [David Planella](https://launchpad.net/~dpm) and many other people have worked to make the next developer.ubuntu.com possible and will tell you all about it.

[17:00 UTC](http://www.timeanddate.com/worldclock/fixedtime.html?month=9&day=8&year=2011&hour=17&min=0&sec=0&p1=0) - **Rapid App Development with Quickly**

<img src="/wp-content/uploads/2011/09/mterry.png" title="Michael Terry" class="alignleft size-full wp-image-1270" width="64" height="64" />[Quickly](https://wiki.ubuntu.com/Quickly) is a wrapper that pulls together all the recommended tools and technologies to bring apps from creation and through their whole life cycle in Ubuntu. With an easy set of commands that hide all the complexity for your, it effectively enables developers to follow rapid development principles and worry only about writing code. [Michael Terry](https://launchpad.net/~mterry), from the Quickly development team will be looking forward to guide you through the first steps with this awesome tool.

[18:00 UTC](http://www.timeanddate.com/worldclock/fixedtime.html?month=9&day=87&year=2011&hour=18&min=0&sec=0&p1=0) **- Developing with Freeform Design Surfaces: GooCanvas and PyGame**

[<img src="/wp-content/uploads/2011/09/rickspencer.jpg" title="Rick Spencer" class="alignleft size-full wp-image-1271" width="64" height="64" />](/wp-content/uploads/2011/09/stuartlangridge.jpg)Have you ever wondered what freeform design surfaces, or canvases are? You probably have now. Well, lucky you then, because [Rick Spencer](https://launchpad.net/~rick-rickspencer3) will be here to tell you what they're good for and how to get started with them ;)

[19:00 UTC](http://www.timeanddate.com/worldclock/fixedtime.html?month=9&day=8&year=2011&hour=19&min=0&sec=0&p1=0) - **Making your app appear in the Indicators**

[<img src="/wp-content/uploads/2011/09/tedgould.jpg" title="Ted Gould" class="alignleft size-full wp-image-1272" width="64" height="64" />](/wp-content/uploads/2011/09/jasonsmith.jpg)In another session on how to integrate with the platform, [Ted Gould](https://launchpad.net/~ted), the man who knows most about them, will describe how to add [indicator](https://wiki.ubuntu.com/DesktopExperienceTeam/ApplicationIndicators) features  to your apps, both in terms of panel indicators and messaging menu support.

[20:00 UTC](http://www.timeanddate.com/worldclock/fixedtime.html?month=9&day=8&year=2011&hour=20&min=0&sec=0&p1=0)** - Will it Blend? Python Libraries for Desktop Integration**

[<img src="/wp-content/uploads/2011/09/person-logo.png" title="person-logo" class="alignleft size-full wp-image-1273" width="64" height="64" />](/wp-content/uploads/2011/09/lucabruno.png)You certainly will want your app to have that familiar look and feel at home in the OS it's running on, but you'll also want it to use all the backend technologies to integrate even deeper and provide a great user experience. Well, fear not, for [Marcelo Hashimot](https://launchpad.net/~conscioususer)o is here to tell you exactly how to do that!

Looking forward to seeing you all there in a few hours!

[<img src="/wp-content/uploads/2011/04/rect3827.png" title="Join Ubuntu App Developer Week" class="aligncenter" width="154" height="42" />](http://webchat.freenode.net/?channels=ubuntu-classroom)
