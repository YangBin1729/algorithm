__author__ = 'yangbin1729'

"""
递归示例：
关键概念：递归跟踪
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)



def draw_line(tick_length, tick_label=''):
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)


def draw_interval(center_length):
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)


def draw_ruler(num_inches, major_length):
    draw_line(major_length, '0')
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))

# draw_ruler(5, 5)


def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) //2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data, target, mid+1, high)


import os
def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)
    print('{0:<7}'.format(total), path)
    return total


import turtle
def drawSpiral(t, length, color, colorBase):

    if length == 0:
        return

    newcolor = (int(color[1:], 16) + 2**10) % (2**24)
    base = int(colorBase[1:], 16)

    if newcolor < base:
        newcolor = (newcolor + base) % (2**24)
    newcolor = hex(newcolor)[2:]

    newcolor = "#" + ("0" * (6 - len(newcolor))) + newcolor

    t.color(newcolor)
    t.forward(length)
    t.left(90)

    drawSpiral(t, length - 1, newcolor, colorBase)

def test_drawSpiral():
    t = turtle.Turtle()
    screen = t.getscreen()
    t.speed(10)
    t.penup()
    t.goto(-100, -100)
    t.pendown()

    drawSpiral(t, 200, "#000000", "#ff00ff")

    screen.exitonclick()


# test_drawSpiral()


# 4.14
def hanoi_tower(n, a, b, c):
    if n==1:
        print(a, '--->', c)
    else:
        hanoi_tower(n-1, a, c, b)
        print(a, '--->', c)
        hanoi_tower(n-1, b, a, c)

# hanoi_tower(5, 'A', 'B', 'C')



# 4.15
def subsets(s):
    if len(s) <= 1:
        return [s]
    i = s.pop()
    t = subsets(s)
    r = [{i}] + t
    for item in t:
        r.append(item.union({i}))
    return r

# s={1, 2, 3, 4}
# print(subsets(s))

# 4.16
def reverse(s):
    if len(s) <= 2:
        return s[-1] + s[0]
    return s[-1] + reverse(s[:-1])

# print(reverse('abcde'))

# 4.17
def is_palindrome(s):
    if len(s) <= 2:
        return s[-1] == s[0]
    return s[-1] == s[0] and is_palindrome(s[1:-1])

# print(is_palindrome('racecar'))
# print(is_palindrome('racecare'))
# print(is_palindrome('gohangasalamiimalasagnahog'))
# print(is_palindrome('gohangasalamiihmalasagnahog'))


# 4.18
def n_of_vowels(s):
    vowels = 'aeiou'

    if len(s) ==1:
        n = 1 if s[0] in vowels else 0
        return n

    t = n_of_vowels(s[:-1])
    n = 1 + t if s[-1] in vowels else t
    return n

# print(n_of_vowels('mike'))
# print(n_of_vowels('mikeioua'))
# print(n_of_vowels('m'))
# print(n_of_vowels('mb'))
# print(n_of_vowels('ab'))



"""如何迭代实现下面三题"""
# 4.19
def even_first(seq):
    n = len(seq)
    j = 0
    for i in range(n):
        if seq[i] % 2:
            seq[i], seq[j] = seq[j], seq[i]
            j += 1
    return seq

# print(even_first(list(range(10))))

# 4.20
def sort_by_k(seq, k):
    n = len(seq)
    j = 0
    for i in range(n):
        if seq[i] <= k:
            seq[i], seq[j] = seq[j], seq[i]
            j += 1
    return seq

# print(sort_by_k(list(range(10,0,-1)), 5))


# 4.21
def solve(seq, k):
    n = len(seq)
    results = []
    for i in range(n):
        left = k - seq[i]
        for j in range(i, n):
            if seq[j] == left:
                results.append((seq[i], seq[j]))
    return results

print(solve(list(range(10)), 10))


# 4.22
def pow(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result