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
def sel_col(matrix,col_num):
    n = 0
    dummy = []
    while n < len(matrix) - 1:
        dummy.append(matrix[n][col_num])
        n += 1
    col = dummy

    return col


# 2-1
def find_max_neg_col(matrix):
    last_row = len(matrix) - 1
    my_max = 0
    n = 0
    for i in matrix[last_row]:
        if float(-1) * i > my_max:
            my_max = float(-1) * i
            col_num = n
        n += 1
    return col_num


# 3-1
def sel_pivot_row_num(col, matrix):
    n = 0
    pivot_pos = 0
    col_num = len(matrix[0]) - 1
    dummy = []
    while n < len(matrix) - 1:
        if matrix[n][col_num] != 0 or col[n] != 0:
            dummy.append((matrix[n][col_num] / col[n], n))
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
def pivot_one(pivot_row_num, matrix,col_num,pivot_ele):
    col_len = len(matrix[0])-1
    dummy = []
    for i in matrix[pivot_row_num]:
        dummy.append(i/pivot_ele)
    matrix[pivot_row_num] = dummy
    return matrix


# 5-1
def make_zero():
    return 0