#!/usr/bin/env python3

import sys
import utils
from functions import Task


def main():
    argc = len(sys.argv)
    if argc != 10:
        utils.error('Missing command line argument.')
    else:
        if sys.argv[1] == '-h':
            print(utils.help())
        else:
            n1 = sys.argv[1]
            n2 = sys.argv[2]
            n3 = sys.argv[3]
            n4 = sys.argv[4]
            po = sys.argv[5]
            pw = sys.argv[6]
            pc = sys.argv[7]
            pb = sys.argv[8]
            ps = sys.argv[9]

            print("Resources: "+n1+" F1, "+n2+" F2, "+n3
            +" F3, "+n4+" F4\n\n")

            ### units function
            
            names = ["Oat","Wheat","Corn","Barley","Soy"]
            units = Task(n1,n2,n3,n4,po,pw,pc,pb,ps)
            
            for i in range(len(units)):
                print(names[i]+": "+units[i]+" at "+sys.argv[4+i]+"/unit")
                

            

            
 

if __name__ == '__main__':
    main()
  