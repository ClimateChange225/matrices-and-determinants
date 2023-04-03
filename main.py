from tabulate import tabulate
import pyfiglet


def main():
    matrices = {}
    print(pyfiglet.figlet_format("Welcome to the Matrixinator!", font="slant"))
    while True:
        print("\nMENU")
        print("1. Input matrix")
        print("2. Print matrix")
        print("3. Add matrices")
        print("4. Subtract matrices")
        print("5. Multiply matrices")
        print("6. Transpose matrix")
        print("7. Calculate determinant")
        print("8. Calculate adjoint")
        print("9. Quit")

        try:
            choice = int(input("Enter your choice: "))
            if choice not in range(1, 10):
                print("Please enter a valid choice (1-9)")
                continue

            if choice == 1:
                name = input("Enter the name of the matrix: ")
                order = input_order()
                matrix = matrix_input(order)
                matrices[name] = matrix
                print(f"Matrix '{name}' added successfully")

            elif choice == 2:
                name = input("Enter the name of the matrix: ")
                if name not in matrices:
                    print(f"Matrix '{name}' not found")
                    continue
                print_matrix(matrices[name])

            elif choice in range(3, 6):
                name1 = input("Enter the name of the first matrix: ")
                name2 = input("Enter the name of the second matrix: ")
                if name1 not in matrices or name2 not in matrices:
                    print("One or both of the matrices not found")
                    continue
                if choice == 3:
                    if len(matrices[name1]) != len(matrices[name2]) or len(matrices[name1][0]) != len(matrices[name2][0]):
                        print("Matrix dimensions do not match for addition")
                        continue
                    result = matrix_addition(matrices[name1], matrices[name2])
                elif choice == 4:
                    if len(matrices[name1]) != len(matrices[name2]) or len(matrices[name1][0]) != len(matrices[name2][0]):
                        print("Matrix dimensions do not match for subtraction")
                        continue
                    result = matrix_subtraction(matrices[name1], matrices[name2])
                else:
                    if len(matrices[name1][0]) != len(matrices[name2]):
                        print("Matrix dimensions do not match for multiplication")
                        continue
                    result = matrix_multiplication(matrices[name1], matrices[name2])
                name = input("Enter a name for the result matrix: ")
                matrices[name] = result
                print(f"Matrix '{name}' added successfully")

            elif choice == 6:
                name = input("Enter the name of the matrix: ")
                if name not in matrices:
                    print(f"Matrix '{name}' not found")
                    continue
                result = matrix_transpose(matrices[name])
                name = input("Enter a name for the result matrix: ")
                matrices[name] = result
                print(f"Matrix '{name}' added successfully")

            elif choice == 7:
                name = input("Enter the name of the matrix: ")
                if name not in matrices:
                    print(f"Matrix '{name}' not found")
                    continue
                if len(matrices[name]) != len(matrices[name][0]):
                    print("Determinant can only be calculated for square matrices")
                    continue
                result = matrix_determinant(matrices[name])
                print(f"Determinant of '{name}' is {result}")

            elif choice == 8:
                name = input("Enter the name of the matrix: ")
                if name not in matrices:
                    print(f"Matrix '{name}' not found")
                    continue
                if len(matrices[name]) != len(matrices[name][0]):
                    print("Adjoint can only be calculated for square matrices")
                    continue
                result = matrix_adjoint(matrices[name])
                name = input("Enter a name for the result matrix: ")
                matrices[name] = result
                print(f"Matrix '{name}' added successfully")

            elif choice == 9:
                print("Exiting program...")
                break

            else:
                print("Please enter a valid choice (8-9)")
                continue

        except ValueError:
            print("Please enter a valid integer choice (8-9)")
            continue



def input_order():
    rows=input("Enter the number of rows: ")
    columns=input("Enter the number of columns: ")
    while True:
        try:
            assert int(rows)>0
            assert int(columns)>0
            break
        except:
            print("Please enter an integer greater than zero")
            pass
    return (int(rows), int(columns))



def matrix_input(order):
    rows=order[0]
    columns=order[1]
    l1=[]
    for i in range(1, rows+1):
        l2=[]
        for j in range(1, columns+1):
            n=float(input(f'Enter a{i}{j}: '))
            l2.append(n)
        l1.append(l2)
    return l1



def print_matrix(matrix):
    for row in matrix:
        print('[', end='')
        for i in range(len(row)):
            if i < len(row) - 1:
                print(row[i], end=', ')
            else:
                print(row[i], end='')
        print(']')



def matrix_pretty_table(matrix):
    headers = [f'Column {i}' for i in range(1, len(matrix[0])+1)]
    table_data = []
    for i, row in enumerate(matrix, start=1):
        table_data.append([f'Row {i}'] + row)
    table = tabulate(table_data, headers=headers, tablefmt='orgtbl')
    print(table)



def matrix_addition(l1, l2):
    sum=[]
    for i, j in zip(l1, l2):
        sum1=[]
        for k in range(len(i)):
            sum1.append(i[k]+j[k])
        sum.append(sum1)
    return sum
 


def matrix_subtraction(l1, l2):
    difference=[]
    for i, j in zip(l1, l2):
        difference1=[]
        for k in range(len(i)):
            difference1.append(i[k]+((j[k])*(-1)))
        difference.append(difference1)
    return difference



def matrix_multiplication(l1, l2):
    result = [[0 for j in range(len(l2[0]))] for i in range(len(l1))]
    for i in range(len(l1)):
        for j in range(len(l2[0])):
            for k in range(len(l2)):
                result[i][j] += l1[i][k] * l2[k][j]
    return result



def matrix_transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transpose = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
    return transpose



def matrix_determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for i in range(n):
            submatrix = [row[:i] + row[i+1:] for row in matrix[1:]]
            sign = (-1) ** i
            cofactor = matrix[0][i]
            det += sign * cofactor * matrix_determinant(submatrix)
        return det



def matrix_cofactor(matrix):
    n = len(matrix)
    if n == 1:
        return [[1]]
    elif n == 2:
        return [[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]]
    else:
        matrix_cofactor = []
        for i in range(n):
            cofactor_row = []
            for j in range(n):
                minor = [row[:j] + row[j+1:] for row in (matrix[:i]+matrix[i+1:])]
                cofactor = (-1) ** (i+j) * matrix_determinant(minor)
                cofactor_row.append(cofactor)
            matrix_cofactor.append(cofactor_row)
        return matrix_cofactor



def matrix_adjoint(matrix):
    return matrix_transpose(matrix_cofactor(matrix))



if __name__=="__main__":
    main()