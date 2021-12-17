# Generate instances of stable marriage at random

import random


def Generate(args=1):
    # check whether the input number <= 1
    if args <= 1:
        print("input must be no less than 2")
        num = random.randint(2, 10)
    elif args > 9:
        num = random.randint(2, 10)
    else:
        num = args

    personList = []  # personList is an ordered list
    womenList = []
    menList = []

    for i in range(1, num + 1):
        personList.append(i)

    # shuffle personList then generate random men/women's preference list
    womenList = [random.sample(personList, num) for _ in range(num)]
    menList = [random.sample(personList, num) for _ in range(num)]

    return menList, womenList