import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb


class BezierSurface:
    def __init__(self, control_points):
        """
        Initialize the BezierSurface with control points.

        :param control_points: 2D array of control points.
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

    def surface(self, num_points=20):
        """
        Compute the Bezier surface.

        :param num_points: Number of points to compute on each parameter.
        :return: Array of points representing the Bezier surface.
        """
        m, n, _ = self.control_points.shape
        m -= 1
        n -= 1
        u_values = np.linspace(0, 1, num_points)
        v_values = np.linspace(0, 1, num_points)

        surface_points = np.zeros((num_points, num_points, 3))

        for u_index, u in enumerate(u_values):
            for v_index, v in enumerate(v_values):
                point = np.zeros(3)
                for i in range(m + 1):
                    for j in range(n + 1):
                        bernstein_u = self.bernstein_poly(i, m, u)
                        bernstein_v = self.bernstein_poly(j, n, v)
                        point += bernstein_u * bernstein_v * self.control_points[i, j]
                surface_points[u_index, v_index] = point

        return surface_points

    def plot(self, num_points=20, save_path=None, title="Bezier Surface"):
        """
        Plot the Bezier surface.

        :param num_points: Number of points to compute on each parameter.
        :param save_path: File path to save the plot.
        :param title: Title of the plot.
        """
        surface_points = self.surface(num_points)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        X = surface_points[:, :, 0]
        Y = surface_points[:, :, 1]
        Z = surface_points[:, :, 2]

        ax.plot_surface(X, Y, Z, color='b', label='Bezier Surface')

        control_x = self.control_points[:, :, 0]
        control_y = self.control_points[:, :, 1]
        control_z = self.control_points[:, :, 2]

        ax.scatter(control_x, control_y, control_z, color='r', label='Control Points')

        # Add title and legend
        ax.set_title(title)
        ax.legend()

        if save_path:
            plt.savefig(save_path)
        else:
            plt.show()

