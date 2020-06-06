from unittest import TestCase
from Source.Condition import Condition


class TestCondition(TestCase):
    def setUp(self):
        self.cond = Condition("Test", 10, 5, 1, False)

    def test_set_max_inc(self):
        self.assertEqual(self.cond.set_max(11), 11)

    def test_set_max_dec(self):
        self.assertEqual(self.cond.set_max(4), 4)

    def test_set_max_zero(self):
        self.assertEqual(self.cond.set_max(0), 0)

    def test_set_max_negative(self):
        self.assertEqual(self.cond.set_max(-1), 0)

    def test_set_max_low_high(self):
        self.assertEqual(self.cond.set_max(0), 0)
        self.assertEqual(self.cond.set_max(10), 10)

    def test_set_max_float(self):
        self.assertEqual(self.cond.set_max(10.5), 10.5)

    def test_set_current_inc(self):
        self.assertEqual(self.cond.set_current(6), 6)

    def test_set_current_dec(self):
        self.assertEqual(self.cond.set_current(4), 4)

    def test_set_current_inc_float(self):
        self.assertEqual(self.cond.set_current(5.5), 5.5)

    def test_set_current_over_max(self):
        self.assertEqual(self.cond.set_current(11), 10)

    def test_set_current_neg(self):
        self.assertEqual(self.cond.set_current(-1), 0)

    def test_alt_current_inc_add(self):
        self.assertEqual(self.cond.alt_current(1), 6)

    def test_alt_current_dec_neg(self):
        self.assertEqual(self.cond.alt_current(-1), 4)

    def test_alt_current_inc_true(self):
        self.assertEqual(self.cond.alt_current(1, True), 6)

    def test_alt_current_dec_false(self):
        self.assertEqual(self.cond.alt_current(1, False), 4)

    def test_alt_current_dec_true(self):
        self.assertEqual(self.cond.alt_current(-1, True), 4)

    def test_alt_current_inc_false(self):
        self.assertEqual(self.cond.alt_current(-1, False), 6)

    def test_alt_current_dec(self):
        self.assertEqual(self.cond.alt_current(5, False), 0)

    def test_alt_current_dec_neg_min(self):
        self.assertEqual(self.cond.alt_current(6, False), 0)

    def test_alt_current_inc(self):
        self.assertEqual(self.cond.alt_current(10, True), 10)

    def test_alt_current_inc_over(self):
        self.assertEqual(self.cond.alt_current(11, True), 10)

    def test_alt_current_inc_float(self):
        self.assertEqual(self.cond.alt_current(.5, True), 5.5)

    def test_get_alert_level(self):
        self.fail()

    def test_set_consume_inc_neg(self):
        self.assertEqual(self.cond.set_consume(-2, False), 2)
        self.assertEqual(self.cond.descend, True)

    def test_set_consume_inc_pos(self):
        self.assertEqual(self.cond.set_consume(1, False), 1)
        self.assertEqual(self.cond.descend, False)

    def test_set_consume_dec_pos(self):
        self.assertEqual(self.cond.set_consume(11, False), 11)
        self.assertEqual(self.cond.descend, False)

    def test_set_consume_zero_false(self):
        self.assertEqual(self.cond.set_consume(0, False), 0)
        self.assertEqual(self.cond.descend, False)

    def test_set_consume_zero_true(self):
        self.assertEqual(self.cond.set_consume(0, True), 0)
        self.assertEqual(self.cond.descend, True)

    def test_set_consume_inc_float(self):
        self.assertEqual(self.cond.set_consume(.5, True), .5)
        self.assertEqual(self.cond.descend, True)

    def test_get_current_display(self):
        self.fail()

    def test_apply_consume_inc(self):
        self.assertEqual(self.cond.apply_consume(), 6)

    def test_apply_consume_inc_over(self):
        self.assertEqual(self.cond.set_consume(10, False), 10)
        self.assertEqual(self.cond.descend, False)
        self.assertEqual(self.cond.apply_consume(), 10)

    def test_apply_consume_dec_under(self):
        self.assertEqual(self.cond.set_consume(10, True), 10)
        self.assertEqual(self.cond.descend, True)
        self.assertEqual(self.cond.apply_consume(), 0)

    def test_apply_consume_dec(self):
        self.assertEqual(self.cond.set_consume(2, True), 2)
        self.assertEqual(self.cond.descend, True)

    def test_apply_consume_inc_multiple(self):
        self.assertEqual(self.cond.apply_consume(), 6)
        self.assertEqual(self.cond.apply_consume(), 7)

    def test_apply_consume_dec_multiple(self):
        self.assertEqual(self.cond.set_consume(1, True), 1)
        self.assertEqual(self.cond.apply_consume(), 4)
        self.assertEqual(self.cond.apply_consume(), 3)

    def test_apply_consume_zero(self):
        self.assertEqual(self.cond.set_consume(0, True), 0)
        self.assertEqual(self.cond.apply_consume(), 5)
        self.assertEqual(self.cond.apply_consume(), 5)

    def test_apply_consume_float(self):
        self.assertEqual(self.cond.set_consume(.5, True), .5)
        self.assertEqual(self.cond.apply_consume(), 4.5)
