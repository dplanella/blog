---
title: "VW Type 2 ECU part number reference"
slug: "vw-type-2-ecu-part-number-reference"
date: 2017-12-06T19:32:00.000Z
tags: ["vw-bus", "l-jetronic"]
images: ["/content/images/2019/07/IMG_20171207_183804.jpg"]
---

Starting with model year 1975, VW busses of the era featured fuel injection via Bosch's L-Jetronic system, with an analog Electronic Control Unit (ECU) to manage fuel induction. Over the years Bosch and VW produced different types of ECUs, with a plethora of part numbers. This guide seeks to provide a reference to their application and interchangeability.

## Part numbers and interchangeability

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th>Model year</th>
<th>California Manual<br />
Part # (VW, Bosch)<br />
Description</th>
<th>California Automatic<br />
Part # (VW, Bosch)<br />
Description</th>
<th>Federal Manual<br />
Part # (VW, Bosch)<br />
Description</th>
<th>Federal Automatic<br />
Part # (VW, Bosch)<br />
Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>1974</td>
<td>n/a<br />
n/a<br />
n/a</td>
<td>022-906-021-K<br />
0 280 000 113<br />
(412E) Model 74 USA, similar to 0 280 000 101, but different adjustments.</td>
<td>n/a<br />
n/a<br />
n/a</td>
<td>n/a<br />
n/a<br />
n/a</td>
</tr>
<tr>
<td>1975</td>
<td>022-906-021-L<br />
0 280 000 108<br />
Model 75 USA, with plastic support frame; with intake air correction, post-start enrichment; anti-bucking circuitry and RPM limiter.</td>
<td>022-906-021-M<br />
0 280 000 117<br />
Model 75 automatic, same as 108, but without anti-bucking circuitry.</td>
<td>022-906-021-H<br />
0 280 000 122<br />
Model 75 USA, same as 108, without RPM limiter.</td>
<td>022-906-021-J<br />
0 280 000 124<br />
Model 75 USA automatic, same as 108, without RPM limiter or anti-bucking circuit.</td>
</tr>
<tr>
<td>1976</td>
<td>022-906-021-Q<br />
0 280 000 141<br />
Model 76 California, with intake air correction</td>
<td>022-906-021-R<br />
0 280 000 145<br />
Model 76 California, with intake air correction</td>
<td>022-906-021-N<br />
0 280 000 139<br />
Model 76 USA, with intake air correction</td>
<td>022-906-021-P<br />
0 280 000 143<br />
Model 76 USA automatic, with intake air correction</td>
</tr>
<tr>
<td>1977</td>
<td>022-906-021-AA<br />
0 280 000 153<br />
Model 77 California, with RPM limiter</td>
<td>022-906-021-AB<br />
0 280 000 155<br />
Model 77 California, with RPM limiter</td>
<td>022-906-021-S<br />
0 280 000 149<br />
Model 77 USA, without full load correction</td>
<td>022-906-021-T<br />
0 280 000 151<br />
Model 77 USA automatic, with intake air correction</td>
</tr>
<tr>
<td>1978</td>
<td>022-906-021-AE<br />
0 280 000 164<br />
Model 78 USA, same as 153, but without acceleration enrichment</td>
<td>022-906-021-AF<br />
0 280 000 168<br />
Model 78 USA, same as 164, but without anti-bucking circuitry.</td>
<td>022-906-021-AG<br />
0 280 000 166<br />
Model 78 Sweden, same as 153, but with acceleration enrichment (<em>with throttle position sensor?</em>)</td>
<td>022-906-021-AH<br />
0 280 000 170<br />
Model 78 Sweden, same as 166, but without anti-bucking circuitry</td>
</tr>
<tr>
<td>1979</td>
<td>039-906-021D<br />
0 280 000 182<br />
Model 79 California, with Lambda control</td>
<td>039-906-021E<br />
0 280 000 184<br />
Model 79 California automatic, same as 182, but without anti-bucking circuitry.</td>
<td>039-906-021-B<br />
0 280 000 178<br />
Model 79, with RPM limiter.</td>
<td>039-906-021-C<br />
0 280 000 180<br />
Model 79 automatic, same as 170 with reworked circuitry</td>
</tr>
<tr>
<td>1980</td>
<td>071-906-021B<br />
0 280 000 194<br />
(Vanagon) Model 80 California, same as 182, but with different adjustments and component placement</td>
<td>071-906-021B<br />
0 280 000 194<br />
(Vanagon) Model 80 California, same as 182, but with different adjustments and component placement</td>
<td>039-906-021-E<br />
0 280 000 184<br />
** (Vanagon) Model 79 automatic California, same as 182, but without anti-bucking circuit.</td>
<td>039-906-021-C<br />
0 280 000 180<br />
(Vanagon) Model 79 automatic, same as 170 with reworked circuitry</td>
</tr>
</tbody>
</table>

<figure class="kg-card kg-image-card kg-card-hascaption">
<img src="/content/images/2019/07/VW-Type-2-l-jetronic-ecu.jpg" class="kg-image" />
<figcaption>A quick look at the insides of my spare ECU, a 039 906 021 B for a Federal 1979 bus</figcaption>
</figure>

