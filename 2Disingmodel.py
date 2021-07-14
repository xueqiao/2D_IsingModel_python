#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt


# In[3]:


##define the function to calculate the change of energy
def deltaU(m,n,status):
    conv = np.array([[0,1,0],[1,0,1],[0,1,0]])
    delta = np.sum(conv*status[m-1:m+2,n-1:n+2])*2*(status[m,n])
    return delta


# In[5]:


np.random.seed()

size = 300 ###here you can set the size of lattice
t = [1.0]
l = len(t)
S = [1,-1] 
count = 100*size*size 

##random the initial situation
initial = np.random.randint(0,2,size=[size+2,size+2]) 
initial[initial == 0] = -1


fig = plt.figure(figsize=(4, 4), dpi=400)
r = np.ceil(l/4)

STATUS = []
for j in range(l):
    T = t[j]
    status = initial

    for i in range (count):
        m = int(np.random.random()*size+1)
        n = int(np.random.random()*size+1)
        delta = deltaU(m,n,status)
        if delta < 0:   ##applying Metropolis Algorithm
            status[m,n] = -status[m,n]
        elif np.random.random() < np.exp(-delta/T):
            status[m,n] = -status[m,n]
    loc = j+1
    #ax = fig.add_subplot(r,1,loc) ###if you want to plot several figures at a time, you can uncomment this line and comment the next line
    ax = fig.add_subplot()
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                wspace=0.3, hspace=0.3)
    img = np.zeros((size,size,3), np.uint8) ##create a black canvas
    for p in range(size):
        for k in range(size):
            if status[p,k] == 1:
                img[k,p] = (255,255,255)  ##give color(here:white or black) to the canvas
    ax.imshow(img)
    T = round(t[j],2)
    plt.title('T=%s'%T,fontsize = 4)
    ax.axis('off')
    name = 'T=%s.png'%T
    plt.show() ###show the plot

