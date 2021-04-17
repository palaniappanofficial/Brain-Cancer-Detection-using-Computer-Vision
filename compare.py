import cv2
import numpy as np
from matplotlib import pyplot as plt
#from skimage.measure import compare_ssim as ssim
from skimage.metrics import structural_similarity as ssim
from tkinter import messagebox
# from tkinter import messagebox
width = 225
height = 225
dim = (width, height)
ssim_val=[]
h_count=0

img1 = cv2.imread('resized/1.jpeg',0)
img3 = cv2.imread('resized/3.jpeg',0)
img4 = cv2.imread('resized/4.jpeg',0)
img5 = cv2.imread('resized/5.jpeg',0)
img6 = cv2.imread('resized/6.jpeg',0)
img7 = cv2.imread('resized/7.jpeg',0)
img8 = cv2.imread('resized/8.jpeg',0)
img9 = cv2.imread('resized/9.jpeg',0)
img10 = cv2.imread('resized/0.jpeg',0)

img2 = cv2.imread('test images/no_1.jpg',0) 
#no_1.jpg is healthy image
#yes_1.jpg is unhealthy image

def img_conv(image):
	resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
	ret,thresh1 = cv2.threshold(resized,72,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
	return thresh1
	# cv2.imwrite("temp.jpeg", thresh1)
test_img=img_conv(img2)

healthy = [img1,img3,img4,img5,img6,img7,img8,img9,img10]

def compare_images(frame, frame1, title):
	s = ssim(frame, frame1)
	# setup the figure
	fig = plt.figure(title)
	plt.suptitle(" SSIM: %.1f" % (s*100))
	ssim_val.append(int(round(s*100)))
 
	# show first image
	ax = fig.add_subplot(1, 2, 1)
	plt.imshow(frame,plt.cm.bone)
	plt.axis("off")
 
	# show the second image
	ax = fig.add_subplot(1, 2, 2)
	plt.imshow(frame1, cmap = plt.cm.bone)
	plt.axis("off")
 
	# show the images
	plt.show()
	
for i in range(8):
		compare_images(healthy[i],test_img,"Brain Tumour Detection Prototype")
print(ssim_val)

avg=0
for val in ssim_val:
	avg+=val
avg=avg/len(ssim_val)

	#if val>=35.0:
	#	h_count+=1

if avg>=45:
	messagebox.showinfo("Report","Healthy")
else:
	messagebox.showerror("Report","Abnormal")
