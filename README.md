# CS764Module4
Homework for Module 4 of Blockchains and Cryptocurrencies

## Running the program

This program is based on the one for Module 3, with minor tweaks to the hash calculation and main driver function. The simulation no longer takes any command-line arguments, and simply runs all three cases and then saves them to output files. The following is how the simulation is run:

```
python main.py
```

The output is placed into the files `a.csv`, `b.csv`, and `c.csv`. The following is an example of the output from `b.csv`:

```
Case,Block #,Num Nonces Tried,Computation Time
B,0,125,0.003998517990112305
B,1,60,0.001998424530029297
B,2,17,0.001003265380859375
B,3,10,0.0009987354278564453
B,4,20,0.0009965896606445312
B,5,44,0.0019996166229248047
B,6,6,0.0
B,7,3,0.0
B,8,22,0.0010001659393310547
B,9,52,0.0020003318786621094
B,10,6,0.0010006427764892578
B,11,1,0.0
B,12,72,0.003000497817993164
B,13,28,0.0010046958923339844
B,14,57,0.0020036697387695312
B,15,5,0.0
B,16,7,0.001001119613647461
B,17,12,0.0
B,18,6,0.00099945068359375
B,19,45,0.001997709274291992
B,20,6,0.0010006427764892578
B,21,1,0.0
B,22,37,0.0009999275207519531
B,23,27,0.0009996891021728516
B,24,12,0.0009996891021728516
B,25,3,0.00099945068359375
```