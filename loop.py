# 循环

# arr = [1, 3, 4, 5]
# for key in arr:
# 	print(key)


# Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list
# 0 - 20 之和
sum = 0
for key in list(range(21)):
    sum += key

print(sum)
