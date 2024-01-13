import matplotlib.pyplot as plt
import numpy as np

'''
PROBLEM STATEMENT 
   Flux = 2*u
   u_0(x) = 1 when x<0
          = 0 when x>=0
    Domain : (-2,2)
'''

##### FOR PANDAS #####
mydata = []
mycol = ["U[n,j]","U_plus_half","u_minus_half","second_term","U[n+1,j]"]
#### END #######

# Defining the variables
N = 500                   # Number of points
xmin,xmax = -2,2             # Domain limits
 
Lx = xmax - xmin             # Domain Size
dx = Lx/N                   # Mesh width
x = np.linspace(xmin,xmax,N) # Mesh Points

dt = 0.001                   # time step 
T = 1                        # Total time
Nt = int(T/dt)               # no of time iterations

U = np.zeros((Nt+1,N)) 

# Defining the initial condition
for i in range(len(x)):
    if x[i]<0:
        U[0,i] = 1
    else:
        U[0,i] = 0


def flux(n,i):
    return  U[n,i]**2/2

def func(n,i,j):
    return (flux(n,i)+flux(n,j))/2 - (dx/dt)*(U[n,j]-U[n,i])/2

# def Uxxx(n,i):
#     return U[n,i] - 3*U[n,i-1] + 3*U[n,i-2] - U[n,i-3]


# Solving using numerical analysis
for n in range(0,Nt):
    for j in range(1,N-1):
        # First calculating the numerical flux
        # third_term = (dt/(dx**3))*Uxxx(n,j)
        # Basic Formula to calculate U^n_j+1
        U[n+1,j] = U[n,j] - (dt/dx)*(func(n,j,j+1)- func(n,j-1,j)) 

    # Assigning U^n+1_0 as loop starts from 1
    U[n+1,0] = U[n+1,N-1] 


    #Ploting 
    if (n==0): fig, ax = plt.subplots(figsize=(5.5,4))
    plt.clf() # Clear Screen
    plt.plot(x,U[n+1,:])
    plt.axis([xmin, xmax, 0, 1.4])
    plt.title('t='+str(round(dt*(n+1),3)),fontsize=16)
    plt.xlabel('x',fontsize=18)
    plt.ylabel('u',fontsize=18)
    plt.grid(True)
    plt.draw()
    plt.pause(0.001)

plt.show()

