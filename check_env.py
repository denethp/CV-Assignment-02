"""Run this after setup to confirm everything works: python check_env.py"""
import sys
import numpy as np, scipy, matplotlib, cv2

print("Python     :", sys.version.split()[0])
print("NumPy      :", np.__version__)
print("SciPy      :", scipy.__version__)
print("Matplotlib :", matplotlib.__version__)
print("OpenCV     :", cv2.__version__)

sift = cv2.SIFT_create()  # needed for Q4
print("SIFT       : OK")

checks = {
    "Q1 sunflower": ("images/the_berry_farms_sunflower_field.jpeg", cv2.IMREAD_REDUCED_COLOR_4),
    "Q3 wadham":    ("images/wadham.jpg", cv2.IMREAD_COLOR),
    "Q3 flag":      ("images/flag.png", cv2.IMREAD_COLOR),
    "Q4 template":  ("images/pcbs/AECC1.jpg", cv2.IMREAD_COLOR),
}
for name, (path, flag) in checks.items():
    im = cv2.imread(path, flag)
    print(f"{name:14s}: {'OK ' + str(im.shape) if im is not None else 'MISSING -> ' + path}")
