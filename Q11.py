class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        sum_n = n * (n + 1) // 2  # Expected sum of first n natural numbers
        sum_sq_n = (n * (n + 1) * (2 * n + 1)) // 6  # Expected sum of squares
        
        sum_actual, sum_sq_actual = 0, 0
        
        for num in A:
            sum_actual += num
            sum_sq_actual += num * num
        
        # Let X be the missing number and Y be the repeated number
        diff1 = sum_actual - sum_n  # Y - X
        diff2 = (sum_sq_actual - sum_sq_n) // diff1  # (Y^2 - X^2) / (Y - X) = Y + X
        
        Y = (diff1 + diff2) // 2
        X = Y - diff1
        
        return [Y, X]
