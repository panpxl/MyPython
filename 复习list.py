classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print(classmates[0], classmates[1], classmates[2])
print(classmates[len(classmates) - 1], classmates[len(classmates) - 2], classmates[len(classmates) - 3])

# 往list中追加元素到末尾
classmates.append('Jackie')
print(classmates)

# 插入到指定的位置
classmates.insert(1, 'banana')
print(classmates)

# 删除末尾的元素
print(classmates.pop())
print(classmates)

# 删除指定位置的元素
print(classmates.pop(1))
print(classmates)

# 把某个元素替换成别的元素
classmates[1] = 'apple'
print(classmates)

#  print(help('pop'))

L = ['abc', 'def', 'ghi']
M = [L, 'jkl', 'mno', 'pqr']
print(M)
print(len(M))
