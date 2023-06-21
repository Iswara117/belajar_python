
record = [['Harry',37.21],['Berry', 37.21],['Tina', 37.2],['Akriti', 41.0]]

# print(record)

scores = [i[1] for i in record]
test_sort = sorted(set(scores))[1]
# print(test_sort)

equal = sorted(i[0] for i in record if i[1] == test_sort)

print(*equal, sep="\n")
