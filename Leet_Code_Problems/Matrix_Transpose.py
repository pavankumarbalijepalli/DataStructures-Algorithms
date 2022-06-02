# Question: https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # Kind of self explanatory. We go through columns, and pick y. The go through rows, and pick x. 
        # We return matrix with [y][x] which will reverse the row and column
        return [[matrix[y][x] for y in range(len(matrix))] for x in range(len(matrix[0]))]
