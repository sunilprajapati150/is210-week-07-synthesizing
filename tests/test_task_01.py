#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 01."""


# Import Python libs
import unittest

# Import user libs
import data
import task_01


class Task01TestCase(unittest.TestCase):
    """Test cases for Task 01."""

    def standardize_output(self, output):
        """Standardizes output for comparison."""
        for index, elem in enumerate(output):
            output[index] = tuple(sorted(elem))
        return sorted(output)

    def test_matchup_count(self):
        """Tests that the count of matchups is correct, eg a half-cartesian."""
        expected = 153
        self.assertEqual(len(task_01.get_matches(data.VERSUS)), 153)

    def test_output(self):
        """Tests that matchups are output in the expected format."""
        expected = self.standardize_output([('Audrey', 'Able'),
                                            ('Axlerod', 'Audrey'),
                                            ('Able', 'Axlerod')])

        returned = task_01.get_matches(['Axlerod', 'Audrey', 'Able'])
        returned = self.standardize_output(returned)
        self.assertEqual(returned, expected)

if __name__ == '__main__':
    unittest.main()
