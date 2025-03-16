if __name__ == '__main__' :
    #print("hello world")

    #f = open("data/song.txt", encoding='UTF-8')
    '''
    with open("data/song.txt", encoding='UTF-8') as f:
        for line in f.readlines():
            print(line, end="")
    '''

    '''
    list = [
        ['손흥민', 40, 'FW', 9],
        ['황희찬', 29, 'FW', 9],
        ['이강인', 30, 'MF', 8]
    ]
    '''

    list = [
        '손흥민,40,FW,9',
        '황희찬,29,FW,9',
        '이강인,30,MF,8'
    ]

    with open("soccerplayer.csv", "w") as f:
        f.write("\n".join(list))
        '''
        for onePlayer in list:
            f.write(onePlayer)
            f.write("\n")
        '''
