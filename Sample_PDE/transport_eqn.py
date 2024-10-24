import matplotlib.pyplot as plt
import numpy as np

'''
PROBLEM STATEMENT 
    Transport Equation 
    i.e. u_t + a.u_x = 0
    Domain : [0,1]   

    U_0(x) = sin(2πx)  
    a = 1
'''

# Defining the variables

N = 1000             # Number of points
xmin,xmax = 0,1     # Domain limits
 
Lx = xmax - xmin    # Domain Size
dx = Lx/(N-1)       # Mesh width
x = np.linspace(xmin,xmax,N) # Mesh Points

dt = 0.001          # time step 
T = 1              # Total time
Nt = int(T/dt)      # no of time iterations

a = 1               # Constant

U = np.zeros((Nt+1,N)) 
U[0,:] = np.sin(2*np.pi*x)
Uex = U[0,:]  # Exact solution for now initialising with u0


# Solving using numerical analysis
for n in range(0,Nt):
    for j in range(1,N):
        U[n+1,j] = U[n,j] - ((a*dt)/(dx))*(U[n,j]-U[n,j-1])
    
    U[n+1,0] = U[n+1,N-1]

# Computing exact solution
   

    #Ploting 
    if (n==0): fig, ax = plt.subplots(figsize=(5.5,4))
    plt.clf()
    plt.plot(x,U[n+1,:])
    plt.axis([xmin, xmax, -1.4, 1.4])
    plt.title('t='+str(round(dt*(n+1),3)),fontsize=16)
    plt.xlabel('x',fontsize=18)
    plt.ylabel('u',fontsize=18)
    plt.grid(True)
    plt.draw()
    plt.pause(0.001)

plt.show()
