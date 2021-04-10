class DecorationRepository:
    def __init__(self):
        # empty list that will contain all decorations (objects)
        self.decorations = []

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        return False

    def find_by_type(self, decoration_type: str):
        try:
            decoration = [d for d in self.decorations if d.__class__.__name__ == decoration_type][0]
            return decoration
        except IndexError:
            return "None"
