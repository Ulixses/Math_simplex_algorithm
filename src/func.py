class simplex(object):
    def __init__(self, n1, n2, n3, n4, p1, p2, p3, p4, p5):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.p5 = p5


def matrix_print(data):
    for i in data:
        print(i)


# 1
def make_matrix(n1, n2, n3, n4, p1, p2, p3, p4, p5):
    matrix = [
        [1, 0, 1, 0, 2, 1, 0, 0, 0, 0, float(n1)],
        [1, 2, 0, 1, 0, 0, 1, 0, 0, 0, float(n2)],
        [2, 1, 0, 1, 0, 0, 0, 1, 0, 0, float(n3)],
        [0, 0, 3, 1, 2, 0, 0, 0, 1, 0, float(n4)],
        [float(-1) * float(p1), float(-1) * float(p2), float(-1) * float(p3),
         float(-1) * float(p4), float(-1) * float(p5), 0, 0, 0, 0, 1, 0]]
    return matrix


# 2-2
def sel_col(matrix, pivot_col_num):
    n = 0
    dummy = []
    while n < len(matrix) - 1:
        dummy.append(matrix[n][pivot_col_num])
        n += 1
    col = dummy

    return col


# 2-1
def find_max_neg_col(matrix):
    last_row = len(matrix) - 1
    my_max = 0
    n = 0
    pivot_col_num = 0
    for i in matrix[last_row]:
        if float(-1) * i > my_max:
            my_max = float(-1) * i
            pivot_col_num = n
        n += 1
    return pivot_col_num


# 3-1
def sel_pivot_row_num(col, matrix):
    n = 0
    pivot_pos = 0
    last_col = len(matrix[0]) - 1
    dummy = []
    # # print("---------------------------fix--------------------------")
    # print("col")
    # print(col)
    while n < len(matrix) - 1:
        # if matrix[n][last_col] != 0 and matrix[n][last_col] != 0.0 and col[n] != 0 and col[n] != 0.0:
        # if col[n] != 0 and col[n] != 0.0: # 변경 전
        if col[n] != 0 and col[n] != 0.0 and col[n] > 0:  # 변경 전
            # print(col[n])
            dummy.append((round(matrix[n][last_col] / col[n], 2), n))
        n = n + 1
    n = 0
    my_min = dummy[0][0]
    while n < len(dummy):
        if my_min > dummy[n][0]:
            my_min = dummy[n][0]
            pivot_pos = dummy[n][1]
        n = n + 1
    return pivot_pos


# 4-1
def pivot_one(pivot_row_num, matrix, pivot_col_num, pivot_ele):
    col_len = len(matrix[0]) - 1
    dummy = []
    for i in matrix[pivot_row_num]:
        dummy.append(round(i / pivot_ele, 2))
    matrix[pivot_row_num] = dummy
    return matrix


# 5-1
def make_other_zero(matrix_pivot_one, pivot_row_num, pivot_col_num):
    matrix = matrix_pivot_one
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
def loop_check_zero(matrix, already_pivot_cal_num):
    objective_row_num = len(matrix) - 1
    objective_row = matrix[objective_row_num]
    result = True
    print("objective row")
    print(objective_row)
    for index, value in enumerate(objective_row):
        for i in already_pivot_cal_num:
            if i == index:
                # print("result is true")
                # print(i,index)
                result = True
                break
            else:
                # print("result is false")
                # result = False
                break
    return result

    # dummy = my_del(already_pivot_cal_num, objective_row)
    # for ele in dummy:
    #     if ele < 0:
    #         print("negative ele")
    #         print(ele)
    #         print("loop start")
    #         return True
    #     else:
    #         return False

# # 6
# def loop_check_zero(matrix, already_pivot_cal_num):
#     objective_row_num = len(matrix) - 1
#     objective_row = matrix[objective_row_num]
#     dummy = my_del(already_pivot_cal_num, objective_row)
#     print("except already pivot col num")
#     print(dummy)
#     for ele in dummy:
#         if ele < 0:
#             print("negative ele")
#             print(ele)
#             print("loop start")
#             return True
#         else:
#             return False

# 6-2
# def my_del(already_pivot_col_num, objective_row):
# #     dummy = []
# #     for index, value in enumerate(objective_row):
# #         for i in already_pivot_col_num:
# #             if index != i:
# #                 continue
# #             else:
# #                 dummy.append(value)
# print(dummy)
# dummy2 = []
# for index, value in enumerate(objective_row):
#     for i in dummy:
#         if check(value, dummy):
#             break
#         else:
#             dummy2.append(index)
#             break
# print(dummy2)
#
# return dummy2


# 6-1
# def check(value, dummy):
#     result = True
#     for i in dummy:
#         if i == value:
#             result = True
#             break
#         else:
#             result = False
#     return result
