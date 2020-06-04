"""

****************zip**************************
-make an iterator that aggregates elements from each of the iterables.
-returns an iterator of tuples, where the i-th tuple contains the i-th element
from each of the arguments sequences or iterables.
-the iterator stops when the shortest input iterable is exhausted 
"""
nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10]
z = zip(nums1, nums2)

print(dict(z))


nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10]
nums3 = [11, 12, 13, 14, 15]
z = zip(nums1, nums2, nums3)
print(list(z))

# note
# the iterables get matched with their index in the iterables being passed into the
# the zip function
# zip stops once the shortest iterable has been iterated

# the unpack operator can also be used with zip
