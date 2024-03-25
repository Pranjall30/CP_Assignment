def mode(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    max_freq = max(freq.values())
    modes = [num for num in freq.keys() if freq[num] == max_freq]
    return modes[0] if len(modes) == 1 else modes[0] if len(modes) > 1 and modes[0] > 0 else modes[1]

arr = []
n = int(input("Enter the number of elements in the stream: "))
print("Min, Max, Sum, Average, Mode")
for i in range(n):
    num = int(input("Enter the number: "))
    arr.append(num)
    print("min, max, sum, average and mode after addition of %d is %d, %d, %d, %f, %d" % (num, min(arr), max(arr), sum(arr), sum(arr)/(i+1), mode(arr[:i+1])))