## ECU capabilities

Most of the L-Jetronic ECUs in VW busses operate in an open control loop, by sensing engine speed and load as the essential inputs, and converting them to injection time (*t<sub>i</sub>*) as output for each driving condition. The last model year (1979) featured a closed control loop with a lambda sensor to sense and feed back the air/fuel mixture density.

The output stage drives the fuel injectors directly, by opening their valves with a pulse width equivalent to the calculated injection time.

It is a fully analog control unit, with no microcontroller or firmware. It is mostly built with discrete electronic components and generally 3 custom Bosch integrated circuits that perform the Pulse shaper/divider, Division control multivibrator and Multiplier functions.

<figure class="kg-card kg-image-card">
<img src="/content/images/2019/07/L-Jetronic-ECU-block-diagram.png" class="kg-image" />
</figure>

In addition to the fundamental engine speed and load inputs, other variables also play a role in adjusting the final injection time. These are listed here in terms of ECU capabilities that were added or removed depending on the application:

**Post-start enrichment** – After the motor has started, an additional quantity of fuel will be injected as means of enrichment, that will be dependent on time and engine temperature (TS2, ECU).

**Intake air correction** – In order to compensate for the physically induced measuring error of the air flow meter, the injection time is corrected as a function of the intake air (Air flow, TS1, ECU)

**Full load enrichment** – when a full load event is detected via the Wide Open Throttle (WOT) switch, the injector time is extended to enrich the mixture (WOT switch, ECU). Only busses from model years '75-'76 and '79 California featured a WOT switch.

**RPM limiter** – fuel injector pulses are stopped at engine speed values higher than 5400 RPM (ECU).

**Acceleration enrichment** – Upon acceleration with the gas pedal, a temperature- and time-controlled fuel enrichment takes place (TS2, ECU)

**Anti-bucking** – When bucking occurs, it is assumed that the load changes are smaller than in an intended acceleration. If a load change occurs below a certain threshold value, the control variable will not be the newly calculated value of the slightly changed load, but instead it will be an approximation of this new value (Air flow, engine RPM, ECU).

## Interchangeability

> Almost all VW Type 2 ECUs are interchangeable with either moderate or no extra effort. The only exception is the '79 CA ECU, which would require major harness modifications.

> There is no difference in manual vs. automatic from the ECU point of view.

In more detail:

- **RPM Limiter** function (interchangeable with all ECUs except '79 CA). A distributor rotor with mechanical RPM limiter is needed if the ECU does not have the electronic function.
- **Wide Open Throttle switch** support (interchangeable with all ECUs except '79 CA). Reportedly, there isn't a noticeable effect in running an ECU with that capability, but without the actual WOT switch.
- **Air temperature sensor** support (interchangeable between '75 and early '76 ECUs). The '75 and early '76 busses AFM did not have an air temperature sensor output (TS1). The AFM can be upgraded to a 7-pin one and a later ECU can be used for replacement, but not the other way round (unless you downgrade to a 6-pin AFM).
- **Lambda sensor** support (only '79 CA). With the right harness to account for the different double-relay and removing the injector series resistors, it might be possible that this ECU can operate in open loop without the O2 sensor. Probably too much of an effort to test this interchangeability option.

## Additional notes

Some things to notice on compiling this overview:

- The Bosch documentation is not very consistent in describing which exact capabilities an ECU part number had. Also some key functons such as injector current control of the '79 CA ECUs were never listed.
- There were separate part numbers for ECUs going to the Swedish market too.
- From the descriptions, some degree of interchangeability can already be inferred.
- The first ever Type 2 ECU (1975, CA Manual) seemed to have all available functions except for Lambda control (which had not yet been on the market). Subsequent ECU parts removed or added functions as necessary. This lead to an explosion of part numbers, but it must have been cost-effective enough to justify it. There are even more ECU part numbers in the Bosch parts list, but this overview is focused only on the known ones from the original ECU part numbers table from the Bentley Manual and the The Samba forum thread (see reference section).
- The different ECU capabilites were translated from some other Bosch document.
- It is unclear to me what the anti-bucking (**Anti-Ruckeln** in German) circuitry does, but it seems to have been an internal circuit in the ECU that acted upon particular changes of air flow and engine speed.
- A couple of ECUs have acceleration enrichment capability, but it is also unclear to me how acceleration was sensed without a throttle position sensor (instead of the WOT switch), such as the D-Jetronic one. The ECU could have sensed the rate of speed change, but there were limits to what a few discrete components could do. This was not a microcontroller-based ECU.

## Reference

- Volkswagen Service Manual Type 2, Robert Bentley publishers, Section 10 (Fuel injection), pp 23.
- [Differences in ECUs between the years](https://www.thesamba.com/vw/forum/viewtopic.php?t=301261), post on The Samba forum.
- [Fuel injection (Bosch parts interchange)](http://www.type2.com/library/fuel/fuelibo.htm) at type2.com
- [Fuel injection swaps, ECU parts numbers](http://ratwell.com/technical/FISwap.html#ecu) by Richard Atwell
