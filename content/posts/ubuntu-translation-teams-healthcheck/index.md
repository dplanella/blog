---
title: "Ubuntu Translation Teams Healthcheck"
slug: "ubuntu-translation-teams-healthcheck"
date: 2010-07-21T16:03:41.000Z
tags: ["survey", "translations", "ubuntu"]
---

Some weeks ago I ran the [Ubuntu Translation teams healthcheck](https://blueprints.edge.launchpad.net/ubuntu/+spec/community-m-translation-teams-healthcheck) survey. The main goal was getting in touch with the teams to have some feedback on how they were doing, if they needed help in any particular area and make sure that they were aware of the latest changes in [translation policies](https://wiki.ubuntu.com/Translations/KnowledgeBase#Policies). While the [results](https://wiki.ubuntu.com/Translations/Surveys/TeamsHealthcheck) were available on the wiki, I hadn't had a chance to post a summary.

Here it is.

# Language info

**Participation**. Up to **71** teams participated in the survey. Of these, **58** submitted the input and explicitly agreed to have it published online. This summary represents the input from the following teams:

*Persian, Welsh, Manx, Armenian, Punjabi, Bulgarian, Telugu, Portuguese, Dhivehi, Asturian, Belarusian, Hebrew, Icelandic, Macedonian, German, Irish, Kazakh, Norwegian, Afar, Gujarati, Spanish, Hungarian, Sinhala, Arabic, Northern Sotho, Japanese, Finnish, Maori, Greek, Shuswap, Frisian, Tamil, Korean, Estonian, Lojban, Lithuanian, Silesian, Occitan, Ukrainian, Simplified Chinese, Tibetan, Low German, Brazilian, Russian, Dutch, Catalan, French, Khmer, Luxembourgish, Galician, Traditional Chinese (Taiwan), Basque, Slovenian, Uyghur, Swedish, Danish, Italian, Romanian*

**Active translators**. On the question of how many active translators a team has, the average is about **12** Launchpad team members or regular translators, with another average of **20** occasional or drive-by translators.

This seems to validate the model of having a small team of reviewers who can submit and review translations and a bigger group of translators submitting translation suggestions, as well as also confirm the migration in the last cycles to smaller, more manageable moderated teams, focusing on translation quality assurance.

**Natural language usability**. On the three categories, we seem to be in good shape.

<img src="/wp-content/uploads/2010/07/languageusability.png" title="LanguageUsability" class="aligncenter size-full wp-image-450" width="480" height="366" alt="Language Usability" />

While we're doing excellent-good in fonts and input method, the interesting bit will be to focus on converting that good-average to excellent-good in applications. One thing to have into account when evaluating fonts and input method though, is that many languages do not need an input method or are nowadays not in need of a set of fonts to correctly display text. So here the challenge will be to concentrate on the languages rated as average and poor to see the areas in which this rating can be improved.

This information is also very useful to me in a per-language basis to see the perception of how usable Ubuntu in a particular language is comparing it to [translation coverage statistics](http://people.ubuntu.com/~dpm/ubuntu-10.04-translation-stats.html).

# Translation team policies

**Translation policies**. While in more than half of the responses translation team coordinators were aware of the new [Ubuntu Translations policies](https://wiki.ubuntu.com/Translations/KnowledgeBase#Policies), there are still quite some teams who did not know about them. I'll take an action to send a reminder explaining the new policies.

**Ubuntu translators mailing list subscription**. We're now asking all translation team coordinators to be subscribed to the [Ubuntu translators mailing list](http://lists.ubuntu.com/mailman/listinfo/ubuntu-translators), and it seems that the majority are. Some of the people who said they were not subscribed did it just after participating in the survey. I'll follow this up with the rest who aren't on the list, but the most important part is to make sure new team coordinators are aware of the need to be subscribed to follow all Ubuntu translations announcements and forward them to their teams when necessary.

**Team membership**. The vast majority of teams have now a [moderated team membership](https://wiki.ubuntu.com/Translations/KnowledgeBase/LaunchpadTeam#TeamSubscription), which allows them to have more oversight on translation quality. There are still a handful of open teams, which I'll be trying to help migrating to a moderate membership.

**Launchpad team page information**. Nearly all teams represented in the survey had up to date information on their Launchpad page, which should be the entry point for translators wanting to translate Ubuntu in their language. Having clear and useful information there is a step that should not take more than a few minutes, but it is extremely important to make the process of joining translation teams easier and thus to get more help in the effort of translating Ubuntu in your own language.

**Communication channel**.

[<img src="/wp-content/uploads/2010/07/communicationchannels.png" title="Translation Team Communication Channels" class="aligncenter size-full wp-image-439" width="480" height="174" alt="Translation Team Communication Channels" />](/wp-content/uploads/2010/07/communicationchannels.png)

Mailing lists, be it on [ubuntu.com](https://lists.ubuntu.com), on [launchpad.net](https://help.launchpad.net/Teams/MailingLists) or externally, are the main communication method for translation coordination. We generally [recommend using lists at ubuntu.com](https://wiki.ubuntu.com/Translations/KnowledgeBase/LaunchpadTeam#TeamCommunication), as Launchpad mailing lists only allow subscription for team members, which for translation teams exclude occasional, non-member, translators.

The important point for me here is that nowadays nearly all translation teams use some form of communication for successful translation coordination.

From the additional comments, other methods were direct e-mail, face to face meetings, instant messaging, regular IRC meetings and wikis.

**Translation guidelines**. While many teams do have guidelines, there is still a 30% of them who haven't, so I see this as an area that needs improvement. I believe translation guidelines are one of the most basic tools for a successful translation process, and each team, be it new or already established, should have some. Guidelines can cointain glossaries on how to translate common software-related terms, grammar rules or conventions specific to the language and translation of free software - or anything that can help in achieving consistency, resolving doubts and making the translation process more effective. IRC meetings, jams or any other events are generally useful to start developing guidelines.

[Our wiki page on guidelines](https://wiki.ubuntu.com/Translations/KnowledgeBase/TranslationGuidelines) contains some very useful information and good examples from teams using them.

# Translation team workflow

**Translation bug tracking**. The majority of teams use their mailing lists or forums to track translation problems and fix them, but there is still a considerable amount using Launchpad to track translation bugs, and to a lesser extent, external bug trackers.

The point risen here was that the important part was getting actual feedback from users about the problems, and some teams are struggling with this.

**Accepting new team members**. As a result of most teams being now moderated, the common practice in accepting team members is them asking to join the team, team members reviewing the application and then accepting them.

The thoroughness of the process varies across teams. Some have requirements on new members to have signed the CoC, having a minimum of karma, submitting the application to vote, or some others have a more relaxed process.

Another practice that some teams tend to follow is to have the main team acting as a small set of reviewers who can accept suggestions and a separate, bigger team that anyone can join. This way occasional or new translators can still submit suggestions as usual, but can also have a feeling of being part of the team.

**Translation events**. That's another area for development, as the majority of teams don't seem to be running any translation events. Translation events, either on IRC, or face to face (e.g. a translation jam) are extremely useful for focusing on particular translation goals and getting together to achieving them. Being all together at the same place makes the process much more agile, as reviews can happen instantly, and doubts can also be discussed straight away. We will need to better raise awareness on [translation jams](https://wiki.ubuntu.com/Jams/Translations), either occasional ones or during the [Ubuntu Global Jam](https://wiki.ubuntu.com/UbuntuGlobalJam).

**Translation review process**.

<img src="/wp-content/uploads/2010/07/translationreview1.png" title="Translation Review" class="aligncenter size-full wp-image-445" width="480" height="221" alt="Translation Review Process" />

Here most of the teams seem to use the Launchpad Translations online interface and take advantage of the more agile translation and review process, either just translating and simply fixing errors when they are found, or through an explicit review process after finishing each translation.

**Upstream coordination**. That was for me one of the most interesting areas of the survey, and I'm quite pleased to see the results.

<img src="/wp-content/uploads/2010/07/upstreamcoordination.png" title="Upstream Coordination" class="aligncenter size-full wp-image-446" width="480" height="209" alt="Upstream Coordination" />

They show that nowadays most of the Ubuntu translation teams actively coordinate with [upstream projects](https://wiki.ubuntu.com/Translations/Upstream). Using a mixture seems to be the most popular choice: indistinctively translating upstream or in Launchpad. The next most popular approach is translating first upstream and then completing Ubuntu-specific translations in Launchpad.

There are still a few teams who are not working with upstream, and we'll have to see what the best approach for them to contribute back is. Another interesting trend are those teams translating everything in Launchpad first and then sending it upstream. They tend to be the same translators both upstream teams and in Ubuntu, and they effectively use the best of both worlds: the best online translation interface for open source software combined with sending translations upstream to make them available to all other projects.

# Final thoughts

It would have been interesting to compare results with previous data from a couple of cycles ago, but having been part of it for a long time now, my feeling is that the Ubuntu Translations community is developing in the right direction, and I hope that this survey also serves as a testimonial to show external translation communities how Ubuntu translators work. The points about the importance of a defined workflow, team communication, quality assurance and upstream coordination are most definitely getting across.

Some areas in which we'll have to concentrate is seeing how we can help those teams that are or have become inactive, better communicate the Ubuntu translation policies and work with the teams who don't have translation guidelines to start developing some. I will also go back to the teams who explicitly asked for help in particular areas.

This has also offered me an invaluable insight on each team and their current situation and workflow, which will help me working with them in the future.

Thanks to everyone who took the time to complete it, as the input has been very valuable to know more about the Ubuntu translations community.﻿ You allow millions of users to use Ubuntu in their own language every day, and you truly rock.
