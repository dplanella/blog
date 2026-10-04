---
title: "Ramping Up: Ubuntu App Developer Week - Day 2"
slug: "ramping-up-ubuntu-app-developer-week-day-2"
date: 2011-09-07T14:33:03.000Z
tags: ["apparmor", "appdeveloperweek", "apps-tag", "gedit", "launchpad", "launchpad-translations", "summary", "translations", "ubuntu", "unity"]
---

## Ubuntu App Developer Week - Day 2 Summary

Another app developer day is over and we're nearly halfway through the week. Here's what happened yesterday:

### Making Your App Speak Languages with Launchpad Translations

*By <a href="https://launchpad.net/%7Edpm" class="interwiki" title="LaunchpadHome">David Planella</a>*

<img src="/wp-content/uploads/2011/09/468171231f740a6eaf57b763b726594f.jpeg" title="David Planella" class="alignleft" width="64" height="64" />In this session we learned how to link up an app that already has internationalization support to [Launchpad Translations](https://translations.launchpad.net/), so that it is exposed to Launchpad's extensive community of translators who'll effectively make your app speak almost any language. From setting up code hosting for a seamless integration, to setting up the translations settings to tips and tricks for best practices, the presentation should give developers a good grasp of how to start getting their apps translated and ready to reach a wider audience.

Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1109/MakingYourAppSpeakLanguageswithLaunchpadTranslations).

### The Making of Unity 2D

*By <a href="https://launchpad.net/%7Efboucault" class="interwiki" title="LaunchpadHome">Florian Boucault</a>*

<img src="/wp-content/uploads/2011/09/5715719850_9283e48226.jpg" title="Florian Boucault" class="alignleft" width="64" height="64" />An interactive and popular session, in which Florian started describing the main goal behind the Unity 2D project: to run on platforms that do not provide accelerated [OpenGL](http://www.opengl.org/). It essentially is an implementation of the main Unity user interface using the [Qt toolkit](http://qt.nokia.com/) and the [QML](http://qt.nokia.com/qtquick/) declarative language, while reusing the backend technologies from Unity. From there he went on describing the Unity 2D architecture and the release policy, pointing out to the [Unity 2D daily PPA](https://launchpad.net/~unity-2d-team/+archive/unity-2d-daily), for those testers who want to be on the bleeding edge., and wrapped up answering the questions from the audience.

Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1109/TheMakingofUnity2D).

### Making App Development Easy: Gedit Developer Plugins

*By <a href="https://launchpad.net/%7Esinzui" class="interwiki" title="LaunchpadHome">Curtis Hovey</a>*

<img src="/wp-content/uploads/2011/09/333622-96-20101203165819.png" title="Curtis Hovey" class="alignleft" width="64" height="64" />Starting off with a description of Gedit plugins, their purpose and how to install them, Curtis delved into the [general-purpose plugins](http://apt.ubuntu.com/p/gedit-plugins) and the [developer plugins](http://apt.ubuntu.com/p/gedit-developer-plugins) (click to install) plugins, explaining how to set them up and his recommended choice of plugins to convert Gedit in the perfect programming editor. The highlights included the GDP Bazaar integration plug in, which allows working with the bzr source revision control system and others (Subversion, Mercurial, Git), as well as the Source Code Browser plugin, a class and function browser based on Exuberant Ctags.

Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1109/MakingAppDevelopmentEasyGeditDeveloperPlugins).

### Publishing Your Apps in the Software Center: The MyApps Portal

*By <a href="https://launchpad.net/%7Eelachuni" class="interwiki" title="LaunchpadHome">Anthony Lenton</a>*

<img src="/wp-content/uploads/2011/09/tony_small.png" title="Anthony Lenton" class="alignleft size-full wp-image-1232" width="64" height="64" />In another session devoted to the app developer strategy, Anthony told us all about the MyApps webapp developers can use to submit their applications to the Software Center. Available on <https://myapps.developer.ubuntu.com>, it started off as the need to automate the submission of commercial apps to the Software Centre, expanding to a full-blown online portal that can now tackle any type of submission. He then walked the audience through the 5-step process to send an app for review, including all the necessary metadata and payment details. Once an app has been submitted, it needs to be packaged (if it wasn't already) and reviewed before being published. Hinting to Jonathan Lange's session on day 1, Anthony explained that they are looking at providing an automated process for packaging, with the intention of removing the last big remaining manual process.

Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1109/PublishingAppsInSoftwareCenterMyApps).

### Publishing Your Apps in the Software Center: The App Review Board

*By <a href="https://launchpad.net/%7Estgraber" class="interwiki" title="LaunchpadHome">Stéphane Graber</a>*

