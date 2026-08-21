""" Calculate the area of a rectangule"""
import argparse
def calculate_rectangle_area(length, width):
"""

    float: The area of the rectangle
"""


return length * width

def main():
    parser = argparse.ArgumentParser
    (description = "Calculate the area of a rectangle.")
    parser.add_argument("length", type=float, help="The length of the rectangle.")
    parser.add_argument("width", type=float, help="the width of the rectangle.")