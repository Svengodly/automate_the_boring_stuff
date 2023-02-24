from random import choice


class RandomWalk:
    """Creates a random walk."""
    def __init__(self, num_of_moves=5000):
        self.num_of_moves = num_of_moves
        # Below creates attributes for the x and y coordinates.
        self.x_points = [0]
        self.y_points = [0]

    def fill_walk(self):
        while len(self.x_points) < self.num_of_moves:
            # Populates list with given number of moves
            x_direc = choice([1, -1])
            x_step = choice([0, 1, 2, 3, 4])

            y_direc = choice([1, -1])
            y_step = choice([0, 1, 2, 3, 4])

            if x_direc * x_step and y_direc * y_step == 0:
                continue
            else:
                self.x_points.append(self.x_points[-1] + x_step * x_direc)
                self.y_points.append(self.y_points[-1] + y_step * y_direc)