<img src="/wp-content/uploads/2011/09/52661-96-20090503165741.png" title="Stéphane Graber" class="alignleft size-full wp-image-1233" width="64" height="64" />Complementing the previous session, Stéphane explained how libre+gratis apps can get into the Software Centre and what the App Review Board's (ARB) role is in that process. He focused on how the Board reviews applications and how other types are distributed in Ubuntu. The types of apps reviewed by the ARB are small, lightweight apps, usually of the type created by Quickly (check out the sessions on Quickly on Thursday!). The next upcoming changes in the way this applications are reviewed will most probably include them being submitted through the MyApps online portal and them being made more secure by wrapping them in a container based on AppArmor or Arkose (or a combination of them).

Check out the session log [here](https://wiki.ubuntu.com/MeetingLogs/appdevweek1109/PublishingAppsInSoftwareCenterARB).

## The Day Ahead: Upcoming Sessions for Day 3

Check out today's rocking lineup:

[16.00 UTC](http://www.timeanddate.com/worldclock/fixedtime.html?month=9&day=7&year=2011&hour=16&min=0&sec=0&p1=0) - **Unity Mail: Webmail Notification on Your Desktop**

<img src="/wp-content/uploads/2011/09/mitya1.jpg" title="Dmitry Shachnev" class="alignleft size-full wp-image-1254" width="64" height="64" />We're starting to see more and more apps that integrate with Unity. [Unity Mail](https://launchpad.net/unity-mail) is a cool app that allows you to stay up to date with your web mail directly from your desktop. It supports any IMAP server, but right now it works best with Gmail, along with notifications, message counts, quicklists and more. [Dmitry Shachnev](https://launchpad.net/%7Emitya57 "LaunchpadHome") will tell us about its features and how he put the application together.

[17:00 UTC](http://www.timeanddate.com/worldclock/fixedtime.html?month=9&day=7&year=2011&hour=17&min=0&sec=0&p1=0) - **Launchpad Daily Builds and Rapid Feedback: Writing Recipe Builds**

<img src="/wp-content/uploads/2011/09/jelmervernooij.jpg" title="Jelmer Vernooij" class="alignleft size-full wp-image-1255" width="64" height="64" />Launchpad has many awesome features. This time around [Jelmer Vernooij](https://launchpad.net/%7Ejelmer "LaunchpadHome") will be explaininghow to set up recipe builds for your project in Launchpad, so that users can get  the latest updates easily packaged on a daily basis, so that they can install them at a click of a button and can test them and make the feedback loop as short as possible.

[18:00 UTC](http://www.timeanddate.com/worldclock/fixedtime.html?month=9&day=7&year=2011&hour=18&min=0&sec=0&p1=0) **- Using the Ubuntu One APIs for Your Apps: An Overview**

[<img src="/wp-content/uploads/2011/09/stuartlangridge.jpg" title="Stuart Langridge" class="alignleft size-full wp-image-1256" width="64" height="64" />](/wp-content/uploads/2011/09/stuartlangridge.jpg)Ubuntu One is starting to be everywhere, and it even has its own developer programme. The [Ubuntu One website](https://one.ubuntu.com/developer/) already provides lots of information to developers, and to make it even more clear, [Stuart Langridge](https://launchpad.net/%7Esil "LaunchpadHome") will walk you through the available Ubuntu One APIs you can use to make your application cloud-ready.

[19:00 UTC](http://www.timeanddate.com/worldclock/fixedtime.html?month=9&day=7&year=2011&hour=19&min=0&sec=0&p1=0) - **Supercharging Your Apps with Unity Launcher Integration**

[<img src="/wp-content/uploads/2011/09/jasonsmith.jpg" title="Jason Smith" class="alignleft size-full wp-image-1257" width="64" height="64" />](/wp-content/uploads/2011/09/jasonsmith.jpg)One of the easiest and more visual ways for your apps to blend in with Unity is for it to integrate with the Launcher. Counts, progress indication, quicklists... are an elegant and simple wayto provide feedback to users. [Jason Smith](https://launchpad.net/%7Ejassmith "LaunchpadHome") knows all about Launcher integration, and he's really looking forward to share it with us!

[20:00 UTC](http://www.timeanddate.com/worldclock/fixedtime.html?month=9&day=7&year=2011&hour=20&min=0&sec=0&p1=0)** - Hello Vala: An Introduction to the Vala Language**

[<img src="/wp-content/uploads/2011/09/lucabruno.png" title="Luca Bruno" class="alignleft size-full wp-image-1258" width="64" height="64" />](/wp-content/uploads/2011/09/lucabruno.png)Vala is a powerful programming language that allows modern programming techniques to be used to write applications that run on the GNOME runtime libraries, particularly GLib and GObject. [Luca Bruno](http://lethalman.blogspot.com/) is part of the team that develops Vala itself, and will be introducing us to the first steps to get started with Vala with the universal "Hello world" app becoming "Hello Vala!".

Looking forward to seeing you all there in a few hours!

[<img src="/wp-content/uploads/2011/04/rect3827.png" title="Join Ubuntu App Developer Week" class="aligncenter" width="154" height="42" />](http://webchat.freenode.net/?channels=ubuntu-classroom)
