import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
plt.plot(squares, linewidth=5)

# Set chart title and label axis
plt.title("Square Numbers", fontsize=24)
plt.xlabel("value", fontsize=18)
plt.ylabel("Square of x", fontsize=18)

# Set size of tick labels
plt.tick_params(axis='both', labelsize=14)

plt.show()
