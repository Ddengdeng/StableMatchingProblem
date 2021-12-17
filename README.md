# StableMatchingProblem(SMP)
This project aims to establish a web application that can generate the visualization of lattice structure of stable matchings.

The basic process of the project is to generate preference lists of men and women randomly or user-inputting,
 then using depth-first-search (DFS) algorithm to seek all possible stable matching results. The lattice structure 
 is created by SMP results and the nodes on the diagram represents SMP results.
 
 ## Features
 ### Random generator
  Users can input the number of men/women from 2 to 9, then the system will randomly generate the preference lists.
  (see lattice_structure/GenerateSM.py)
  
  ### User-input instance
  Users can input prefrence lists by themselves, and the format of TXT input file follows requirements underneath:
  
  2 # Initialize: 2 men/women (= 2 preference lists of each man/woman) 
  
1 2 # The preference list of m1

2 1 # The preference list of m2

1 2 # The preference list of w1

2 1 # The preference list of w2 

###  Search stable matchings
The system can search all stable matchings under certain perference lists of men and women using DFS algorithm, and the results 
are form men-optimal(first one) to women-optimal(last one).(see lattice_structure/SearchSM.py)

### Visualization of lattice structure
The system can visualize the lattice structure according to the SMP results, the top-end represents the men-optimal result and 
the bottom represents the women-optimal result.(see lattice_structure/LatticeStructure)

## Testing
### Software test
The range of software testing is from 2 to 9, and all unit tests passed successfully, proving the system can operate reasonable and stably.(see Test/UnitTest.py)

### Correctness test
The system randomly generates numerous samples and the corresponding stable matching results and output as txt documents. The output files will be used 
as the input data of Dr Olasosebikan’s python code about SPA (student-project allocation) problem(https://github.com/sofiatolaosebikan/spa-s-enumerateSMs).

The input format of data conforms to the required format of Dr Olasosebikan’s code.(see Sample/GenerateSample.py and other txt documents in Sample document).

The system converts SMP instance to SPA instance:

SMP instance: men become students, women become lecturers and projects

m1: w1 w2    

m2: w2 w1

w1: m2 m1    

w2: m1 m2

Student-Project Allocation instance:

s1: p1 p2

s2: p2 p1

l1: s1 s2 -- offers p1

l2: s1 s2 -- offers p2

Meanwhile, the capacity of all projects and lecturers is 1

 
