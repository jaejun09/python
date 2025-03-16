import random
import time

def main():
    print("Hello World")

    countA = 0
    countB = 0
    countC = 0

    startTime = time.time()

    print("startTime : %.3f" % startTime)

    for i in range(10000000):
        num = random.randrange(1, 7)
        #print("[%s]:%s" % (i, num))

        '''
        if num % 2 == 0:
            print("짝수입니다")
        else:
            print("홀수입니다")

        if num % 3 == 0:
            print("A")
        elif num % 3 == 1:
            print("B")
        else:
            print("C")
        '''
        if num % 3 == 0:
            countA += 1
        elif num % 3 == 1:
            countB += 1
        else:
            countC += 1

    print("CountA = %s, CountB = %s, CountC = %s" % (countA, countB, countC))

    endTime = time.time()
    print("endTime : %.3f" % endTime)

    processTime = endTime - startTime
    print("processTime : %.3f" % processTime)

if __name__ == '__main__':
    main()