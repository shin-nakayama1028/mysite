#自作コード
H, W, y, x, N = map(int, input().split(" "))

directions = ["N", "E", "S", "W"]
S = [list(input()) for _ in range(H)]
now = 0

def move(input_d, distance, now, y, x):
    if input_d == "L":
        now = (now + 3) % 4
    else:
        now = (now + 1) % 4
    #print("途中経過★input_d, distance, now, y, x=", input_d, distance, now, y, x)
    
    flag = False
    for _ in range(int(distance)):
        bfore_y = y
        bfore_x = x
        if directions[now] == "N":
            y -= 1
        elif directions[now] == "E":
            x += 1
        elif directions[now] == "S":
            y += 1
        else:
            x -= 1
        #print("途中経過2★input_d, now, y, x=", input_d, now, y, x)
        
        if S[y][x] == "#" or y < 0 or y > H or x < 0 or x > W:
            y = bfore_y
            x = bfore_x
            flag = True
    
    if flag:
        print(y, x)
        print("Stop")
    
    print(y, x)

for i in range(N):
    input_d, distance = input().split(" ")
    #print("input_d, now, y, x=", input_d, now, y, x)
    move(input_d, distance, now, y, x)



#回答コード
h, w, sy, sx, n = input().split()
s = [list(input()) for _ in range(int(h))]
sy = int(sy)
sx = int(sx)
directions = ["N", "E", "S", "W"]
now = 0

for _ in range(int(n)):
    d_i, l_i = input().split()
    l_i = int(l_i)
    if d_i == "L":
        now = (3 + now) % 4
    else:
        now = (1 + now) % 4

    flag = False
    for i in range(l_i):
        if directions[now] == "N":
            sy -= 1
        elif directions[now] == "E":
            sx += 1
        elif directions[now] == "S":
            sy += 1
        elif directions[now] == "W":
            sx -= 1

        if sx < 0 or sx >= int(w) or sy < 0 or sy >= int(h) or s[sy][sx] == "#":
            flag = True
            if directions[now] == "N":
                sy += 1
            elif directions[now] == "E":
                sx -= 1
            elif directions[now] == "S":
                sy -= 1
            elif directions[now] == "W":
                sx += 1
            break

    print(sy, sx)
    if flag:
        print("Stop")
        break