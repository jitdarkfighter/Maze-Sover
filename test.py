from PIL import Image
import numpy as np
import heapq
import time 

start_time = time.time()
img= Image.open(r"C:\JITHIN\CP\Nigga Challenge\frame_0.png")
img=img.convert("RGB")
rows,cols=5769,5769
L=[]
for i in range(rows):
    l=[]
    for j in range(cols):
        print(img.getpixel((i,j)))