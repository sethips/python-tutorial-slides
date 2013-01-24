from pprint import pprint

list1 = [chr(i) for i in range(85, 110)]
list2 = [i for i in list1 if i.isupper()]

print(list1)
print(list2)

# replace the normal for loop
[print(i) for i in list2]   # Py3k only

# one can also used dict comprehension
d = {k: v for k, v in zip(list1, list2)}
pprint(d)

# nested, different meaning
d = {k: v for k in list1 for v in list2}
pprint(d)

# it is often used together with str.join()
print(', '.join(['e'+str(i) for i in range(1, 9, 2)]))
