tool_quantity = int(input())
tools = input().split(" ")
[a, b] = input().split(" ")
money = int(a)
num = int(b)

for i in range(num):
    [c, d] = input().split(" ")
    purchase_tool = int(c) - 1
    purchase_quantity = int(d)
    
    total = int(tools[purchase_tool]) * int(d)
    if total < money:
        money -= total

print(money)
        