import math

def paint_calc(height, width, cover):
    """The program calculates the number of cans needed to paint a wall given
    the height, width and coverage"""

    area = height * width
    num_of_cans = math.ceil(area/cover)

    print(f"You'll need {num_of_cans} cans of paints")

paint_calc(2,4,5)
