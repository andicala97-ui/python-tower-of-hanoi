
# Python Tower of Hanoi Solver

## Overview
This project implements the classic Tower of Hanoi puzzle using Python and recursion.

The program solves the puzzle by moving disks between three rods while following the rules of the game. It also records and displays the state of all three rods after every movement.

## Features
- Recursive algorithm to solve the Tower of Hanoi puzzle.
- Supports different numbers of disks.
- Simulates disk movements between three rods.
- Records the state of the rods after each move.
- Calculates the minimum number of moves required.

## Technologies
- Python 3
- Recursion
- Lists
- Nested Functions
- String Manipulation

## How It Works

The solver uses a recursive approach:

1. Move the smaller disks from the source rod to the auxiliary rod.
2. Move the largest remaining disk to the target rod.
3. Move the smaller disks from the auxiliary rod to the target rod.

The process continues until all disks are successfully transferred to the target rod.

## Example Usage

```python
from hanoi_solver import hanoi_solver

print(hanoi_solver(2))
```

### Expected Output

```text
[2, 1] [] []
[2] [] [1]
[] [2] [1]
[] [2, 1] []
```

## Minimum Number of Moves

The minimum number of moves required to solve the puzzle is calculated using:

`2^n - 1`

Where `n` represents the number of disks.

| Disks | Minimum Moves |
|---|---:|
| 1 | 1 |
| 2 | 3 |
| 3 | 7 |
| 4 | 15 |
| 5 | 31 |

## How to Run

1. Clone or download this repository.
2. Open the project folder.
3. Run the Python file:

```bash
python hanoi_solver.py
```

## Learning Objectives

This project was developed to practice:
- Recursive problem-solving.
- Base cases and recursive calls.
- Python lists and list methods.
- Nested functions.
- Algorithmic thinking.

## Acknowledgment

Developed as part of my Python learning journey through the freeCodeCamp curriculum.

---

**Language:** Python 3

