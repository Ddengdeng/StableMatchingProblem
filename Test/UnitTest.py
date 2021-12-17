import unittest
from lattice_structure import GenerateSM
from lattice_structure.LatticeStructure import LatticeStructure
from lattice_structure.SearchSM import SearchSM
# test result of sm


class Test_SM(unittest.TestCase):
    def test_01(self):
        unit_count = 8
        menList, womenList = GenerateSM.Generate(unit_count)

        sm = SearchSM(unit_count, menList, womenList)
        sm.search_match(0)


# test lattice structure
class Test_LS(unittest.TestCase):
    def setUp(self):
        unit_count = 8
        menList, womenList = GenerateSM.Generate(unit_count)
        self.sm = SearchSM(unit_count, menList, womenList)
        self.sm.search_match(0)

    def test_add01(self):
        la = LatticeStructure(self.sm.SMList)
        la.calculate_rotation()