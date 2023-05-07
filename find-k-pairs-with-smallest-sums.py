class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []

        for  i in range(len(nums1)):
            for j in range(len(nums2)):
                temp = nums1[i] + nums2[j]
                if len(heap) < k:
                    heappush(heap, (-temp, (nums1[i], nums2[j])))
                elif -heap[0][0] > temp:
                    heapreplace(heap,(-temp, (nums1[i], nums2[j])))
                else:
                    break

        return [x[1] for x in heap]