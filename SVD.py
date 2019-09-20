# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 10:52
# @Author  : DrMa
import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
from sklearn import datasets
from skimage import io

def getImgAsMat(index):
    ds = datasets.fetch_olivetti_faces()
    return np.mat(ds.images[index])

def getImgAsMatFromFile(filename):#读取照片转为矩阵
    img = io.imread(filename, as_grey=True)
    return np.mat(img)
def plotImg(imgMat):#展示图片,将矩阵显示成照片
    plt.imshow(imgMat, cmap=plt.cm.gray)
    plt.show()
def recoverBySVD(imgMat, k):
    # singular value decomposition
    U, s, V = la.svd(imgMat)
    # choose top k important singular values (or eigens)
    Uk = U[:, 0:k]
    Sk = np.diag(s[0:k])

    Vk = V[0:k, :]
    # recover the image
    imgMat_new = Uk * Sk * Vk

    return imgMat_new,U,Uk


# -------------------- main --------------------- #
A = getImgAsMatFromFile('./A.jpg')
plotImg(A)
A_new,U,Uk = recoverBySVD(A, 30)
plotImg(A_new)