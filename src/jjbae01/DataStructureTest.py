

if __name__ == "__main__" :

    '''
    a = []
    a.append(1)
    a.append(2)

    print(a)

    b = [1, 2, 3, 4]

    print(b)

    c = a + b

    print(c)
    '''

    d = {}
    d["name"] = "배재준"
    print(d)
    d["age"] = 17
    print(f"age:{d['age']}")
    print("age:%s" % d['age'])


    '''
    name     pos    age     hp      speed   kick
    손흥민    FW     33      80      80      90
    살라      FW     30      89      90      80     
         
    '''
    players = []

    # onePlayer = {
    #     "name": "손흥민",
    #     "pos": "FW",
    #     "age": "33",
    #     "hp": "80",
    #     "speed": "80",
    #     "kick": "90"
    # }
    #
    # onePlayer["name"] = "손흥민"

    players.append({
        "name" : "손흥민",
        "pos" : "FW",
        "age" : "33",
        "hp" : "80",
        "speed" : "80",
        "kick" : "90"})

    players.append({
        "name" : "살라",
        "pos": "FW",
        "age" : "30",
        "hp": "89",
        "speed" : "90",
        "kick" : "80"})

    print(players)

