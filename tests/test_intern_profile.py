"""Tests for the intern profile module."""

import contextlib
import io
import unittest
 
from src import intern_profile


class InternProfileTests(unittest.TestCase):
    def test_formatted_profile_contains_required_fields(self):
        text = intern_profile.format_profile()
        self.assertIn(f"Name: {intern_profile.INTERN_NAME}", text)
        self.assertIn(f"Role: {intern_profile.ROLE}", text)
        self.assertIn(f"Department: {intern_profile.DEPARTMENT}", text)
        self.assertIn("Skills: " + ", ".join(intern_profile.SKILLS), text)

    def test_print_profile_outputs_formatted_profile(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            intern_profile.print_profile()
        self.assertEqual(output.getvalue().strip(), intern_profile.format_profile())


if __name__ == "__main__":
    unittest.main()
