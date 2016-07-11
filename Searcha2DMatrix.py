#coding:gb2312
'''
leetcode: Search a 2D Matrix
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        '''
        row = len(matrix) - 1
        column = len(matrix[0]) - 1

        target_row = -1 #��ʾtarget�������ڵ���

        for i in range(len(matrix)):
            #target���ܳ�����ĳһ����
            if matrix[i][0] <= target <= matrix[i][column]:
                target_row = i
                break

        if target_row == -1:
            return False
        else:
            for j in range(column + 1):
                if matrix[target_row][j] == target:
                    return True
                elif matrix[target_row][j] > target:
                    return False
        '''
        row = len(matrix)
        column = len(matrix[0])

        if row > 0 and column > 0:
            # �Ӿ�������Ͻǿ�ʼѰ��
            curr_row = 0
            curr_column = column - 1
            while curr_row < row and curr_column >= 0:
                if target == matrix[curr_row][curr_column]:
                    return True
                elif target < matrix[curr_row][curr_column]: # ��ǰԪ������һ�е���Сֵ,���С�ڵĻ�,��˵��������һ��
                    curr_column -= 1
                else: # ��ǰԪ������һ�е����ֵ,������ڵĻ���˵��������һ��
                    curr_row += 1
        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 11))