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

        # 1
        matrix = func.make_matrix(n[0], n[1], n[2], n[3], po, pw, pc, pb, ps)
        # while loop
        while func.loop_check_zero(matrix):
            # 2
            pivot_col_num = func.find_max_neg_col(matrix)
            col = func.sel_col(matrix, pivot_col_num)
            # 3
            pivot_row_num = func.sel_pivot_row_num(col, matrix)
            # 4
            pivot_ele = matrix[pivot_row_num][pivot_col_num]
            func.pivot_one(pivot_row_num, matrix, pivot_col_num, pivot_ele)
            # 5
            func.make_other_zero(matrix, pivot_row_num, pivot_col_num)
        quantities = [0,0,0,0,0]
        for i in range(5):
            col = func.sel_col(matrix,i)
            if col.count(1) == 1 and col.count(0) == len(matrix) - 1:
                quantities[i] = round(matrix[col.index(1)][len(matrix[0]) - 1],3)
                if quantities[i] == 0:
                    quantities[i] = int(quantities[i])
        for i in range(len(names)):
            if quantities[i] == 0:
                print(names[i] , ": 0 units at $" , sys.argv[5 + i] , "/unit", sep='')
            else:
                print(names[i] , ": " , "{0:.2f}".format(quantities[i]), " units at $" , sys.argv[5 + i] , "/unit", sep='')
        total = 0
        for i in range(5):
            total +=  quantities[i] * float(sys.argv[5 + i])
        print("\nTotal production value:" + " ${0:.2f}".format(total))


if __name__ == '__main__':
    main()
