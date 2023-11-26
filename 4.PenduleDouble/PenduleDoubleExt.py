#=======================================================================================================================================
# This script computes the equation of motion of a damped double pendulum using a full Newtonian analysis with sympy, 
# then solve them numerically, and finally visualize the solution using matplotlib.
#=======================================================================================================================================


import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


####################################################################################################
#Derivation of motion Equations USING SYMPY

sp.init_printing(use_latex='mathjax')

m1, m2, g, t, b = sp.symbols ('m_1, m_2, g, t, b')
R1, R2 = sp.symbols('R_1 R_2')
theta1 = sp.Function("theta_1")(t)
theta2 = sp.Function("theta_2")(t)
T1 = sp.Function("T_1")(t)
T2 = sp.Function("T_2")(t)


# First pendulum

r1 = sp.Matrix([R1*sp.sin(theta1),-R1*sp.cos(theta1)])
a1 = sp.diff(r1,t,2)

# forces are weight1, tension1, tension2 and damping1
forces1 = sp.Matrix([0,-m1*g]) + sp.Matrix([-T1*sp.sin(theta1), T1*sp.cos(theta1)])+ sp.Matrix([T2*sp.sin(theta2), -T2*sp.cos(theta2)])
forces1 += sp.Matrix([-b*R1*sp.diff(theta1,t)*sp.cos(theta1), -b*R1*sp.diff(theta1,t)*sp.sin(theta1)])

# We change the basis to simplify the problem
base1 = sp.Matrix([[sp.sin(theta1),-sp.cos(theta1)],[sp.cos(theta1),sp.sin(theta1)]])
eq1 = sp.simplify(base1*(m1*a1 - forces1)) 

#Second pendulum

r2 = sp.Matrix([R2*sp.sin(theta2),-R2*sp.cos(theta2)])
a2 = sp.diff(r2,t,2)

# forces are weight2, tension2 and damping2
forces2 = sp.Matrix([0,-m2*g]) + sp.Matrix([-T2*sp.sin(theta2), T2*sp.cos(theta2)])
forces2 += sp.Matrix([-b*R2*sp.diff(theta2,t)*sp.cos(theta2), -b*R2*sp.diff(theta2,t)*sp.sin(theta2)])

# We must take into account the forces not inertial forces
base2 = sp.Matrix([[sp.sin(theta2),-sp.cos(theta2)],[sp.cos(theta2),sp.sin(theta2)]])
eq2 = sp.simplify(base2*(m2*a2 - (forces2 - m2*forces1/m1)))

eqlist = [eq1[0],eq1[1],eq2[0],eq2[1]]

# We solve the linear system for tension1, tension2 and the angular accelerations of both pendulums
sv = sp.solve(eqlist, [T1, T2, sp.diff(theta1,t,2),sp.diff(theta2,t,2)])

omega1 = sp.Function("omega_1")(t)
omega2 = sp.Function("omega_2")(t)

alpha1 = sv[sp.diff(theta1,t,2)].subs(sp.diff(theta2,t),omega2).subs(sp.diff(theta1,t),omega1)
alpha2 = sv[sp.diff(theta2,t,2)].subs(sp.diff(theta2,t),omega2).subs(sp.diff(theta1,t),omega1)


####################################################################################################
# lambdify equations to integrate them with odeint

aph1 = sp.lambdify([theta1,theta2,omega1,omega2,g,R1,R2,m1,m2, b], alpha1)
aph2 = sp.lambdify([theta1,theta2,omega1,omega2,g,R1,R2,m1,m2, b], alpha2)


from scipy.integrate import odeint

def vectorfield(var, t, cst):
    q0, q1, w0, w1 = var
    g, l1, l2, m1, m2, b = cst

    
    f = [w0, w1, aph1(q0, q1, w0, w1, g, l1, l2, m1, m2, b), aph2(q0, q1, w0, w1, g, l1, l2, m1, m2, b)]

    return f


