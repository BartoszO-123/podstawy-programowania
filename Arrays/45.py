import matplotlib.pyplot as plt
import numpy as np

x_degrees = np.linspace(0, 360, 100)
x_radians = np.deg2rad(x_degrees)

y_sin = np.sin(x_radians)

print("\n--- 3.27 PLOT SIN(X) ---")
print(
    "Matplotlib code to plot y = sin(x) is prepared. Requires a graphical environment to display."
)

plt.plot(x_degrees, y_sin, label="y = sin(x)", color="blue")
plt.title("Plot of y = sin(x)")
plt.xlabel("x (degrees)")
plt.ylabel("y")
plt.axhline(0, color="black", linewidth=0.5, ls="--")
plt.axvline(0, color="black", linewidth=0.5, ls="--")
plt.grid(color="gray", linestyle="--", linewidth=0.5)
plt.legend()
plt.show()
