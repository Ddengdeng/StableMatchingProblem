# partner info
# ID : A globally unique identifier for this partner
# preferList : Rank the ids of the opposite sex in order of preference from largest to smallest
# current : current match, -1 means no match


class Partner:
    def __init__(self, id, preferList):
        self.id = id
        self.preferList = preferList
        self.current = -1