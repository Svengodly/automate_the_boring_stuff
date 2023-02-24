import random
import os

# Program that creates 35 different quizzes on the US capitals.
# Also generates answer key for each of the quizzes.

# First we create a dictionary containing the states along with their capitals.

stateCapitals = {"Alabama": "Montgomery", "Alaska": "Juneau", "Arizona": "Phoenix", "Arkansas": "Little Rock",
                 "California": "Sacramento", "Colorado": "Denver", "Connecticut": "Hartford", "Delaware": "Dover",
                 "Florida": "Tallahassee", "Georgia": "Atlanta", "Hawaii": "Honolulu", "Idaho": "Boise",
                 "Illinois": "Springfield",
                 "Indiana": "Indianapolis", "Iowa": "Des Moines", "Kansas": "Topeka", "Kentucky": "Frankfort",
                 "Louisiana": "Baton Rogue", "Maine": "Augusta", "Maryland": "Annapolis", "Massachusetts": "Boston",
                 "Michigan": "Lansing", "Minnesota": "Saint Paul", "Mississippi": "Jackson",
                 "Missouri": "Jefferson City", "Montana": "Helena", "Nebraska": "Lincoln", "Nevada": "Carson City",
                 "New Hampshire": "Concord", "New Jersey": "Trenton", "New Mexico": "Santa Fe", "New York": "Albany",
                 "North Carolina": "Raleigh", "North Dakota": "Bismarck", "Ohio": "Columbus",
                 "Oklahoma": "Oklahoma City", "Oregon": "Salem", "Pennsylvania": "Harrisburg",
                 "Rhode Island": "Providence", "South Carolina": "Columbia", "South Dakota": "Pierre",
                 "Tennessee": "Nashville", "Texas": "Austin", "Utah": "Salt Lake City", "Vermont": "Montpelier",
                 "Virginia": "Richmond", "Washington": "Olympia", "West Virginia": "Charleston", "Wisconsin": "Madison",
                 "Wyoming": "Cheyenne"}

# Putting a dictionary within a list() returns a list of keys.
states = list(stateCapitals)

# I can now shuffle this list. This will modify the order of the states.
random.shuffle(states)

# Now I can loop to create 50 randomized questions
# I need to do this 35 times. This will create each test.

os.chdir("C:\\Users\\rmorr\\Documents\\Quiz")
for number in range(35):
    for index, state in enumerate(states):
        # Create a list of 4 answers
        answer, answers = stateCapitals[state], [stateCapitals[state]]
        capitals = list(stateCapitals.values())
        random.shuffle(capitals)
        while len(answers) < 4:
            for place in capitals:
                if place not in answers:
                    answers.append(place)
                    if len(answers) == 4:
                        break
                    else:
                        continue
        random.shuffle(answers)
        choices = zip(["a", "b", "c", "d"], answers)
        # Create quiz that is numbered.
        quiz = open(f"quiz_{number + 1}.txt", "a")
        quizAnswers = open(f"quiz_answers{number + 1}.txt", "a")
        quiz.write(f"{index + 1}) What is the capital of {state}?")
        for pair in choices:
            if pair[1] == answer:
                x = pair
            quiz.write(f"\n{pair[0]}. {pair[1]}")
        quizAnswers.write(f"{index + 1}) {x[0]}. {x[1]}\n")
        quizAnswers.close()
        quiz.write("\n\n")
        quiz.close()
