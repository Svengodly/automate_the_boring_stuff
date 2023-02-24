import matplotlib.pyplot as plt

fig, ax = plt.subplots()

values = range(1, 11)

cubes = [number**3 for number in values]

ax.plot(values, cubes)
ax.scatter(values, cubes)
ax.set_title("Cubes")
ax.set_xlabel("Value to Cube")
ax.set_ylabel("Cubed Value")
ax.tick_params(axis="both", labelsize=10)

plt.show()
