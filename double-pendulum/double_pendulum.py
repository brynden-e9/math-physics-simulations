import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ---------- parameters ----------
m1, m2 = 1, 1
L1, L2 = 1, 1
g = 9.81

# ---------- equations of motion ----------
def derivatives(t, state):
    th1, th2, w1, w2 = state
    d = th1 - th2          # shorthand for theta1 - theta2

    # Your two equations in the form:
    #   A*alpha1 + B*alpha2 = C
    #   D*alpha1 + E*alpha2 = F
    A = (m1*L1**2+m2*L1**2)  # <-- FILL IN: coefficient of alpha1 in equation 1
    B = (m2*L1*L2*np.cos(th1-th2))   # <-- FILL IN: coefficient of alpha2 in equation 1
    C = (m2*L1*L2*w2*(w1-w2)*np.sin(th1-th2) - m2*L1*L2*w1*w2*np.sin(th1-th2) - m1*g*L1*np.sin(th1)-m2*g*L1*np.sin(th1))  # <-- FILL IN: everything else in equation 1, moved to RHS
    D = (m2*L1*L2*np.cos(th1-th2))   # <-- FILL IN: coefficient of alpha1 in equation 2
    E = (m2*L2**2)   # <-- FILL IN: coefficient of alpha2 in equation 2
    F = (m2*L1*L2*w1*(w1-w2)*np.sin(th1-th2) - m2*g*L2*np.sin(th2) + m2*L1*L2*w1*w2*np.sin(th1-th2))  # <-- FILL IN: everything else in equation 2, moved to RHS

    M = np.array([[A, B], [D, E]])
    rhs = np.array([C, F])
    alpha1, alpha2 = np.linalg.solve(M, rhs)

    return [w1, w2, alpha1, alpha2]

# ---------- initial conditions ----------
state0 = [np.pi/2, np.pi/2, 0.0, 0.0]   # th1, th2, w1, w2
t_end = 20.0
t_eval = np.linspace(0, t_end, 2000)

sol = solve_ivp(derivatives, (0, t_end), state0,
                t_eval=t_eval, rtol=1e-10, atol=1e-10)

th1, th2, w1, w2 = sol.y

# ---------- energy check ----------
T = (0.5*m1*L1**2*w1**2
     + 0.5*m2*(L1**2*w1**2 + L2**2*w2**2
               + 2*L1*L2*w1*w2*np.cos(th1 - th2)))
V = -(m1 + m2)*g*L1*np.cos(th1) - m2*g*L2*np.cos(th2)
E = T + V

print(f"initial energy: {E[0]:.10f}")
print(f"max drift:      {np.max(np.abs(E - E[0])):.3e}")
print(f"relative drift: {np.max(np.abs(E - E[0]))/abs(E[0]):.3e}")

plt.figure()
plt.plot(sol.t, E - E[0])
plt.xlabel("time (s)")
plt.ylabel("energy drift")
plt.title("Energy drift (should be ~flat)")
plt.show()

# ---------- animation ----------
x1 = L1*np.sin(th1)
y1 = -L1*np.cos(th1)
x2 = x1 + L2*np.sin(th2)
y2 = y1 - L2*np.cos(th2)

fig, ax = plt.subplots()
R = L1 + L2 + 0.2
ax.set_xlim(-R, R)
ax.set_ylim(-R, R)
ax.set_aspect("equal")
ax.grid(alpha=0.3)

line, = ax.plot([], [], "o-", lw=2, markersize=8)
trace, = ax.plot([], [], "-", lw=0.8, alpha=0.5)
time_text = ax.text(0.03, 0.95, "", transform=ax.transAxes)

trail_x, trail_y = [], []

def update(i):
    line.set_data([0, x1[i], x2[i]], [0, y1[i], y2[i]])
    trail_x.append(x2[i])
    trail_y.append(y2[i])
    trace.set_data(trail_x[-400:], trail_y[-400:])
    time_text.set_text(f"t = {sol.t[i]:.2f} s")
    return line, trace, time_text

ani = animation.FuncAnimation(fig, update, frames=len(sol.t),
                              interval=10, blit=True)
plt.show()