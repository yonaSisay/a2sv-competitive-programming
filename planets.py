N = int(input())

for i in range(N):
    dict_ = {}
    count = 0
    temp = list(map(int,input().split()))
    no_planet = temp[0]
    c = temp[1]
    planets = list(map(int,input().split()))
    for planet in planets:
        if planet in dict_:
            dict_[planet] += 1
        else:
            dict_[planet] = 1
    for key,value in dict_.items():
        if value<c:
            count +=value
        elif value == 1:
            count += 1
        elif value>=c:
            count += c
    print(count)
