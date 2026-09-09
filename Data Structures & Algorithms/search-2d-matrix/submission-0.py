class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start=0
        end=len(matrix)-1
        row=-1
        while(start<=end):
            mid=(start+end)//2
            if matrix[mid][0]<=target<=matrix[mid][-1]:
                row=mid
                break
            elif matrix[mid][0]<target:
                start=mid+1
            else:
                end=mid-1
        if row==-1:
            return False
        start_col=0
        end_col=len(matrix[0])-1
        while(start_col<=end_col):
            mid_col=(start_col+end_col)//2
            if matrix[row][mid_col]==target:
                return True
            elif matrix[row][mid_col]<target:
                start_col=mid_col+1
            else:
                end_col=mid_col-1
        return False