class NumericalErrors:
    def __init__(self, exact, estimated):
        self.exact = exact
        self.estimated = estimated

    def absolute_error(self):
        return abs(self.exact-self.estimated)

    def relative_error(self):
        d = abs(self.exact-self.estimated)
        return (d/self.exact)*100

    def __str__(self):
        return f'{self.exact}'
