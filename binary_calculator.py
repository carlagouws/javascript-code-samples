# 10001101 = 141
# 10101010 = 170
# 101100 = 44
# 1111 = 15

x = input("Enter a binary number: \n")
reversed_binary = [i for i in reversed(str(x))]
number_list = []

for i in range(len(reversed_binary)):
    if reversed_binary[i] == "1":
        number_list.append(int(2 ** i))
    else:
        number_list.append(0)

print(sum(number_list))
