import pytest

from merge import Solution


testdata = [
    ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
    ([1], 1, [], 0, [1]),
    ([0], 0, [1], 1, [1]),
]


@pytest.mark.parametrize("nums1, m, nums2, n, expected", testdata)
def test_merge(nums1, m, nums2, n, expected):
    sol = Solution()
    sol.merge(nums1, m, nums2, n)

    assert nums1 == expected
