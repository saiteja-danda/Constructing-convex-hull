import sys
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from random_geometry_points.circle2d import Circle2D

def RightTurn(point1, point2, point3):
    if (point3[1]-point1[1])*(point2[0]-point1[0]) >= (point2[1]-point1[1])*(point3[0]-point1[0]):
        return False
    return True

def GrahamScan(P):
    P.sort()            # Sort the set of points
    P = np.array(P)            # Convert the list to numpy array
    plt.figure(figsize=(9,7))            # Create a new fig
    upper = [P[0], P[1]]
    # Compute the upper part of the hull
    for i in range(2,len(P)):
        upper.append(P[i])
        while len(upper) > 2 and not RightTurn(upper[-1],upper[-2],upper[-3]):
            del upper[-2]
        L = np.array(upper)
        plt.clf()        # Clear plt.fig
        plt.plot(L[:,0],L[:,1], 'r-', picker=5)    
        plt.plot(P[:,0],P[:,1],'o',color='black')
        plt.axis('off')        
        plt.show(block=False)
        plt.pause(0.0000001)
    lower = [P[-1], P[-2]]    # Initialize the lower part
    # Compute the lower part of the hull
    for i in range(len(P)-3,-1,-1):
        lower.append(P[i])
        while len(lower) > 2 and not RightTurn(lower[-1],lower[-2],lower[-3]):
            del lower[-2]
        H = np.array(upper + lower)
        plt.clf()               # Clear plt.fig
        plt.plot(H[:,0],H[:,1], 'r-', picker=5)
        plt.plot(P[:,0],P[:,1],'o',color='black')
        plt.axis('off')
        plt.show(block=False)
        plt.pause(0.0000001)
    del lower[0]
    del lower[-1]
    L = upper + lower         # Build the full hull
    plt.axis('off')
    plt.title('Convex Hull by Graham Scan')
    plt.ylim([-1.5,1.5])
    plt.xlim([-1.5,1.5])
    plt.show()
    return np.array(L)
def rand_points(n):
    P = [(np.random.randint(-100,100),np.random.randint(-100,100)) for i in range(n)]
    return P

def Linear(n):
    def y(x, m, b):
        return m*x + b
    X = np.array(np.linspace(1,6, n))
    P=np.array((X,np.zeros(n)))
    P=(P.transpose()).astype(int)
    P=list(tuple(map(tuple, P)))
    return P

def Circular(n):
    tu=Circle2D(100,100,50)
    Pt=tu.create_random_points(n)
    return Pt
    
def generate_points(ch,N):
    switcher={
            1: rand_points(N),
            2: Linear(N),
            3: Circular(N)}
    return switcher.get(ch, "Wrong choice")

def main():
    try:
        N = int(sys.argv[1])
    except:
        N = int(input("Enter number of points: "))
    if N>2:
        start=datetime.now()
        try:
            choice = int(sys.argv[2])
        except:
            choice = int(input("1. Random Points\n 2. Linear Points\n 3. Circular Points\n Enter your choice:  "))
        Point_set=generate_points(choice,N)
        GrahamScan(Point_set)
        run_time=datetime.now()-start
        print('         Run time:',run_time)
    else:
        print('Points should be greater than 2 to construct a convex hull')

if __name__ == '__main__':
  main()