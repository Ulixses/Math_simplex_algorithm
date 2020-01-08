#!/usr/bin/env python3

import sys
sys.path.append('src/')
import utils
import func

def main():
    argc = len(sys.argv)
    if argc >= 2 and sys.argv[1] == '-h':
        print(utils.help())
    elif argc == 10:
        try:
            for i in range(1,10):
                if int(sys.argv[i]) < 0:
                    utils.error('Numbers must be >= 0')
        except ValueError:
            utils.error('Arguments must be numbers')
        #End of error checking
        print("Resources: " + n[0] + " F1, " + n[1] + " F2, " + n[2]+ " F3, " + n[3] + " F4\n")
        
        n = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]]
        po = sys.argv[5]
        pw = sys.argv[6]
        pc = sys.argv[7]
        pb = sys.argv[8]
        ps = sys.argv[9]

        

        names = ["Oat", "Wheat", "Corn", "Barley", "Soy"]

        pivot_col_num = 0
        # 1
        matrix = func.make_matrix(n[0], n[1], n[2], n[3], po, pw, pc, pb, ps)
        # while 문
        while func.loop_check_zero(matrix):
            print("1")
            print(func.loop_check_zero(matrix))
            # 2
            pivot_col_num = func.find_max_neg_col(matrix)
            col = func.sel_col(matrix, pivot_col_num)
            # 3
            pivot_row_num = func.sel_pivot_row_num(col, matrix)
            # 4
            pivot_ele = matrix[pivot_row_num][pivot_col_num]
            matrix_pivot_one = func.pivot_one(pivot_row_num, matrix, pivot_col_num, pivot_ele)
            # 5
            other_zero_matrix = func.make_other_zero(matrix_pivot_one,pivot_row_num,pivot_col_num)
            matrix = other_zero_matrix
            print("2")
            print(func.loop_check_zero(matrix))
            print("3")
        func.matrix_print(matrix)


        # for i in range(len(names)):
        #     print(names[i] + ": " + " units at $" + sys.argv[5 + i] + "/unit")
        #
        # print("\nTotal production value:" + " $")
    else:
        utils.error('Error: command line argument.')

if __name__ == '__main__':
    main()
