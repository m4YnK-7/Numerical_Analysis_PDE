import matplotlib.pyplot as plt
import numpy as np 

# Initial data
N = 1000
xmin,xmax = 0,40
L = xmax - xmin
dx = L/N
x = np.linspace(xmin,xmax,N)

dt = dx*0.5
T = 5            
Nt = int(T/dt)     

U = np.zeros((Nt,N),dtype = float)
U[0,:] = 0.25*(1/np.square(np.cosh((0.5**(1/2)/2)*x - 7)))
Uex = 0.25*(1/np.square(np.cosh((0.5**(1/2)/2)*(x-T/2) - 7)))

def Uxxx(n,i):
    return U[n,i] - 3*U[n,i-1] + 3*U[n,i-2] - U[n,i-3]

def flux(n,i):
    return  (U[n,i]**2)/2

def func(n,i,j):
    return (flux(n,i)+flux(n,j))/2 - (dx/dt)*(U[n,j]-U[n,i])/2

for n in range(0,Nt-1):
    for j in range(3,N-1):
        second_term = (dt/dx)*(func(n,j,j+1)-func(n,j-1,j))
        third_term = (dt/(dx**3))*Uxxx(n,j)

        U[n+1,j] = U[n,j] - float(second_term) - float(third_term)


    if (n==0): fig, ax = plt.subplots(figsize=(5.5,4))
    plt.clf()
    plt.plot(x,U[n+1,:],label = "Approx Data")
    Uex = 0.25*(1/np.square(np.cosh((0.5**(1/2)/2)*(x-(dt*(n+1)/2)) - 7)))
    plt.plot(x,Uex,label = "Exact Data")
    plt.axis([xmin,xmax,-0.05,0.3])
    plt.xlabel('x',fontsize=12)
    plt.ylabel('u',fontsize=12)
    plt.title("Time step : "+str(n+1),fontsize=16)
    plt.grid(True)
    plt.legend()
    plt.draw()
    plt.pause(1)

plt.show()

