array = [20, 50, 60, 7, 9, 3, 100, 200, 50, 40]


def findminmax(arr):
    if len(arr) == 0:
        return [None, None]  # معالجة الحالة الخاصة بالمصفوفة الفارغة
    
    minVal = arr[0] 
    maxVal = arr[0]
    
    for i in arr:
        if i < minVal:
            minVal = i 
        if i > maxVal:  # يجب المقارنة مع maxVal نفسه
            maxVal = i 
    
    return [maxVal, minVal]

print(findminmax(array))