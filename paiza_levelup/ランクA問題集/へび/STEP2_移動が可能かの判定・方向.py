h, w, sy, sx, d, m = input().split()
s = [list(input()) for _ in range(int(h))]
sy = int(sy)
sx = int(sx)
directions = ["N", "E", "S", "W"]
now = directions.index(d)

'''
方角を配列で保持している場合、
どの方向を向いてたとしても、その方角に対して左を向くためには添字を+3
　例）北向いている時の左は「西」　（「北」→東→南→「西」）
　　　西向いている時の左は「南」　（「西」→北→東→「南」）
逆に、どの方向を向いてたとしても、その方角に対して右を向くためには添字を+1
　例）東向いている時の右は「南」　（「東」→「南」）
　　　西向いている時の右は「北」　（「西」→「北」）
'''

if m == "L":
    now = (3 + now) % 4
else:
    now = (1 + now) % 4


if directions[now] == "N":
    sy -= 1
elif directions[now] == "E":
    sx += 1
elif directions[now] == "S":
    sy += 1
elif directions[now] == "W":
    sx -= 1

if sx < 0 or sx >= int(w) or sy < 0 or sy >= int(h) or s[sy][sx] == "#":
    print("No")
else:
    print("Yes")