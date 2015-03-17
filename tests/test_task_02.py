#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for Task 02"""


# Import Python libs
import mock
import unittest
import task_02


class Task02TestCase(unittest.TestCase):
    """Test cases for Task 02"""

    def test_params(self):
        """Tests that login() has the correct required parameters."""
        msg = 'Parameters are incorrectly named, ordered, or (not) optional'
        with self.assertRaises(TypeError):
            task_02.login()

        with self.assertRaises(TypeError):
            task_02.login(maxattempts=0)

        self.assertFalse(task_02.login(username='blah', maxattempts=0), msg)

    def test_login_authentication(self):
        """Tests that login() can correctly authenticate a user."""
        with mock.patch('getpass.getpass', return_value='greed'):
            mock_stdin = mock.Mock()
            mock_stdin.isatty = mock.Mock()
            mock_stdin.isatty.return_value = True
            self.assertTrue(task_02.login('veruca'))

        with mock.patch('getpass.getpass', return_value='corruption'):
            mock_stdin = mock.Mock()
            mock_stdin.isatty = mock.Mock()
            mock_stdin.isatty.return_value = True
            self.assertFalse(task_02.login('veruca'))

    def test_login_attempts(self):
        """Tests that the number of allowed login attempts are enforced."""
        with mock.patch('getpass.getpass', return_value='greed'):
            mock_stdin = mock.Mock()
            mock_stdin.isatty = mock.Mock()
            mock_stdin.isatty.return_value = True
            self.assertFalse(task_02.login('veruca', 0))

        with mock.patch('getpass.getpass', side_effect=['', '', '', 'greed']):
            mock_stdin = mock.Mock()
            mock_stdin.isatty = mock.Mock()
            mock_stdin.isatty.return_value = True
            self.assertTrue(task_02.login('veruca', 4))


if __name__ == '__main__':
    unittest.main()
