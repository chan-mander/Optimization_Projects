import scipy as sp
import numpy as np


def cal_A(n, pr, pc, gr, gc):

    A = np.zeros((n*n, n*n))

    # for i in range(len(A)):

    #     if(i != (gr*n)+gc):
    #         if(i == 0):
    #             A[i][i] = -2
    #             A[i][i+1] = 1
    #             A[i][i+n] = 1
    #         elif(i == n-1):
    #             A[i][i] = -2
    #             A[i][i-1] = 1
    #             A[i][i+n] = 1
    #         elif(i == ((n-1)*n)):
    #             A[i][i] = -2
    #             A[i][i+1] = 1
    #             A[i][i-n] = 1
    #         elif(i == ((n-1)*n)+ (n-1)):
    #             A[i][i] = -2
    #             A[i][i-1] = 1
    #             A[i][i-n] = 1
    #         elif(i < n):
    #             A[i][i]=-3
    #             A[i][i+1]=1
    #             A[i][i-1]=1
    #             A[i][i+n]=1
    #         elif(n*(n-1) < i and i < (n*n)-1):
    #             A[i][i]=-3
    #             A[i][i+1]=1
    #             A[i][i-1]=1
    #             A[i][i-n]=1
    #         elif(i%n == 0 ):
    #             A[i][i]=-3
    #             A[i][i+1]=1
    #             A[i][i+n]=1
    #             A[i][i-n]=1
    #         elif(i%n == n-1):
    #             A[i][i]=-3
    #             A[i][i-1]=1 
    #             A[i][i+n]=1
    #             A[i][i-n]=1
    #         else:
    #             A[i][i]=-4
    #             A[i][i+1]=1 
    #             A[i][i-1]=1 
    #             A[i][i+n]=1
    #             A[i][i-n]=1


    #     print(A[i])
    
    for i in range((pr*n)+pc):

        if(i != (gr*n)+gc):
            if(i == 0):
                A[i][i] = -2
                A[i][i+1] = 1
                A[i][i+n] = 1
            elif(i == n-1):
                A[i][i] = -2
                A[i][i-1] = 1
                A[i][i+n] = 1
            elif(i == ((n-1)*n)):
                A[i][i] = -2
                A[i][i+1] = 1
                A[i][i-n] = 1
            elif(i == ((n-1)*n)+ (n-1)):
                A[i][i] = -2
                A[i][i-1] = 1
                A[i][i-n] = 1
            elif(i < n):
                A[i][i]=-3
                A[i][i+1]=1
                A[i][i-1]=1
                A[i][i+n]=1
            elif(n*(n-1) < i and i < (n*n)-1):
                A[i][i]=-3
                A[i][i+1]=1
                A[i][i-1]=1
                A[i][i-n]=1
            elif(i%n == 0 ):
                A[i][i]=-3
                A[i][i+1]=1
                A[i][i+n]=1
                A[i][i-n]=1
            elif(i%n == n-1):
                A[i][i]=-3
                A[i][i-1]=1 
                A[i][i+n]=1
                A[i][i-n]=1
            else:
                A[i][i]=-4
                A[i][i+1]=1 
                A[i][i-1]=1 
                A[i][i+n]=1
                A[i][i-n]=1


    for i in range((pr*n)+pc, len(A)):

        if(i != (gr*n)+gc):
            if(i == 0):
                A[i][i] = -2
                A[i][i+1] = 1
                A[i][i+n] = 1
            elif(i == n-1):
                A[i][i] = -2
                A[i][i-1] = 1
                A[i][i+n] = 1
            elif(i == ((n-1)*n)):
                A[i][i] = -2
                A[i][i+1] = 1
                A[i][i-n] = 1
            elif(i == ((n-1)*n)+ (n-1)):
                A[i][i] = -2
                A[i][i-1] = 1
                A[i][i-n] = 1
            elif(i < n):
                A[i][i]=-3
                A[i][i+1]=1
                A[i][i-1]=1
                A[i][i+n]=1
            elif(n*(n-1) < i and i < (n*n)-1):
                A[i][i]=-3
                A[i][i+1]=1
                A[i][i-1]=1
                A[i][i-n]=1
            elif(i%n == 0 ):
                A[i][i]=-3
                A[i][i+1]=1
                A[i][i+n]=1
                A[i][i-n]=1
            elif(i%n == n-1):
                A[i][i]=-3 
                A[i][i-1]=1 
                A[i][i+n]=1
                A[i][i-n]=1
            else:
                A[i][i]=-4
                A[i][i+1]=1 
                A[i][i-1]=1 
                A[i][i+n]=1
                A[i][i-n]=1

    return A


def main():
    print("The size of the board is N x N ")
    n = int(input("N = " ))

    print("input player position")
    p_row = int(input("Enter the row (0 to {}): ".format(n - 1)))
    p_column = int(input("Enter the column (0 to {}): ".format(n - 1)))

    print("input goal position")
    g_row = int(input("Enter the row (0 to {}): ".format(n - 1)))
    g_column = int(input("Enter the column (0 to {}): ".format(n - 1)))

    A = 1/4 * cal_A(n, p_row, p_column, g_row, g_column)
    b = -np.ones((9,1))
    b[(g_row*n)+g_column]=0
    c = np.ones((9,1))

    res = sp.optimize.linprog(c, A_ub=A, b_ub=b)
    print(res.x)
    

if __name__ == '__main__':
    main()