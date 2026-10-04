---
title: "Maverick UDS Translations Sessions"
slug: "maverick-uds-translations-sessions"
date: 2010-05-05T22:02:16.000Z
tags: ["translations", "ubuntu", "uds"]
---

[<img src="/wp-content/uploads/2010/05/3748161364_5c743407f5.jpg" title="Cautious Meerkats" class="aligncenter size-full wp-image-350" width="480" height="319" alt="Cautious Meerkats" />](http://www.flickr.com/photos/anotherpintplease/3748161364/)

Engines are warming up for the next [Ubuntu Developer Summit](https://wiki.ubuntu.com/UDS) next week in Brussels, and on the Community track we've got a rich set of sessions to discuss a lot of topics around Translations. These will help shaping up the roadmap for the next version of Ubuntu, the Maverick Meerkat.

We discussed the sessions in the [last translations meeting](https://wiki.ubuntu.com/Translations/Meetings/2010-04-22) and they have now all been scheduled. You can also see [the overview on the wiki](https://wiki.ubuntu.com/Translations/UDS), although they will all be tracked from the linked blueprints. Here they are:

1.  **[Translations community roundtable](https://blueprints.launchpad.net/ubuntu/+spec/community-m-translations-community-roundtable "UbuntuSpec")**
    - Unstructured session to discuss and gather feedback on all around the Ubuntu translations community
      - Proposed topic: QA of language packs ([GaborKelemen](https://wiki.ubuntu.com/GaborKelemen)) - asking translators to test each updated package before release may be too much. With on-demand updates, it may be unnecessary to withhold untested updates.
2.  **[Launchpad Translations roundtable](https://blueprints.launchpad.net/ubuntu/+spec/community-m-launchpad-translations-roundtable "UbuntuSpec")**
    - Unstructured session to discuss and gather feedback on all around Launchpad Translations as a tool
3.  **[Desktop and Translations roundtable](https://blueprints.launchpad.net/ubuntu/+spec/community-m-desktop-translations-roundtable "UbuntuSpec")**
    - Roundtable with members of the desktop team to discuss everything related to translations. Proposed topics:
      - Overview of Launchpad Translations changes in Maverick: automatic generation of translation templates, import of translations from upstream bzr branches and translation sharing. This will also be explained in a plenary.
      - Implementing gettext support to PolicyKit
      - Firefox and OpenOffice.org translations
      - Common approach for building POT template on non-desktop packages using plain gettext instead of intltool, e.g. mountall, in the same way as CDBS GNOME packages use `langpack.mk`
      - Could langpack-o-matic build the translated XML files for documentation to be shipped in language packs? Even if we cannot get it to build for all packages, even if only for ubuntu-docs would be a big improvement.
      - Enabling keyboard indicator applet by default on users with a non-Latin alphabet keyboard layout (see [bug 550704](https://bugs.launchpad.net/bugs/550704))?
      - Evaluate the use of mlterm instead of VTE for RTL locales?
4.  **[Kubuntu Translations roundtable](https://blueprints.launchpad.net/ubuntu/+spec/community-m-kubuntu-translations-roundtable "UbuntuSpec")**
    - Unstructured session to discuss and gather feedback on all around Kubuntu translations.
5.  **[Translations Community Advocacy](https://blueprints.launchpad.net/ubuntu/+spec/community-m-translations-community-advocacy "UbuntuSpec")**
    - Session to discuss how to rise awareness on the global Ubuntu Translations community, both within and outside the Ubuntu community.
6.  **[Translations Community Learning Content](https://blueprints.launchpad.net/ubuntu/+spec/community-m-translations-community-learning-content "UbuntuSpec")**
    - Session to discuss ways of providing content to ease start contributing to translations.
7.  **[Translations Community Events](https://blueprints.launchpad.net/ubuntu/+spec/community-m-translations-community-events "UbuntuSpec")**
    - Discuss a series of events throughout the cycle to help promoting the Ubuntu Translations project and increase participation in translating Ubuntu.
8.  **[Extend the translations reporting site](https://blueprints.launchpad.net/ubuntu/+spec/community-lucid-improving-translation-status-reporting "UbuntuSpec")**
    - Continuation of the Lucid blueprint on how to improve how we report translation status for Ubuntu
9.  **[Translation teams health check](https://blueprints.launchpad.net/ubuntu/+spec/community-m-translation-teams-healthcheck "UbuntuSpec")**
    - A session on an effort to get in touch with all of the translations teams for a health check. Make sure to understand their needs and if they need help in any area. Raise awareness on the new team policies, especially on having information on the team's communication channel on their Launchpad page, along with info on how to join the team.
10. **[Launchpad Translations Reporting API](https://blueprints.launchpad.net/ubuntu/+spec/community-m-launchpad-translations-reporting-api "UbuntuSpec")**
    - Discuss the current status and implementation of the Launchpad Translations reporting API, as per the [specification](https://dev.launchpad.net/Translations/Specs/ReportingAPI) Adi is working on.
11. **[Developer education on localization](https://blueprints.launchpad.net/ubuntu/+spec/community-m-developer-education-on-localization "UbuntuSpec")**
    - Get feedback on the creation of a resource with developer reference on localization, extending [the internationalization guide](https://wiki.ubuntu.com/UbuntuDevelopment/Internationalisation).
12. **[Universe is translatable in Launchpad](https://blueprints.launchpad.net/ubuntu/+spec/community-m-universe-is-translatable-in-launchpad "UbuntuSpec")**
    - Session to assess if it's desirable to make all localized applications from universe also translatable in Launchpad, not only those from the main repository.
    - [Previous spec](https://wiki.ubuntu.com/LanguagePacksForUniverse)
13. **[Improve Translations Packaging for Help in Ubuntu Applications](https://blueprints.launchpad.net/ubuntu/+spec/community-m-improve-translations-packaging-for-help-in-ubuntu-applications "UbuntuSpec")**
    - Development of a strategy to provide translatable documentation for Ubuntu applications.
    - This will also allow OEM projects to use documentation and its translations from Ubuntu, installed independently from the monolithic ubuntu-docs package.
    - Ideally the translated documentation should be shipped in language packs.
14. **[Proactive bug detection](https://blueprints.launchpad.net/ubuntu/+spec/community-m-proactive-bug-detection "UbuntuSpec")**
    - Discuss the possibilities of proactive bug detection: this would need more and earlier testing of packages for translation problems (lack of i18n infrastructure, untranslatable files/strings, needs-pot-on-build, needs-desktop-entry-i18n...)
    - We also need to devote more manpower to fix bugs in time, and reducing the average lifespan of bugs. Goal: 0 translation bugs at release time <img src="https://wiki.ubuntu.com/htdocs/ubuntu/img/smile.png" title=":)" width="15" height="15" alt=":)" />
    - Rejecting string changing uploads that do not close a string exception tagged bug? ([TimoJyrinki](https://wiki.ubuntu.com/TimoJyrinki))
15. **[Fixed schedule for translation updates](https://blueprints.launchpad.net/ubuntu/+spec/community-m-fixed-schedule-for-translation-updates "UbuntuSpec")**
    - Predictable translation updates could help scheduling work
    - Not only language packs, but DDTP, (k)ubuntu-docs, and whatnot too
    - Perhaps we could introduce on-demand updates, so that a language can get an update when it needs it the most
    - "Supported release" should mean not only security fixes, but translation updates too!
16. **[Creating a localized help.ubuntu.com](https://blueprints.launchpad.net/ubuntu/+spec/community-m-localized-help-dot-ubuntu-dot-com "UbuntuSpec")**
    - help.ubuntu.com should detect my browsers locale settings and show the content on my language
    - Asking teams to create [localized versions](http://sugo.ubuntu.hu/) of that site makes no sense: we duplicate the infrastructure and the work to maintain it for nothing.
17. **[Improving communication with translators in Launchpad](https://blueprints.launchpad.net/ubuntu/+spec/community-m-launchpad-translator-communication "UbuntuSpec")**
    - (From the Ubuntu Manual Team)

## How to participate

<div>

Whether you can attend UDS presentially or remotely, if you see any translation session you're interested in, you can participate or follow the progress by subscribing to the blueprint. And if you are at UDS, just join the session! Here's how you can do it:

</div>

- **Go to the blueprint**. Click on the session you're interested in, either in this overview or in the UDS schedule. This will take you to the blueprint in Launchpad.
- **Subscribe to it**. Subscribe to the blueprint, optionally ticking the "Participation essential" checkbox.
- **Add feedback**. If you like, add feedback to the blueprint's whiteboard.
- **Join in!** Remember that if you are participating remotely, there's IRC projected in all rooms and sound is streamed, so you can interact with those in the session. Check out Jorge's [Ubuntu Open Week](https://wiki.ubuntu.com/UbuntuOpenWeek) IRC session next Friday at 18:00 UTC on \#ubuntu-classroom

<div>

I'm already looking forward to seeing everyone again in Brussels, it's going to be epic once more!

</div>

<div>

<a href="http://www.flickr.com/photos/anotherpintplease/" rel="cc:attributionURL">http://www.flickr.com/photos/anotherpintplease/</a> / <a href="http://creativecommons.org/licenses/by-nc-sa/2.0/" rel="license">CC BY-NC-SA 2.0</a>

</div>
