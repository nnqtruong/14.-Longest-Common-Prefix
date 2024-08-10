class Solution:
    def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""

    # Sort the string alphabetically of the strings
    maxstr = max(strs)
    minstr = min(strs)

    # The shortest string is the longest possible common prefix
    length = min(len(maxstr),len(minstr))
    for i in range(length):
        
