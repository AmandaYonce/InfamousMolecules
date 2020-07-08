#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Infamous Molecules"""

__author__ = "Amanda Yonce"

import itertools


def get_file_contents(file_name):
    """
    A function that will read an input file and
    convert the lines in a list to tuples of 4 lines
    """
    data_list = []
    with open(file_name, "r") as f:
        contents = f.readlines()
    start = 0
    end = 4
    for i, each in enumerate(contents):
        contents[i] = each.strip('\n')
    while end < len(contents):
        short_list = list(contents[start:end])
        data_list.append(short_list)
        start += 4
        end += 4
    # print(data_list)
    return data_list


def possible_permutations():
    """
    a function that creates all of the possible
    permutations of numbers 0-3
    """
    poss_permutations = []
    for p in itertools.permutations(range(4), 4):
        poss_permutations.append(p)
    for i, perm in enumerate(poss_permutations):
        poss_permutations[i] = list(perm)
    return poss_permutations


def intersection_points(x, y):
    """
    this function takes in two strings and returns a list
    of tuples of all possible intersection points
    """
    intersection_points = []
    first_word_list = list(x)
    second_word_list = list(y)
    for f, letter in enumerate(first_word_list):
        for s, s_letter in enumerate(second_word_list):
            if letter == s_letter and f != 11 and f != 0\
               and s != 11 and s != 0:
                int_list = [f, s]
                intersection_points.append(int_list)
    if len(intersection_points) > 0:
        intersection_points.sort(key=lambda tup: (tup[0]*tup[1]))
        # print(intersection_points)
        return intersection_points
    else:
        return "None"


def super_molecule(chains, permutates):
    """
    A function that will check groups of 4 chains
    for their largest inner area and return a list
    """
    poss_area = []
    for poss_perm in permutates:
        chain = [chains[poss_perm[0]], chains[poss_perm[1]],
                 chains[poss_perm[2]], chains[poss_perm[3]]]
        top_left = intersection_points(chain[0], chain[2])
        top_right = intersection_points(chain[1], chain[2])
        bottom_left = intersection_points(chain[0], chain[3])
        bottom_right = intersection_points(chain[1], chain[3])
        if top_left != "None" and top_right != "None" and bottom_left !=\
           "None" and bottom_right != "None":
            intersect_perms = [[a, b, c, d] for a in top_left
                               for b in top_right
                               for c in bottom_left
                               for d in bottom_right]
            for perm in intersect_perms:
                vert = perm[2][0]-perm[0][0]
                horz = perm[1][1]-perm[0][1]
                if perm[3][1]-perm[2][1] == horz and\
                   perm[3][0]-perm[1][0] == vert and\
                   vert > 0 and horz > 0:
                    area = (horz-1)*(vert-1)
                    if area > 0:
                        poss_area.append(area)
    poss_area.sort()
    # print(poss_area)
    if len(poss_area) > 0:
        return poss_area[-1]
    else:
        return 0


def main():
    """
    A program that will check for the largest molecule fuel
    """
    file_name = input(
        'Please input a file name: '
    )
    output = []
    permutates = possible_permutations()
    chains = get_file_contents(file_name)
    for chain in chains:
        output.append(super_molecule(chain, permutates))
    f = open("output.txt", "w")
    for each in output:
        f.write(str(each))
        f.write('\n')
    f.close()


if __name__ == '__main__':
    main()
