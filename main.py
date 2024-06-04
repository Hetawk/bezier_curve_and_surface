from bezier_curve import BezierCurve
from bezier_surface import BezierSurface

def main():
    # Example usage for Bezier Curve
    control_points_curve = [(0, 0), (1, 2), (3, 3), (4, 0)]
    bezier_curve = BezierCurve(control_points_curve)
    bezier_curve.plot(save_path='bezier_curve.png')

    # Example usage for Bezier Surface
    control_points_surface = [
        [(0, 0, 0), (1, 0, 1), (2, 0, 0)],
        [(0, 1, 1), (1, 1, 2), (2, 1, 1)],
        [(0, 2, 0), (1, 2, 1), (2, 2, 0)]
    ]
    bezier_surface = BezierSurface(control_points_surface)
    bezier_surface.plot(save_path='bezier_surface.png')

if __name__ == "__main__":
    main()
