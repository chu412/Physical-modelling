import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

##### PARAMETERS #####

Tf = 100000      # Final time - seconds
m = 1          # Particle mass
gamma = 2      # Friction
kb = 1         # Boltzmann cte = 1 for simplicity
T = 300        # [k] - Temperature


###### Discrete time
t = np.linspace(0, 1000, num = Tf)
dt = t[2]-t[1]

###### Noise
aux = np.zeros(Tf) # auxiliar array of the right size

# Function to create random numbers
Random = lambda n: np.random.normal(loc=0.0, scale=1.0) # Generate random number
MapRandom = map(Random,aux)

# Array of Noise
eta = np.sqrt(2*kb*T*gamma)*np.array(list(MapRandom)) # eta(t)

###### Initial position and velocity

x0 = 0          
v0 = 0       

###### Arrays of position and velocities

x = np.zeros(1)
x[0] = x0
v = np.zeros(1)
v[0] = v0

###### Discrete Langevin Equation

i = 1
while i < Tf:
    v = np.append(v, ((dt/m)*eta[i]+v[i-1])/(1+(dt/m)*gamma))
    x = np.append(x, x[i-1] + v[i]*dt)
    i+=1
fig, (left, right) = plt.subplots(1, 2, figsize=(15,5))

right.plot(t, x)
left.plot(t, v)

fig.suptitle('1-D Броуновское движение', fontsize=20)
right.set(xlabel = "Время, с", ylabel = "x(t)")
left.set(xlabel = "Время, с", ylabel = "v(t)")

right.set_xlim([0, 1000]);
left.set_xlim([0, 1000]);
plt.show()


