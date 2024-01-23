class HelperFunctions:
    @staticmethod
    def compare_two_dimensional_arrays(
        expected: list[list[int]], actual: list[list[int]]
    ) -> bool:
        # Convert each list in the arrays to a set
        expected_sets = [set(subset) for subset in expected]
        actual_sets = [set(subset) for subset in actual]

        # Create sets of these sets to remove any duplicates and ensure order doesn't matter
        return set(map(frozenset, expected_sets)) == set(map(frozenset, actual_sets))
