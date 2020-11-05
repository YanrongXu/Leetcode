class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # check if the solution can be negative
        is_negative = False
        if dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0:
            is_negative = True
            
        ans, count, tmp_divisor, tmp_dividend = 0, 1, abs(divisor), abs(dividend)
        
        while tmp_dividend >= tmp_divisor:
            # divisor keep multiple by two
            tmp_divisor = tmp_divisor << 1
            
            # if divisor after mulple by 2 is still smaller by,
            # we recored the count
            if tmp_divisor <= tmp_dividend:
                count = count << 1
            
            # elif divisor is bigger than dividend, we need to fallback, and record what preview multiple, and fallback the cont
            else:
                tmp_divisor = tmp_divisor >> 1
                tmp_dividend = tmp_dividend - tmp_divisor
                tmp_divisor = abs(divisor)
                ans += count
                count = 1
                
        if is_negative:
            ans = -ans
            
        if ans >= 1 << 31 :
            ans = (1 << 31) - 1
        
        return ans
