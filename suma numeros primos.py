#cuales y cuantos numeros primos comprendidos entre 1 y 1000
count = 0
for num in range(2, 1001):
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        count += 1
        print (num)
print(count)