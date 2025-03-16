'''
처음 짜 보는 파이썬입니다.
'''

def printHelloWorld():
    print('Hello World')

def printGreeting():
    print('안녕하세요')
    
def printSong():
    a = """
        동해물과 백두산이
        마르고 닳도록
        하나님이 보우하사
        우리나라 만세"""
    
    print(len(a))
    
def printList():
    a = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
    #print(a[2:])
    #print(len(a))

    a.append('fff')
    
    b = a[:2] + a[3:]
    print(b)
    
def printDict():
    a = {
        '1': 'aaa',
        '2': 'bbb',
        '3': 'ccc'
    }
    
    a['4'] = 'ddd'
    
    #print(a)
    print (a['3'])

def printTuple():
    a = (1, 2, 3)

    print("a:%s, a.type:%s" % (a, type(a)))

if __name__ == '__main__':
    ''' 
    printHelloWorld()
    printGreeting()
    printSong()
    '''
    printList()
    printDict()
    printTuple()