import matplotlib.pyplot as plt
import numpy as np

'''
PROBLEM STATEMENT 
   Flux = 2*u
   u_0(x) = 1 when x<0
          = 0 when x>=0
    Domain : (-2,2)
'''

# Defining the variables

N = 2000              # Number of points
xmin,xmax = -2,2     # Domain limits
 
Lx = xmax - xmin    # Domain Size
dx = Lx/N           # Mesh width
x = np.linspace(xmin,xmax,N) # Mesh Points

dt = 0.001          # time step 
T = 1                # Total time
Nt = int(T/dt)      # no of time iterations


U = np.zeros((Nt+1,N)) 
U[0,:] = 1
for i in range(len(x)):
    if x[i]<0:
        U[0,i] = 1
    else:
        U[0,i] = 0

# Uex = U[0,:]  # Exact solution for now initialising with u0

# Solving using numerical analysis
for n in range(0,Nt):
    for j in range(1,N-1):
        F_j1 = U[n,j] + U[n,j+1] - (dx/dt)*(U[n,j+1] - U[n,j])/2
        F_j2 = U[n,j] + U[n,j-1] - (dx/dt)*(U[n,j] - U[n,j-1])/2 

        U[n+1,j] = U[n,j] - (dt/dx)*(F_j1 - F_j2)

    U[n+1,0] = U[n+1,N-1] 


# Computing exact solution


#Ploting 
    if (n==0): fig, ax = plt.subplots(figsize=(5.5,4))
    plt.clf()
    plt.plot(x,U[n+1,:])
    plt.axis([xmin, xmax, 0, 1.4])
    plt.title('t='+str(round(dt*(n+1),3)),fontsize=16)
    plt.xlabel('x',fontsize=18)
    plt.ylabel('u',fontsize=18)
  
    plt.draw()
    plt.pause(0.001)

plt.show()
