import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb


class BezierCurve:
    def __init__(self, control_points):
        """
        Initialize the BezierCurve with control points.

        :param control_points: List of tuples representing control points (x, y).
        """
        self.control_points = np.array(control_points)

    def bernstein_poly(self, i, n, t):
        """
        Compute the Bernstein polynomial of n, i as a function of t.

        :param i: Index of the Bernstein polynomial.
        :param n: Degree of the polynomial.
        :param t: Parameter t, where 0 <= t <= 1.
        :return: Value of the Bernstein polynomial at t.
        """
        return comb(n, i) * (t ** i) * ((1 - t) ** (n - i))

    def curve(self, num_points=100):
        """
        Compute the Bezier curve.

        :param num_points: Number of points to compute on the curve.
        :return: Array of points representing the Bezier curve.
        """
        n = len(self.control_points) - 1
        t_values = np.linspace(0, 1, num_points)
        curve_points = np.zeros((num_points, 2))

        for t_index, t in enumerate(t_values):
            point = np.zeros(2)
            for i in range(n + 1):
                bernstein = self.bernstein_poly(i, n, t)
                point += bernstein * self.control_points[i]
            curve_points[t_index] = point

        return curve_points

    def plot(self, num_points=100, save_path=None):
        """
        Plot the Bezier curve.

        :param num_points: Number of points to compute on the curve.
        :param save_path: File path to save the plot.
        """
        curve_points = self.curve(num_points)
        plt.plot(curve_points[:, 0], curve_points[:, 1], label="Bezier Curve")
        plt.scatter(self.control_points[:, 0], self.control_points[:, 1], color='red', label="Control Points")
        plt.plot(self.control_points[:, 0], self.control_points[:, 1], 'r--')
        plt.legend()
        if save_path:
            plt.savefig(save_path)
        else:
            plt.show()
