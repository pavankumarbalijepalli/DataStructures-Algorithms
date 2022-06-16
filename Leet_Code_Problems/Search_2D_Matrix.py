# Question: https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)-1, -1, -1):
            if target >= matrix[i][0]:
                return (target in matrix[i])