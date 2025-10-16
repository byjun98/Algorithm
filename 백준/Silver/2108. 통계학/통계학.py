import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()

mean = round(sum(nums) / N)

median = nums[N // 2]

freq = {}
for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

max_freq = max(freq.values())
modes = []
for k in freq:
    if freq[k] == max_freq:
        modes.append(k)

modes.sort()
if len(modes) == 1:
    mode = modes[0]
else:
    mode = modes[1]

range_ = nums[-1] - nums[0]

print(mean)
print(median)
print(mode)
print(range_)
