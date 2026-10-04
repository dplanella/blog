---
title: "Launchpad Translations projects in Google Summer of Code 2010"
slug: "launchpad-translations-projects-in-google-summer-of-code-2010"
date: 2010-03-24T17:23:42.000Z
tags: ["gsoc", "launchpad", "translations", "ubuntu"]
---

As most of you know, we've got an [amazing translations community in Ubuntu](https://translations.launchpad.net/+groups/ubuntu-translators). Every day, hundreds of translators use [Launchpad Translations](https://translations.launchpad.net/) as a tool to make our OS of choice available in almost any language.

As such, I'm thrilled to announce a set of [GSoC projects focused on Launchpad Translations](https://wiki.ubuntu.com/GoogleSoC2010/Ideas#Package_set_views_in_Launchpad_Translations) and aimed towards improving the Ubuntu translations community experience. Here they are:

## Projects

### Package set views in Launchpad Translations

Currently we expose the full list of translations in the main archive to Ubuntu translators. This is generally overwhelming for new translators and it does not show accurate statistics on how well translated a distribution is.

It would be useful to have a global view of projects or modules which would only include the templates which are part of them (e.g. Ubuntu, Kubuntu, UNR, or even further granularisation in subprojects or most important upstreams: GNOME, KDE, etc.). This could be e.g. modelled after the package sets already available from Launchpad.

### Full Launchpad Translations API

The aim of this project is to implement a full API for the Launchpad Translations component.

This will allow accessing translations-related data from Launchpad through launchpadlib. The API can be subdivided in several components (e.g. reporting -already being developed-, imports queue, translations, etc.) and will open the door to a broad range of uses of Launchpad Translations: more automated management of Ubuntu translations, automated status tracking of imports by users, client-side online translation, navigation of the site in custom applications, requesting downloads, fetching individual messages or suggestions, etc.

### Native support for OpenOffice.org translations format in Launchpad Translations

Launchpad Translations standardizes on using the Gettext PO format for importing and exporting translations.

While this covers the majority of Open Source projects supporting localization, there are a couple of notable exceptions. These implement custom formats and cannot be directly imported or exported. OpenOffice.org is one of them. Its custom GSI/SDF translation format needs to be converted to gettext before importing it into Launchpad. This causes quite a lot of packaging overhead and manual work, and the translations cannot use the language pack infrastructure. Due to this, we had to recently disable OpenOffice.org translations in Launchpad.

We want Ubuntu translators to be able to translate OpenOffice.org in Launchpad as any other Ubuntu package and to be able to contribute translations back to upstream. The aim of this project is to implement native support for importing and exporting OpenOffice.org's GSI/SDF translation format.

### Full native support for Mozilla translations format in Launchpad Translations

Launchpad Translations standardizes on using the Gettext PO format for importing and exporting translations. While this covers the majority of Open Source projects supporting localization, there are a couple of notable exceptions. These implement custom formats and cannot be directly imported or exported. Firefox uses the custom XPI translations format and is one of them. While native import support is already implemented and functional, translations are currently exported in an intermediate format and the conversion back to XPI is done outside of Launchpad. We want the Ubuntu Mozilla translations to be exported in native format and be able to use them directly in language packs and allow contributing the translations back to upstream. The aim of this project is to complete the support for the Mozilla translation format and enabling native export.

### Native support for XML documentation in Launchpad Translations

Launchpad Translations standardizes on using the Gettext PO format for importing and exporting translations. This generally covers the majority of Open Source projects supporting localization, but only their user interface. Documentation is generally produced in other formats (mostly docbook) and must be converted to the Gettext PO format before importing it into Launchpad and converted back to XML upon export. This additional step, generally performed by tools such as `xml2po` or `po4all` currently stops us from importing documentation of upstream projects for translation in Launchpad in Ubuntu. The aim of this project is to implement native XML support for translatable documentation in Launchpad Translations, so that it can be seamlessly imported and exported.

### Adding POT template generation support for layouts other than intltool in Launchpad Translations

Upstream integration is the current development focus in Launchpad. To that end, the Launchpad Translations component is being extended to enable translation imports directly from bzr branches of upstream projects. One important aspect of this feature is the automatic regeneration of POT translation templates from the branches, which is implemented using what is internally called the pottery infrastructure. Pottery currently supports the intltool layout, which already covers a great number of Open Source projects. However, there will still a percentage of upstream projects which do not follow this standard intltool layout. The aim of this project is to extend pottery to support additional formats, so that the maximum number of upstreams can be imported into Launchpad Translations.

## So, you'd like to work on this?

[Danilo Šegan](https://launchpad.net/~danilo), the Launchpad Translations team lead, will be the mentor for these projects, but you can use me as a backup contact as well, especially this week, as Danilo is away on a coding sprint. You'll find all the information you need on Ubuntu's participation in the GSoC 2010 and how to get involved here:

- <https://wiki.ubuntu.com/GoogleSoC2010>

So here's your chance of joining the team of Launchpad developer legends and making the Ubuntu translation experience even more awesome. If you are wondering what all this is about, here is some content to get you started:

- [How to get started with Launchpad development](https://dev.launchpad.net/Getting)
- [Adi Roiban](http://adi.roiban.ro/) and [Henning Eggers](https://launchpad.net/~henninge)' Ubuntu Developer Week session on [Launchpad Translations Under the Hood](https://wiki.ubuntu.com/MeetingLogs/devweek1001/LPTranslate)
- [Additional content](https://wiki.ubuntu.com/UbuntuDeveloperWeek/Sessions/LaunchpadTranslationsUnderTheHood) for the Launchpad Translations Under the Hood session

And if you've got any questions, feel free to ask!
