class Solution:
    def wordPatternMatch(self, pattern, s):
        mapping = {}
        used = set()

        def backtrack(p, start):
            if p == len(pattern):
                return start == len(s)

            char = pattern[p]

            if char in mapping:
                word = mapping[char]

                if not s.startswith(word, start):
                    return False

                return backtrack(p + 1, start + len(word))

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                if word in used:
                    continue

                mapping[char] = word
                used.add(word)

                if backtrack(p + 1, end):
                    return True

                del mapping[char]
                used.remove(word)

            return False

        return backtrack(0, 0)
