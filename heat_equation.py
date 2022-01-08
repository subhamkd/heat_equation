#solving the heat equation using finite difference method
import numpy as np

def heatBC(a,b,c,d,T,dx,dy):
    #left
    if a[0]=='N':
        T[:, 0]=a[1]*dx+T[:, 1]
    elif a[0]=='D':
        T[:,0]=a[1]
    else:
        return('Please enter a valid BC type')

    if b[0]=='N':
        T[:, -1]=b[1]*dx+T[:, -2]
    elif b[0]=='D':
        T[:, -1]=b[1]
    else:
        return('Please enter a valid BC type')

    #top
    if c[0]=='N':
        T[-1,:]=c[1]*dy+T[-2, :]
    elif c[0]=='D':
        T[-1,:]=c[1]
    else:
        return('Please enter a valid BC type')

    #bottom
    if d[0]=='N':
        T[0,:]=d[1]*dy+T[1, :]
    elif d[0]=='D':
        T[0,:]=d[1]
    else:
        return('Please enter a valid BC type')


def heat_equation(T,dx,dy,alpha,dt,nt,TBCs):
    Tn = np.empty_like(T)
    for n in range(nt):
        Tn = T.copy()
        T[1:-1,1:-1]=Tn[1:-1,1:-1]+(alpha*dt/dx**2)*(Tn[2:,1:-1]-2*Tn[1:-1,1:-1]+Tn[0:-2,1:-1])+(alpha*dt/dy**2)*(Tn[1:-1,2:]- 2 * Tn[1:-1, 1:-1] + Tn[1:-1, 0:-2])
        
        TLeft=TBCs[0]
        TRight=TBCs[1]
        TTop=TBCs[2]
        TBottom=TBCs[3]

        heatBC(TLeft,TRight,TTop,TBottom,T,dx,dy)
    return T

"""def heatBC(a,b,c,d,T,dx,dy):
    #left
    if a[0]=='N':
        T[0,:]=a[1]*dy+T[1, :]
    elif a[0]=='D':
        T[0,:]=a[1]
    else:
        return('Please enter a valid BC type')

    if b[0]=='N':
        T[-1,:]=b[1]*dy+T[-2, :]
    elif b[0]=='D':
        T[-1,:]=b[1]
    else:
        return('Please enter a valid BC type')

    #top
    if c[0]=='N':
        T[:, -1]=c[1]*dx+T[:, -2]
    elif c[0]=='D':
        T[:, -1]=c[1]
    else:
        return('Please enter a valid BC type')

    #bottom
    if d[0]=='N':
        T[:, 0]=d[1]*dx+T[:, 1]
    elif d[0]=='D':
        T[:, 0]=d[1]
    else:
        return('Please enter a valid BC type')
"""