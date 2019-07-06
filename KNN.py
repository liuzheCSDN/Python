import numpy as np
Dataset=np.array([[1.0,2.0],[1.2,0.1],[0.1,1.4],[0.3,3.5]])
labels=['A','A','B','B']
test=[1.1,0.3]
k=3
#分类
diff=test-Dataset
squaredist=np.sum(diff**2,axis=1)
dist=squaredist**0.5
index=np.argsort(dist)
dict={}
for i in range(k):
    vote=labels[index[i]]
    dict[vote]=dict.get(vote,0)+1
max=0
for key,value in dict.items(): #以列表返回可遍历的(键, 值) 元组数组
    if max<value:
        max=value
        classes=key

print(classes)