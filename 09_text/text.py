__author__ = 'yangbin1729'

"""一、BF(Brute Force) 算法"""


def find_brute(T, P):
    n, m = len(T), len(P)
    for i in range(n - m + 1):
        k = 0
        while k < m and T[i + k] == P[k]:
            k += 1
        if k == m:
            return i
    return -1


"""二、BM（Boyer-Moore）算法"""


# 1. 坏字符规则（bad character rule）
def find_boyer_moore(T, P):
    n, m = len(T), len(P)
    if m == 0: return 0
    
    # 模式串中字符对应的索引，后面出现的会覆盖前面的：'abab'-->{'a':2, 'b':3}
    last = {}
    for k in range(m):
        last[P[k]] = k
    
    # 从模式串的末尾往前倒着匹配
    i = m - 1
    k = m - 1
    while i < n:
        if T[i] == P[k]:
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(T[i], -1)
            # 坏字符在模式串中的索引:
            # 不存在 j=-1 ， i = i + m
            # 位于 k 后方， i = i + m - (k+1) +1
            # 位于 k 前方， i = i + m - (j+1)
            i += m - min(k, j + 1)  # KEY：关键逻辑--> P 右移一位(m-k) 或 P 右移到
            k = m - 1
    return -1


# 单独的函数构建坏字符哈希表：
# 假设字符串的字符集不是很大，创建长 256 的数组表示，数组的下标对应字符的ASCII 码值
def generateBC(P):
    bc = [-1] * 256
    for i in range(len(P)):
        ind = ord(P[i])
        bc[ind] = i
    return bc


# TODO：2. 好后缀规则（good suffix shift）
def generateGS(P):
    """
    对于长度为 m 的模式串 P：
    suffix[k] 表示长度为 k 的后缀子串，在 P[:k] 中的索引；
    prefix[k] 表示长度为 k 的后缀子串与前缀子串是否相同。
    
    P = 'cabcab'
    后缀子串    长度   suffix          prefix
    b          1     suffix[1]=2     prefix[1]=False
    ab         2     suffix[2]=1     prefix[2]=False
    cab        3     suffix[3]=0     prefix[3]=True
    bcab       4     suffix[4]=-1    prefix[4]=False
    abcab      5     suffix[5]=-1    prefix[5]=False
    """
    m = len(P)
    prefix = [False] * m
    suffix = [-1] * m
    for i in range(m - 1):
        j = i
        k = 0  # 公共后缀子串的长度
        while j >= 0 and P[j] == P[m - 1 - k]:
            j -= 1
            k += 1
            suffix[k] = j + 1
        if j == -1:
            prefix[k] = True
    return prefix, suffix


def moveByGS(j, m, suffix, prefix):
    k = m - 1 - j  # 好后缀的长度
    if suffix[k] != -1:
        return j - suffix[k] + 1  # 模式串中存在该后缀子串
    for r in (j + 2, m):  # 遍历好后缀的后缀子串是否存在前缀子串
        if prefix[m - r]:
            return r
    return m


def boyer_moore_gs(S, P):
    """
    好后缀 M 的长度是 k，P[m-k:m]：
    suffix[k] != -1，模式串中存在该后缀子串，模式串移动 j-suffix[k]+1 位；
    否者，依次查找好后缀 M 长为 t(k-1 ~ 1之间) 的 prefix[t]=True，模式串后移 m-t 位
    都没有找到，则模式串移动 m 位
    """
    n = len(S)
    m = len(P)
    
    bc = generateBC(P)
    prefix, suffix = generateGS(P)
    
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0:
            if S[i + j] != P[j]:
                break  # 坏字符对应模式串的下标 j
            j -= 1
        
        if j < 0:
            return i  # 匹配成功
        
        x = j - bc[ord(S[i + j])]  # 坏字符的移动距离
        
        y = 0
        if j < m - 1:
            y = moveByGS(j, m, suffix, prefix)  # 好后缀的移动距离
        
        i = i + max(x, y)
    
    return -1


S = 'abcacabcbcbacabc'
P = 'cbacabc'


# TODO: 验证正确性！！！
# boyer_moore_gs(S, P)


