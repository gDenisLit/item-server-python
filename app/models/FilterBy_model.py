class FilterBy:
    def __init__(self, txt):
        self.txt = txt

    def to_dict(self):
        return {
            "txt": self.txt
        }
