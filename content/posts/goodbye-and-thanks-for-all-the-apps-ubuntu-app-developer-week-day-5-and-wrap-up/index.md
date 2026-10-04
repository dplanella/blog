---
title: "Goodbye And Thanks For All the Apps: Ubuntu App Developer Week - Day 5 And Wrap-Up"
slug: "goodbye-and-thanks-for-all-the-apps-ubuntu-app-developer-week-day-5-and-wrap-up"
date: 2011-09-13T17:45:58.000Z
tags: ["appdeveloperweek", "apps-tag", "go", "goocanvas", "indicators", "launchpad", "libgrip", "multitouch", "pygame", "python", "qml", "qt", "qt-quick", "quickly", "summary", "ubuntu", "ubuntu-one", "unity"]
---

<img src="/wp-content/uploads/2011/09/uadw.png" title="Ubuntu App Developer Week" class="aligncenter size-full wp-image-1308" width="384" height="256" />

Another edition of the Ubuntu App Developer Week and another amazing knowledge sharing fest around everything related to application development in Ubuntu. Brought to you by a range of the best experts in the field, here's just a sample of the topics they talked about: *App Developer Strategy, Bazaar, Bazaar Explorer, Launchpad, Python, Internationalization, Launchpad Translations, Unity, Unity 2D, Gedit Developer Plugins, the MyApps Portal, the App Review Board, the UbuntuSoftware Centre, Unity Mail, Launchpad Daily Builds, Ubuntu One APIs, Rapid App Development, Quickly, GooCanvas, PyGame, Unity Launcher, Vala, the App Developer Site, Indicators, Python Desktop Integration, Libgrip, Multitouch, Unity Lenses, Ubuntu One Files Integration, The Business Side of Apps, Go, Qt Quick*... and more. Oh my!

And a pick of what they had to say:

