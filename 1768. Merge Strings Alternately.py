class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        w3 = ''
        i = 0

        if len(w1) == len(w2):

            for k in range(len(w1)):
                w3 = w3 + w1[i] + w2[i]
                i += 1

        else:
            # w1>w2
            if len(w1) > len(w2):
                for _ in range(len(w2)):
                    w3 = w3 + w1[i] + w2[i]
                    i += 1
                w3 += w1[i:]
            #w2>w1
            else:
                for _ in range(len(w1)):
                    w3 = w3 + w1[i] + w2[i]
                    i += 1
                w3 += w2[i:]
        return w3
