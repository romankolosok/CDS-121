import re

ip_expression = '(?<=\D)((((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\.)){3})((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])))(?=\D)'
with open("IP_search.txt") as file:
    ip_list = []
    for line in file.readlines():
        ip_list += [element[0] for element in re.findall(ip_expression, line)]

    print(ip_list)

#https://regex101.com/r/ttv7s2/1


with open('pass_in.txt') as input_f:
    with open('pass_out.txt', 'w') as output_f:
        for line in input_f.readlines():
            for match in re.findall(r'((?<=Password: )\w+)', line):
                line = re.sub(match, "*" * len(match), line)
            output_f.write(line)