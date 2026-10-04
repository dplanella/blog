---
title: "VW bus spark plugs service"
slug: "vw-bus-spark-plugs-service"
date: 2017-10-27T20:29:00.000Z
tags: ["vw-bus"]
images: ["/content/images/2019/07/CameraZOOM-20190718140901649-1-.jpg"]
---

... for Type 1 and Type 4 engines (1968-1979)

## Service and specifications

![Spark-gap-1](/content/images/2019/07/Spark-gap-1.jpg)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>A</th>
<th>Value</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>Inspect every</td>
<td>10,000 km<br />
(6,000 mi)</td>
<td>From "So wird's gemacht" manual:<br />
- Inspect: 10K km<br />
- Replace: 20K km</td>
</tr>
<tr>
<td>Replace every</td>
<td>24,000 km (15,000 mi)</td>
<td>The FI engine originally used long-life spark plugs. If NGK plugs are used, their replacement interval is 30,000 mi. (48,000 km).</td>
</tr>
<tr>
<td>Type</td>
<td>NGK B5ES<br />
NGK B5HS</td>
<td>Type 4 engine<br />
Type 1 engine<br />
Modern replacement for originally recommended spark plugs in the Owner's Manual (see appendix for reference). Part number codes:<br />
<strong>B</strong>: 14 mm thread<br />
<strong>5</strong>: heat range (lower is hotter)<br />
<strong>E</strong>: 19 mm thread reach / <strong>H</strong>: 12.7 mm thread reach<br />
<strong>S</strong>: copper core center electrode.<br />
Trivalent metal plating on the threadprovides anti-corrosion and anti-seizing properties. Longevity: 30,000 mi. (48,000 km). Other than old stock, only the BR5ES (with 5 kOhm resistor) type is currently available</td>
</tr>
<tr>
<td>Air gap</td>
<td>0.7 mm (0.028")<br />
0.6 mm (0.024")</td>
<td>Fuel injection engine (Type 4)<br />
Carbureted engines (Type 1, Type 4)</td>
</tr>
<tr>
<td>Torque</td>
<td>30 N·m (22 lb·ft)</td>
<td>NGK recommends 18-21.6 lb·ft (25-30 N·m) for aluminum heads. There is also a <a href="https://www.thesamba.com/vw/forum/viewtopic.php?p=7602295">spark plug torque discussion</a> at The Samba forum.</td>
</tr>
<tr>
<td>Thread size</td>
<td>M14 x 1.25 x 20.8 mm</td>
<td>Diameter x pitch x hexagon size.</td>
</tr>
<tr>
<td>Thread reach</td>
<td>19 mm</td>
<td></td>
</tr>
<tr>
<td>Hex socket size</td>
<td>21 mm</td>
<td></td>
</tr>
</tbody>
</table>

## Installation tips

- 👉 Do the removal and installation with a cold engine. Metal expands when it's hot. The aluminium heads expand more than the spark plug when heated up, with the consequence that the spark plug can be fastened in place.
- 👉 Clean up the spark plug holes before installation. You don't want to torque against dirt or debris.
- 👉 Finger tight the sparkplugs first, then use a torque wrench set at the specified torque.
- 💡 Your fingers won't reach to the spark plug sockets where the engine tin covering them is higher. You can use a small section of fuel hose plugged into the spark plug's terminal end snuggly. Then do the installation from the rubber hose with longer reach.
- 💡 Consider removing only one spark plug wire at a time. That way there is no chance of possibly getting the spark plug wires mixed up.
- 💡 The firing order for all air-cooled Volkswagen engines is 1-4-3-2, so make sure the plug wires go around the distributor cap clockwise in that order.
- 💡 You should use a torque wrench for installation. Consider investing in one if you don't have it, or borrowing it from someone. If you are intending to continue servicing your bus yourself, you'll be using it for many other maintenance procedures. In a pinch, if you are in a situation where a torque wrench is not available, you can install the spark plugs finger tight and then add another quarter turn (90°) with a hex wrench.

## FAQ

![spark-plug-parts](/content/images/2019/07/spark-plug-parts.jpg)

### Should I use a spark plug with RFI suppression resistor?

ℹ️ VW busses with stock ignition do not *need* spark plugs with integrated resistor.

This is because the ignition circuit already contains the additional resistance: the rotor cap has 5 kΩ resistor, and each spark plug connector has an integral 1 kΩ resistor. That said, resistor spark plugs *can* be used (see more below).

![VW-type-2-ignition-lead-spark-plug-resistance](/content/images/2019/07/VW-type-2-ignition-lead-spark-plug-resistance.jpg)

Early fuel injector systems were designed to use resistor spark plugs to reduce radio frequency interference (RFI) that could affect sensitive electronic systems, such as ECUs. The effect of the resistor is to attenuate the spark's energy and thus minimize RFI. Not all vehicles featured the integral resistance in the ignition wiring as the Type 2 bus.

At the time of writing (2017), spark plug manufacturers have phased out non-resistor spark plugs and only the resistor type is available. Non-resistor spark plugs are still available from old stock, though. So if you want to be close to stock, the non-resistor option is still that option available.

That said, the additional resistance added by the spark plug resistor (generally 5 kΩ) is probably not critical. **The extra resistance on the circuit affects the spark line section** of the secondary circuit's voltage waveform by varying its slope.

![SparkWaveform_30b](/content/images/2019/07/SparkWaveform_30b.jpg)

According to this source, as long as a value of 20 kΩ is not exceeded:

> Spark or burn section (spark duration): the amount by which this line slopes away from the horizontal is directly related to resistance in the plug and coil HT leads (ignition supression). \[...\] The total resistance between the centre terminal of the coil and the centre electrode of the plug should not exceed about 20 kΩ \[...\] Actual resistance is not critical but anything more than 30 kΩ may cause problems.

*[Testing your ignition with an oscilloscope](https://www.princeton.edu/ssp/tiger_cub/library/ignition_waveforms.pdf), Electronics Today International, February 1977*

Richard Atwell performed and documented some tests with varying rotor cap resistance as well. As it's a series circuit, the results can be extrapolated to be similar for varying spark plug resistance. The result was that with an increased resistance (up to the stock 5 kΩ of the rotor cap) a more optimal waveform was generated.

*[Understanding the ignition system](http://www.ratwell.com/technical/IgnitionSystem.html), Richard Atwell* (scroll down to the "*Which rotor*" section for the results)

Finally, to conclude that resistor plugs can be used nevertheless in VW busses, here is a quote from Bosch's spark plug documentation:

> Resistor spark plugs can be fitted in non-resistor applications. Bosch recommends fitting a resistor type spark plug for every application.

### Can I reuse the crushable gasket when reinstalling my spark plugs?

ℹ️ Plug manufacturers **recommend the use of a new gasket any time a plug is reinstalled** after inspection or cleaning.

You can purchase inexpensive 14 mm gaskets such as these:

![spark-plug-gasket](/content/images/2019/07/spark-plug-gasket.jpg)

That said, many bus owners have reinstalled spark plugs without replacing the gaskets over the years, so in a pinch, you can also do the same.

### With terminal nut?

ℹ️ Use spark plugs with a threaded terminal stud. They are generally sold with a removable terminal nut that can be detached before installation.

The terminal is connected to the ignition lead connector via a small clip that pushes against the terminal stud's thread.

[More on spark plug terminal types](https://www.sparkplugs.com/learning-center/article/794/spark-plug-terminal-types)

### Regular, extended or recessed center electrode tip?

ℹ️ Spark plugs for the Type 2 use a regular center electrode tip, raising 1 mm from the thread.

[More on spark plug center electrode designs](https://www.sparkplugs.com/learning-center/article/774/spark-plug-center-electrode-designs)

### Which heat range?

ℹ️ Spark plugs for the Type 2 are on the hotter heat range end (e.g. **heat range code 8 for Bosch**, or code 5 for NGK).

- [More on spark plug heat range, from sparkplugs.com](https://www.sparkplugs.com/learning-center/article/131/what-is-a-spark-plugs-heat-range)
- [More on spark plug heat range, from Bosch](https://www.boschautoparts.com/documents/101512/0/0/0ebd7cc0-b6f7-4590-99c5-ff1ee52a693b)

### Should I use anti-seize to prevent galling of the threads?

> Sparingly apply anti-seize compound to the upper two thirds of the threads to lubricate them. Don't get any anti-seize on the plug electrode or it will foul

(Tom Wilson on *How to Rebuild Your Volkswagen Air-Cooled Engine*, pp138)

Plug manufacturers do **not recommend** the use of anti-seize, though, as it modifies the torque specifications. If anti-seize *is* used, they suggest reducing the torque values by 20 - 40 %.

## Appendix: historical plug type cross-reference

### Fuel injection engine

<figure class="kg-card kg-image-card kg-card-hascaption">
<img src="/content/images/2019/07/Bosch-W8C0-W145M2-0241229021-spark-plug-1.jpg" class="kg-image" />
<figcaption>Obsolete: original W8C0 spark plug for FI engines. Notice the gap preset at 0.7 mm and the Cr electrode.</figcaption>
</figure>

<figure class="kg-card kg-image-card kg-card-hascaption">
<img src="/content/images/2019/07/bosch-w8cc-1.jpg" class="kg-image" />
<figcaption>Obsolete: the W8CC was a newer model as a replacement for the W8C0. Cu electrode (not seen).</figcaption>
</figure>

*From [type2.com's spark plug reference charts](http://www.type2.com/library/electrip/sparkpl.htm)*:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>Brand</th>
<th># in Bentley</th>
<th>Alternate #</th>
</tr>
</thead>
<tbody>
<tr>
<td>Beru</td>
<td>145/14/3L</td>
<td>-</td>
</tr>
<tr>
<td>Bosch</td>
<td>W145M2 W8C0 [0 241 229 021]</td>
<td>W8CC0 [??]<br />
W8CC [0 241 229 579]<br />
W7 DTC [0 241 235 643]<br />
WR 8 AC [0 242 229 534]<br />
WR 7 DP [0 242 235 541]<br />
WR 7 D+ [0 242 235 909, -946, -663]</td>
</tr>
<tr>
<td>Champion</td>
<td>N288 or N5C (replaced N288)</td>
<td>N11YC</td>
</tr>
<tr>
<td>NGK</td>
<td>-</td>
<td>B5ES or BR5ES (resistor)</td>
</tr>
</tbody>
</table>

*From ["Reparaturleitfaden" Aug. '81 (V.A.G)](http://www.michaelknappmann.de/bulli/michaelk/vw_bus_d/rlf_typ1_typ2_-06-79/06.html):*

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>Type/Engine/Feature</th>
<th>under 25°C</th>
<th>over 25°C</th>
</tr>
</thead>
<tbody>
<tr>
<td>2/2.0 l/L-Jetronic</td>
<td>Bosch W8CO<br />
Beru 145/14/3 L<br />
Champion N288</td>
<td>Bosch W8C0<br />
Beru 145/14/3 L<br />
Champion N288</td>
</tr>
</tbody>
</table>

ℹ️ The original Bosch part number was W 145 M2 / W8C0. The newer part number was W8CC0. It was reportedly a long life version of the W8CC, with reinforced electrodes. Insted of having ~2.5mm electrodes, the W8CC0 had ticker (ca. 3.0 mm) electrodes, so that the gap erosion was slower.

ℹ️ Bentley shows Bosch W 145 T2 (0 241 229 548). The latest designation by Bosch is W8CC (0 241 229 579). Stock gap is 0.024 inch, 0.60 mm.

### Dual carburetor engine

<figure class="kg-card kg-image-card kg-card-hascaption">
<img src="/content/images/2019/07/w8c.jpg" class="kg-image" />
<figcaption>obsolete: W8C with gap preset at 0.6 mm for dual-carburetor engines</figcaption>
</figure>

### All engines

<table style="width:100%;">
<colgroup>
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Source</th>
<th style="text-align: left;">Engine</th>
<th style="text-align: left;">Conditions</th>
<th style="text-align: left;">Beru</th>
<th style="text-align: left;">Bosch</th>
<th style="text-align: left;">Champion</th>
<th style="text-align: left;">NGK</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Haynes</td>
<td style="text-align: left;">1.7L-1.8L carbs</td>
<td style="text-align: left;">Normal</td>
<td style="text-align: left;"><del>145/14/3</del><br />
14-8 C</td>
<td style="text-align: left;"><del>W 145 T2</del><br />
W8C</td>
<td style="text-align: left;">N. 88</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;">Haynes</td>
<td style="text-align: left;">1.7L-1.8L carbs</td>
<td style="text-align: left;">Tropics</td>
<td style="text-align: left;">175/14/3</td>
<td style="text-align: left;">W 175 T2</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;">Haynes</td>
<td style="text-align: left;">1.8L-2.0L FI</td>
<td style="text-align: left;">N/A</td>
<td style="text-align: left;">145/14/3L</td>
<td style="text-align: left;">W 145 M2</td>
<td style="text-align: left;">N 288</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;">'79 owner's manual (US)</td>
<td style="text-align: left;">2.0L FI</td>
<td style="text-align: left;">N/A</td>
<td style="text-align: left;">145/14/3L</td>
<td style="text-align: left;">W 145 M2</td>
<td style="text-align: left;">N-288</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;">'79 owner's manual (DE/UK)</td>
<td style="text-align: left;">1.6L carbs</td>
<td style="text-align: left;">Normal</td>
<td style="text-align: left;">145/14/14-8a</td>
<td style="text-align: left;">W 145 T1·1 / W8a</td>
<td style="text-align: left;">L88A</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;">'79 owner's manual (DE/UK)</td>
<td style="text-align: left;">1.6L carbs</td>
<td style="text-align: left;">Heavy duty above 25°C</td>
<td style="text-align: left;">175/14</td>
<td style="text-align: left;">W 145 T1</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;">'79 owner's manual (DE/UK)</td>
<td style="text-align: left;">2.0L carbs</td>
<td style="text-align: left;">Normal</td>
<td style="text-align: left;">145/14/3/14-8c</td>
<td style="text-align: left;">W 145 T2/W8C</td>
<td style="text-align: left;">N7</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: left;">Bosch (2017)</td>
<td style="text-align: left;">2.0L FI</td>
<td style="text-align: left;">N/A</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">W 8 AC</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;"><em>B5HS</em></td>
</tr>
<tr>
<td style="text-align: left;">Bosch (2017)</td>
<td style="text-align: left;">2.0L FI</td>
<td style="text-align: left;">N/A</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">W 7 DP</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;"><em>BP6ES</em></td>
</tr>
<tr>
<td style="text-align: left;">Bosch (2017)</td>
<td style="text-align: left;">2.0L FI</td>
<td style="text-align: left;">N/A</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;">W 7 D+</td>
<td style="text-align: left;">-</td>
<td style="text-align: left;"><em>BP6ES</em></td>
</tr>
</tbody>
</table>

From [Reparaturleitfaden](http://www.michaelknappmann.de/bulli/michaelk/vw_bus_d/rlf_typ1_typ2_-06-79/06.html), Aug. '81

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Engine</th>
<th style="text-align: left;">Fuel delivery</th>
<th style="text-align: left;">Normal conditions (&lt; 25°C)</th>
<th style="text-align: left;">Heavy duty (&gt; 25°C)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">1.3L-1.6L</td>
<td style="text-align: left;">Carbs</td>
<td style="text-align: left;">Bosch W 8 A<br />
Beru 14-8 A<br />
Champion L 88 A</td>
<td style="text-align: left;">Bosch W 7 A<br />
Beru 14-7A</td>
</tr>
<tr>
<td style="text-align: left;">1.7L-1.8L-2.0L</td>
<td style="text-align: left;">Carbs</td>
<td style="text-align: left;">Bosch W 8 C<br />
Beru 14-8 C<br />
Champion N 7</td>
<td style="text-align: left;">Bosch W 7 C<br />
Beru 14-7 C</td>
</tr>
<tr>
<td style="text-align: left;">2.0L</td>
<td style="text-align: left;">Injection</td>
<td style="text-align: left;">Bosch W 8 CO<br />
Beru 145/14/3 L<br />
Champion N 288</td>
<td style="text-align: left;">Bosch W 8 CO<br />
Beru 145/14/3 L<br />
Champion N 288</td>
</tr>
</tbody>
</table>

## Further reading

- [Spark plug terms](https://www.sparkplugs.com/learning-center)
- [Spark plug replacement](http://www.type2.com/bartnik/spplug.htm)
- [Spark plug torque](https://www.thesamba.com/vw/forum/viewtopic.php?p=7602295)
- [Spark plug heat ranges](https://matchlessclueless.com/mechanical/ignition/spark-plug-temperature/)
