#自作コード
line = input().split(" ")
H = int(line[0])
W = int(line[1])
N = int(line[2])

banmen2 = []


for i in range(H):
    line2 = list(input())
    #print("line2=", line2)
    banmen1 = []
    for j in line2:
        banmen1.append(j)
        #print("banmen1=", banmen1)
    banmen2.append(banmen1)
    #print("banmen2=", banmen2)
    
for k in range(N):
    line3 = input().split(" ")
    #print("line3=", line3)
    position_X = int(line3[0])
    position_Y = int(line3[1])
    
    print(banmen2[position_X][position_Y])

#回答コード
H, W, N = map(int, input().split())
S = [list(input()) for _ in range(H)]
for _ in range(N):
  y, x = map(int, input().split())
  print(S[y][x])