def main():
    for i in range(5):
        for i in range(5):
            print("*", end="")
        print()

def main2():
    for i in range(5):
        for j in range(i + 1):
            print("*", end="")
        print()

def main3():
    # 라인수 만큼 루프를 돈다.
    for i in range(5):
        # 라인별로 공백을 찍는다.
        for j in range(5 - (i + 1)):
            print(" ", end="")
        # 라인별로 *을 찍는다.
        for k in range(i + 1):
            print("*", end="")
        print()

def main4():
    # 라인수 만큼 루프를 돈다.
    for i in range(5):
        # 라인별로 공백을 찍는다.
        for k in range(i):
            print(" ", end="")
        # 라인별로 *을 찍는다.
        for j in range(5 - i):
            print("*", end="")
        print()

def main5():
    # 라인수 만큼 루프를 돈다.
    for i in range(10):
        for j in range(10):
            if (j == 4 or j == 5):
                if (i == 0 or i == 9):
                    print("*", end="")
                else:
                    print(" ", end="")
            else:
                print("*", end="")
        print()

def main6():
    loopNum = 20
    # 라인수 만큼 루프를 돈다.
    for i in range(loopNum):
        for j in range(loopNum):
            if (j < loopNum-i):
                print("*", end="")
            else:
                print(" ", end="")

        for j in range(loopNum):
            if (j < i):
                print(" ", end="")
            else:
                print("*", end="")
        print()

    for i in range(loopNum):
        for j in range(loopNum):
            if (i >= j):
                print("*", end="")
            else:
                print(" ", end="")

        for j in range(loopNum):
            if (j < (loopNum - (i + 1))):
                print(" ", end="")
            else:
                print("*", end="")
        print()

def main7():
    loopNum = 20
    # 라인수 만큼 루프를 돈다.
    num = 0
    for i in range(loopNum):
        for j in range(loopNum):
            # 앞쪽 별을 찍는다.
            if (j < (loopNum/2) - num):
                print("*", end="")

        for j in range(num):
            print(" ", end="")

        for j in range(num):
            print(" ", end="")

        for j in range(loopNum):
            # 뒤쪽 별을 찍는다.
            if (j < (loopNum/2) - num):
                print("*", end="")

        if i < (loopNum/2)-1:
            num += 1
        elif i >= (loopNum/2):
            num -= 1

        print()


if __name__ == "__main__":
    #main()
    #main2()
    #main3()
    #main4()
    #main5()
    #main6()
    main7()