#!/usr/bin/env python3

# Created by: Matsuru Hoshi
# Created on: Nov 2019
# This is program number rounder

import random


def round(numbers, round_position):
    # This'll round the number given by the position given

    numbers[0] = rounded


def main():
    # This is getting user number and running round()

    # This is a list holding the number to be rounded
    numbers = []

    # process
    number = float(input("What is the number: "))
    round_position = int(input("What is the round position: "))
    numbers.append(number)
    round(numbers, round_position)

    # output
    print("\nThe answer is " + str(numbers[0]))


if __name__ == "__main__":
    main()
