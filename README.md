# EV3-PixelPlotter

Source code for the final project for the course INGT1001 at NTNU Trondheim 2021.
The constrains for the project was to build something using Legos, the MINDSTORM EV3 robot and for it to be written in Python using an object-oriented style.

We have made a robot that can paint a 40x40 image to a piece of paper. We have also made a program that takes any image, scales it to 40x40 and then output an array of 0's (white) and 1's (black) based on every pixel in the image. Since the EV3 robot only has access to the Python standard library, we have to do these steps on a computer, and then pass in the output array as a textfile to the EV3 robot. We then parse that textfile containing the array of 0's and 1's. Then the robot prints that array on to a piece of paper using two motors, one controlling the paper (y-axis), and one controlling the arm (x-axis). We also have one motor that can move a pen up and down depending on if the current pixel is 0 (white) or 1 (black).

<div align="center">
  Demo of robot:
  to-do add gif timelapse of robot in action!
</div>
<div align="center">
  Demo of paint program:
</div>
<div align="center">
<img src="https://github.com/LytixDev/EV3-PixelPlotter/blob/main/paint.gif" width="500">
</div>
