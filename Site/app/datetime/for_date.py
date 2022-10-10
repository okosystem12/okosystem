
def for_date(self):
    if self is not None:
        return self.strftime("%Y-%m-%d")
    else:
        return ''
