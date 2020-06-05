from unittest import TestCase
from Source.Condition import Condition


class TestCondition(TestCase):
    def setUp(self):
        self.cond = Condition("Test", 10, 5, 1, False)

    def test_set_max(self):
        self.assertEqual(self.cond.set_max(11), 11)
        self.assertEqual(self.cond.set_max(4), 4)
        self.assertEqual(self.cond.set_max(0), 0)
        self.assertEqual(self.cond.set_max(-1), 0)
        self.assertEqual(self.cond.set_max(10), 10)

    def test_set_current(self):
        self.assertEqual(self.cond.set_current(6), 6)
        self.assertEqual(self.cond.set_current(4), 4)

        self.assertEqual(self.cond.set_current(11), 10)
        self.cond.set_max(9)
        self.assertEqual(self.cond.current, 9)

        self.assertEqual(self.cond.set_current(-1), 0)

    def test_alt_current(self):
        self.assertEqual(self.cond.alt_current(1), 6)
        self.assertEqual(self.cond.alt_current(-1), 5)

        self.assertEqual(self.cond.alt_current(1, True), 6)
        self.assertEqual(self.cond.alt_current(1, False), 5)
        self.assertEqual(self.cond.alt_current(-1, True), 4)
        self.assertEqual(self.cond.alt_current(-1, False), 5)

        self.assertEqual(self.cond.alt_current(5, False), 0)
        self.assertEqual(self.cond.alt_current(1, False), 0)

        self.assertEqual(self.cond.alt_current(10, True), 10)
        self.assertEqual(self.cond.alt_current(1, True), 10)

    def test_get_alert_level(self):
        self.fail()

    def test_set_consume(self):
        self.assertEqual(self.cond.set_consume(-2, False), 2)
        self.assertEqual(self.cond.descend, True)

        self.assertEqual(self.cond.set_consume(1, False), 1)
        self.assertEqual(self.cond.descend, False)

        self.assertEqual(self.cond.set_consume(11, False), 11)
        self.assertEqual(self.cond.descend, False)

    def test_get_current_display(self):
        self.fail()

    def test_apply_consume(self):
        self.assertEqual(self.cond.apply_consume(), 6)
        self.assertEqual(self.cond.set_consume(5, False), 5)
        self.assertEqual(self.cond.descend, False)
        self.assertEqual(self.cond.apply_consume(), 10)

        self.assertEqual(self.cond.set_consume(2, True), 2)
        self.assertEqual(self.cond.descend, True)
        self.assertEqual(self.cond.apply_consume(), 8)
        self.assertEqual(self.cond.apply_consume(), 6)

        self.assertEqual(self.cond.set_consume(10, True), 10)
        self.assertEqual(self.cond.descend, True)
        self.assertEqual(self.cond.apply_consume(), 0)
