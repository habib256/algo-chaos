#!/usr/bin/python
#coding: utf8

# Velocity Verlet integrator

def Verlet(r, v, dt, a):
	"""Return new position and velocity from current values, time step and acceleration.

	Parameters:
	   r is a numpy array giving the current position vector
	   v is a numpy array giving the current velocity vector
	   dt is a float value giving the length of the integration time step
	   a is a function which takes x as a parameter and returns the acceleration vector as an array

	Works with arrays of any dimension as long as they're all the same.
	"""
	# Deceptively simple (read about Velocity Verlet on wikipedia)
	r_new = r + v*dt + a(r)*dt**2/2
	v_new = v + (a(r) + a(r_new))/2 * dt
	return (r_new, v_new)


# Start main program

if __name__=="__main__":
	# Import required libraries
	from numpy.linalg import norm
	from numpy import array, zeros
	
	# Define acceleration function
	# First some natural constants
	G = 6.673e-11 # Gravitational constant
	MGsun = 1.98e30 * G # Mass of the sun
	sun = array([0, 0, 0]) # Place sun at origin
	# Then the function itself
	def a(r):
		# This is just the sun's force of gravity per unit mass:
		Asun = -MGsun * r / norm(r)**3
		return Asun
	
	# Set starting values for position and velocity
	r = array([1.49e11, 0, 0])
	v = array([0, 29.783e3, 0])


	# We are now running a simulation of 180 days with 20000 timesteps
	T = 86400*180*200 # simulated time in seconds
	N = 20000 # integration time steps
	M = 500   # save position every M timestep
	dt = T*1.0 / (N) # calculate timestep length in seconds

	# Lists for storing the position and velocity
	Rlist = zeros([3,int(N/M)])
	Vlist = zeros([3,int(N/M)])
	# Put the initial values into the lists
	Rlist[:,0] = r
	Vlist[:,0] = v

	# Run simulation
	print ("Integrating %d seconds with time step dt = %f seconds." % (T, dt))
	print ("Total number of steps:", N)
	print ("Saving location every %d steps." % (M))
	print ("Start.")
	for i in range(int(N/M)):
		# Run for M steps before saving values
		for j in range(M):
			# Update position and velocity based on the current ones
			# and the acceleration function 
			r, v = Verlet(r, v, dt, a)
		# Save values into lists
		Rlist[:, i] = r
		Vlist[:, i] = v
	print ("Stop.")

	# Plot results	
	from matplotlib import pyplot as plot
	plot.title("%d seconds, $dt=%f$, sampled every %.2f seconds" % (T, dt, M*dt))
	# Set equal axis
	plot.axis('equal')
	# Draw x and y axis lines
	plot.axhline(color="black")
	plot.axvline(color="black")
	
	# Draw the sun as a 
	plot.scatter(sun[0], sun[1], 400, c=["y"])
	# Plot the orbit as a line
	plot.plot(Rlist[0,:], Rlist[1,:], "-")
	plot.show()
