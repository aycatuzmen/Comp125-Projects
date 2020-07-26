#!/usr/bin/env python3
"""
CS106AP Summer 2019
Written by Sonja Johnson-Yu
7.17.19
"""

def add_key_value(d, key, value):
    d[key] = value

def main():

    dictionary = {'tomato': 'fruit'}
    # Note that we don't catch the return value.
    # dictionary is being modified inplace!
    add_key_value(dictionary, 'broccoli', 'vegetable')
    print('dictionary:', dictionary)


if __name__ == '__main__':
    main()