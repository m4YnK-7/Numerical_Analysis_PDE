import matplotlib.pyplot as plt
import numpy as np

"""
PROBLEM STATEMENT
f(u) = u^2/2
u_0 = 1 for x<0 and 0 for x>=0
"""

#Declaring the variables
N = 1000                        # No of cells
xmin,xmax = -2,2                # Limits
L = xmax - xmin                 # Grid width
dx = L/N                        # Cell width
x = np.linspace(xmin,xmax,N)    # Cell Centers

dt = 0.001                      # Time step
T = 1                           # Total time
Nt = int(T/dt)                  # no of iterations

# U_x and initial data
U = np.zeros((Nt+1,N))

# Declaring u_0
for i in range(len(x)):
    if(x[i]<0): U[0,i] = 1
    else: U[0,i] = 0

# Function for Numerical flux
def Num_Flux(n,i,j):
    return (U[n,i]**2 + U[n,j]**2)/4 - (dx/dt)*(U[n,j] - U[n,i])/2

# Numerical Analysis
for n in range(0,Nt):
    for j in range(1,N-1):
        # First calculating the numerical flux
        F_nj1 = Num_Flux(n,j,j+1)
        F_nj2 = Num_Flux(n,j-1,j)

        # Basic Formula to calculate U^n_j+1
        U[n+1,j] = U[n,j] - (dt/dx)*(F_nj1 - F_nj2) 

    # Assigning U^n+1_0 as loop starts from 1
    U[n+1,0] = U[n+1,N-1]


    if(n == 0): fig,ax = plt.subplots(figsize = (5.5,4))
    plt.clf()
    plt.plot(x,U[n+1,:])
    plt.axis([xmin,xmax,0,1.4]) 
    plt.title('t='+str(round(dt*(n+1),3)),fontsize=16)
    plt.xlabel('x')
    plt.ylabel('u')
    plt.grid(True)
  
    plt.draw()
    plt.pause(0.001)

plt.show()





