import re

ip_expression = '(?<=[\D])((((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\.)){3})((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])))(?=\D)'
with open("IP_search.txt") as file:
    ip_list = []
    for line in file.readlines():
        # ip_list.extend([element[0] for element in ])
        print(re.findall(ip_expression, line))

#https://regex101.com/r/ttv7s2/1