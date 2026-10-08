# Double-Pendulum Simulation

**Python · NumPy · SciPy · Matplotlib · October 2026**

A numerical simulation and animation of a double pendulum, built from equations of motion I derived by hand using Lagrangian mechanics.

![Double pendulum trajectory](trajectory.png)

## Background

A double pendulum is a pendulum with a second pendulum attached to its end. Its motion is chaotic: tiny changes in the starting angles lead to completely different paths. That makes it hard to analyze by hand but a good test of a numerical simulation.

## Approach

**1. Derivation.** I learned Lagrangian mechanics and used it to derive the system's two coupled equations of motion. With angles θ₁ and θ₂ measured from the vertical, masses m₁ and m₂, and rod lengths l₁ and l₂:

- Kinetic energy: T = ½(m₁ + m₂) l₁² θ̇₁² + ½ m₂ l₂² θ̇₂² + m₂ l₁ l₂ θ̇₁ θ̇₂ cos(θ₁ − θ₂)
- Potential energy: V = −(m₁ + m₂) g l₁ cos θ₁ − m₂ g l₂ cos θ₂
- The Lagrangian is L = T − V. Applying the Euler–Lagrange equation to each angle gives two coupled second-order differential equations.

**2. Simulation.** I rewrote the equations as a system of first-order ODEs and solved them numerically with SciPy.

**3. Animation.** Matplotlib animates the pendulum and traces the path of the bottom mass. The masses, lengths, and initial angles are adjustable, so you can see how changing them affects the motion.

## Checking accuracy

With no friction, total mechanical energy (T + V) should stay exactly constant, so any change in it comes from numerical error. I tracked total energy throughout the run. Over a 20-second test simulation, the **maximum absolute energy drift was about 10⁻⁷ J**.

![Energy drift over a 20-second run](energy_drift.png)

The slow downward trend is typical of Runge–Kutta solvers, which are not designed to conserve energy exactly. The brief spikes line up with moments of fast motion, where the solver has more difficulty keeping the error small.

## How to run

```
pip install numpy scipy matplotlib
python double_pendulum.py
```

## Note on tools

I used AI assistance to choose and learn how to use the Python libraries. The mathematical derivation and the implementation of the equations are my own work.
