#!/usr/bin/env python3

import sys
import utils
import func


def main():
    argc = len(sys.argv)
    if argc != 10:
        if sys.argv[1] == '-h':
            print(utils.help())
        else:
            utils.error('Missing command line argument.')
    else:
        n = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]]
        po = sys.argv[5]
        pw = sys.argv[6]
        pc = sys.argv[7]
        pb = sys.argv[8]
        ps = sys.argv[9]

        print("Resources: " + n[0] + " F1, " + n[1] + " F2, " + n[2]
              + " F3, " + n[3] + " F4\n")

        names = ["Oat", "Wheat", "Corn", "Barley", "Soy"]

        #1
        matrix = func.make_matrix(n[0], n[1], n[2], n[3], po, pw, pc, pb, ps)
        # while 문
        # 2
        col = func.sel_col(matrix)
        # 3
        pivot_element = func.sel_pivot_pos(col,matrix)
        # 4

        # 5

        for i in range(len(names)):
            print(names[i] + ": " + " units at $" + sys.argv[5 + i] + "/unit")
        
        print("\nTotal production value:" + " $")


if __name__ == '__main__':
    main()
