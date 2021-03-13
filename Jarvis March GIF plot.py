import sys
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from random_geometry_points.circle2d import Circle2D

#check for orientation
def Check_orientation(p1, p2, p3):
    if (p3[1]-p1[1])*(p2[0]-p1[0]) >= (p2[1]-p1[1])*(p3[0]-p1[0]):
    #if (p2[0]-p1[0]) <= (p3[0]-p1[0]):
        return True
    return False

# Main function:
def JarvisMarch(S):
    plt.figure()
    index = 0
    n = len(S)
    P = [None] * n
    l = np.where(S[:,0] == np.min(S[:,0]))
    #l = np.where(S[:,1] == np.min(S[:,1]))
    Point_on_hull = S[l[0][0]]
    i = 0
    while True:
        P[i] = Point_on_hull
        lastpoint = S[0]
        for j in range(1,n):
            if (lastpoint[0] == Point_on_hull[0] and lastpoint[1] == Point_on_hull[1]) or not Check_orientation(S[j],P[i],lastpoint):
                lastpoint = S[j]
        i = i + 1
        Point_on_hull = lastpoint
        J = np.array([P[k] for k in range(n) if P[k] is not None])
        plt.clf()
        plt.plot(J[:,0],J[:,1], 'r-', picker=5)
        plt.plot(S[:,0],S[:,1],'o',color='black')              
        plt.axis('off')
        plt.show(block=False)
        plt.pause(0.0000001)    # pause
        index += 1
        if lastpoint[0] == P[0][0] and lastpoint[1] == P[0][1]:
            break
    for i in range(n):
        if P[-1] is None:
            del P[-1]
    P = np.array(P)
    
    # Plot final hull
    plt.clf()
    plt.plot(P[:,0],P[:,1], 'r-', picker=5)
    plt.plot([P[-1,0],P[0,0]],[P[-1,1],P[0,1]], 'r-', picker=5)
    plt.plot(S[:,0],S[:,1],'o',color='black')
    plt.axis('off')
    plt.show(block=False)
    plt.pause(0.0000001)
    return P

def rand_points(n):
    P = [(np.random.randint(-100,100),np.random.randint(-100,100)) for i in range(n)]
    return P

def Linear(n):
    def y(x, m, b):
        return m*x + b
    X = np.array(np.linspace(1,6, n))
    P=np.array((X,np.zeros(n)))
    P=P.transpose()
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
    start=datetime.now()
    try:
        N = int(sys.argv[1])
    except:
        N = int(input("Enter number of points: "))
    if N>2:
        try:
            choice = int(sys.argv[2])
        except:
            choice = int(input("1. Random Points\n 2. Linear Points\n 3. Circular Points\n Enter your choice: "))
        Point_set=generate_points(choice,N)
        P = np.array(Point_set)
        H = JarvisMarch(P)
        plt.figure(figsize=(5,5))
        plt.plot(H[:,0],H[:,1], 'r-', picker=5)
        plt.plot([H[-1,0],H[0,0]],[H[-1,1],H[0,1]], 'r-', picker=5)
        plt.plot(P[:,0],P[:,1],'o',color='black')
        plt.axis('off')
        plt.title('Convex Hull by Jarvis March')
        plt.show()
        run_time=datetime.now()-start
        print('         Run time:',run_time)
    else:
        print('Points should be greater than 2 to construct a convex hull')

if __name__ == '__main__':
    main()