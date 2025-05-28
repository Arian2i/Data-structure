def merge_sorted_lists(L1, L2): # الگوریتم بر اساس فصل مرتب سازی و زمان خطی 
    i, j = 0, 0
    merged = []

    # مرحله اصلی ادغام با مقایسه عناصر باید بررسی کنیم لیست کوچک به لیست بزرگ مرج شود
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            merged.append(L1[i])
            i += 1
        else:
            merged.append(L2[j])
            j += 1

    # اگر عنضری از یک لیست باقی مانده باشد باید اضفاه کنیم
    while i < len(L1):
        merged.append(L1[i])
        i += 1

    while j < len(L2):
        merged.append(L2[j])
        j += 1

    return merged


L1 = [1, 2, 3, 5, 7]
L2 = [2, 4, 6, 8, 10]

p = merge_sorted_lists(L1, L2)
print(p)


## O(n + m) که هر کدام بیانگر طول ارایه ها اند 