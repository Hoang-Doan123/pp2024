import math

def get_input(message):
    return input(message)

def get_float_input(message):
    return float(input(message))

def get_int_input(message):
    return int(input(message))

def round_down_decimal(number):
    return math.floor(number * 10) / 10
