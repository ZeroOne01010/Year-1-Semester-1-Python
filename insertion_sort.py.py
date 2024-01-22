
#Insertion sort function
def insertion_sort(arr):
    for i in range(1, len(arr)):
        value = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > value:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = value

my_array = []

for i in range(5):
    element = int(input(f"Enter element {i + 1}: "))
    my_array.append(element)

insertion_sort(my_array)
my_array.reverse()
print(my_array)