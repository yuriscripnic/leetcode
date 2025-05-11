class Solution:
    def reverse(self, x: int) -> int:
        sx = str(x)
        signal = 1

        if x < 0:
            sx = sx[1:]
            signal = -1

        res=0

        for i, v in enumerate(sx):
            res+= int(v) * 10**i
        fr = signal * res
        if  fr >= (-2**31)  and fr <= ((2**31) - 1):
            return fr
        else:
            return 0        
            

if __name__ == "__main__":

    s = Solution()
    print(s.reverse(321))
    print(s.reverse(-321))
    print(s.reverse(2**32))
    print(s.reverse(9534236469))