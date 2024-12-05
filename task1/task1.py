with open('input.txt') as fd:
    pairs = list(map(lambda x: x.strip().split('   '),fd.readlines()))
first_list = []
second_list = []
for first, second in pairs:
    first_list.append(int(first))
    second_list.append(int(second))
res = sum([abs(first - second) for first, second in zip(sorted(first_list),sorted(second_list))])
print(res)