# CSCI-UA310
Programing Assignment for CSCI-UA310 Basic Algorithm classes

PA2:
The board of directors are very impatient. It has been 5 days since the company restarted and the economy has not collapsed into itself. This suggests that the finance department needs to be sacked and has been thrown into the fourth closest sun.

The board has decided to increase the fees for the parks by at least 4 million altairian dollars. Some others think it might be better to increase each park individually and there are some who think it might be better to increase the fees of multiple parks at the same time. The finer points are still under scrutiny whereas the chairman is nowhere to be found after he went to take a stroll in the park.

They have decided that you, having helped implement the database in the first place, would be a good choice as a programmer to do the updates in the system.

There will be three types of queries to the database

insert a planet with name a and entrance fee k into the database
increase the entrance fee for all planets between a,b by k 
return the entrance fee for a planet name a from the database
Input Format

The first line contains n the number of queries to be made to the database.

The next n lines contain queries of the following 3 types

a k, insert a planet with name a and entrance fee k into the database
a b k, increase the entrance fee for all planets between a b by k
a, return the entrance fee for a planet name a from the database
Constraints
n<= 100000
|a|,|b| <= 10
0<=k<=100000

The entrance fee for any planet will always be less than 2^30

YOU MUST USE 2-3 TREE DATA STRUCTURES PROVIDED IN CLASS

Output Format:
For each query of type  print the entrance fee of the planet in a new line.

PA3:
The SPARTAN-II program has been restarted and needs to get more soldiers out as the war is starting to look bad for the humans. Dr.Catherine Halsey has decided that instead of the normal procedure of choosing the survivors of the tests of the SPARTAN-II program it would be better to administer repeated evaluations of the candidates and disqualify the ones which fail to meet the mark.

In the new system each soldier gets an initial score when he enrolls. Throughout the course of the program they need to keep improving their score, which will be appraised at the next evaluation. Every soldier who does not meet the standard will be permanently discarded at that evaluation. Only those who remain at the end of all the evaluations will get to be called SPARTAN-II commandos.

Help Dr.Catherine decide the eligible candidates who remain at the end.

Input Format:

The first line of the input is a number n, which is the number candidates enrolled.

The next n lines are of the format
s a

where s is the name of the candidate and a is the original score of the candidate.

The next line is a number m, which is the number of subsequent lines in the input.

The next m lines can be of 2 types

s,b which tells that the score of candidate s has improved by b 

k, which tells that an evaluation has been conducted with a standard k. All candidates with score less than k will be disqualified and permanently discarded in this evaluation.

Constraints
1<=n,m<= 1000000
|s|<=10
a,b <= 1000000000
k<= 1000000000000000000

YOU MUST USE A MIN HEAP (WHICH YOU IMPLEMENT YOURSELF), TOGETHER WITH A JAVA HASHMAP (OR PYTHON DICTIONARY). OTHER THAN THE HASHMAP (OR DICTIONARY) AND STANDARD I/O METHODS, YOU SHOULD NOT USE ANY OTHER CLASSES OR METHODS FROM THE STANDARD LIBRARY.

SEE: "Implementation notes for heaps" in the Priority Queues slides on the course home page for the approach you should take. We also discussed this in quite some detail in class.

Output Format:

The output should contain the number of remaining soldiers after each query of type 2.
