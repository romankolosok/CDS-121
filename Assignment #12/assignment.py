from collections import defaultdict
import random
from pprint import pprint
from collections import Counter
import itertools as it


#first
d = defaultdict(lambda: random.randint(0, 100))
d['a'] = 34
d['b'] = 84
print(d, d['c'])
print(d)

#second
stocks = defaultdict(lambda: [])
with open("input.txt") as f:
    for line in f.readlines():
        line = line.strip().split(";")
        line[1] = [float(price) for price in line[1].split(",")]
        stocks[line[0]] = line[1]

pprint(stocks)
pprint(stocks["NVDA"])
pprint(stocks)

#third
word = "bananas"
#let's count letters in this word
count_letters = Counter(word)
pprint(count_letters)
#counter counted letters in word and has dictionary with count of each letter within it, since it has dictionary, maybe it work like a dictionary too? :]
#lets try to access data inside Counter()

print("Going inside Counter(): ")
for element in count_letters:
    print(element, ":", count_letters[element])
print("Left Counter()")

#Counter elements are accessible like dictionary elements. Lets try to get a list of .keys, .values and .items and see if it works
print("Keys:",count_letters.keys())
print("Values:", count_letters.values())
print("Items:", count_letters.items())

#Also we can add, substract, intersect, combine(examples in textboox)
#We can get a sorted by descensing list of key frequencies with .most_common() function, we can get n-first elements of the list if we put integer between parentheses in function call
print("List of frequencies:",count_letters.most_common())
print("Most frequent element(list with one-first element):", count_letters.most_common(1))
#or other way to do get same result
print("Most frequent element(list element):", count_letters.most_common()[0])
#find less frequent key
print("Less frequent element(list element):", count_letters.most_common()[-1])

#fourth

#count
even_rule = it.count(step=2)
print("List of first 50 even numbers :", list(next(even_rule) for _ in range(50)))
rule_2 = it.count(start=-10, step=0.3)
print("List of 10 numbers form -10 with step 0.3:", list(next(rule_2) for _ in range(10)))

#zip_longest
list_1 = list(range(7))
list_2 = ['a', 'g', 'f', 'e', 't']
#will insert None for  all missing values, unless other 'fillvalue' is indicated in function call
print("Longest list zip:", list(it.zip_longest(list_1, list_2)))
print("Longest list zip(with fillvalue):", list(it.zip_longest(list_1, list_2, fillvalue='Here could be your ad')))

#compress
motivation_speech = "You should read lots of books and improve your skills, instead of sleep all day!"
motivation_speech = motivation_speech.split(" ")
print(motivation_speech)
select_words = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
print(f"Motivation speech for students: '{' '.join(list(it.compress(motivation_speech, select_words)))}'")
#selects elements of list if they are mentioned(1)
