# with open("input.txt") as input_txt:
#     loo = input_txt.readlines()
#     dict_list=[]
#     for el in loo:
#         el = el.strip().split(",")
#         el[1:] = [float(el[2])-float(el[1])]
#         dict_list.append(el)
#     print(dict(dict_list))

def rerere(n):
    re = 'P'
    for _ in range(n):
        yield re
        re += 'P'

for i in rerere(5):
    print(i)
