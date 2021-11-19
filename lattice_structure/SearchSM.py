#  Generate all matchings(including stable and unstable), the total is N!
#  Then remove the unstable matchings according to the defination of unstable matchings
#  Get stable matchings,
#  Output these stable matchings for constructing the lattice structure

from Partner import Partner
import GenerateSM as GSM
from LatticeStructure import LatticeStructure


class SearchSM:
    # import the information of the preference list of men and women
    def __init__(self, unit_count, menList, womenList):
        self.UNIT_COUNT = unit_count  # the numbers of men/women = unit_count
        self.men = []
        self.women = []
        self.SMList = []
        for i in range(len(menList)):  # each line is a perference list
            man = Partner(i, menList[i])  # construct the object of the Partner
            self.men.append(man)  # add the object to men's preference list
        for i in range(len(womenList)):  # the same as men
            woman = Partner(i, womenList[i])
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


def test():
    unit_count = 8

    # the prefrence list include the number from 0 to 7, because index starts from 0
    # menList =  [[4, 6, 0, 1, 5, 7, 3, 2],
    #             [1, 2, 6, 4, 3, 0, 7, 5],
    #             [7, 4, 0, 3, 5, 1, 2, 6],
    #             [2, 1, 6, 3, 0, 5, 7, 4],
    #             [6, 1, 4, 0, 2, 5, 7, 3],
    #             [0, 5, 6, 4, 7, 3, 1, 2],
    #             [1, 4, 6, 5, 2, 3, 7, 0],
    #             [2, 7, 3, 4, 6, 1, 5, 0]]
    # womenList = [[4, 2, 6, 5, 0, 1, 7, 3],
    #              [7, 5, 2, 4, 6, 1, 0, 3],
    #              [0, 4, 5, 1, 3, 7, 6, 2],
    #              [7, 6, 2, 1, 3, 0, 4, 5],
    #              [5, 3, 6, 2, 7, 0, 1, 4],
    #              [1, 7, 4, 2, 3, 5, 6, 0],
    #              [6, 4, 1, 0, 7, 5, 3, 2],
    #              [6, 3, 0, 4, 1, 2, 5, 7]]

    # menList =  [[2, 0, 4, 6, 3, 1, 7, 5],
    #             [5, 0, 2, 3, 7, 6, 4, 1],
    #             [6, 3, 2, 5, 4, 0, 1, 7],
    #             [4, 2, 7, 1, 5, 0, 3, 6],
    #             [3, 0, 1, 7, 6, 2, 5, 4],
    #             [5, 1, 4, 6, 7, 3, 2, 0],
    #             [6, 7, 0, 5, 1, 2, 3, 4],
    #             [1, 5, 6, 0, 7, 2, 3, 4]]
    # womenList = [[3, 2, 7, 0, 1, 4, 6, 5],
    #              [2, 6, 4, 7, 5, 3, 0, 1],
    #              [6, 4, 7, 2, 5, 1, 0, 3],
    #              [5, 3, 1, 6, 2, 0, 4, 7],
    #              [7, 6, 5, 4, 0, 3, 2, 1],
    #              [4, 3, 6, 5, 1, 7, 2, 0],
    #              [0, 3, 4, 5, 1, 7, 2, 6],
    #              [1, 4, 3, 2, 6, 7, 0, 5]]

    # ???????

    menList = [[4, 5, 1, 6, 0, 2, 7, 3],
               [1, 0, 7, 4, 5, 3, 2, 6],
               [6, 5, 3, 1, 4, 2, 7, 0],
               [7, 1, 4, 3, 2, 6, 0, 5],
               [2, 0, 6, 5, 7, 4, 1, 3],
               [3, 2, 5, 1, 0, 4, 7, 6],
               [4, 1, 7, 0, 5, 6, 2, 3],
               [4, 3, 0, 6, 2, 7, 1, 5]]

    womenList = [[5, 6, 2, 3, 0, 1, 4, 7],
                 [0, 7, 6, 1, 3, 5, 2, 4],
                 [2, 4, 3, 7, 6, 1, 5, 0],
                 [4, 6, 2, 7, 3, 1, 0, 5],
                 [1, 2, 5, 7, 0, 3, 6, 4],
                 [3, 4, 6, 2, 1, 5, 7, 0],
                 [6, 5, 7, 4, 3, 2, 0, 1],
                 [0, 7, 5, 3, 6, 1, 2, 4]]

    # menList = [[0, 1, 2, 3],
    #            [1, 0, 3, 2],
    #            [2, 3, 0, 1],
    #            [3, 2, 1, 0]]

    # womenList = [[3, 2, 1, 0],
    #              [2, 3, 0, 1],
    #              [1, 0, 3, 2],
    #              [0, 1, 2, 3]]

    # menList,womenList = GSM.Generate(unit_count)

    # # print the prefrence list of men and women
    # for i in range(len(menList)):
    #     print("man", i, "'s preference list: ", menList[i])
    # for i in range(len(womenList)):
    #     print("woman", i, "'s preference list: ", womenList[i])

    sm = SearchSM(unit_count, menList, womenList)
    sm.search_match(0)

    for i in menList:
        print(i)
    print()

    la = LatticeStructure(sm.SMList)

    la.calculate_rotation()


if __name__ == '__main__':
    test()













