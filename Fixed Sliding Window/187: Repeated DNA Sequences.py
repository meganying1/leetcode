# https://leetcode.com/problems/repeated-dna-sequences/description/
# difficulty: medium
# topics: hash table, string, bit manipulation, sliding window, rolling hash, hash function

# problem:
# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
#   For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.
# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        length = len(s)
        if length <= 10: return []

        end = 9
        counts = defaultdict(int)
        valMap = {'A':1, 'C':2, 'G':3, 'T':4}
        ans = []
        hashVal = 0
        for i in range(10): hashVal = hashVal * 10 + valMap[s[i]]
        counts[hashVal] += 1

        while end+1 < length:
            hashVal = ((hashVal % 1000000000) * 10) + valMap[s[end+1]]
            end += 1
            if hashVal in counts and counts[hashVal] == 1: ans.append(s[end-9:end+1])
            counts[hashVal] += 1
        return ans
# recommend using start and end to represent range of window

"""
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        length = len(s)
        if length <= 10: return []

        end = 10
        counts = defaultdict(int)
        valMap = {'A':1, 'C':2, 'G':3, 'T':4}
        ans = []
        hashVal = 0
        for i in range(10): hashVal = hashVal * 10 + valMap[s[i]]
        counts[hashVal] += 1

        while end < length:
            hashVal = ((hashVal % 1000000000) * 10) + valMap[s[end]]
            end += 1
            counts[hashVal] += 1
            if counts[hashVal] == 2: ans.append(s[end-10:end])
        return ans
"""
# time complexity: O(n)
#     we slide over window of size n and each time we slide, we do math operations in constant time
# space complexity: O(n)
#     n space for the hashes since numbers only take n auxiliary space and are capped at certain size

# if numbers are very large, math operations become much slower, so we need to convert hashes to number smaller than cap
#     this creates hash collisions, so we don't have guarantee that if our hashes match, the strings match as well

# rolling hash converts time and space complexity of hasing and searching for a little string in a big text from O(n*m) to O(n+m)
#   technically O(n*m) worst case scenario because we still need to do a naive check in case of hash collisions, but we assume most substrings do not have same hash value

"""
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        start, end = 0, 10
        counts = defaultdict(int)
        while end <= len(s):
            substr = s[start:end]
            counts[substr] += 1
            start += 1
            end += 1
        return [substr for substr in counts if counts[substr] > 1]
"""
# time complexity: O(10n)
# space complexity: O(10n)

# in general, seraching for substring within string is O(n*m) time and space, where m is length of substring
# if length of string < 10^5, we need at least a linear solution
