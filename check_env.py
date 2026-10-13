"""Run this after setup to confirm everything works: python check_env.py"""
import sys
import numpy as np, scipy, matplotlib, cv2

print("Python     :", sys.version.split()[0])
print("NumPy      :", np.__version__)
print("SciPy      :", scipy.__version__)
print("Matplotlib :", matplotlib.__version__)
print("OpenCV     :", cv2.__version__)

im = cv2.imread("images/the_berry_farms_sunflower_field.jpeg", cv2.IMREAD_REDUCED_COLOR_4)
print("Sunflower  :", "OK " + str(im.shape) if im is not None else "MISSING")
