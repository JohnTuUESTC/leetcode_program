#coding:gb2312

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if (len(nums1) + len(nums2)) % 2 == 1:
            return self.find(nums1, -1, nums2, -1, (len(nums1) + len(nums2)) / 2 + 1)
        else:
            return (self.find(nums1, -1, nums2, -1, (len(nums1) + len(nums2)) / 2) + float(self.find(nums1, -1, nums2, -1, (len(nums1) + len(nums2)) / 2 + 1))) / 2

    # ��nums1��nums2��Ѱ�ҳ���k�����
    def find(self, nums1, start_1, nums2, start_2, k):

        if len(nums1) - start_1 > len(nums2) - start_2:
            return self.find(nums2, start_2, nums1, start_1, k)

        if len(nums1) == 0:
            return nums2[start_2 + k]

        if start_1 == len(nums1) - 1:
            return nums2[start_2 + k]

        if k == 1:
            return min(nums1[start_1 + 1], nums2[start_2 + 1])

        # �Ƚ�����������k/2��λ��Ԫ�صĴ�С
        k_1 = start_1 + k/2

        if k_1 >= len(nums1):
            k_1 = len(nums1) - 1

        k_2 = start_2 + k - (k_1 - start_1)

        # ˵��nums1��start_1��k_1���ֶ���ǰk������
        if nums1[k_1] < nums2[k_2]:
            return self.find(nums1, k_1, nums2, start_2, k - (k_1 - start_1))
        elif nums1[k_1] > nums2[k_2]:
            return self.find(nums1, start_1, nums2, k_2, k - (k_2 - start_2))
        else:
            return nums1[k_1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.findMedianSortedArrays([], [1,2,3,4,5]))