matrix = []
column_condition = None

while True:
    n = input().split()
    
    if n == ["-1"]:
        if not all(len(row) == column_condition for row in matrix):
            print("Invalid matrix")
            break

        num_rows = len(matrix)
        num_cols = len(matrix[0])

        transpose = []

        for i in range(num_cols):
            row = [0] * num_rows
            transpose.append(row)
        
        for i in range(num_cols):
            for j in range(num_rows):
                transpose[i][j] = matrix[j][i]
        
        for row in transpose:
            for x in row:
                print(x, end=" ")
            print()

        break
    
    else:
        row = [int(x) for x in n]
        matrix.append(row)
