import random

num_units = 0

random_problems = []

problems_per_unit = []

def get_numbers():
    global num_units
    global problems_per_unit

    num_units = int(input("Enter # of units (e.g homeworks, sections): "))
    print("You are revising ", num_units, " units.")

    problems_per_unit = [0] * num_units

    for i in range(num_units):
        problems_per_unit[i] = int(input(f"How many problems for homework {i  + 1}?: "))

    print("-----Summary-------")
    for i in range(num_units):
        print(f"Homework {i+1}: {problems_per_unit[i]} problems")
    

def generate_random_problems(amount):
    for i in range(amount):
        random_hw = random.randint(0,num_units - 1) # first pick a random hw
        #then go to that index in problems_per_unit, and pick a random int within that range

        random_problem = random.randint(1, problems_per_unit[random_hw])

        random_problems.append(f"Homework #{random_hw + 1} - Problem #{random_problem}")
    

    for problem in random_problems:
        print(problem)


get_numbers()
amount = int(input("How many random problems would you like to review? : "))
generate_random_problems(amount)

