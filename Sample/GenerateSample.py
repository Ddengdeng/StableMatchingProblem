import random
from lattice_structure import GenerateSM, SearchSM
import string

# generate Sample, include a intput.txt and a output.txt
# Input => a instance represented as a .txt file
# Output => all stable matchings that the instance admits
# File format reference：https://github.com/sofiatolaosebikan/spa-s-enumerateSMs

def GenerateSample(samplenum):
    for i in range(samplenum):
        num = random.randint(2, 10)
        menList, womenList = GenerateSM.Generate(num)
        sm = SearchSM.SearchSM(num, menList, womenList)
        sm.search_match(0)
        sm_list = sm.SMList

        # input Sample
        filename = "input" + str(i) + ".txt"
        f = open(filename, "w")
        f.write(str(num)+" "+str(num)+" "+str(num)+"\n")
        # student
        for j in range(1, num+1):
            menstring = ' '.join('%s' % id for id in menList[j-1])
            f.write(str(j)+" "+str(menstring)+"\n")
        # project
        lecturelist = [x for x in range(num)]
        lecturestring = ' '.join('%s' % id for id in lecturelist)
        for j in range(1, num+1):
            f.write(str(j)+" "+str(1)+" "+str(lecturestring)+"\n")
        # lecture
        for j in range(1, num+1):
            womenstring = ' '.join('%s' % id for id in womenList[j-1])
            f.write(str(j)+" "+str(womenstring)+"\n")
        f.close()

        # output Sample
        filename = "output" + str(i) + ".txt"
        f = open(filename, "w")
        smstring = " ".join('%s' % id for id in sm_list)
        print(sm_list)
        print(smstring)
        f.write(smstring)
        f.close()


if __name__ == '__main__':
    GenerateSample(3)

