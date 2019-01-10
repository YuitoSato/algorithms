import hashlib


def set_value(hash_table, key, value):
    index = int(hashlib.sha256(key.encode('utf-8')).hexdigest(), 16) % len(hash_table)

    if hash_table[index] is None:
        hash_table[index] = [key, value]
    elif type(hash_table[index][0]) is str:
        content = hash_table[index].copy()
        hash_table[index] = [content, [key, value]]
    else:
        hash_table[index].append([key, value])


def get_value(hash_table, key):
    index = int(hashlib.sha256(key.encode('utf-8')).hexdigest(), 16) % len(hash_table)
    content = hash_table[index]

    if content[0] == key:
        return content[1]

    print('Linear Search')
    for child in content:
        if child[0] == key:
            return child[1]


hash_table1 = [None] * 10000

for i in range(1000):
    set_value(hash_table1, str(i), i)

for i in range(1000):
    print(get_value(hash_table1, str(i)))
