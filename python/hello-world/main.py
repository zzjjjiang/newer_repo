def main():
    str = int(input("Enter a number(1-10) "))
    if 1 < str < 10:
        for i in range(str):
            print("Hello World")
    else:
        print("input out of range")


if __name__ == '__main__':
    main()