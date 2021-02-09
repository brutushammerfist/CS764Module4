# CS764Module3
Homework for Module 3 of Blockchains and Cryptocurrencies

## Running the program

To run the Blockchain simulation, you'll simply need to run the following command. Output type is an integer that you pass into the program, between 0 and 3.

```
python main.py {output-type}
```

The following is what output will be given based upon the argument that you pass in. Triple dots denote that the output continues, but I've truncated the rest for readability.

- 0 - Prints out the entire Blockchain.
    - ```
      PS C:\Users\Matt\Desktop\School\CS764\CS764Module3> python.exe .\main.py 0
      ---------------------------
      Customer Public Key: 0
      Merchant Public Key: 0
      Date: 0
      Amount: 0
      ---------------------------
      ---------------------------
      Customer Public Key: PublicKey  (75731429187645185965965487185296269344631270542066825222570853542348315567739  53673942798830340263714945696936888707263036761115961244441580344798733917287,   65537)
      Merchant Public Key: PublicKey  (81748327641275905383693291060768721108359228501228692981077988853821785352046  87885339580142963861060878317660471345041407340585218518098578825241984849059,   65537)
      Date: 01292020
      Amount: 744717.45
      ---------------------------
      ---------------------------
      Customer Public Key: PublicKey  (70212183194374231092402455717834633811624276565644005302054500321853470225181  81640475043844054211727227004476619927488735379546282794003578323387272217561,   65537)
      Merchant Public Key: PublicKey  (10198915055183480465207928706886287807801383368018474131107513373182169431408  669146484024815000928396218510371855666402957314463365661651125200827328803133  , 65537)
      Date: 02182020
      Amount: 943596.5
      ---------------------------

      ...
      ```
- 1 - Increments the fifteenth block's transaction amount by 10 and checks to ensure that the blockchain is still valid.
    - ```
      PS C:\Users\Matt\Desktop\School\CS764\CS764Module3> python.exe .\main.py 1
      The Blockchain has not been tampered with!
      Incrementing transaction 15 amount by 10.
      Previous Hash: b'\x1a\'\x80\xf9\xca\x83\x96\xe0)  =T\xbe\x1d\xa6\xa6\x8f\xbc\xc0\x03+9"\xb8\xe8\xc0\xef\x18\x15J\xdf\t\xf7'
      Recaclulated Previous Hash: b'A\xf1\x1c\xac\x9bX(/  \x88\xea~\x92U\xfb\x12M\xafm\xb7\xa6\x89\xf08\x18\xa2QF_\xcb\xce\xf07'
      The Blockchain HAS been tampered with!
      ```
- 2 - Prints out all of the transactions made by the third customer.
    - ```
      PS C:\Users\Matt\Desktop\School\CS764\CS764Module3> python.exe .\main.py 2
      Print Customer 3 Transactions:
      ---------------------------
      Customer Public Key: PublicKey    (921441131087114102436073312085403329461699357776027344585933256376927782293046650      3906282506932906896459707568141137576378098035355956873990921825382755057, 65537)
      Merchant Public Key: PublicKey    (801634431145830643950634837027765024682805795839184591734519643481536931326449086      2170295182447036861613920815881164446518706832514054974619287956586265157, 65537)
      Date: 03282020
      Amount: 423944.64
      ---------------------------
      ---------------------------
      Customer Public Key: PublicKey    (921441131087114102436073312085403329461699357776027344585933256376927782293046650      3906282506932906896459707568141137576378098035355956873990921825382755057, 65537)
      Merchant Public Key: PublicKey    (105425729589605321289382126974771774449892887081291267587005095766062690742808320      55004725267133420375216510419462449265536025391275738745072395435869140251, 65537)
      Date: 05062020
      Amount: 643461.15
      ---------------------------

      ...
      ```
- 3 - Prints out all of the transactions made by the second merchant.
    - ```
      PS C:\Users\Matt\Desktop\School\CS764\CS764Module3> python.exe .\main.py 3
      Print Merchant 2 Transactions:
      ---------------------------
      Customer Public Key: PublicKey    (672509786580026252887696782386803680396281897242644913688007275432536026208404768      4949281048981348722701790198052110934885194191684129888041430524486027871, 65537)
      Merchant Public Key: PublicKey    (966875693179974226965188699335815772825400314202318913875363035401719905175835300      6919702007583697893496746357902069130814444268043923038053436363977993163, 65537)
      Date: 02132020
      Amount: 163437.73
      ---------------------------
      ---------------------------
      Customer Public Key: PublicKey    (104702160994730206990361747784745855588587117089037730996011672474586883730845594      63679118384334159596344706895604349301551653539737505151556010443216600333, 65537)
      Merchant Public Key: PublicKey    (966875693179974226965188699335815772825400314202318913875363035401719905175835300      6919702007583697893496746357902069130814444268043923038053436363977993163, 65537)
      Date: 03252020
      Amount: 793067.39
      ---------------------------

      ...
      ```