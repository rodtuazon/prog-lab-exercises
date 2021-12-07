row_number = 10
print("Input number of rows:", row_number, "\n")
for i in range(1, row_number + 1):
    for j in range(1, i + 1):
        print(j, end='\n')
    print('\r')
