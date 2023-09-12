import numpy as np

def read_matrix_from_file(filename):
    with open("E:\KTLT\GTSCUOIKI\ketqua.txt", 'r') as file:
        lines = file.readlines()

    # Số ẩn là số hàng của ma trận
    n = len(lines)

    # Tạo mảng numpy kích thước n x n+1 và khởi tạo các phần tử bằng 0
    a = np.zeros((n, n+1))

    # Đọc hệ số của ma trận từ tệp tin
    for i in range(n):
        row = lines[i].split()
        for j in range(n+1):
            a[i][j] = float(row[j])

    return a

def PerformOperation(a, n):
    # Các bước thực hiện khử ma trận
    for i in range(n):
        if a[i][i] == 0:
            c = 1
            while i + c < n and a[i + c][i] == 0:
                c += 1
            if i + c == n:
                return 3  # Hệ vô nghiệm

            # Hoán đổi hàng i và hàng i+c
            a[[i, i + c]] = a[[i + c, i]]

        for j in range(n):
            if i != j:
                p = a[j][i] / a[i][i]
                a[j] = a[j] - a[i] * p

    return 1

def PrintResult(a, n, flag):
    if flag == 2:
        print("Vô số nghiệm")
    elif flag == 3:
        print("Vô nghiệm")
    else:
        print("Nghiệm của hệ phương trình:")
        for i in range(n):
            print(a[i][n] / a[i][i], end=" ")
        print()

def SolveEquations(filename):
    try:
        # Đọc ma trận từ file
        a = read_matrix_from_file(filename)
        n = a.shape[0]  # Số ẩn là số hàng của ma trận

        flag = PerformOperation(a, n)  # Khử ma trận

        if flag == 1:
            # Tính và in ra kết quả
            PrintResult(a, n, flag)
        else:
            # In thông báo vô nghiệm hoặc vô số nghiệm
            PrintResult(a, n, flag)

    except FileNotFoundError:
        print("File not found.")

# Nhập file đầu vào và giải hệ phương trình
filename = input("Nhập tên file: ")
SolveEquations(filename)
