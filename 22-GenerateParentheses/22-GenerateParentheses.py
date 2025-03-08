class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # if (f(n-1)) or ()(n-1)
        res = []
        curr = ''

        # Start with 0 open and 0 close
        # Stop when all the open parantheses and close parenthesis is in place
        # If not put it recursively
        def recursivePar(open,close,curr):
            if len(curr) == n*2:
                res.append(curr)
                return
            
            if open < n:
                recursivePar(open+1, close, curr+'(')
            
            # CLOSE NEED TO BE PUT AFTER OPEN
            if close < open:
                recursivePar(open, close+1, curr+')')
            
        recursivePar(0,0,'')

        return res

            
            
        