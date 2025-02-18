class Solution:
    def smallestNumber(self, pattern: str) -> str:

        def check_if_consistent_with_pattern(combination, pattern):
            idx = 0
            for c in pattern:
                if c == 'I':
                    if combination[idx] > combination[idx+1]:
                        return False
                else:
                    if combination[idx] < combination[idx+1]:
                        return False
                idx += 1
            return True


                    
        possible_digit = ['1','2','3','4','5','6','7','8','9']
        n = len(pattern)
        for digit in itertools.permutations(possible_digit, n+1):
            # print(digit)
            if check_if_consistent_with_pattern(digit, pattern):
                break
        return ''.join(digit)
