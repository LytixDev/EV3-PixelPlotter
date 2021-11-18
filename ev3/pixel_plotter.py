#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
import time

PIXELS = 40
# Speeds
SPEED_NEW_PIXEL = 25
SPEED_NEW_LINE = 50
SPEED_PAPER = -100
SPEED_PEN = 20
# Angles
PAPER_NEW_LINE = 600 // PIXELS
ARM_NEW_LINE = 400
NEW_PIXEL = ARM_NEW_LINE // PIXELS
# Relative angles
PEN_DOWN = 3 # relative positional degree from 0 which is at top
PEN_UP = -10 # relative positional degree

class PixelPlotter:

    def __init__(self):
        self.image_array = self.set_image_array()

        self.ev3 = EV3Brick()
        self.arm = Motor(Port.A)
        self.paper = Motor(Port.B)
        self.pen = Motor(Port.C)

        self.speed_new_pixel = SPEED_NEW_PIXEL

        self.arm_at_start = True
        self.printPaper()

    # reads the file and converts it to a python array
    def set_image_array(self):
        array = []
        with open("image_array.txt", "r") as f:
            for r in f.readlines():
                # removes any spaces or newline characters
                array.append([value for value in r if value in ("0", "1")])

        return array

    # main method for printing
    def printPaper(self):
        self.pen.run_target(SPEED_PEN, PEN_UP) # since the pen starts at the paper, move it up
        for print_line in self.image_array:
            # if there is nothing to draw in a line, we skip it
            if "1" in print_line:
                ''' instead of always moving the arm back to it's start position
                when on a new line, we can instead start drawing from the end
                position of the arm, as long as we reverse the array to be drawn'''
                if not self.arm_at_start:  # if arm at the end, reverse array
                    print_line = print_line[::-1] # reverse list
                    self.speed_new_pixel = -25  # opposite direction when list is reversed

                else:
                    self.speed_new_pixel = 25 # normal direction
                for pixel in print_line:
                    if pixel == "1": # check if current pixel is one
                        self.move_pen(pixel) # draw pixel with pen
                    self.move_arm() # move the arm for next pixel with current speed_per_pixel

                # arm is now at the opposite side
                self.arm_at_start = not self.arm_at_start
            
            self.new_line()
            
    # moves pen up or down when a 1 is to be written
    def move_pen(self, pixel):
        print("DOWN")
        self.pen.run_target(SPEED_PEN, PEN_DOWN)
        self.pen.run_target(SPEED_PEN, PEN_UP)

    # Moves arm for every pixel
    def move_arm(self):
        self.arm.run_angle(self.speed_new_pixel, NEW_PIXEL)

    # moves paper down when at the end of a line
    def new_line(self):
        self.paper.run_angle(SPEED_PAPER, PAPER_NEW_LINE)
         
def main():
    PixelPlotter()


if __name__ == "__main__":
    main()