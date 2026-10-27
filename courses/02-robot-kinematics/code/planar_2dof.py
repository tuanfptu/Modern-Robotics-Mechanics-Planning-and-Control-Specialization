"""Original planar 2R example: metres, radians, counterclockwise joint angles."""

import argparse
from pathlib import Path

import numpy as np


def joint_positions(lengths, angles):
    """Return base, elbow and tip as a (3, 2) array.

    Angles are relative joint rotations; the base is at (0, 0).
    Both inputs must contain exactly two finite values; lengths must be positive.
    """
    lengths = np.asarray(lengths, dtype=float)
    angles = np.asarray(angles, dtype=float)
    if lengths.shape != (2,) or angles.shape != (2,):
        raise ValueError("lengths and angles must each have shape (2,)")
    if not np.all(np.isfinite(lengths)) or not np.all(lengths > 0):
        raise ValueError("lengths must be finite and positive")
    if not np.all(np.isfinite(angles)):
        raise ValueError("angles must be finite")
    headings = np.cumsum(angles)
    steps = lengths[:, None] * np.column_stack((np.cos(headings), np.sin(headings)))
    return np.vstack((np.zeros(2), np.cumsum(steps, axis=0)))


def forward_kinematics(lengths, angles):
    """Return the end-effector position (x, y), in metres."""
    return joint_positions(lengths, angles)[-1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--save", type=Path, help="Save a plot, e.g. outputs/robot.png")
    parser.add_argument("--show", action="store_true", help="Open an interactive plot")
    args = parser.parse_args()
    lengths = (1.0, 1.0)
    points = joint_positions(lengths, (np.pi / 4, np.pi / 2))
    print(f"End effector (m): x={points[-1, 0]:.6f}, y={points[-1, 1]:.6f}")
    if args.save or args.show:
        import matplotlib

        if not args.show:
            matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots()
        ax.plot(points[:, 0], points[:, 1], "o-", linewidth=3)
        reach = sum(lengths) * 1.1
        ax.set(xlim=(-reach, reach), ylim=(-reach, reach),
               xlabel="x (m)", ylabel="y (m)", title="Planar 2-DOF robot (2R)")
        ax.set_aspect("equal")
        ax.grid(True)
        if args.save:
            args.save.parent.mkdir(parents=True, exist_ok=True)
            fig.savefig(args.save, dpi=150, bbox_inches="tight")
        if args.show:
            plt.show()
        plt.close(fig)


if __name__ == "__main__":
    main()
