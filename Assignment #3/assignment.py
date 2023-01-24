
with open("data.txt", "r") as f:
    txt = [el.split(",") for el in f.read().splitlines()]

max_index = 0

for i in range(len(txt)):
    txt[i][1] = float(txt[i][1])#tried to use walrus in IF below but it doesnt work for some reason
    if txt[i][1] > txt[max_index][1]:
        max_index = i
    txt[i] = tuple(txt[i])

print(f"The most expensive product is {txt[max_index][0]}, it costs ${txt[max_index][1]}")
#end of second task


txt.sort()#sort the list so we wont come back to already checked samples

i = 1
counter = 1
arr = []
while i < len(txt):
    if txt[i][0] == txt[i-1][0]:
        counter += 1
    else:
        arr.append((txt[i-1][0], counter))
        counter = 1
    i += 1
arr.append((txt[i-1][0], counter))

print(f"\n|{'Product':^10}|{'Mentions':^10}|\n{'':-^23}")
[print(f"|{el[0]:^10}|{el[1]:^10}|") for el in arr]