#  Generate all matchings(including stable and unstable), the total is N!
#  Then remove the unstable matchings according to the defination of unstable matchings
#  Get stable matchings,
#  Output these stable matchings for constructing the lattice structure

from . import Partner
from . import LatticeStructure


class SearchSM:
    # import the information of the preference list of men and women
    def __init__(self, unit_count, menList, womenList):
        self.UNIT_COUNT = unit_count  # the numbers of men/women = unit_count
        self.men = []
        self.women = []
        self.SMList = []
        for i in range(len(menList)):  # each line is a perference list
            mlist = []
            for x in menList[i]:
                mlist.append(x - 1)
            man = Partner.Partner(i, mlist)  # construct the object of the Partner
            self.men.append(man)  # add the object to men's preference list
        for i in range(len(womenList)):  # the same as men
            wlist = []
            for x in womenList[i]:
                wlist.append(x - 1)
            woman = Partner.Partner(i, wlist)
            self.women.append(woman)

    # check whether the matching is stable
    def is_stable_matching(self):

        # iterate every man, then find the position of current woman in men's perference list
        for i in range(0, self.UNIT_COUNT):

            curwomanid = self.men[i].current
            womanpos = self.men[i].preferList.index(curwomanid)

            # iterate women in men's perference list before current matching
            for k in range(0, womanpos):
                womanid = self.men[i].preferList[k]
                # for one prefered woman, find the position of the man under current matching
                manpos = self.women[womanid].preferList.index(i)
                curmanid = self.women[womanid].current
                # find the position of the man that matched with this prefered woman
                curmanpos = self.women[womanid].preferList.index(curmanid)

                # compare the priority of manpos and curmanpos
                if manpos < curmanpos:
                    return False

        return True

    # check whether a woman is matched from womanid to current matched woman
    def is_partner_matched(self, womanid):
        if self.women[womanid].current == -1:  # means this woman is single
            return False
        return True

    # generate all matchings and check the satbility
    def search_match(self, index):

        # after iterating all men's preference list, end the matching process
        if index == self.UNIT_COUNT:
            # print("A perfect matching")    # the matching may not be stable

            if self.is_stable_matching():
                print("A stable matching")
                temp_sm = []

                for i in range(len(self.men)):
                    # print(i, '--', self.men[i].current)
                    temp = [i, self.men[i].current]
                    temp_sm.append(temp)
                print(temp_sm)
                self.SMList.append(temp_sm)  # store all stable matchings in order (two-dimensional array)

            return

        # use recursion algorithm to implement DFS(depth first search) and to find all matchings(stable and unstable)
        for i in range(len(self.men[index].preferList)):  # iterate to the deepest of the tree structure
            womanid = self.men[index].preferList[i]

            if not self.is_partner_matched(womanid):  # if it is true, match man(i) with this woman
                self.men[index].current = womanid
                self.women[womanid].current = index
                self.search_match(index + 1)  # start to find the matching of man(i + 1) under man(i) matched
                # go back to the previous layer to find matching, until back to the outermost layer means already found all the matchings
                self.men[index].current = -1  # unmatch the previous layer of man and start to find other matchings
                self.women[womanid].current = -1  # unmatch corresponding woman













