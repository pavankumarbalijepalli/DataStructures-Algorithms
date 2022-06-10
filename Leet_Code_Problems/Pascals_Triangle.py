# Question: https://leetcode.com/problems/pascals-triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Base conditions
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        
        # Starting triangle being common for all
        out = [[1],[1,1]]
        
        # Since we have added 2 rows, we traverse till numRows from 2
        for i in range(2, numRows):
            
            # Each row starts with 1
            app = [1]
            
            # From 1 to rowNum
            for j in range(1, i):
                # In the last appended row, we add values from 'j-1' and 'j'.
                # Draw it on a paper, it will make a lot of sense. 
                # It is basically choosing left and right on top of the element in triangle
                app.append(out[-1][j-1] + out[-1][j])
            
            # Each row ends with 1
            app.append(1)
            
            # Add row to output array
            out.append(app)
        return out
