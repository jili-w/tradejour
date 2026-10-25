from week1 import *

import pytest
import heapq


@pytest.mark.parametrize("nums, k, expected", [
    ([1,2,3,4,5], 2 , 4),
])
def test_kth_largest(nums: list[int], k: int, expected:int) -> None:
    assert kth_largest(nums,k) == expected


@pytest.mark.parametrize("nums, expected", [
    ([], 0),
    ([2,2,2,2], 1)
])
def test_empty_list_LUR(nums:list[int], expected:int) -> None:
    assert longest_unique_run(nums) == expected


@pytest.mark.parametrize("nums ,expected", [
    ([[1,2,3]], [1,2,3])
])
def test_k_sorted_list(nums: list[list[int]], expected: list[int]) -> None:
    assert merge_k_sorted(nums) == expected