# boyer_moore 方案2
class BoyerMooreSearch:
    
    def __init__(self, text, pattern):
        self.text, self.pattern = text, pattern
        self.textLen, self.patLen = len(text), len(pattern)
    
    def match_in_pattern(self, char):
        for i in range(self.patLen - 1, -1, -1):
            if char == self.pattern[i]:
                return i
        return -1
    
    def mismatch_in_text(self, currentPos):
        for i in range(self.patLen - 1, -1, -1):
            if self.pattern[i] != self.text[currentPos + i]:
                return currentPos + i
        return -1
    
    def bad_character_heuristic(self):
        positions = []
        for i in range(self.textLen - self.patLen + 1):
            mismatch_index = self.mismatch_in_text(i)
            if mismatch_index == -1:
                positions.append(i)
            else:
                match_index = self.match_in_pattern(self.text[mismatch_index])
                i = mismatch_index - match_index
        return positions


"""三、KMP（Knuth-Morris-Pratt）算法"""


# Knuth-Morris-Pratt 方案1
def compute_kmp_fail(P):
    m = len(P)
    fail = [0] * m
    j = 1
    k = 0
    while j < m:
        if P[j] == P[k]:
            fail[j] = k + 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k - 1]  # TODO: 这一步为什么？？？
        else:
            j += 1
    return fail


P = "abcdabd"
fail = "0000120"
print(compute_kmp_fail(P))


def find_kmp(T, P):
    n, m = len(T), len(P)
    if m == 0: return 0
    fail = compute_kmp_fail(P)
    j = 0
    k = 0
    while j < n:
        if T[j] == P[k]:
            if k == m - 1:
                return j - m + 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k - 1]
        else:
            j += 1
    return -1


# # Knuth-Morris-Pratt 方案2
# def get_failure_array(pattern):
#     failure = [0]
#     i = 0
#     j = 1
#     while j < len(pattern):
#         if pattern[i] == pattern[j]:
#             i += 1
#         elif i > 0:
#             i = failure[i - 1]
#             continue
#         j += 1
#         failure.append(i)
#     return failure
#
#
# def kmp(pattern, text):
#     failure = get_failure_array(pattern)
#     i, j = 0, 0
#     while i < len(text):
#         if pattern[j] == text[i]:
#             if j == len(pattern) - 1:
#                 return True
#             j += 1
#         elif j > 0:
#             j = failure[j - 1]
#             continue
#         i += 1
#     return False
#


# def test():
#     T = 'There is a simple example'
#     P = 'example'
#     print(find_boyer_moore(T, P))
#
#     text = "ABAABA"
#     pattern = "AB"
#     bms = BoyerMooreSearch(text, pattern)
#     positions = bms.bad_character_heuristic()
#
#     if len(positions) == 0:
#         print("No match found")
#     else:
#         print("Pattern found in following positions: ")
#     print(positions)
#


def prefix_table(P):
    """
    table[i] 表示 P 的前 i 个字符组成的子串，其前缀子串 等于 后缀子串 时的最大长度：
    P = "ababc"
    i = 4 时：
    子串 "abab" 的前缀子串 "aba" != 后缀子串 "bab"，但前缀子串 "ab" == 后缀子串 "ab"， 故 table[i] = 2
    i = 3 时：
    子串 "aba" 的前缀子串 "ab" != 后缀子串 "ba"，但前缀子串 "a" == 后缀子串 "a"， 故 table[i] = 1
    i = 2 时：
    子串 "ab" 的前缀子串 "a" != 后缀子串 "b"， 故 table[i] = 0
    i = 1 时：
    子串 "a" ，没有前缀子串和后缀子串， 故 table[i]=0
    """
    n = len(P)
    table = [-1] * n
    
    for i in range(1, n):
        prefix = P[:i]
        for k in range(i - 1, -1, -1):
            if prefix[:k] == prefix[i - k:]:
                table[i] = k
                break
    
    return table


print(prefix_table(P))


def find(s, p):
    table = prefix_table(p)
    
    m = len(p)
    n = len(s)
    i = j = 0
    while i <= n:
        if s[i] == p[j]:
            i += 1
            j += 1
            if j == m:
                return i - j
        else:
            if table[j] == -1:
                i += 1
                j = 0
            else:
                j = table[j]
    
    return -1


print(find("abaacababcbc", 'ababc'))


