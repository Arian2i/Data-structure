from itertools import permutations
"""
    کتابخانه‌ی itertools یکی از ماژول‌های استاندارد پایتون است.

permutations(iterable):

تمام جایگشت‌های ممکن از یک لیست را تولید می‌کند.

مثلاً permutations([1, 2, 3]) خروجی: (1,2,3), (1,3,2), (2,1,3), ...
    """


def is_valid_matrix(matrix):
    # بررسی مجموع سطرها
    for row in matrix:
        if sum(row) != 15:
            return False

    # بررسی مجموع ستون‌ها
    for col in range(3):
        if matrix[0][col] + matrix[1][col] + matrix[2][col] != 15:
            return False

    return True


def print_all_valid_matrices():
    count = 0
    for perm in permutations(range(1, 10)): # تولید جایگشت های عدد ۹ برای ساخت ماتریس دلخواه 
        # ساختن ماتریس ۳×۳
        matrix = [list(perm[i:i+3]) for i in range(0, 9, 3)]

        if is_valid_matrix(matrix):
            count += 1
            print(f"Matrix #{count}")
            for row in matrix:
                print(row)
            print("-" * 20)


print_all_valid_matrices()
