arr = [5, 9, 3, 7, 2, 8, 6]
max = arr[0]
min = arr[0]
i = 0
while i < len(arr):
    if max < arr[i]:
        max = arr[i]
    if min > arr[i]:
        min = arr[i]   
    i +=1

print("Максимальное число равно ", max)
print("Минимальное число равно ", min)
