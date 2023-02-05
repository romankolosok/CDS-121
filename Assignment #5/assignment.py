names = {}
with open("files.txt") as filenames:

    while line := filenames.readline().strip():
        line = line.split(".")
        if line[1] in names:
            names[line[1]].append(line[0])
        else:
            names[line[1]] = [line[0]]

suffix = input("Enter an arbitrary file suffix: ").strip(" .")
if suffix in names.keys():
    [print(f"{name}.{suffix}") for name in names[suffix]]
else:
    print("There is no files with that suffix")

