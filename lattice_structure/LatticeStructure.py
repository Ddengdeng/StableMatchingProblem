# calculate the rotations between every two stable matchings
# find the shortest path for drawing lattice structure(Hasse)
# the way to find rotations: store every relations of rotations from M1 to Mn
# in other word: traverse the pathes from M1 to Mn and store them, compare with each other to check whether there has cotainment relationship


class LatticeStructure:

    def __init__(self, SMList):
        self.SMList = SMList
        self.path_list = []

        # pass the stable matching list generated from SearchSM

    def is_stable_matching(self, temp_sm):
        flag = -1
        for i in range(len(self.SMList)):
            sm = self.SMList[i]
            t = [x for x in sm if x in temp_sm]
            if len(t) == len(temp_sm):
                flag = 1
        return flag

    def calculate_diff(self, sm1, sm2):  # calculate rotation between two SM
        rotation = []

        # check different pairs between two stable matchings
        # find the different women between sm1 and sm2
        for i in range(len(sm1)):
            woman1 = sm1[i][1]
            woman2 = sm2[i][1]
            if woman1 != woman2:  # add every different pairs to correspounding rotation
                rotation.append(sm1[i])
        return rotation

    # check whether there is a contaionment relationship between rotations(list1 list2)
    def calculate_division(self, list1, list2):
        flag = 1  # flag == 1 means exiting containment relationship

        # check whether there exits same path in all rotations or not
        if list1 == list2:
            flag = -1
            return flag

        for x in list1:
            if x not in list2:
                flag = -1  # means pairs in list2 are not all included in list1(no cotainment relationship)
                break
        return flag

    def calculate_rotation(self):

        # initialize all path to 0
        UNIT_COUNT = len(self.SMList)
        self.path_list = [[0] * UNIT_COUNT for _ in range(UNIT_COUNT)]
        rotation_list = [[[]] * UNIT_COUNT for _ in range(UNIT_COUNT)]

        for i in range(UNIT_COUNT):
            for j in range(UNIT_COUNT):
                rotation = self.calculate_diff(self.SMList[i], self.SMList[j])
                rotation_list[i][j] = rotation

                # the generation of rotations between Mi and the rest of the stabla matchings related to Mi
        for i in range(UNIT_COUNT):
            for j in range(UNIT_COUNT):
                x = rotation_list[i][j]
                flag = 1
                for k in range(UNIT_COUNT):
                    if j == k or i == j or i == k:
                        continue
                    y = rotation_list[i][k]

                    # check whether rotation x and y has containment relationship
                    if self.calculate_division(y, x) == 1:
                        flag = -1

                # if has, change path to 1(there has connection between Mi and Mj)
                if flag == 1:
                    self.path_list[i][j] = 1

        for x in rotation_list:
            print(x)

        print("path_list")
        for x in self.path_list:
            print(x)




