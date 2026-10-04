---
title: "Daily build awesomeness"
slug: "daily-build-awesomeness"
date: 2010-06-30T11:35:50.000Z
tags: ["daily-builds", "launchpad", "translations"]
---

Today I'd like to let you know about a very cool [Launchpad](http://www.launchpad.net/) feature: Daily Builds.

In a nutshell: daily builds get Launchpad to work for developers and produce automatically or semi-automatically built packages of the latest code, ready for everyone to test and taste.

With daily builds you'll be able to:

- Make your software available to early adopters and testers very easily
- Facilitate the work of testers and thus improve your software's QA process

If that wheted your appetite, [check out the documentation](https://wiki.ubuntu.com/DailyBuilds) for more detailed info.

As I'm slightly biased towards everything that's got to do with translations, I cannot but think how cool it will be to combine the existing functionality in Launchpad to integrate [translations](https://help.launchpad.net/Translations), [bzr branches](https://help.launchpad.net/Code) and [daily builds](https://wiki.ubuntu.com/DailyBuilds). I can imagine the following scenario and chain of events:

**Day 1:**\
A translator [translates a string in Launchpad](https://translations.launchpad.net/ubuntu)

**Day 1, a bit later:**\
That translated string is [automatically committed to a bzr branch](http://blog.launchpad.net/general/exporting-translations-to-a-bazaar-branch)

**Day 1, even a bit later:**\
A daily package is built from the [bzr branch](https://help.launchpad.net/Code) and released in a [PPA](https://help.launchpad.net/Packaging/PPA)

**Day 1, finally:**\
The translator and everyone else can easily install the PPA, containing the new translation ready to test with the application

That's just an example on how this awesome functionality can be used, today. I'm sure you can find many other interesting uses for daily builds!
