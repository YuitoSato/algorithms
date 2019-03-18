list = [3,5,8,1,2,9,4,7,6]

def quick_sort(arr):
    left = []
    right = []
    if len(arr) <= 1:
        return arr

    ref = arr[0]
    ref_count = 0

    for ele in arr:
        if ele < ref:
            left.append(ele)
        elif ele > ref:
            right.append(ele)
        else:
            ref_count += 1
    left = quick_sort(left)
    right = quick_sort(right)
    return left + [ref] * ref_count + right

print(quick_sort(list))




def _quick_sort(array, left, right):
    if left >= right: return

    # ピボットを決定
    pivot = median(array[left], array[(left + (right - left) // 2)], array[right])
    l = left
    r = right

    # ピボットを中心に分ける
    while True:
        # ピボットより小さい値を左、大きい値を右に移動する
        while array[l] < pivot:
            l += 1
        while pivot < array[r]:
            r -= 1
        if (r <= l): break

        # 見つかった要素を交換
        tmp = array[l]
        array[l] = array[r]
        array[r] = tmp
        l += 1
        r -= 1

    # 左右に分けた部分を再帰的にクイックソート
    _quick_sort(array, left, l - 1)
    _quick_sort(array, r + 1, right)

def quick_sort(array):
    _quick_sort(array, 0, len(array)-1)

def median(x, y, z):
    if x < y:
        return (y if y < z else z) if x < z else x
    else:
        return (x if x < z else z) if y < z else y

# デバッグ
if __name__ == "__main__":
    array = [1,2,3,4,5,3,2,1,4,3,4,5,0]
    print("before", array)
    quick_sort(array)
    print("after ", array)