# ODE solver parameters
abserr = 1.0e-8
relerr = 1.0e-6
tfin = 40.0
steps = 300

b = 0.1
m1 = 1;
m2 = 1;
g = 9.81;
l1 = 1;
l2 = 1;

# Initial conditions

q0 = 0.979999999*np.pi
q1 = 0.979999999*np.pi
w0 = -1.0
w1 = -0.5


# ODE solver parameters
abserr = 1.0e-9
relerr = 1.0e-9
tfin = 40.0
h = 0.025
steps = int(np.rint(tfin/h))


t = np.linspace(0,tfin,steps+1)

cst = [g, l1, l2, m1, m2, b]
varini = [q0, q1, w0, w1]

sol = odeint(vectorfield, varini, t, args=(cst,), atol=abserr, rtol=relerr)
sol = np.transpose(sol)


####################################################################################################
#plot the solution with matplotlib


#Gradient plot definition
def make_segments(x, y):
    """
    Create list of line segments from x and y coordinates, in the correct format
    for LineCollection:  [[(x1, y1), (x2, y2)],...,[(xn-1, yn-1), (xn, yn)]]
    """

    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    return segments

from matplotlib.collections import LineCollection

def gradientplot(x, y, colors, cmap=plt.get_cmap('gist_rainbow'), linewidth=3, alpha=1.0,zorder=10):
    
    lines = make_segments(x, y)
    col = LineCollection(lines, array=colors, cmap=cmap, linewidth=linewidth, alpha=alpha,zorder=zorder)
    return col




from matplotlib.widgets import Slider  # import the Slider widget


fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(1,1,1)

plt.subplots_adjust(bottom=0.2,left=0.15)



ax.axis('equal')
ax.axis([-2.5, 2.5, -2.5, 2.5])
ax.set_title('damped double pendulum')
ax.set_xlabel('x (t)')
ax.set_ylabel('y (t)')


q1 = sol[0]
q2 = sol[1]
w1 = sol[2]
w2 = sol[3]

x1 = l1*np.sin(q1)
y1 = -l1*np.cos(q1)

x2 = x1+l2*np.sin(q2)
y2 = y1-l2*np.cos(q2)


pot = m1*g*y1 + m2*g*y2

kin = l1*l1*w1*w1 + 0.5*l2*l2*w2*w2+ l1*l2*w1*w2*np.cos(q1-q2)

e_s = kin + pot


trail = gradientplot(x2[:0],y2[:0], t[:steps+1], 'gist_rainbow', linewidth=1, alpha=0.5)
ax.add_collection(trail)

line1 = ax.plot([0,x1[0]],[0,y1[0]], color='k', lw=2, zorder=20)[0]
line2 = ax.plot([x1[0],x2[0]],[y1[0],y2[0]], color='k', lw=2, zorder=20)[0]

circle1 = plt.Circle((x1[0], y1[0]), 0.08, ec="k", lw=1.5, zorder=30)
ax.add_patch(circle1)
circle2 = plt.Circle((x2[0], y2[0]), 0.08, ec="k", lw=1.5, zorder=30)
ax.add_patch(circle2)

slider_ax = plt.axes([0.1, 0.05, 0.8, 0.05])

slider = Slider(slider_ax,      # the axes object containing the slider
                  't [s]',            # the name of the slider parameter
                  0,          # minimal value of the parameter
                  tfin,          # maximal value of the parameter
                  valinit=0,  # initial value of the parameter 
                  color = '#5c05ff' 
                 )


def update(time):
    i = int(np.rint(time*steps/tfin))
  
    #trail.set_array(t[:i+1])

    trail.set_segments(make_segments(x2[:i+1], y2[:i+1]))
    
    line1.set_ydata([0,y1[i]])
    line1.set_xdata([0,x1[i]])
    line2.set_ydata([y1[i],y2[i]])
    line2.set_xdata([x1[i],x2[i]])
    
    circle1.center = x1[i], y1[i]
    circle2.center = x2[i], y2[i]


slider.on_changed(update)

plt.show()
