import numpy as np
import matplotlib.pyplot as plt
import tomllib
from pathlib import Path
import sys

# How many iterations of the
# simulator are to be run.
# The higher the value, the
# less frequently terminal
# outputs will be made.
until = 500000

"""
fp = Path("config")
if (fp.is_file()):
  print("Config file found")
else:
  print("Config file not found in directory. Exiting.")
  sys.exit(1)
"""

G = 6.6743 * (10**-11) # m^3 kg^-1 s^-2

### R VECS ###

# Adjust each of these to change the
# positions of each of the bodies.

r_moon = np.array([-384398861.0, 1000])
r_earth = np.array([-100.0, -150.0])
r_sun = np.array([1.496e11, 700.0])

# Position vector of the spacecraft
r_sc = np.array([100000000.0, 5.0])

##############


def mass(index):
  return bds[index][1]


### ARRAY OF BODIES ###

# The second part of each tuple is the weight, in kilograms, of each body.

bds = [ (r_earth, 5.972 * (10**24)), (r_sun, 1.989 * (10**30)), (r_moon, 7.34767309 * (10**22)) ]

#######################

dt = 1
v = np.array([0.0, 1996.0])
_iter = 0

traj = []

modulo = until // 20

print("In progress")

### FORCE DEFS PRE LOOP ###

a_g_0 = -G * ( mass(0) * (r_sc - r_earth) ) / np.linalg.norm(r_earth - r_sc)**3
a_g_1 = -G * ( mass(1) * (r_sc - r_sun) ) / np.linalg.norm(r_sun - r_sc)**3
a_g_2 = -G * ( mass(2) * (r_sc - r_moon) ) / np.linalg.norm(r_moon - r_sc)**3

###########################
# Compute initial accel pre loop
a = a_g_0 + a_g_1 + a_g_2

while _iter < until:

  r_sc += v*dt + 0.5*a*(dt**2)  # Compute new position based on accel

  ### FORCE DEFS NEW POS ###

  a_g_0 = -G * ( mass(0) * (r_sc - r_earth) ) / np.linalg.norm(r_earth - r_sc)**3
  a_g_1 = -G * ( mass(1) * (r_sc - r_sun) ) / np.linalg.norm(r_sun - r_sc)**3
  a_g_2 = -G * ( mass(2) * (r_sc - r_moon) ) / np.linalg.norm(r_moon - r_sc)**3

  ##########################

  a_new = a_g_0 + a_g_1 + a_g_2 # Compute accel at new position
  v += 0.5 * (a + a_new) * dt   # New vel for next loop, avg of a and a_new
                                # vel production
  if (_iter % modulo == 0):
    print("r_sc        = " + str(r_sc))
    print("|r_scearth| = " + str(np.linalg.norm(r_earth - r_sc)))
    print("Iter " + str(_iter) + "/" + str(until) + " (" + str(_iter*100/until) + ")%")

  _iter += 1
  traj.append(r_sc.copy())

  a = a_new

traj = np.array(traj)

fig, ax = plt.subplots()
ax.set_xlim(-120000000, 120000000)
ax.set_ylim(-120000000, 120000000)
ax.set_aspect('equal')

### MPL BODY COLORS ###

# Change the last argument of ax.plot to change how
# each of the bodies appears in the plot. The 'o',
# or the first character of the last arg, dictates
# the shape of the point, and the first character
# dictates the color. For more info, google "mpl
# format strings".
dote = ax.plot([r_earth[0]], [r_earth[1]], 'bo')
dots = ax.plot([r_sun[0]], [r_sun[1]], 'yo')  
dotm = ax.plot([r_moon[0]], [r_moon[1]], 'ko')

# Traj start marker
ax.plot([traj[0][0]], [traj[0][1]], '^g')

#######################

plt.grid(True)
plt.plot(traj[:,0], traj[:,1], 'm-')
plt.show()
