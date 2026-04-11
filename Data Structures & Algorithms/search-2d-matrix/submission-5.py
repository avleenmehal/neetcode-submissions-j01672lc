class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = len(matrix) - 1
        j = len(matrix[0]) - 1

        print(i)
        print(j)
        top =0
        bottom = i
        mid = 0
        while top < bottom:
            mid = top + ((bottom-top) // 2)
            if matrix[mid][j] == target:
                return True
            elif matrix[mid][j] > target:
                bottom = mid
            else:
                top = mid +1
        # print("mid")
        # print(mid)
        i = top
        left = 0
        right = j 
        print(j)

        while left<= right:
            mid = left + ((right-left)//2)

            if matrix[i][mid] == target:
                return True
            elif matrix[i][mid] > target:
                right = mid -1
                print(right)
            else:
                left = mid +1
            
        return False
        