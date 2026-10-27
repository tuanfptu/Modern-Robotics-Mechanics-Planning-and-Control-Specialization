"""Check independent geometric configurations and invalid model inputs."""
import importlib.util
from pathlib import Path

import numpy as np
import pytest

SOURCE = (Path(__file__).resolve().parents[1] / "courses" /
          "02-robot-kinematics" / "code" / "planar_2dof.py")
SPEC = importlib.util.spec_from_file_location("planar_2dof", SOURCE)
robot = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(robot)


@pytest.mark.parametrize("angles, expected", [
    ((0, 0), (3, 0)),
    ((np.pi / 2, 0), (0, 3)),
    ((0, np.pi), (1, 0)),
    ((np.pi / 2, -np.pi / 2), (1, 2)),
])
def test_known_configurations(angles, expected):
    np.testing.assert_allclose(robot.forward_kinematics((2, 1), angles), expected, atol=1e-12)


def test_demo_and_link_lengths():
    points = robot.joint_positions((1, 1), (np.pi / 4, np.pi / 2))
    np.testing.assert_allclose(points[-1], (0, np.sqrt(2)), atol=1e-12)
    np.testing.assert_allclose(np.linalg.norm(np.diff(points, axis=0), axis=1), (1, 1))
    np.testing.assert_array_equal(points[0], (0, 0))


@pytest.mark.parametrize("lengths, angles", [
    ((0, 1), (0, 0)), ((-1, 1), (0, 0)),
    ((np.inf, 1), (0, 0)), ((1, 1), (np.nan, 0)),
    ((1,), (0, 0)), ((1, 1), (0,)),
])
def test_invalid_inputs(lengths, angles):
    with pytest.raises(ValueError):
        robot.forward_kinematics(lengths, angles)
