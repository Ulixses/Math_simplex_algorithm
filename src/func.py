def matrix_print(data):
    for i in data:
        print(i)

# 1
def make_matrix(n1, n2, n3, n4, p1, p2, p3, p4, p5):
    matrix = [
        [1.0, 0.0, 1.0, 0.0, 2.0, 1.0, 0.0, 0.0, 0.0, 0.0, float(n1)],
        [1.0, 2.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, float(n2)],
        [2.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, float(n3)],
        [0.0, 0.0, 3.0, 1.0, 2.0, 0.0, 0.0, 0.0, 1.0, 0.0, float(n4)],
        [-float(p1), -float(p2), -float(p3), -float(p4), -float(p5), 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]]

    return matrix

# 2-1
def find_max_neg_col(matrix):
    last_row = len(matrix) - 1
    my_max = 0
    n = 0
    for i in matrix[last_row]:
        if -i > my_max:
            my_max = -i
            pivot_col_num = n
        n += 1
    return pivot_col_num

# 2-2
def sel_col(matrix, pivot_col_num):
    dummy = []
    for x in matrix:
        dummy.append(x[pivot_col_num])
    return dummy

# 3-1
def sel_pivot_row_num(col, matrix):
    n = 0
    pivot_pos = 0
    last_col = len(matrix[0]) - 1
    dummy = []
    while n < len(matrix) - 1:
        if col[n] > 0:
            dummy.append((round(matrix[n][last_col] / col[n], 2), n))
        n = n + 1
    n = 0
    my_min = dummy[0][0]
    pivot_pos = dummy[0][1]
    while n < len(dummy):
        if my_min > dummy[n][0]:
            my_min = dummy[n][0]
            pivot_pos = dummy[n][1]
        n = n + 1
    return pivot_pos

# 4-1
def pivot_one(pivot_row_num, matrix, pivot_col_num, pivot_ele):
    dummy = []
    print("pivot_ele :",pivot_ele)
    print("matrix_pivot_row_num",matrix[pivot_row_num])
    for i in matrix[pivot_row_num]:
        dummy.append(round((i / pivot_ele),2))
    print("dummy : ",dummy)
    matrix[pivot_row_num] = dummy

# 5-1
def make_other_zero(matrix, pivot_row_num, pivot_col_num):
    col_count = len(matrix[0])
    pivot = matrix[pivot_row_num][pivot_col_num]
    ele_row_num = 0
    # check whether each elements in pivot_col are 0  or not.
    while ele_row_num < len(matrix):
        ele = matrix[ele_row_num][pivot_col_num]
        if ele != 0 and ele_row_num != pivot_row_num:
            # if it is not 0
            if ele < 0:
                # if it is positive number
                if ele <= -100:
                    matrix_and_ele = plus_100(matrix, col_count, ele_row_num, pivot_row_num, pivot_col_num, ele)
                    matrix = matrix_and_ele[0]
                    ele = matrix_and_ele[1]
                    if ele <= -1:
                        matrix_and_ele = plus_1(matrix, col_count, ele_row_num, pivot_row_num, pivot_col_num,
                                                ele)
                        matrix = matrix_and_ele[0]
                        ele = matrix_and_ele[1]
                else:
                    if ele <= -1:
                        matrix_and_ele = plus_1(matrix, col_count, ele_row_num, pivot_row_num, pivot_col_num,
                                                ele)
                        matrix = matrix_and_ele[0]
                        ele = matrix_and_ele[1]
            elif ele > 0:
                if ele >= 100:
                    matrix_and_ele = minus_100(matrix, col_count, ele_row_num, pivot_row_num, pivot_col_num, ele)
                    matrix = matrix_and_ele[0]
                    ele = matrix_and_ele[1]
                    if ele >= 1:
                        matrix_and_ele = minus_1(matrix, col_count, ele_row_num, pivot_row_num, pivot_col_num,
                                                 ele)
                        matrix = matrix_and_ele[0]
                        ele = matrix_and_ele[1]
                else:
                    if ele >= 1:
                        matrix_and_ele = minus_1(matrix, col_count, ele_row_num, pivot_row_num, pivot_col_num,
                                                 ele)
                        matrix = matrix_and_ele[0]
                        ele = matrix_and_ele[1]
        ele_row_num += 1
    return matrix

# 5-1
def plus_100(matrix, col_count, ele_row_num, pivot_row_num, pivot_col_num, ele):
    while ele <= -100:
        dummy = []
        k = 0
        while k < col_count:
            dummy.append(round((matrix[ele_row_num][k] + 100 * matrix[pivot_row_num][k]), 2))
            k += 1
        matrix[ele_row_num] = dummy
        ele = matrix[ele_row_num][pivot_col_num]
    return matrix, ele

# 5-2
def plus_1(matrix, col_count, ele_row_num, pivot_row_num, pivot_col_num, ele):
    while ele <= -1:
        dummy = []
        k = 0
        while k < col_count:
            dummy.append(round((matrix[ele_row_num][k] + 1 * matrix[pivot_row_num][k]), 2))
            k += 1
        matrix[ele_row_num] = dummy
        ele = matrix[ele_row_num][pivot_col_num]
    return matrix, ele

# 5-3
def minus_100(matrix, col_count, ele_row_num, pivot_row_num, pivot_col_num, ele):
    while ele >= 100:
        dummy = []
        k = 0
        while k < col_count:
            dummy.append(round((matrix[ele_row_num][k] - 100 * matrix[pivot_row_num][k]), 2))
            k += 1
        matrix[ele_row_num] = dummy
        ele = matrix[ele_row_num][pivot_col_num]
    return matrix, ele

# 5-4
def minus_1(matrix, col_count, ele_row_num, pivot_row_num, pivot_col_num, ele):
    while ele >= 1:
        dummy = []
        k = 0
        while k < col_count:
            dummy.append(round((matrix[ele_row_num][k] - 1 * matrix[pivot_row_num][k]), 2))
            k += 1
        matrix[ele_row_num] = dummy
        ele = matrix[ele_row_num][pivot_col_num]
    return matrix, ele

# 6
def loop_check_zero(matrix):
    for x in matrix[len(matrix) - 1]:
        if x < 0:
            return True
    return False
