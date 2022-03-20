

def scalar(a, b):
    try:
        num_a = len(a)
        num_b = len(b)
        if(num_a != num_b):
            raise BaseException("the two lists have different size")

        result = 0
        for i in range(num_a):
            result = result+a[i]*b[i]
        return(result)

    except BaseException as err:        # in case of any error
        print("Error = %s " % (err))
        return(None)


def row_by_col(a, b):
    try:
        row_a = len(a)
        col_a = len(a[0])
        row_b = len(b)
        col_b = len(b[0])

        print("row_A =", row_a,",col_A =", col_a)
        print("row_B =", row_b,",col_B =", col_b)
        if(row_a != col_b):
            raise BaseException("Row of A and Col of B have different size")

      
        result=[]                           #preallocate the result array
        for i in range(col_b):
            result.append([0]*col_b)
        #print (result)

        #result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

        # iterate through col of B
        for j in range(col_b):
            # iterate through row of A
            for i in range(row_a):
                # iterate through rows of B
                for k in range(row_b):
                    #old = result[i][j]
                    result[i][j] += a[i][k] * b[k][j]
                    #print("i=%d, j=%d, k=%d, oldval=%d, val=%d" % (i, j, k, old, result[i][j]))
                    #print("     ", result)
        return(result)

    except BaseException as err:        # in case of any error
        print("Error = %s " % (err))
        return(None)


list_a = [1, 2, 3, 4, 5]
list_b = [6, 7, 8, 9, 10]

print()
print("list_A=", list_a)
print("list_B=", list_b)
print("prodotto scalare = ", scalar(list_a, list_b))
print()

list_a = [1, 2, 3, 7]       #test for raise with error
list_b = [4, 5, 6]
print("list_A=", list_a)
print("list_B=", list_b)
print("prodotto scalare = ", scalar(list_a, list_b))
print()


matrix_a = [[2, 3], [4, 6], [1, 9], [5, 2]]
matrix_b = [[1, 6, 4, 2], [3, 7, 8, 1]]
print("matrix_A=", matrix_a)
print("matrix_B=", matrix_b)
print("prodotto riga colonna = ", row_by_col(matrix_a, matrix_b))
print()


matrix_a = [[2, 3], [4, 6], [1, 9], [5, 2]]     #test bad row col nuber
matrix_b = [[1, 6, 4, 2, 4], [3, 7, 8, 1, 7]]
print("matrix_A=", matrix_a)
print("matrix_B=", matrix_b)
print("prodotto riga colonna = ", row_by_col(matrix_a, matrix_b))
print()

matrix_a = [[2, 3], [4, 6], [1, 9], [5, 2]]     #test for raise with error
matrix_b = [[1, 6, 4, 2], [3, 7, 8,'f' ]]
print("matrix_A=", matrix_a)
print("matrix_B=", matrix_b)
print("prodotto riga colonna = ", row_by_col(matrix_a, matrix_b))
print()


