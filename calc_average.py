l = [4, 5, 6, 7, 8, 9, 12, 12, 13, 14]

k = 0
avg = 0

for n in l:
    new_avg = avg + ((n - avg) / (k + 1))
    k += 1
    avg = new_avg
    print(new_avg)
