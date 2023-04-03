import numpy as np
import skimage.io
import matplotlib.pyplot as plt

img = skimage.io.imread('tiger.png', as_gray=True) #dtype uint8, dimenzije: 640x960
plt.figure(1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)



img2 = img.copy()
rows, cols = img2.shape
rotate = np.zeros((cols,rows))
mirror = np.zeros((rows,cols))
lowres = np.zeros((rows,cols))
cut = np.zeros((rows,cols))

for i in range(rows):
    for j in range(cols):
            img2[i][j] += 50 #jaci brightness

for i in range(rows):
    rotate[:,-i] = img2[i,:] #rotacija za 90

for j in range(cols):
    mirror[:,j] = img2[:,cols-1-j] #zrcaljenje

#smanjenje rezolucije
lowers = img2[::5,::5]            

#cutovanje
cut = np.zeros((rows,cols))
for x in range(int (cols/4),int (cols/2)):
     cut[:,x]=img2[:,x]

plt.figure(2)
plt.imshow(rotate, cmap='gray', vmin=0,vmax=255)

plt.figure(3)
plt.imshow(mirror, cmap='gray', vmin=0,vmax=255)

plt.figure(4)
plt.imshow(lowers, cmap='gray', vmin=0,vmax=255)

plt.figure(5)
plt.imshow(cut, cmap='gray', vmin=0,vmax=255)

plt.show()