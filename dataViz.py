import matplotlib.pyplot as plt
from Random import RandomWalk

# input_values = range(1, 350)
# squares = [number**2 for number in input_values]
myWalk = RandomWalk()
myWalk.fill_walk()

plt.style.use('bmh')
fig, ax = plt.subplots()
# ax.plot(input_values, squares, linewidth=3)
ax.plot(myWalk.x_points, myWalk.y_points, linewidth=2)

ax.set_title("Squares", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.set_xlabel("Value", fontsize=14)
ax.scatter(0, 0, c='Green', s=200)
ax.scatter(myWalk.x_points[-1], myWalk.y_points[-1], c='Red', s=200)
ax.tick_params(axis="both", which="major", labelsize=14)
plt.show()
