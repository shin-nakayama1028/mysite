n = input().split(" ")
H = int(n[0])
W = int(n[1])
ans = []

for i in range(H):
    total = 0
    nums = input().split(" ")
    for num in nums:
        total += int(num)
    sum = total / 2
    total = 0
    for j in range(W):
        total += int(nums[j])
        if sum == total:
            ans.append("A" * (j + 1 ) + "B" * (W - j - 1))
            
if ans:
    print("Yes")
    for k in ans:
        print(k)
else:
    print("No")
            