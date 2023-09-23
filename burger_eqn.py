import matplotlib.pyplot as plt
import numpy as np

"""
PROBLEM STATEMENT
flux = u^2/2
u_0(x) = sin(x)
Domain (0,2)
"""

#Declaring the variables
N = 1000                        # Number of points

xmin,xmax = 0,np.pi             # Domain limits
L = xmax - xmin                 # Domain Size
dx = L/N                        # Mesh width
x = np.linspace(xmin,xmax,N)    # Mesh Points

dt = 0.001                      # time step 
T = 1                           # Total time
Nt = int(T/dt)                  # no of time iterations

# U_x and initial data
U = np.zeros((Nt+1,N))
U[0,:] = np.sin(x)

# A function to calculate numerical flux 
# This is to avoid data overflow error 
def Num_flux(i,j):
    return (U[n,i]**2 + U[n,j]**2)/4 - (dx/dt)*(U[n,j]-U[n,i])/2

# Numerical Analysis
for n in range(0,Nt):
    for j in range(1,N-1):
        # First calculating the numerical flux
        F_nj1 = Num_flux(j,j+1)
        F_nj2 = Num_flux(j-1,j)

        # Basic Formula to calculate U^n_j+1
        U[n+1,j] = U[n,j] - (dt/dx)*(F_nj1 - F_nj2)

    # Assigning U^n+1_0 as loop starts from 1
    U[n+1,0] = U[n+1,N-1]

    # Plotting
    if(n == 0): fig,ax = plt.subplots(figsize = (5.5,4))
    plt.clf()
    plt.plot(x,U[n+1,:])
    plt.axis([xmin,xmax,0,1.5]) 
    plt.title('t='+str(round(dt*(n+1),3)),fontsize=16)
    plt.xlabel('x')
    plt.ylabel('u')
    plt.grid(True)
  
    plt.draw()
    plt.pause(0.001)

plt.show()