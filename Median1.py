#git changes
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2,):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        res = nums1 + nums2
        sorted_res = sorted(res)
        n = len(sorted_res)
        if n%2==1:
            ans = sorted_res[n//2]
        else:
            ans = (sorted_res[n//2-1] + sorted_res[n//2])/2.0
        return ans
    

sol = Solution()
print(sol.findMedianSortedArrays([1,3], [2]))
print(sol.findMedianSortedArrays([1,2], [3,4]))
