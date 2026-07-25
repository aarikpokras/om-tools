# Hohmann Transfer Calculator
A calculator for ascending Hohmann transfers between circular orbits, using Keplerian motion.

The calculator outputs the phase angle (in this program solely based on orbital period) required for a rendezvous between spacecraft. The phase angle describes how many degrees of difference there must be (relative to the center of the body) for the Hohmann burn to start and for the chaser to reach the target.

## Customization
The hash box indicates the designated area for modification. It includes:

|Name|Purpose|Unit|
|---|---|---|
|mu|Gravitational Parameter (GM)|m³ s⁻²|
|h0|Radius of the body being orbited|m|
|h_chase|Height of the orbit of the chaser above the **surface**|m|
|h_target|Height of the orbit of the target above the **surface**|m|
