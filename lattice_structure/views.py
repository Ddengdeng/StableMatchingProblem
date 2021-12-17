from django.shortcuts import render
from django.http import HttpResponse
from . import SearchSM
from . import GenerateSM
from . import LatticeStructure
from django.views.decorators.csrf import csrf_exempt
from collections import defaultdict
import time
import sys
import numpy as np


def index(request):
    return render(request, 'lattice_structure/index.html')


def about(request):
    return render(request, 'lattice_structure/about.html')


def algorithms(request):
    return render(request, 'lattice_structure/algorithms.html')

@csrf_exempt
def results(request):
    # get people's number from algorithm.html through POST method
    if request.method == 'POST':
        print(request.POST.get('person_number'))
        inputfile = request.FILES.get('inputfile')
        person_number = request.POST.get('person_number')
        if person_number != None:
            person_number = int(person_number)
            menList, womenList = GenerateSM.Generate(int(person_number))
        elif inputfile != None:
            with open('inputfile.txt', 'wb') as fp:
                for chunk in inputfile.chunks():
                    fp.write(chunk)

            file = open('inputfile.txt')

            with open('inputfile.txt', 'r', encoding='utf-8') as f:  # open the file
                lines = f.readlines()  # read all lines
                person_number = int(lines[0])  # get the number of first line
                print(person_number, len(lines))
                menList = []
                womenList = []
                for i in range(1, person_number + 1):
                    curLine = lines[i].strip().split(" ")
                    curLine = list(map(int, curLine))
                    menList.append(curLine[:])
                for i in range(person_number + 1, person_number * 2 + 1):
                    curLine = lines[i].strip().split(" ")
                    curLine = list(map(int, curLine))
                    womenList.append(curLine[:])

    sm = SearchSM.SearchSM(person_number, menList, womenList)

    s_time = time.perf_counter()
    sm.search_match(0)
    e_time = time.perf_counter()
    print('Run time:%s ms' % ((e_time - s_time)*1000))

    # generate stable matching results to show on the web page
    sm_list = sm.SMList
    res_list = []
    for i in range(len(sm_list)):
        temp_list = []
        match_name = 'M' + str(i + 1)
        temp_list.append(match_name)
        match_str = ''
        for each in sm_list[i]:
            match_str += '(m' + str(each[0]+1) + ', w' + str(each[1]+1) + ') '
        temp_list.append(match_str)
        res_list.append(temp_list)

    # generate preference lists
    res_men_list = []
    res_women_list = []
    for i in range(len(menList)):
        temp_man_list = []
        temp_woman_list = []
        man_name = 'm' + str(i+1)
        woman_name = 'w' + str(i+1)
        temp_man_list.append(man_name)
        temp_woman_list.append(woman_name)
        man_match_str = ''
        woman_match_str = ''
        for each in womenList[i]:
            man_match_str += 'w' + str(each) + ', '
        for each in menList[i]:
            woman_match_str += 'm' + str(each) + ', '
        temp_man_list.append(man_match_str)
        temp_woman_list.append(woman_match_str)
        res_men_list.append(temp_man_list)
        res_women_list.append(temp_woman_list)

    # get path_list from SearchSM
    la = LatticeStructure.LatticeStructure(sm.SMList)
    la.calculate_rotation()
    path_list = la.path_list
    number = len(path_list)


    # Traverse the graph line by line and count the depth of each point (depthlist)
    visit = [0]*number
    for i in range(number):
        visit[i] = 0
    glist = [0]  # insert the 0 SM
    visit[0] = 1
    depthlist = {0: 0}  # The 0 SM result is at layer 0
    while glist != []:
        i = glist.pop(0)
        for j in range(i + 1, number):
            if path_list[i][j] == 1 and visit[j] == 0:
                visit[j] = 1
                depthlist[j] = depthlist[i] + 1
                glist.append(j)

    # calculate coordinates of x and y
    x_center = 550
    y_top = 100
    x_margin = 100
    y_margin = 100
    res_link_list = []
    res_node_list = []

    link_dict = {'M1': [x_center, y_top]}

    rever_depthlist = defaultdict(list)  # reverse depthlist
    for key, value in depthlist.items():
        rever_depthlist[value].append(key)

    for key, value in rever_depthlist.items():
        layerlist = rever_depthlist[key]
        layernumber = len(layerlist)
        for i in range(layernumber):
            node = 'M' + str(layerlist[i] + 1)
            x = x_center + x_margin * (i - layernumber / 2)
            y = y_top + y_margin * key
            link_dict[node] = [x, y]

    for each in link_dict.keys():
        res_node_list.append([each, link_dict[each][0], link_dict[each][1]])

    for i in range(number):  # calculate the link list according to the upper triangle of the pathlist
        for j in range(i + 1, number):
            if path_list[i][j] == 1:
                source_node_name = 'M' + str(i + 1)
                target_node_name = 'M' + str(j + 1)
                res_link_list.append([source_node_name, target_node_name])

    return render(request, 'lattice_structure/results.html',
                  {'sm_list': res_list,
                   'men_list': res_men_list,
                   'women_list': res_women_list,
                   'node_list': res_node_list,
                   'link_list': res_link_list})