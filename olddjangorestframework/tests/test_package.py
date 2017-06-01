"""Tests for the olddjangorestframework package setup."""
from django.test import TestCase
import olddjangorestframework

class TestVersion(TestCase):
    """Simple sanity test to check the VERSION exists"""

    def test_version(self):
        """Ensure the VERSION exists."""
        olddjangorestframework.VERSION

