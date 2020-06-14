import numpy as np
from scipy.special import comb, logsumexp
from matplotlib import pyplot as plt
import argparse
import os
import ast


def bernstein_poly(i, n, t):
    """
     The Bernstein polynomial of n, i as a function of t
    """

    return comb(n, i) * ( t**(n-i) ) * (1 - t)**i


def bezier_curve(points, f_output):
    """
       Given a set of control points, return the
       bezier curve defined by the control points.

       points should be a list of lists, or list of tuples
       such as [ [1,1], 
                 [2,3], 
                 [4,5], ..[Xn, Yn] ]
    """

    nPoints = len(points)
    xPoints = np.array([p[0] for p in points])
    yPoints = np.array([p[1] for p in points])

    t = np.linspace(0.0, 1.0, 1000)

    polynomial_array = np.array([ bernstein_poly(i, nPoints-1, t) for i in range(0, nPoints)   ])

    xvals = np.dot(xPoints, polynomial_array)
    yvals = np.dot(yPoints, polynomial_array)
    
    nPoints = len(points)
    xpoints = [p[0] for p in points]
    ypoints = [p[1] for p in points]

    plt.plot(xvals, yvals)
    plt.plot(xpoints, ypoints, "ro")
    for nr in range(len(points)):
        plt.text(points[nr][0], points[nr][1], nr)
    plt.savefig(f_output)
   
    return xvals, yvals


def getArgParser():
    parser = argparse.ArgumentParser(description = 'Command line arguments for cisExpress')
    parser.add_argument('-p', '--points', dest = 'points', required = True, type = str)
    parser.add_argument('-o', '--output', dest = 'output_name', default = None, type = str)
    return parser
    
    
def main():
    parser = getArgParser()
    args = parser.parse_args()
    output_name = args.output_name
    points = args.points
    points = ast.literal_eval(points)
    bezier_curve(points, f_output = output_name)
    
    
if __name__ == "__main__":
    main()
    
    
    