"""
=====
Algo & Chaos 3
PenduleBasic.py
=====
2021 GPL3 VERHILLE Arnaud (gist974@gmail.com) 
pour l'IREM de la Réunion (https://irem.univ-reunion.fr)

"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
g = 9.8
L = 3  # Changed from 1.0 to 9.0
theta_0 = np.pi / 4
b = 0.2  # Damping coefficient

# Time
t_max = 45.0
dt = 0.01
t = np.arange(0, t_max, dt)

# Pendulum's initial angle and angular velocity
theta = np.zeros_like(t)
theta_dot = np.zeros_like(t)
theta[0] = theta_0
theta_dot[0] = 4 # Initial angular velocity

for i in range(1, len(t)):
    theta_dot[i] = theta_dot[i-1] + (-b * theta_dot[i-1] - (g / L) * np.sin(theta[i-1])) * dt
    theta[i] = theta[i-1] + theta_dot[i] * dt

# Create figure and axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Create phase space plot
line2, = ax2.plot([], [], 'r-')
ax2.set_xlim(0, 10)
ax2.set_ylim(-4, 4)
ax2.set_xlabel('Angle °')
ax2.set_ylabel('Vitesse m/s')
ax2.set_title('Espace des phases')  # Set title for the second plot

# Create pendulum animation
line, = ax1.plot([0, np.sin(theta_0)], [0, -np.cos(theta_0)], 'o-', markersize=10)
ax1.set_xlim(-1.1, 1.1)
ax1.set_ylim(-1.1, 1.1)  # This line positions the pendulum's axis at the top of the plot
ax1.axis('off')  # This line turns off the axis
ax1.set_title('Le Pendule')  # Set title for the first plot

# Create a text object
temps_text = ax1.text(0, 0, '', transform=ax1.transAxes)

def animer(i):
    # Update the line and text objects
    line.set_data([0, np.sin(theta[i])], [0, -np.cos(theta[i])])
    temps_text.set_text('Temps = %.1f s' % (i*dt))
    line2.set_data(theta[:i], theta_dot[:i])  # Update phase space plot
    return line, line2, temps_text,

ani = animation.FuncAnimation(fig, animer, frames=len(t), interval=dt*1000, blit=True)

plt.show()
