import sys

arr = [
    [2, 3, 7],
    [5, 4, 5],
    [1, 4, 4]
]

start = [0, 2]
end = [2, 0]

checked = []


def up(now):
    if now[0] == 0:
        return now

    return [now[0] - 1, now[1]]


def down(now):
    if now[0] == len(arr) - 1:
        return now

    return [now[0] + 1, now[1]]


def left(now):
    if now[1] == 0:
        return now

    return [now[0], now[1] - 1]


def right(now):
    if now[1] == len(arr[0]) - 1:
        return now

    return [now[0], now[1] + 1]


def get(now):
    return arr[now[0]][now[1]]


def search_path(now):
    checked.append(now)

    if now[0] == end[0] and now[1] == end[1]:
        print('fin', now)
        print(checked)
        sys.exit()

    if get(up(now)) < get(start):
        search_path(up(now))

    if get(left(now)) < get(start):
        print('left')
        search_path(left(now))

    if get(down(now)) < get(start):
        search_path(down(now))

    if get(right(now)) < get(start):
        search_path(right(now))

    print('fail', now)
    print(checked)


search_path(start)
