class Operation:

    def addition(my_list):
        add = 0
        for i in my_list:
            add += i
        print(add)

    def subtraction(my_list):
        sub = 0
        sub = my_list[0]
        for i in my_list[1:]:
            sub -= i
        print(sub)


class Obtain:

    def user_input():
        input_new = []
        input_list = input(
            "Enter series of numbers [Example: 1,2,3,...]: ").split(',')
        for i in input_list:
            if i.isdigit():
                input_new.append(float(i))
            else:
                print("Could not convert string to float: ", i)
        return input_new


if __name__ == "__main__":
    print("------------------------------")
    print("-C--A--L--C--U--L--A--T--O--R-")

    print("------------------------------")
    print("Choose an operation\n[1] - Addition\n[2] - Subtraction")
    print("------------------------------")

choice = input("Input choice from 1-2: ")
my_list = Obtain.user_input()

if choice == '1':
    Operation.addition(my_list)
elif choice == '2':
    Operation.subtraction(my_list)
