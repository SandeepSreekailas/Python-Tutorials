numbers = [5, 3, 8, 2, 1]

n=len(numbers)

for i in range(n):
    for j in range(n-i-1):
        if numbers[j]>numbers[j+1]:
            numbers[j],numbers[j+1] = numbers[j+1], numbers[j]

print(numbers)



def larno(n):
    index_length=len(n)-1
    sorted=False

    while not sorted:
        sorted = True
        for i in range(0,index_length):
            if n[i]>n[i+1]:
                sorted=False
                n[i],n[i+1]=n[i+1],n[i]
    return n

print(larno([5,3,8,2,1]))