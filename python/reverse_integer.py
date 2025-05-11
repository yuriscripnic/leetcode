## optimized solution
"""
Reversing an integer can be done similarly to reversing a string.

We want to repeatedly "pop" the last digit off of x and "push" it to the back of the rev. In the end, rev will be the reverse of the x.

To "pop" and "push" digits without the help of some auxiliary stack/array, we can use math.

// pop operation:
pop = x % 10;
x /= 10;

// push operation:
temp = rev * 10 + pop;
rev = temp;
Luckily, it is easy to check beforehand whether or this statement would cause an overflow.
rev > INTMAX/10 then temp=rev⋅10+pop is guaranteed to overflow

"""


class Solution:
    ## My v3rsion
    
    def reverse_simple(self, x: int) -> int:
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


    def reverse(self, x: int) -> int:
        sign = [1, -1][x < 0] ## sign = 1 if x >= 0 else -1  True=1, False=0
        reverse_value, x = 0, abs(x)
        while x:
            x, mod = divmod(x, 10) ## Return the tuple (x//y, x%y). Invariant: div*y + mod == x., x == (x // y) * y + (x % y)
            reverse_value = reverse_value * 10 + mod
            if reverse_value > 2**31 - 1:
                return 0
        return sign * reverse_value
    
            

if __name__ == "__main__":
    print(Solution().reverse(321))
    print(Solution().reverse(-321))
    print(Solution().reverse(2**32))
    print(Solution().reverse(9534236469))