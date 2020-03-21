def reversePairs(nums):
    res = 0

    def merge_sort(nums):
        n = len(nums)
        if n <= 1:
            return nums
        s1 = merge_sort(nums[:n // 2])
        s2 = merge_sort(nums[n // 2:])
        return merge(s1, s2)

    def merge(s1, s2):
        nonlocal res
        i = j = 0
        while i < len(s1) and j < len(s2):
            if s1[i] > 2 * s2[j]:
                res += len(s1) - i
                j += 1
            else:
                i += 1
        return sorted(s1 + s2)

    merge_sort(nums)
    return res


nums = [2, 4, 3, 5, 0]
# print(reversePairs(nums))

nums.sort(key=lambda x: x)
print(nums)


def sortColors(nums):
    d = {0: 0, 1: 1, 2: 2}
    nums.sort(key=lambda x: d.get(x))


nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)
