def LinearSearch(list, item):
  index = 0
  found = False
  while index < len(list) and  found is False:
    if list[index] == item:
      found = True
    else:
      index = index + 1
  return found

list = [12, 33, 11, 99, 22, 55, 90]
print(LinearSearch(list, 12))
print(LinearSearch(list, 91))
