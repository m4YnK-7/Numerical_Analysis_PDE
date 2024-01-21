import numpy as np 
import matplotlib.pyplot as plt

# INITIAL DATA
N = 1000
xmin,xmax = 0,2*np.pi
L = xmax-xmin
dx = 0.
x = np.linspace(xmin,xmax,N)

T = 1
dt = 0.001

Nt = int(T/dt)

U = np.zeros((Nt+1,N+4))
Uex = -np.cos(x)

u0 = np.sin(x)
U[0,3:N+3] = u0
U[0,0:3] = u0[N-3:N]
U[0,N+3:N+4] = u0[0:1] 

for n in range(0,2):
    # U[n+1,3:N+3] = (U[n,3:N+3] - 3*U[n,2:N+2] + 3*U[n,1:N+1] - U[n,0:N])/dx**3
    U[n+1,2:N+2] =  (U[n,4:N+4] - 2*U[n,3:N+3] + 2*U[n,1:N+1] - U[n,0:N])/(2*dx**3)
        
    U[n+1,0:2] = U[n,N+2:N+4]
    U[n+1,N+2:N+4] = U[n+1,2:4]

    plt.clf()
    # plt.plot(x,U[0,:],label = "Initial Data")
    plt.plot(x,U[n+1,3:N+3],label = "Approx Data")
    # plt.plot(x,-np.cos(x),label = "-cos(x)")

    Uex = -np.cos(x - (n+1)*dt)
    plt.plot(x,Uex,label = "Exact Solution")    

    
    plt.axis([xmin,xmax,-1.2,1.2])
    plt.xlabel('x',fontsize=12)
    plt.ylabel('u',fontsize=12)
    plt.title("time step " + str(n+1),fontsize=16)
    plt.grid(True)
    plt.draw()
    plt.legend()
    plt.pause(2)

plt.show()




