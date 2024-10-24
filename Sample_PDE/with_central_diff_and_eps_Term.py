import matplotlib.pyplot as plt
import numpy as np 

# Initial data
N = 1000
xmin,xmax = 0,40
L = xmax - xmin
dx = L/(N-1)
x = np.linspace(xmin,xmax,N)

cfl = 0.1
c = 1

dt = cfl * dx / c
# dt = 0.001
print(dx,dt)
T = 5            
Nt = int(T/dt)     

U = np.zeros((Nt+1,N+4),dtype = float)
Uex = np.zeros((Nt+1,Nt))
u0 = 0.25*(1/np.square(np.cosh((0.5**(1/2)/2)*x - 7)))
### END #####

U[0,2:N+2] = u0
U[0,0:2] = u0[N-2:N]
U[0,N+2:N+4] = U[0,0:2] 

def f(u):
    return (u**2)/2 

def num_flux(n,j):
    if j==-1:
        return (f(U[n,2:N+2]) + f(U[n,1:N+1]))/2 - (dx/dt)*(U[n,2:N+2]-U[n,1:N+1])/2
    else:
        return (f(U[n,2:N+2]) + f(U[n,3:N+3]))/2 - (dx/dt)*(U[n,3:N+3]-U[n,2:N+2])/2


for n in range(0,Nt):
    second_term = (dt/dx)*(num_flux(n,1) - num_flux(n,-1))
    third_term = (dt/dx**3)*(U[n,4:N+4] - 2*U[n,3:N+3] + 2*U[n,1:N+1]- U[n,0:N])*(0.5)
    U[n+1,2:N+2] = U[n,2:N+2]  - 0.01*third_term

    U[n+1,0:2] = U[n+1,N:N+2]
    U[n+1,N+2:N+4] = U[n+1,2:4]
    
    if (n==0): fig, ax = plt.subplots(figsize=(5.5,4))
    plt.clf()
    plt.plot(x,U[n+1,2:N+2],label = "Approx Data")
    Uex = 0.25*(1/np.square(np.cosh((0.5**(1/2)/2)*(x-(dt*(n+1)/2)) - 7)))
    plt.plot(x,Uex,label = "Exact Data")
    plt.title("Time : "+ str(round((n+1)*dt,4)),fontsize=16)
    plt.text(x = 0, y = 0.25 ,s  = "N= "+str(N) + " cfl= " + str(c*dt/dx),fontsize=13)
    plt.axis([xmin,xmax,-0.05,0.3])
    plt.xlabel('x',fontsize=12)
    plt.ylabel('u',fontsize=12)
    plt.grid(True)
    plt.legend()
    plt.draw()
    plt.pause(0.0001)
    

plt.show()
    
