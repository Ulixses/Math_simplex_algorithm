#!/usr/bin/env python3

import sys
sys.path.append("src/")
import utils
import func

def main():
    argc = len(sys.argv)
    if argc != 10:
        if argc >= 2 and sys.argv[1] == '-h':
            print(utils.help())
        else:
            utils.error('Missing command line argument.')
    else:
        try:
            for i in range (1, 10):
                if float(sys.argv[i]) < 0:
                    utils.error('Arguments must be >= 0.')
        except ValueError:
            utils.error('Arguments must be numbers.')

        #End of error checking
        
        n = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]]
        po = sys.argv[5]
        pw = sys.argv[6]
        pc = sys.argv[7]
        pb = sys.argv[8]
        ps = sys.argv[9]
        print("Resources: " + n[0] + " F1, " + n[1] + " F2, " + n[2]+ " F3, " + n[3] + " F4\n")

        names = ["Oat", "Wheat", "Corn", "Barley", "Soy"]

        count = 0
        already_pivot_col = []
        # 1
        matrix = func.make_matrix(n[0], n[1], n[2], n[3], po, pw, pc, pb, ps)
        # while loop
        while func.loop_check_zero(matrix,already_pivot_col):
            print("before start")
            func.matrix_print(matrix)
            # print("during loop start check")
            # 2
            pivot_col_num = func.find_max_neg_col(matrix)
            print("pivot_col_num: ", pivot_col_num)
            if pivot_col_num == -1:
                break
            already_pivot_col.append(pivot_col_num)
            col = func.sel_col(matrix, pivot_col_num)
            # print("col")
            # print(col)
            # 3
            pivot_row_num = func.sel_pivot_row_num(col, matrix)
            print("pivot_row_num: ", pivot_row_num)
            # 4
            pivot_ele = matrix[pivot_row_num][pivot_col_num]
            matrix_pivot_one = func.pivot_one(pivot_row_num, matrix, pivot_col_num, pivot_ele)
            print("matrix_pivot_one")
            func.matrix_print(matrix_pivot_one)
            # 5
            other_zero_matrix = func.make_other_zero(matrix_pivot_one, pivot_row_num, pivot_col_num)
            matrix = other_zero_matrix
            print("five stage end")
            func.matrix_print(matrix)
            print("already pivot col")
            print(already_pivot_col)
            # print("during loop end check")
            # print(func.loop_check_zero(matrix))

            count += 1
            print("count : " , count)
        print("loop finish")
        func.matrix_print(matrix)

        # for i in range(len(names)):
        #     print(names[i] + ": " + " units at $" + sys.argv[5 + i] + "/unit")
        #
        # print("\nTotal production value:" + " $")


if __name__ == '__main__':
    main()
