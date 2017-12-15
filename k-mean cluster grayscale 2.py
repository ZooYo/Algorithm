import random
import numpy as np
import scipy.misc
import matplotlib.pyplot as plt

def kMeanClusterGayscale(k,img):
    m=img.shape[0]
    n=img.shape[1]
    
    tempV=[]
    v=[]
    T=0
    for i in range(k):
        v.append(random.randint(0,256))
    
    while not (tempV==v):
        print("v = ",v)
        print("tempV = ",tempV)
        T+=1
        tempV=v[:]
        pLen=np.zeros(k)
        cluster=np.zeros((k,m,n))
        for r in range(m):
            for c in range(n):
                distance=np.zeros(k)
                for i in range(k):
                    distance[i]=abs(img[r,c]-v[i])
                minIndex=np.argmin(distance)
                pLen[minIndex]+=1
                cluster[minIndex][r][c]=1
        for i in range(k):
            pSum=0
            if pLen[i]!=0:
                for r in range(m):
                    for c in range(n):
                        if cluster[i][r][c]==1:
                            pSum+=img[r,c]
            v[i]=int(pSum/pLen[i])       
    
    newImg=img
    for i in range(k):
        for r in range(m):
            for c in range(n): 
                if cluster[i][r][c]==1:
                    newImg[r][c]=v[i]
    plt.imshow(newImg,cmap='gray')
    scipy.misc.imsave("ans.jpg",newImg)
    return T
    
img=scipy.misc.imread('k-means.jpg')
print(kMeanClusterGayscale(5,img))