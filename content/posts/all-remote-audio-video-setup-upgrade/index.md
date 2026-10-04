---
title: "All-remote audio/video setup upgrade"
slug: "all-remote-audio-video-setup-upgrade"
date: 2021-11-23T20:58:17.000Z
tags: ["all-remote", "open-source"]
---

After being tasked with delivering the Community keynote at GitLab's internal Contribute 2021 event, I decided it was high time to refresh my A/V setup to step up streaming quality a notch.

This is a work in progress post, but after someone asked, I thought I'd share what I did in case it can be of use to anyone.

Starting point:

- A decent HD webcam for audio and video (Logitech C920)
- A decent set of speakers and headphones (Creative Gigaworks T3, Logitech Marshall Monitor). The speakers had already started developing a noise and needed to be replaced

Goals:

- Significant video quality improvement (more focus, sharpness, optional blur)
- Significant audio quality improvement (clean voice sound, no background noise)
- Platform-neutral hardware or hardware that works with Linux- Not a high-end set up. I do occasional talks, but I'm not a content creator

With that in mind, I came up with a basic setup to meet those goals and that is adapted to my workflow:

<figure class="kg-card kg-image-card kg-card-hascaption">
<img src="/content/images/2021/11/Desktop-setup.JPG" class="kg-image" width="2000" height="1337" />
<figcaption>A/V setup upgrade, iteration #1</figcaption>
</figure>

This is the first iteration for now. The setup works really well for my needs, but I'm also thinking of the second iteration once a new standing desk arrives.

## The hardware

- **Video**: <span class="mark">Sony a6400 mirorless camera</span>, with the 16-50mm kit lens. I was considering upgrading my venerable Nikon D5100+ in any case, which does not have clean HDMI output, so I went with it. Most professional content creators seem to recommend the a6100 or a6400. *Backup*: Logitech C920 webcam.
- **Audio input**: <span class="mark">Elgato Wave:1 microphone</span>. I decided to go for an USB microphone instead of an XLR microphone for setup and cable management simplicity (one cable only, no additional interfacing hardware required). I might reconsider this in the future, but for now this suits my needs. *Backup*: Deity V-Mic D4 Mini passive microphone, to enable offline, on-media-card recording, and also to plug the microphone to a teleprompter app with voice recognition. The additional backup is the integrated Logitech C920 webcam's microphone.
- **Audio output**: <span class="mark">Audioengine HD3 speakers</span>. Outstanding sound, extremely qualitative and compact build, with Bluetooth. <span class="mark">Marshall Monitor headphones</span>, which I've had for years. They might not be top of the range or have noise cancelling, but they are sturdy and made of metal. Unlike my old Sennheiser headphones, which were made of plastic and disintegrated at some point. I like the fact that I can choose between Bluetooth and wires.
- **Light**: <span class="mark">Elgato Ring Light</span>. A pair of Elgato Key Light or Key Light Air seem to be some of the de-facto standards for streamers and content creators. I went with the ring light for the extra flexibility to be able to mount the camera in the middle, and because it seems to be easier on the eyes than the other two if it's pointing at you.
- **Gear mounts**: I mount the camera on a <span class="mark">SmallRig a6000/a6300 cage</span>, which in turn is mounted onto a tripod with an Arca-Swiss quick release plate. Any good quality tripod will do. This allows me to either remove the whole camera setup and mount it somewhere else, and to also easily remove the camera body whenever I take it out for family and amateur photos. In this case, the microphone and any other attachments can be left in the cage, without having to mount them to the body every time. <span class="mark">Elgato Multimount S</span> to mount the light source on. It came already with the light and it's modular, so I might add an arm attachment to it to replace the (temporary) tripod. Also, my desk plate is too wide for any mount clamps, so I had to improvise a temporary mount location with a piece of wood and a woodworking clamp. The microphone is on an <span class="mark">Elgato Wave Mic Arm LP</span> (Low Profile) arm, which folds beautifully on the side when not used, and does not get in the way when used. The original Elgato microphone stand could be nicely recycled into a headphone stand after the microphone was mounted on the mic arm.
- **Interfaces**: to interface the HDMI output from the camera to the computer, I use an <span class="mark">Avermedia ExtremeCap</span> HDMI/USB3.0 converter. The nice thing about it is that it's hardware-only and works on any platform without the need for drivers or additional software. With an aluminum body it's very sturdy and has a handy LED to inform about the link's status. All devices are ultimately connected with the computer through a <span class="mark">Wavlink USB 3.0 7-port hub</span>. The nice thing about it is that it has independent switches to turn outputs on and off. The not so nice thing about it is that it's the second in a row that I'll have to return as the output status LEDs are either permanently on or off. Also Sony's IR Remote control to quickly adjust the zoom and other settings in the camera.

## The software

- **Videoconferencing**: <span class="mark">Zoom</span>, occasionally Google Meet for external conferences, or any other online conferencing platform
- **Recording**: <span class="mark">OBS Studio</span>
- **Monitoring**: <span class="mark">pasystray</span>, pulsemixer or pavucontrol to watch audio levels and setup default sources. Mixxx for easy microphone sound monitoring.
- **Hardware control**: <span class="mark">Elgato Light Control GNOME extension</span> to control the brightness and light temperature from the Ring Light. Great that it has a REST API, although it's not publicly documented. I also tried the Android apps: Sony's Imaging Edge for camera zoom and settings (abandoned it as WiFi pairing is clumsy at best) and Elgato Light Control (works ok).

## What's next

For the next iteration, I'm planning to:

- Simplify the number of mounts/tripods. Optionally integrate them in a new monitor stand.
- Learn more about audio post-processing. Potentially add noise and compressor filters with OBS and route sound to other applications.
