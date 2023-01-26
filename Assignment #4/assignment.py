
with open("data.txt", "r") as f:
    txt = [el for el in f.read().splitlines()]

print(txt)

int_list = [len(el) for el in txt]
print(int_list)

tuple_list = [(str_, n) for str_, n in zip(txt, int_list)]
print(tuple_list)

[print(el[0]) for el in tuple_list if len(el[0]) <= 10]