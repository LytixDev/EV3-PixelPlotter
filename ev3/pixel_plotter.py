#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port

PIXELS = 40
SPEED_NEW_PIXEL = 25
SPEED_NEW_LINE = 50
SPEED_PAPER = 100
PAPER_NEW_LINE = 12000 // PIXELS
ARM_NEW_LINE = -430
NEW_PIXEL = -ARM_NEW_LINE // PIXELS
PEN = 20
PEN_DOWN = 10
PEN_UP = 0
MTR_TIME = 1000

class PixelPlotter:

    def __init__(self):
        self.image_array = self.set_image_array

        self.ev3 = EV3Brick()
        self.paper = Motor(Port.A)
        self.arm = Motor(Port.B)
        self.pen = Motor(Port.C)

        self.print(self.image_array)

    
    # reads the file and converts it to a python array
    def set_image_array(self):
        tmp = []
        with open("image_array.txt", "r") as f:
            for r in f.readlines():
                # removes any spaces or newline characters
                tmp.append([value for value in r if value in ("0", "1")])
        
        return tmp

    # main method for printing
    def print(self):
        for print_line in self.image_array:
            for pixel in print_line:
                self.move_pen(pixel)
                self.move_arm()
            self.new_line()
            
    # moves pen up or down
    def move_pen(self, pixel):
        if pixel == 1:
            self.pen.reset_angle(PEN_DOWN) # or run_angle(PEN, PEN_DOWN) or run_target(PEN, PEN_DOWN)
        else: 
            self.pen.reset_angle(PEN_UP)

    # Moves arm for every pixel
    def move_arm(self):
        self.arm.run_angle(SPEED_NEW_PIXEL, NEW_PIXEL)

    # moves paper down and arm back
    def new_line(self):
        self.arm.run_angle(SPEED_NEW_LINE, ARM_NEW_LINE)
        self.paper.run_angle(SPEED_PAPER, PAPER_NEW_LINE)

         
def main():
    PixelPlotter()

if __name__ == "__main__":
    main()