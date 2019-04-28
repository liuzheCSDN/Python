import numpy as np

def py_cpu_nms(dets, thresh):
#x1、y1、x2、y2、以及score赋值
    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]
    scores = dets[:, 4]
    #每一个检测框的面积
    areas = (x2 - x1 + 1) * (y2 - y1 + 1)
    #  #按照score置信度降序排序
    order = scores.argsort()[::-1]#argsort()函数默认是将x中的元素从小到大排列,[::-1]设置从大到小排列
    keep = []
    #  #保留的结果框集合
    while order.size > 0:
        i = order[0]
        keep.append(i)#保留该类剩余box中得分最高的一个
        # #得到相交区域,左上及右下
        xx1 = np.maximum(x1[i], x1[order[1:]])
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.minimum(x2[i], x2[order[1:]])
        yy2 = np.minimum(y2[i], y2[order[1:]])
        #计算相交的面积,不重叠时面积为0
        w = np.maximum(0.0, xx2 - xx1 + 1)
        h = np.maximum(0.0, yy2 - yy1 + 1)
        inter = w * h
        #计算IoU：重叠面积 /（面积1+面积2-重叠面积）
        ovr = inter / (areas[i] + areas[order[1:]] - inter)
        #保留IoU小于阈值的box,删除大于阈值的框
        inds = np.where(ovr <= thresh)[0]#np.where()[0] 表示行的索引，np.where()[1] 则表示列的索引
        order = order[inds + 1]  #因为ovr数组的长度比order数组少一个,所以这里要将所有下标后移一位
    return keep

def soft_nms(dets, thresh,method):
#x1、y1、x2、y2、以及score赋值
    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]
    scores = dets[:, 4]
    #每一个检测框的面积
    areas = (x2 - x1 + 1) * (y2 - y1 + 1)
    #  #按照score置信度降序排序
    order = scores.argsort()[::-1]#argsort()函数默认是将x中的元素从小到大排列,[::-1]设置从大到小排列

    i = order[0]
    # #得到相交区域,左上及右下
    xx1 = np.maximum(x1[i], x1[order[1:]])
    yy1 = np.maximum(y1[i], y1[order[1:]])
    xx2 = np.minimum(x2[i], x2[order[1:]])
    yy2 = np.minimum(y2[i], y2[order[1:]])
    #计算相交的面积,不重叠时面积为0
    w = np.maximum(0.0, xx2 - xx1 + 1)
    h = np.maximum(0.0, yy2 - yy1 + 1)
    inter = w * h
    #计算IoU：重叠面积 /（面积1+面积2-重叠面积）
    ovr = inter / (areas[i] + areas[order[1:]] - inter)
    #保留IoU小于阈值的box,删除大于阈值的框
    if method==1:
        inds = np.where(ovr >= thresh)[0]#np.where()[0] 表示行的索引，np.where()[1] 则表示列的索引
        weight=1-ovr[inds]
        dets[inds, 4]=weight*dets[inds,4]#修改分数
    if method==2:
        weight=np.exp(-(ovr * ovr)/0.3)
        dets[order[1:], 4] = weight * dets[order[1:], 4]
    return dets[:,4]
if __name__=='__main__':
    det=np.array([[1,1,3,3,0.8],[2,2,4,5,0.5],[3,2,5,4,0.9]])
    thresh=0.3
    f=py_cpu_nms(det, thresh)
    scores=soft_nms(det, thresh,2)
    print(scores)
    print(f)