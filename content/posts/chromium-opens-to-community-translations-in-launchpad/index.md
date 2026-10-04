---
title: "Chromium opens to community translations in Launchpad"
slug: "chromium-opens-to-community-translations-in-launchpad"
date: 2010-12-09T13:34:09.000Z
tags: ["chromium", "google", "launchpad", "translations"]
---

<figure class="kg-card kg-image-card">
<img src="/content/images/2019/07/chromium-lp.png" class="kg-image" />
</figure>

I'm very much thrilled to announce that [Chromium](http://www.chromium.org/Home), the Open Source project behind [Google Chrome](http://www.google.com/chrome), the browser that is transforming the way we experience the web, is now open for community translation in [Launchpad](https://launchpad.net/).

Chromium will be hosting its translations in [Launchpad Translations](https://translations.launchpad.net/), the [collaborative online tool](https://launchpad.net/+tour/translation) for translating Open Source projects and building community around them.

[![Translate Chromium in Launchpad](/content/images/2019/07/translatechromiumbutton.png)](https://translations.launchpad.net/chromium-browser)

**You can now translate Chromium online into almost any language.** Using Launchpad's simple web interface you'll only need a [Launchpad account](https://help.launchpad.net/YourAccount/NewAccount), a web browser and good knowledge of English and the language you'll be translating into.

## Under the Hood

For the technically minded among us, here's an overview of how everything fits together. But first of all, I need to mention that all this would not have been possible without the fantastic work of [Fabien Tassin](https://launchpad.net/~fta), the legendary Ubuntu community member of Chromium and Firefox packaging fame. Big thanks also go to Evan Martin from the Chromium project, the Launchpad Translations developers and anyone else involved in making this possible. In short, after seeing the willingness from the Chromium project to use translations infrastructure in Launchpad, Fabien single-handedly designed and implemented the machinery that performs the conversion between the Chrome translation format and [Gettext](http://www.gnu.org/software/gettext/), the widely-used standard format Launchpad understands. He did not stop here, and he also devised a way to package these translations and submit them to upstream.

The following diagram illustrates the Chromium translations lifecycle:

<figure class="kg-card kg-image-card kg-width-wide kg-card-hascaption">
<img src="/content/images/2019/07/chromium-translations-v2.png" class="kg-image" />
<figcaption>Chromium Translations Lifecycle - Diagram by Fabien Tassin</figcaption>
</figure>

The work is happening between **Fabien's server**, where he maintains a local copy of the Chromium upstream branches, and **Launchpad**, where the [PPA](https://help.launchpad.net/Packaging/PPA) builds and translations happen. These are the two big blocks you see on the diagram.

The existing Chromium translations are imported into Launchpad after being converted to the gettext format. The result is then committed into a [bzr branch](https://code.launchpad.net/~chromium-team/chromium-browser/chromium-translations.head), which is enabled with [automatic translation imports](http://blog.launchpad.net/translations/import-translation-templates-from-your-projects-bazaar-branches) to make the translations available through [the web UI](https://translations.launchpad.net/chromium-browser/translations).

At this point translators can do their work: either complete missing translations, improve existing ones or add new languages. This work is then committed daily to [another bzr branch](https://code.launchpad.net/~chromium-team/chromium-browser/chromium-translations-exports.head) making use of another cool Launchpad integration feature: [automatic translation exports](http://blog.launchpad.net/general/exporting-translations-to-a-bazaar-branch).

The rest of the process is also fully automatic: every day, a bot in Fabien's server fetches the [translations export branch](https://code.launchpad.net/~chromium-team/chromium-browser/chromium-translations-exports.head), converts back from gettext to the Chromium translation format, merges that with the upstream trunk and lands the changes in the corresponding PPA of the [daily builds](https://launchpad.net/~chromium-daily).

For other branches the process is the same, except that it is only run when there is a new upstream release. From there, patches with the translations are generated daily for anyone else interested in using them.

## Q+A

**What does community translation mean?** It means that any Open Source enthusiast will be able to translate Chromium to their language through volunteer contributions.

**Why do we need community translations?** Many of the translations already available in Chromium come from private translations originated in Chrome. Until now, Chromium did not have any translation infrastructure to enable the community to localize the software, and therefore some languages were incomplete. In Launchpad you can now a) complete Chromium translations, b) improve them and c) add new languages.

**How do I get started translating Chromium?** If you don't have one already, you'll need a [Launchpad account](https://help.launchpad.net/YourAccount/NewAccount). Once you've created it and [selected your prefered languages](https://launchpad.net/people/+me/+editlanguages), simply point your browser to <https://translations.launchpad.net/chromium-browser>, click on your language of choice, and that's it, you can now start translating!

**I can submit neither translations suggestions nor translations. How can I translate Chromium?** If you aren't already logged in to Launchpad, [try to log in](https://login.launchpad.net/+login) and see if it helps. If it doesn't, that's probably because there is no translation team for your language yet. Launchpad Translations is built around a model of community (in the form of translation teams) and [permissions](https://help.launchpad.net/Translations/YourProject/PermissionPolicies) (chosen by the project developer). The permission model for Chromium is Restricted, which provides a good balance between community participation and translation quality. This means that while everyone can submit translations suggestions, only the members of the translation team will be able to accept them after review. Have a look at the list of teams in the [Launchpad Translators group](https://translations.launchpad.net/+groups/launchpad-translators). If there isn't one, you should be able to start a new team in a matter of minutes following these [simple instructions](https://help.launchpad.net/Translations/LaunchpadTranslators#StartingTeam), which will allow you to start translating Chromium once the team is approved.

**When I try to translate my translations are saved as suggestions. Why can't I directly submit translations?** That's because you are not part of the translation team for your language. You can [look for your language's translation team here](https://translations.launchpad.net/+groups/launchpad-translators) and get in touch with them. If you wish, you can ask them if you can join the team or if they can review your suggestions. See the previous question for more information on translation teams, suggestions and permissions. **How do I get support for Launchpad Translations?** There are many ways to get support if you need help. Here are some of them: you can [ask a question in Launchpad](https://answers.launchpad.net/rosetta/+addquestion), you can send an e-mail to the [launchpad-users mailing list](https://launchpad.net/~launchpad-users) or you can [ask on the \#launchpad IRC channel](http://webchat.freenode.net/?channels=launchpad) on the Freenode network. You will find more information [here](https://help.launchpad.net/Feedback).

**Will Chromium translations make it to Google Chrome?** Most probably not. Google Chrome and its translations are subject to different [QA](http://en.wikipedia.org/wiki/Quality_assurance "Quality assurance") processes than Chromium and we're not contemplating this possibility at this time. We are only making those strings either common or specific to Chromium available for translation.

**How often will translations be updated?** It depends on the Chromium version and the operating system you are using:

- **Ubuntu, stable:** if you are using the Chromium version provided in the Ubuntu package through Software Center, you will get a translations update whenever there is a new Chromium stable version released upstream.
- **Ubuntu, PPA:** If you are using the [Chromium daily PPA](https://launchpad.net/%7Echromium-daily) for Ubuntu, there are several options depending on which actual PPA (channel) you are using: for [trunk](https://launchpad.net/%7Echromium-daily/+archive/ppa), once a string is translated in Launchpad it takes about 2 days to be available; for the other channels ([dev](https://launchpad.net/%7Echromium-daily/+archive/dev), [beta](https://launchpad.net/%7Echromium-daily/+archive/beta), [stable](https://launchpad.net/%7Echromium-daily/+archive/stable)) translations are only made available whenever there is a Chromium upstream release.
- **Other:** the frequency of updates in other distributions will depend on the use they make of the translations and their update policies. There are currently no Chromium builds for Windows or Mac.

This is a fully automatic process: [translations exported from Launchpad](https://code.edge.launchpad.net/%7Echromium-team/chromium-browser/chromium-translations-exports.head) are fetched daily, merged with the upstream trunk and changes are landed in the corresponding PPA of the [daily builds](https://launchpad.net/%7Echromium-daily).

**How can other Operating Systems use the Chromium community translations?** The intention is that any Operating System/Linux distribution can benefit from the work from Launchpad translators, so these translations will be available to anyone interested in using them. They can even be used for Windows and Mac.

If you are interested in using the translations for another distro, the best thing is to **get in touch with [Fabien](https://launchpad.net/~fta)** (you'll also find him as **fta** in the **\#chromium** IRC channel on Freenode). If you've got more questions, also feel free to ask by sending a comment to this blog post.

Happy translating!
