tree = []

iterations = input(f'kies een getal van 1 tot 20,\n')

for i in range(int(iterations)):
    if i == 0:
        tree.append("*")
    else:
        tree.append(f'{tree[i - 1]}*')
    print(tree[i], end="")
# print("driehoek van 1 tot 8 met for:")
# for i in range(8):
#     for j in range(i + 1):
#         print("*", end="")
#     print()