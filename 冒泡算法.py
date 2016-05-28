import random

list_data = []
for i in range(10):
    list_data.append(random.randint(0, 20))
print(list_data)

list_len = len(list_data) - 1
for i in range(10):
    sort_over = True
    for j in range(list_len - i):
        if list_data[j] > list_data[j + 1]:
            tmp = list_data[j]
            list_data[j] = list_data[j + 1]
            list_data[j + 1] = tmp
            print("y i=%d,j=%d,%s" % (i, j, list_data))
            sort_over = False
        else:
            print("n i=%d,j=%d,%s" % (i, j, list_data))
    if sort_over:
        print("o i=%d,j=%d,%s" % (i, j, list_data))
        break

print(list_data)
