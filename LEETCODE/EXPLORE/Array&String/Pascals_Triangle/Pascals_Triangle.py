class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            line = []
            if i == 0:
                line.append(1)
            else:
                for j in range(i+1):
                    if j == 0:
                        line.append(triangle[i-1][j])
                    elif j == i:
                        line.append(triangle[i-1][j-1])
                    else:
                        line.append(triangle[i-1][j-1] + triangle[i-1][j])

            triangle.append(line)

        return triangle
