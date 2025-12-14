import matplotlib.pyplot as plt

x = []
y = []

for n in range(-10, 11):
    x.append(n)

for n in x:
    y.append(n**2 - 3)

print("\n--- 3.26 PLOT QUADRATIC FUNCTION ---")
print(
    "Matplotlib code to plot f(x)=x^2-3 is prepared. Requires a graphical environment to display."
)

plt.plot(x, y, marker="o")
plt.title("Graph of the function $f(x) = x^2 - 3$")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)

plt.show()
