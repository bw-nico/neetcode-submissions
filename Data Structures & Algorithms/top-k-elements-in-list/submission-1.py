from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        num_map = defaultdict(int)
        for num in nums:
            num_map[num] += 1
        freq_list = [(freq, num) for num, freq in num_map.items()]

        # Sort the list by frequency in descending order
        freq_list.sort(key=lambda x: x[0], reverse=True)

        # Extract the top k frequent numbers
        return [num for _, num in freq_list[:k]]