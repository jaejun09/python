
def main():
    with open("soccerplayer.csv", "r") as f :
        for one_line in f.readlines():
            print(one_line, end="")

if __name__ == '__main__':
    main()
