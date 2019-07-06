#对于列表和字典，参数传递的方式是引用传递。
def bubble_sort(l):
    list=l.copy()    #对列表进行拷贝，这样不会改变参数l的值
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if(list[j]>list[j+1]):
                list[j+1],list[j]=list[j],list[j+1]
    return list

def selection_sort(l):
    list = l.copy()
    n=len(list)
    for i in range(n-1):
        maxidx=i
        for j in range(i+1,n):
            if list[j]>list[maxidx]:
                maxidx=j
        if maxidx!=i:
            list[i],list[maxidx]=list[maxidx],list[i]
    return list

def insert_sort(l):
    list = l.copy()
    # 从第二个位置，即下标为1的元素开始向前插入
    for i in range(1,len(list)):
        # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
        for j in range(i,0,-1):#不包含0
            if list[j]<list[j-1]:
                list[j],list[j-1]=list[j-1],list[j]
    return list

def shell_sort(l):
    list=l.copy()
    gap=len(list)//2
    while gap>0:
        for i in range(gap,len(list)):
            j=i;
            while j>=gap and list[j]<list[j-gap]:
                list[j - gap], list[j] = list[j], list[j - gap]
                j=j-gap
        gap=gap//2
    return list


#二分查找
def binary_select(list,item):
    first=0
    last=len(list1)-1

    while last>=first:
        mid = first + last // 2
        if list[mid]==item:
            return mid
        if list[mid]>item:
            last=mid-1
        if list[mid]<item:
            first = mid+1
    return False

def numSubarraysWithSum(A, S):
        """
        :type A: List[int]
        :type S: int
        用到前缀和的方法，使用字典sum_dict,和为“key”的个数有“sum_dict[key]”个
        """
        result, cur_sum = 0, 0
        sum_dict = {0: 1}
        for num in A:
            cur_sum += num
            if cur_sum - S in sum_dict:
                result += sum_dict[cur_sum - S]
            if cur_sum in sum_dict:
                sum_dict[cur_sum] += 1
            else:
                sum_dict[cur_sum] = 1
        return result



list = [54,26,93,17,77,31,44,55,20,1]
A = [1,0,1,0,1,0]
S = 2
num=numSubarraysWithSum(A,S)

list1=bubble_sort(list)
list2=selection_sort(list)
list3=insert_sort(list)
list4=shell_sort(list)
print(list1)
print(list2)
print(list3)
print(list4)
print(list)
print(binary_select(list1,26))