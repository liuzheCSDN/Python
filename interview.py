#字节跳动2018校招算法方向笔试题https://blog.csdn.net/qq_30815237/article/details/94153154
# list=[[1,2],[5,3],[4,6],[7,5],[9,0]]
# len=len(list)
# a=list[0][1]
# result=[]
# for i in range(len):
#     for j in range(len):
#         if list[i][0]<list[j][0] and list[i][1]<list[j][1]:
#             break
#         elif j==(len-1):
#             result.append(list[i])
# idx=[i for i,v in sorted(enumerate(result))]

# list1=[6,2,1]
# list=[]
# result=[]
# len1=len(list1)
# for m in range(len1):
#     for j in range(m,len1):
#         list=list1[m:j+1]
#         mi=min(list)
#         su=sum(list)
#         b=mi*su
#         a=[m,j,b]
#         result.append(a)
# maxnum=result[0][2]
# maxidx=0;
# len2=len(result)#定义了一个名为len的变量与len()方法重名，后期再遇到len时，python将其认为是len这个int类型的变量，而不是len()方法
# for i in range(len2):
#     if result[i][2]>maxnum:
#         maxnum=result[i][2]
#         maxidx=i

#在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数
import numpy as np
def find(array,target):
    row = array.shape[0]
    col=array.shape[1]
    i=0
    j=col
    while(i<row and j>0):
        start=array[i,j-1]
        if start>target:
            j=j-1
        elif start<target:
            i+=1
        else:

            return 1,i,j#返回一个元组

    return 0

a=np.array([[1,3,8,10],[4,5,7,12],[9,11,14,19],[21,24,25,30]])
flag=find(a,25)
print(flag)



#实现字符串反转的几种方法
s="abcdefghijk"
result=s[::-1]
#转化为列表
l=list(s)
l.reverse()
result2="".join(l)
#列表模拟栈（先进先出）
m=list(s)
result3=""
while len(m)>0:
    result3+=m.pop()
#for循环
result4=""
result5=""
for i in range(len(s)-1,0,-1):
    result4+=s[i]
result4+=s[0]

for i in range(len(s)):
    result5+=s[len(s)-i-1]