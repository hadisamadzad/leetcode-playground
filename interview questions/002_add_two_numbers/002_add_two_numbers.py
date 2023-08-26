https://leetcode.com/problems/add-two-numbers/?envType=featured-list&envId=top-interview-questions

from typing import Optional

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]):

    l1: Optional[str] = [2,4,3]
    l2

    n = len(nums)
    map_dict = {}

    for index, value in enumerate(nums):

        if not (value in map_dict):
            map_dict[value] = index

        for index in reversed(range(n)):
            diff = target - nums[index]
            if diff in map_dict and index != map_dict[diff]:
                return [map_dict[diff], index]


print(addTwoNumbers(nums=[2, 7, 11, 15], target=9))
