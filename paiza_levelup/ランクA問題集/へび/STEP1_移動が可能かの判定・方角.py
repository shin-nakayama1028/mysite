'''
★★★思考プロセス★★★
try-except の箇所で配列の添字にマイナス値が指定された時に「IndexError」
が起きると考えたため、その場合は例外をキャッチして「No」と出力しようと思っていた。

→以下の入力で実行してみるとエラーが起きず、「Yes」と出力された。
　配列の添字にマイナス値を指定すると
　「後ろから数えて何番目」かを指定できるらしい。
　今回の場合は、S[1][-1]は「.」のため、「Yes」と出力された。

入力値↓
--------------
5 7 1 0 W
##...#.
.......
#..#...
#...#.#
...#.#.
--------------

'''
#自作コード
H, W, y, x, direction = input().split(" ")
＃print("direction=", direction)
＃print("move前", y, x)
S =[list(input()) for _ in range(int(H))]

def move(x, y, direction):
    if direction == "N":
        y -= 1
    elif direction == "E":
        x += 1
    elif direction == "S":
        y += 1
    else:
        x -= 1
    return y, x

y, x = move(int(x), int(y), direction)
＃print("move後", y, x)
＃print(S[-1][0])
try:
    if S[y][x] == "#":
        print("No")
    elif S[y][x] == ".":
        print("Yes")
except Exception as e:
    print("No")

#回答コード
h, w, sy, sx, m = input().split()
s = [list(input()) for _ in range(int(h))]
sy = int(sy)
sx = int(sx)

if m == "N":
    sy -= 1
elif m == "E":
    sx += 1
elif m == "S":
    sy += 1
elif m == "W":
    sx -= 1

if sx < 0 or sx >= int(w) or sy < 0 or sy >= int(h) or s[sy][sx] == "#":
    print("No")
else:
    print("Yes")