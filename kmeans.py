import numpy as np
import matplotlib.pyplot as plt
Xn=np.array([2, 3, 1.9, 2.5, 4])
Yn=np.array([5, 4.8, 4, 1.8, 2.2])

# 标识符号
sign_n = ['A', 'B', 'C', 'D', 'E']
sign_k = ['k1', 'k2']

def dist(Xn,Yn,idx):
    dist=[]
    for i in range(len(Xn)):
        d=np.sqrt((Xn[i]-Xn[idx])**2+(Yn[i]-Yn[idx])**2)
        dist.append(d)
    return dist

def select_seed(Xn):
    idx=np.random.choice(range(len(Xn)))
    return idx

def select_other_seed(Xn,Yn,dist):
    dist_sum=np.sum(dist)
    rom=np.random.random()*dist_sum
    for i in range(len(Xn)):
        rom -= dist[i]
        if rom>0:
            continue
        else:
            return i

def select_all_seed(seed_num):
    Xk=[]
    Yk=[]
    idx_list=[]
    for i in range(seed_num):
        flag=True
        if i==0:
            idx=select_seed(Xn)
            Xk.append(Xn[idx])
            Yk.append(Yn[idx])
            idx_list.append(idx)
        else:
            while flag:
                idx=select_other_seed(Xn, Yn, dist)
                if idx not in idx_list:
                    flag=False
                else:
                    continue
            dist= dist(Xn, Yn, idx)
            Xk.append(Xn[idx])
            Yk.append(Yn[idx])
            idx_list.append(idx)
    Xk = np.array(Xk)
    Yk = np.array(Yk)
    return Xk, Yk

def start_class(Xk,Yk):
    cls_dict = {}
    for i in range(len(Xn)):
        dist=[]
        for j in range(len(Xk)):
            d=np.sqrt((Xn[i]-Xk[j])**2+(Yn[i]-Yk[j]))
            dist.append(d)
        dmin=np.min(dist)
        idx=dist.index(dmin)
        cls_dict[i] = idx      #####
        print(cls_dict)
    return cls_dict

##重新计算分类的坐标点
def recal_class_point(Xk, Yk, cls_dict):
    x1=0
    y1=0
    num_k1=0
    x2 = 0
    y2 = 0
    num_k2 = 0
    for i in range(len(Xn)):
        if cls_dict[i]==1:
            ##累加x值
            x1 += Xn[i]
            ##累加y值
            y1 += Yn[i]
            ##累加分类个数
            num_k1 += 1
        else:
            x2 += Xn[i]
            ##累加y值
            y2 += Yn[i]
            ##累加分类个数
            num_k2 += 1
    k1_new_x = x1 / num_k1  # 新的k1的x坐标
    k1_new_y = y1 / num_k1  # 新的k1的y坐标

    k2_new_x = x2 / num_k2  # 新的k2的x坐标
    k2_new_y = y2 / num_k2  # 新的k2的y坐标

if __name__ == "__main__":

    ##选取2个种子点
    Xk, Yk = select_all_seed(2)

    ##循环三次进行分类
    for i in range(3):
        cls_dict = start_class(Xk, Yk)
        Xk_new, Yk_new = recal_class_point(Xk, Yk, cls_dict)
        Xk = Xk_new
        Yk = Yk_new