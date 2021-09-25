# Bucket Sort in Python
def Bucket_sort(list_no):
    largest = max(list_no)
    length = len(list_no)
    size = largest / length
    Buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(list_no[i] / size)
        if j != length:
            Buckets[j].append(list_no[i])
        else:
            Buckets[length - 1].append(list_no[i])
    for i in range(length):
        insertion_sort(Buckets[i])
    result = []
    for i in range(length):
        result = result + Buckets[i]
    return result
def insertion_sort(list_no):
    for i in range(1, len(list_no)):
        temp = list_no[i]
        j = i - 1
        while (j >= 0 and temp < list_no[j]):
            list_no[j + 1] = list_no[j]
            j = j - 1
        list_no[j + 1] = temp
list_no = input('Enter the list of (positive) numbers: ').split()
list_no = [int(x) for x in list_no]
sorted_list = Bucket_sort(list_no)
print('Sorted list: ', end='')
print(sorted_list)
