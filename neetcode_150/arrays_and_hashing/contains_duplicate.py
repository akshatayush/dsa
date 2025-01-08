from typing import List


def has_duplicate(nums: List[int]) -> bool:
    duplicate = None
    if len(nums) == len(set(nums)):
        duplicate = False
    else:
        duplicate = True
    return duplicate


if __name__ == "__main__":

    nums = [1, 2, 3, 3]
    print(has_duplicate(nums))
    nums = [1, 2, 3, 4]
    print(has_duplicate(nums))
