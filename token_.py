class Token:
    def __init__(self, ID, tag, value, readonly=False):
        self.id = ID
        self.tag = tag
        self.value = value
        self.readonly = readonly
