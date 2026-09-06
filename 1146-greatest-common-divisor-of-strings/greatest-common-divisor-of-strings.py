class Solution(object):

    def gcdOfStrings(self, str1, str2):

        if str1 + str2 != str2 + str1:
            return ""

        for i in range(min(len(str1), len(str2)), 0, -1):

            word = str1[:i]

            if len(str1) % i != 0 or len(str2) % i != 0:
                continue

            if word * (len(str1) // i) == str1 and word * (len(str2) // i) == str2:
                return word

        return ""
        