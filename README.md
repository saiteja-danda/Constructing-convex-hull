# Constructing-convex-hull
This is written in python.

Whta is convex hull?
In geometry, the convex hull or convex envelope or convex closure of a shape is the smallest convex set that contains it. The convex hull may be defined either as the intersection of all convex sets containing a given subset of a Euclidean space, or equivalently as the set of all convex combinations of points in the subset. For a bounded subset of the plane, the convex hull may be visualized as the shape enclosed by a rubber band stretched around the subset - Wikipedia

Algorithms to construct convex hull are given below.
Jarvis March algorithm is considered as simple linear algorithm for constructing a convex hull. It selects one point which is on the convex hull with the smallest x-coordinate. Then it wraps point set from starting point, always find the next vertex of convex hull as the one which is rightmost with respect to the direction given by the previous two
vertices.

Graham scan algorithm was invented to imrpove the complexity of construction hull problem.
Source to this algorithm is here: Preparata, Shamos, Computational Geometry, Chapter
”Convex Hulls: Basic Algorithms”.

Working of code.
You need to input number points to construct convex hull and then select shape from the options given to see the convex hull.
