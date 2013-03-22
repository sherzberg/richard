import unittest
from richard.context_processors import duration, _pluralize


class PluralizeTest(unittest.TestCase):

    def test_pluralize(self):
        self.assertEquals("dragons", _pluralize("dragon", 0))
        self.assertEquals("dragon", _pluralize("dragon", 1))
        self.assertEquals("dragons", _pluralize("dragon", 5))


class DurationFilterTest(unittest.TestCase):

    def test_seconds(self):
        self.assertEquals("15 seconds", duration('15'))
        self.assertEquals("1 second", duration('1'))

    def test_minutes(self):
        self.assertEquals("1 minute, 1 second", duration('61'))
        self.assertEquals("1 minute", duration('60'))
        self.assertEquals("2 minutes", duration('120'))

    def test_hours(self):
        self.assertEquals("1 hour", duration('3600'))
        self.assertEquals("1 hour, 2 seconds", duration('3602'))
        self.assertEquals("2 hours", duration('7200'))
        self.assertEquals("2 hours, 2 minutes", duration('7320'))
        self.assertEquals("2 hours, 2 minutes, 1 second", duration('7321'))
        self.assertEquals("2 hours, 2 minutes, 2 seconds", duration('7322'))
