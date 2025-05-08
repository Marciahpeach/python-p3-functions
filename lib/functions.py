#!/usr/bin/env python3


def greet_programmer(name="programmer"):
    print(f"Hello, {name}!")
greet_programmer()

def greet(name):
    print(f"Hello, {name}!")
greet("Naureen")

def add(num1, num2):
    return num1 + num2
print(add(1, 2))

def halve(number):
    return number / 2
print(halve(2))

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
greet_with_default()