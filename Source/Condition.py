class Condition(object):
    name = ""
    max = 0
    current = 0
    consume = 0
    descend = False

    def __init__(self, name_, max_=0, current_=0, consume_=0, descend_=False):
        self.name = name_
        self.max = max_
        self.current = current_
        self.consume = consume_
        self.descend = descend_

    def set_max(self, max_):
        if max_ < 0:
            max_ = 0

        self.max = max_

        # If current value greater than maximum, reduce current to max
        if self.current > self.max:
            self.set_current(self.max)

        return self.max

    def set_current(self, current_):
        if current_ < 0:
            current_ = 0

        if current_ > self.max:
            current_ = self.max

        self.current = current_

        return self.current

    def alt_current(self, amount_, inc_=True):
        current = self.current

        if inc_:
            current += amount_
        else:
            current -= amount_

        return self.set_current(current)

    def get_alert_level(self):
        # 0 = 100-76
        # 1 = 75-51
        # 2 = 50-26
        # 3 = 25-11
        # 4 = 10-00
        return 0

    def set_consume(self, consume_, descend_=True):
        consume = abs(consume_)
        descend = descend_

        if consume_ < 0:
            descend = not descend

        self.consume = consume
        self.descend = descend
        return self.consume

    def get_current_display(self):
        return self.current

    def apply_consume(self):
        return self.alt_current(self.consume, not self.descend)
