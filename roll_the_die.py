from die import Die

from plotly.graph_objs import Bar, Layout
from plotly import offline

# Create two 6 sided die.
die1 = Die()
die2 = Die()

sideprod = die1.num_sides + die2.num_sides

# Need to roll the pair of die 1000 times and store the results.
# outcome = []

# for number in range(5000):
#     outcome.append(die1.roll() * die2.roll())
outcome = [die1.roll() + die2.roll() for number in range(5000)]
# Now that we have list containing the outcome of each roll, we need to get the frequency of each value in the
# Outcome list.
# frequency = []

# for number in range(2, sideprod + 1):
#     frequency.append(outcome.count(number))
frequency = [outcome.count(number) for number in range(2, sideprod + 1)]

# Now we need to graph the results.
# First, the x values which are the possible outcomes of rolling the die. These values will represent each bar in
# The histogram
x_values = list(range(2, sideprod + 1))

# The y values, which represent the occurrence of each outcome are passed to the Bar class.
data = [Bar(x=x_values, y=frequency)]

# Now we are going to create settings for the layout of the histogram
x_axis_config = {"title": "Result", "dtick": 1}
y_axis_config = {"title": "Frequency of Result"}
my_layout = Layout(title="Results of rolling two D6s 5000 times", xaxis=x_axis_config, yaxis=y_axis_config)

# Finally, we plot the graph
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')
