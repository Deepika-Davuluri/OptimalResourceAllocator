import unittest
from resourceallocator import ResourceAllocator


class ResourceAllocatorTest(unittest.TestCase):

    def setUp(self):
        self.combinations = ResourceAllocator()

    def test_combinationSumWithNegativeSum(self):
        all_combos = self.combinations.machineCapacitySum([10, 20, 30], -10)
        self.assertEqual(None, all_combos)

    def test_combinationSumWithZeroSum(self):
        all_combos = self.combinations.machineCapacitySum([10, 20, 30], 0)
        self.assertEqual([[]], all_combos)

    def test_combinationSumWithNoneSum(self):
        all_combos = self.combinations.machineCapacitySum([10, 20, 30], None)
        self.assertEqual(None, all_combos)

    def test_combinationSumWithValidSum(self):
        all_combos = self.combinations.machineCapacitySum([10, 20, 40], 40)
        self.assertEqual(4, len(all_combos))