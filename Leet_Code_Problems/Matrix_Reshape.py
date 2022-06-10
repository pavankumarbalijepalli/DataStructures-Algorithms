# Question: https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # Capture original row, col length
        _or = len(mat)
        _oc = len(mat[0])
        
        # if the matrix reshape is not possible, return original matrix
        if _or*_oc != r*c:
            return mat
        
        # Output array - {0: (1 x _or) matrix, 1: (r x c) matrix}
        out = [[], []]
        
        # Add all rows side by side to get (1 x _or) matrix
        for i in range(_or):
            out[0] += mat[i]
        
        # For 'r' rows, 
        for i in range(r):
            
            # Append row with 'c' elements from out[0]
            out[1].append(out[0][:c]) 
            
            # Update out[0] with out[0] after 'c' elements
            out[0] = out[0][c:]
        
        # Since, out[0] is depleted, we return out[1]
        return out[1]