> We believe that to get Ubuntu from 20 million to 200 million users, we need more and better apps on Ubuntu [Jonathan Lange](https://launchpad.net/~jml) on making Ubuntu a target for app developers

> Bazaar is the world's finest revision control system [Jonathan Riddell](https://launchpad.net/~jr) on Bazaar

> So you've got your stuff, wherever you are, whichever device you're on [Stuart Langridge](https://launchpad.net/%7Esil) on Ubuntu One

> Oneiric's EOG and Evince will be gesture-enabled out of the box [Jussi Pakkanen](https://launchpad.net/~jpakkane) on multitouch in Ubuntu 11.10

> I control the upper right corner of your screen ;-) [Ted Gould](https://launchpad.net/~ted) on Indicators

If you happened to miss any of the sessions, you’ll find the logs for all of them on the [Ubuntu App Developer Week page](https://wiki.ubuntu.com/UbuntuAppDeveloperWeek/), and the summaries for each day on the links below:

- [Day 1 Summary](http://davidplanella.wordpress.com/2011/09/06/great-is-the-art-of-beginning-ubuntu-app-developer-week-day-1/)
- [Day 2 Summary](http://davidplanella.wordpress.com/2011/09/07/ramping-up-ubuntu-app-developer-week-day-2/)
- [Day 3 Summary](http://davidplanella.wordpress.com/2011/09/08/knowing-your-destination-is-half-the-journey-ubuntu-app-developer-week-day-3/)
- [Day 4 Summary](http://davidplanella.wordpress.com/2011/09/09/all-good-things-come-to-an-end-ubuntu-app-developer-week-day-4/)
- Day 5 Summary (this post)

## Ubuntu App Developer Week - Day 5 Summary

The last day came with a surprise: an extra session for all of those who wanted to know more about Qt Quick and QML. Here are the summaries:

### Getting A Grip on Your Apps: Multitouch on GTK apps using Libgrip

*By [Jussi Pakkanen](https://launchpad.net/%7Ejpakkane "LaunchpadHome")*

<img src="/wp-content/uploads/2011/09/jussipakkanen1.jpg" title="Jussi Pakkanen" class="alignleft" width="64" height="64" />In his session, Jussi talked about one of the most interesting technologies where Ubuntu is leading the way in the open source world: multitouch. Walking the audience through the [Grip Tutorial](https://wiki.ubuntu.com/Multitouch/GripTutorial), he described how to add gesture support to existing applications based on GTK+ 3. He chose to focus on the higher layer of the uTouch stack, where he explained the concepts on which libgrip, the gesture library, is built upon, such as device types and subscriptions. After having explored in detail the code examples, he then revealed that in Oneiric Eye Of GNOME and Evince, Ubuntu's default image viewer and default PDF reader, will be gesture-enabled.

Check out the [session log](https://wiki.ubuntu.com/MeetingLogs/appdevweek1109/MultitouchGtkUsingLibgrip).

### Creating a Google Docs Lens

*By [Neil Patel](https://launchpad.net/%7Enjpatel "LaunchpadHome")*

<img src="/wp-content/uploads/2011/09/njpatel1.jpg" title="Neil Patel" class="alignleft" width="64" height="64" />Neil introduced his session explaining the background behind Lenses: a re-architecture effort of the now superseded Places concept to make them more powerful, provide more features and make it easier to add features through a re-engineered API. Lenses create its own instance, add categories, filters and leave the searching to Scopes. The Lenses/Scopes pairs are purely requests for data, independent of the type of UI, and being provided by the libunity library, they can be written in any of the programming languages supported by GObject Introspection (Python, Javascript, C/C++, Vala, etc.). To illustrate all of this concepts, Neil devoted the rest of the session to a real example of creating a Lens for Google Docs.

Check out the [session log](https://wiki.ubuntu.com/MeetingLogs/appdevweek1109/CreatingGoogleDocsLens).

### Practical Ubuntu One Files Integration

*By [Michael Terry](https://launchpad.net/%7Emterry "LaunchpadHome")*

[<img src="/wp-content/uploads/2011/09/mterry.png" title="Michael Terry" class="alignleft" width="64" height="64" />](/wp-content/uploads/2011/09/stuartlangridge.jpg)Another hands-on session from Michael, with a real world example on how to supercharge apps with cloud support. Using his experience in integrating the Ubuntu One Files API to Deja Dup, the default backup application in Ubuntu, he went in detail through the code of a simple program to talk to a user's personal Ubuntu One file storage area. We liked Michael's session so much that it will very soon be featured as a tutorial on developer.ubuntu.com!

Check out the [session log](https://wiki.ubuntu.com/MeetingLogs/appdevweek1109/UbuntuOneFilesIntegration) and Michael's [awesome notes](https://wiki.ubuntu.com/mterry/UbuntuOneFilesNotes11.10).

### Publishing Your Apps in the Software Center: The Business Side

*By [John Pugh](https://launchpad.net/%7Ejpugh "LaunchpadHome")*

[<img src="/wp-content/uploads/2011/09/johnpugh.jpeg" title="John Pugh" class="alignleft" width="64" height="64" />](/wp-content/uploads/2011/09/johnpugh.jpeg)Ubuntu directly benefits from Canonical becoming a sustainable business to support its development, and that's exactly what John talked about. Being responsible for business development in the Ubuntu Software Centre, he's got a privileged  insight on how to make it happen. He started off explaining that the main goal is to present Ubuntu users with a large catalog of apps available for purchase, and then continued concentrating on how to submit paid applications to be published in the Software Centre. A simple 5-step process, the behind-the-scenes work can be summarized in: Canonical helps packaging the app, it hosts the app and provides the payment via pay.ubuntu.com, in a 80%/20% split. Other highlights include the facts that only non-DRM, non-licensed apps cannot be submitted right now, but there is ongoing work to implement license key support, and that MyApps, the online app submission portal, can take any nearly any content: apps with adverts, "free" online game clients and HTML5 apps.

Check out the [session log](https://wiki.ubuntu.com/MeetingLogs/appdevweek1109/SoftwareCenterTheBusinessSide).

### Writing an App with Go

*By [Gustavo Niemeyer](https://launchpad.net/%7Eniemeyer "LaunchpadHome")*

[<img src="/wp-content/uploads/2011/09/niemeyer.jpeg" title="Gustavo Niemeyer" class="alignleft" width="64" height="64" />](/wp-content/uploads/2011/09/lucabruno.png)Gustavo's enthusiasm for [Go](http://golang.org/), the new programming language created by Google shows every time you start a conversation with him on that topic. And it showed as well on this session, in which he created yet another "Hello world" application in a new language -you guessed-: Go. Along the way, he had time to describe all of the features of this new addition of the extensive family of programming languages: statically compiled with good reflection capabilities, structural typing, interfaces and more.

Check out the [session log](https://wiki.ubuntu.com/MeetingLogs/appdevweek1109/WritingAnAppWithGo).

### Qt Quick At A Pace

*By [Donald Carr](https://launchpad.net/%7Esirspudd-gmail "LaunchpadHome")*

[<img src="/wp-content/uploads/2011/09/donaldcarr.png" title="Donald Carr" class="alignleft" width="64" height="64" />](/wp-content/uploads/2011/09/lucabruno.png)Closing the week on the last -and surprise- session, we had the luxury of having Donald, from the Nokia Qt team, the makers of Qt itself, to talk about Qt Quick. Using a clear and concise definition, Qt Quick is an umbrella term used to refer to QML and its associated tooling; QML being a declarative markup language with tight bindings to Javascript. A technology equally suited to mobile or to the desktop, QML enables developers to rapidly create animation-rich, pixmap-oriented UIs. Through the [qtmediahub](http://gitorious.org/qtmediahub) and [Qt tutorial examples](http://qt.nokia.com/learning/online/training/materials/qt-essentials-qt-quick-edition), he explored QML's capabilities and offered good practices for succesfully developing QML-based projects.

Check out the [session log](https://wiki.ubuntu.com/MeetingLogs/appdevweek1109/QtQuickAtAPace).

## Wrapping Up

Finally, if you've got any feedback on UADW, on how to make it better, things you enjoyed or things you believe should be improved, your comments will be very appreciated and useful to tailor this event to your needs.

Thanks a lot for participating. I hope you enjoyed it  as much as I did, and see you again in 6 months time for another week full with app development goodness\![\
](http://webchat.freenode.net/?channels=ubuntu-classroom)
