class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if len(matrix) == 0:
            return res
        c = 0
        while True:
            if c == len(matrix[0]) - c:
                break
            res += matrix[c][c:len(matrix[0]) - c]
            
            if c == len(matrix) - 1 - c:
                break
            for i in range(c + 1, len(matrix) - c):
                res.append(matrix[i][len(matrix[0]) - 1 - c])
            
            if len(matrix[0]) - 1 - c == c:
                break
            for i in range(len(matrix[0]) - 2 - c, c - 1, -1):
                res.append(matrix[len(matrix) - 1 - c][i])
            
            if len(matrix) - 2 - c == c:
                break
            for i in range(len(matrix) - 2 - c, c, -1):
                res.append(matrix[i][c])
            c += 1
        return res