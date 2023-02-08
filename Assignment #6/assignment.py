def remove_outliers(arr):
    mas = []
    # min_n = min(arr)
    # max_n = max(arr)
    min_n = max_n = arr[0]
    for el in arr:
        if el < min_n:
            min_n = el
        elif el > max_n:
            max_n = el

    for i in arr:
        if not {min_n, max_n} & {i}:
            mas.append(i)
    return mas

# print(remove_outliers([(1,2),(0,2),(5,7),(6,5),(7,1)]))
# print(remove_outliers([1,2,0,2,5,7,6,5,7,1]))
print(remove_outliers('abcdeabaaddd'))
print(remove_outliers(('ab', 'as', 'af', 'dr', 'yt', 'hy')))
# print(remove_outliers(543))
print(remove_outliers({'a': 4, 3: 5, 'g': 6, 65: 8, 'ggd': 2}))
# print(remove_outliers({'a': 4, 3: 5, 'g': 6, 65: 8, 'ggd': 2}.keys()))
# print(remove_outliers(list({'a', 3, 'g', 65, 'ggd'})))

#function works almost with all iterables, depends from type of iterable,
# lets say, if it's a string it compares all symbols amd finds min and max
# symbol(relying on ASCII), if it's iterable of stringsit counts sum of those chars
# in ASCII and founds min and max then relying on sum values, the same process happens
# with iterable with tuples of numbers, counts sum of tuple and then determines min and max.
# With just list of numbers it works as it suppose to. Now I have to mention that 'iterables'
# that I mentioned before didnt included 'lazy iterables', I tried to put dict_keys() iterable
# as a parameter and it threw an error %object is not subscriptable%, so it seems like lazy iterables cant be used.
#If we try to pass iterables with different type values it them we will get an error that different types arent compatable,
#and finally If we try to pass non iterable we will get an error %object is not subscriptable%(if it's int for example),
# but if we pass a dictionary, we will get a Key Error