import matplotlib.pyplot as plt

x = []
y = []

for n in range(-10, 11):
    x.append(n)

for n in x:
    y_value = n**2 - 3
    y.append(y_value)

plt.figure(figsize=(8, 6))
plt.plot(x, y, marker="o", linestyle="-", color="red", label="$f(x) = x^2 - 3$")

plt.title("Graph of the function $f(x) = x^2 - 3$")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.legend()

plt.show()
