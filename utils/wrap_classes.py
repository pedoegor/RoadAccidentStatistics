
class RegionOffset:

    def __init__(self, name, level):
        self.name = name
        self.offset = '&nbsp;' * (level * 4)


class Parameter:

    def __init__(self, name, value):
        self.name = name
        self.value = value
