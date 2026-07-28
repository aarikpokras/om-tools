# Velocity Verlet 4-body problem integrator

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
|`dt`|seconds|Timestep|

<!-- MPL adjustables, like line color, start marker style, dots -->

## Add a body
To add a body, add it to the `bdy` tuple array. The format is as follows:
```python
[ ... ( pos_vector_m, mass_kg ) ]
```

The position vectors are NumPy arrays, which can be added with something along the lines of:
```python
r_body = np.array([ pos_x_m, pos_y_m ])
```

A dot can be added to designate the position of the body in the Matplotlib visualization:
```python
### MPL BODY COLORS ###
# ...

ax.plot( [r_body[0]], [r_body[1]], '[color][shape]')

# ...
#######################
```

For `shape`, you can just use o. Additionally, you can use any shape usable in Matplotlib format strings.

The placeholders for color and shape can be changed based on Matplotlib format strings. A quick reference for the colors:
|Color|Code|
|---|---|
|Blue|b|
|Green|g|
|Red|r|
|Cyan|c|
|Magenta|m|
|Yellow|y|
|Black|k|
|White|w|
