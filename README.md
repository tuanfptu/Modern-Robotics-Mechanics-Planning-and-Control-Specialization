# Modern Robotics: Mechanics, Planning, and Control

A personal learning journal by Tuan Ha and a free study resource accompanying Northwestern University's six-course **Modern Robotics** specialization on Coursera. This repository brings together study notes, original practice problems, Python implementations, and simulation experiments.

**Current status:** the six-course scaffold, lesson templates, and a tested planar 2-DOF forward kinematics example are available. Course notes have not been written, and no course is marked complete.

## Learning Objectives

- Understand configuration space, rigid-body motion, and reference frames.
- Implement and verify kinematics, dynamics, motion planning, and control algorithms.
- Connect mathematical models to simulations with explicit assumptions and limitations.
- Develop precise technical explanations supported by reproducible experiments.

## Prerequisites

Basic linear algebra, calculus, mechanics, and Python. The core uses **Python 3.10+**, NumPy, Matplotlib, Jupyter, and pytest. Robot hardware and ROS are optional.

## Course Roadmap

| Course | Course overview | Textbook chapters | Learning status |
| --- | --- | --- | --- |
| 1 | [Foundations of Robot Motion](courses/01-foundations-of-robot-motion/README.md) | 2, 3 | Not started |
| 2 | [Robot Kinematics](courses/02-robot-kinematics/README.md) | 4, 5, 6, 7 | Not started |
| 3 | [Robot Dynamics](courses/03-robot-dynamics/README.md) | 8, 9 | Not started |
| 4 | [Robot Motion Planning and Control](courses/04-robot-motion-planning-and-control/README.md) | 10, 11 | Not started |
| 5 | [Robot Manipulation and Wheeled Mobile Robots](courses/05-robot-manipulation-and-wheeled-mobile-robots/README.md) | 12, 13 | Not started |
| 6 | [Capstone Project, Mobile Manipulation](courses/06-capstone-mobile-manipulation/README.md) | Integration | Not started |

Follow the courses in order. Chapter numbers refer to the Modern Robotics textbook; consult Coursera for the current course schedule and requirements.

## Learning Progress

- [ ] Course 1: Foundations of Robot Motion
- [ ] Course 2: Robot Kinematics
- [ ] Course 3: Robot Dynamics
- [ ] Course 4: Robot Motion Planning and Control
- [ ] Course 5: Robot Manipulation and Wheeled Mobile Robots
- [ ] Course 6: Capstone Project, Mobile Manipulation

Mark an item only after completing the corresponding learning activities. Templates and starter examples do not count as course completion.

## Installation — Ubuntu 22.04

```bash
sudo apt update
sudo apt install -y git python3 python3-venv python3-pip
git clone https://github.com/tuanfptu/Modern-Robotics-Mechanics-Planning-and-Control-Specialization.git
cd Modern-Robotics-Mechanics-Planning-and-Control-Specialization
python3 --version  # Python >= 3.10
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

For an existing local checkout, start with the virtual environment steps. Dependencies use bounded version ranges rather than an exact lockfile.

## Run the Example and Tests

From the repository root, with `.venv` activated:

```bash
python courses/02-robot-kinematics/code/planar_2dof.py
python courses/02-robot-kinematics/code/planar_2dof.py --save outputs/planar_2dof.png
python -m pytest -q
jupyter notebook
```

The first command prints the end-effector position. `--save` writes a plot without requiring a display; `--show` opens an interactive plot on a desktop. In Jupyter, start with a notebook template under `courses/01-foundations-of-robot-motion/notebooks/`.

### Planar 2R Robot — Forward Kinematics

The example models two revolute joints and two rigid links. Link lengths $l_1,l_2>0$ are in metres; joint angles $\theta_1,\theta_2$ are in radians, positive counterclockwise. The base frame is at joint 1, with $x$ pointing right and $y$ pointing up. Angle $\theta_1$ is measured from the base-frame $x$ axis; $\theta_2$ is measured relative to link 1.

The end-effector position, expressed in the base frame, is:

$$
x = l_1\cos\theta_1 + l_2\cos(\theta_1+\theta_2),\qquad
y = l_1\sin\theta_1 + l_2\sin(\theta_1+\theta_2).
$$

For $l_1=l_2=1$, $\theta_1=\pi/4$, and $\theta_2=\pi/2$, the expected position is approximately $(0, 1.414214)$ m. This is an original standalone example, not a graded assignment solution.

## Repository Structure

Each course contains:

| Directory | Purpose |
| --- | --- |
| `notes/` | Lesson templates, mathematical notation, and future study notes |
| `code/` | Original, tested Python implementations |
| `notebooks/` | Visualization and simulation experiments |
| `exercises/` | Original practice problems and self-assessment |
| `README.md` | Course overview, chapter navigation, and progress |

## Start with Course 1

1. Open the [Course 1 overview](courses/01-foundations-of-robot-motion/README.md).
2. Study the official material, then fill in the [Chapter 2 template](courses/01-foundations-of-robot-motion/notes/chapter-02.md) in your own words.
3. Define notation, units, and reference frames; record questions and evidence of understanding.
4. Create experiments when useful. Publish only code that has been run and tested, and report actual results.

## Writing and Study Conventions

Use English for technical terms, headings, code, and concise technical summaries. Use Vietnamese explanations where they make intuition or a derivation easier to follow. Avoid repeating every sentence in both languages.

Build each lesson around **intuition → definitions → assumptions → derivation → worked example → verification and limitations**. Define abbreviations on first use, cite specific sources, and distinguish established results from personal observations. See the [writing guide](docs/writing-guide.md) and [terminology reference](docs/terminology.md).

## Optional ROS 2 Integration

[ROS 2 Humble](optional/ros2/README.md) is a separate future extension. No ROS packages or nodes are implemented yet, and the core does not depend on ROS.

## Official Resources

- [Coursera specialization](https://www.coursera.org/specializations/modernrobotics)
- [Modern Robotics — textbook and software](https://modernrobotics.org/), Kevin M. Lynch and Frank C. Park, Cambridge University Press, 2017
- [Northwestern video supplements](https://modernrobotics.northwestern.edu/)
- [Official Modern Robotics library](https://github.com/NxRLab/ModernRobotics), referenced but not required by the core

## Independence and License

This is an **independent educational project**, not affiliated with or endorsed by Northwestern University or Coursera. It does not reproduce course videos, slides, textbook copies, quizzes, or graded assignment solutions. Access third-party materials through their official sources.

Original code and documentation are released under the [MIT License](LICENSE). Linked third-party materials remain subject to their owners' terms.
