
# Leetcode 215. Kth Largest Element in an Array
#
# Problem Description:
# Given an integer array `nums` and an integer `k`, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Can you solve it without sorting?
#
# Constraints:
# *   `1 <= k <= nums.length <= 10^5`
# *   `-10^4 <= nums[i] <= 10^4`

from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        # To find k-th largest, use min-heap with size k
        # e.g. [1, ... k] with 1 is also root and k-th largest element, when 2 is inserted, 1 will be popped out because of fixed size k then [2, ...k]
        # 2 becomes new root and k-th largest element

        min_heap = nums[:k]
        heapq.heapify(min_heap)

        for n in nums[k:]:
            # we need to keep size fixed by ourself
            # root is first index, min_heap[0]
            if n > min_heap[0]:
                heapq.heappushpop(min_heap, n)
        return min_heap[0]