import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Time axis
t = np.linspace(0, 2*np.pi, 1000)

# Initial parameters
A = 1.0   # amplitude
w = 4.0   # initial angular frequency
phi = 0   # phase

# Initial wave
y = A * np.sin(w * t + phi)

# Create plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
line, = plt.plot(t, y, lw=2)
ax.set_title("Sine Wave with Adjustable Angular Frequency")
ax.set_xlabel("Time")
ax.set_ylabel("Amplitude")

# Frequency slider
ax_w = plt.axes([0.25, 0.1, 0.65, 0.03])
w_slider = Slider(ax_w, 'ω (rad/s)', 0.1, 10.0, valinit=w)

# Update function
def update(val):
    w_new = w_slider.val
    line.set_ydata(A * np.sin(w_new * t + phi))
    fig.canvas.draw_idle()

w_slider.on_changed(update)

plt.show()
