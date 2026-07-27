# Euler-Cromer 4-body problem integrator
Probably not what you're thinking of in that this doesn't calculate the bodies' influence on each other (yet).

The next step for that would be letting the user define functions that govern the x and y movement of each of the bodies, which will almost definitely come before the sandbox-type "let-it-happen" approach, which will most definitely be very annoying to configure.

Currently, this assumes three, nonmoving bodies that are nailed in place (yes, only three; any more bodies that you might want will have to be manually added to the integration loop and array of bodies) and a spacecraft. I'm plan on making the capability for programmatically adding new bodies soon.

There are a few user-defined configuration variables in the main script (all of which I hope to move out to a config file soon):

|Variable|Units|Purpose|
|---|---|---|
|`until`|frames|Define the amount of frames the simulation is to run.|
|`r_*` (vector)|meters from origin|Defines position of Earth, Moon, Sun, and spacecraft initially|
|`bds[*][1]`|kilograms|Defines the mass of each body|
|`v`|meters per second|Defines starting velocity|

<!-- MPL adjustables, like line color, start marker style, dots -->
