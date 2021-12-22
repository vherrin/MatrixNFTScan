# MatrixNTFScan

## Overview


Below shows the rarity and count of all the publicly known attributes for Niftys Matrix NFTs.  

There are two jupyter notebooks with one what scrapes the Nifty Matrix site and pulls the attributes per NTF then writes it out to a file.  The second then aggregates the files together into a dataframe then displays count and percentages

Please note this is a work in progress and I will update the attribute files periodically based on changes I see in on Nifty's site.  Also, this site is for informational purposes only.

My daughter and I are excited about 2022 and what this Matrix NFT journey will entail so hence the reason to discover this information 

Lastly, if you find this information useful then buy me a coffee @ vinceherrin.eth or like my matrix nft's here https://niftys.com/vinceherrin

Thanks for reading this and I hope this information is useful 

Rarity ranking calculation article [Ranking Rarity: Understanding Rarity Calculation Methods](https://raritytools.medium.com/ranking-rarity-understanding-rarity-calculation-methods-86ceaeb9b98c).


## Metrics

```

You can change the pull count in GetRarityFromAll.ipynb.  
Ranking is using the Rarity ranking method described in the 
article listed above

Top 25
       rankingID  niftyID     rarity
               1    11621  11753.500
               2    29795   6971.444
               3    63467   6745.087
               4    86373   6663.687
               5    53836   6616.759
               6    49110   6605.011
               7    83101   6597.546
               8    68770   6582.487
               9     5135   6553.885
              10    22889   6517.527
              11     2942   6512.232
              12    93728   6506.497
              13    38379   6505.447
              14    63775   6500.603
              15      750   6488.856
              16    17313   5614.408
              17    39591   5272.704
              18    81747   5254.856
              19    52344   5216.025
              20    74825   5211.553
              21    48223   5207.643
              22     1367   5198.539
              23    26797   5184.565
              24    58945   5172.361
              25    93679   5166.613


Bottom 25 please note reverse order listing

       rankingID  niftyID  rarity
           96406    15504  29.495
           96405    29479  29.903
           96404    70646  29.943
           96403    88333  30.290
           96402    23442  30.810
           96401     1189  31.484
           96400    12840  31.505
           96399      471  31.543
           96398    31021  31.581
           96397    69174  31.802
           96396    67863  32.134
           96395    22942  32.183
           96394    57198  32.264
           96393    12197  32.310
           96392    94080  32.385
           96391    94640  32.801
           96390    17248  32.801
           96389     2654  32.901
           96388    53827  33.032
           96387    30386  33.180
           96386    84020  33.218
           96385    16765  33.348
           96384    89747  33.526
           96383    59463  33.708
           96382    38555  33.729


Empty Count =  3303 out of 100,000

0
White    96697
Name: Background, dtype: int64
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
White    1.0
Name: Background, dtype: float64
=====================================================
=====================================================
1
Straight Sideswept Fringe    9671
Short Messy                  9641
Buzz Cut                     8730
Short Afro Fade              8710
Short Coil                   8687
Medium Curly Bob             7706
Long Messy                   6793
Low Ponytail                 6763
Short Pixie                  6761
Updo Bun                     4854
Short Updo                   4833
Long Straight Bangs          1942
Long Afro                    1933
Name: Hair Style, dtype: int64
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
Straight Sideswept Fringe    0.111130
Short Messy                  0.110786
Buzz Cut                     0.100317
Short Afro Fade              0.100087
Short Coil                   0.099823
Medium Curly Bob             0.088550
Long Messy                   0.078059
Low Ponytail                 0.077714
Short Pixie                  0.077691
Updo Bun                     0.055778
Short Updo                   0.055536
Long Straight Bangs          0.022316
Long Afro                    0.022212
Name: Hair Style, dtype: float64
=====================================================
=====================================================
2
Black          29013
Light Brown    21255
Dark Brown     17437
Blonde         13549
Light Grey      9665
Auburn          5778
Name: Hair Color, dtype: int64
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
Black          0.300040
Light Brown    0.219810
Dark Brown     0.180326
Blonde         0.140118
Light Grey     0.099951
Auburn         0.059754
Name: Hair Color, dtype: float64
=====================================================
=====================================================
3
Stubble     9646
Thin        4839
Mustache    3867
Goatee      3842
Beard       1924
Name: Facial Hair, dtype: int64
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
Stubble     0.399950
Thin        0.200639
Mustache    0.160337
Goatee      0.159300
Beard       0.079774
Name: Facial Hair, dtype: float64
=====================================================
=====================================================
4
Light Gray Longsleeve                                   6783
Charcoal Blazer with Light Blue Shirt and No Tie        6066
Blue Longsleeve                                         5788
Navy Blazer with Striped Shirt and No Tie               5232
Navy Oxford with Buttons                                4165
Charcoal Blazer with Light Blue Shirt and Black Tie     4035
Dark Gray Longsleeve                                    3868
Olive Oxford with Buttons                               3535
Navy Blazer with Striped Shirt and Navy Tie             3501
Gray Blazer with Black Shirt and No Tie                 3482
Navy Oxford with Tie                                    2971
Navy Oxford with Pocket                                 2963
Red Longsleeve                                          2933
Tan Blazer with Off-White Shirt and No Tie              2640
Olive Oxford with Pocket                                2525
Olive Oxford with Tie                                   2524
Khaki Oxford with Buttons                               2364
Gray Blazer with Black Shirt and Gray Tie               2312
Gray Oxford with Buttons                                1784
Navy Oxford with Tie and Pocket                         1765
Tan Blazer with Off-White Shirt and Tan Tie             1740
Khaki Oxford with Tie                                   1700
Navy Jumpsuit                                           1698
Khaki Oxford with Pocket                                1691
Olive Oxford with Tie and Pocket                        1525
Denim Jumpsuit                                          1445
Gray Oxford with Pocket                                 1279
Gray Oxford with Tie                                    1251
Khaki Oxford with Tie and Pocket                        1015
Gray Jumpsuit                                            965
Gray Oxford with Tie and Pocket                          764
Khaki Jumpsuit                                           720
Light Gray Cardigan with Light Gray Longsleeve Shirt     707
Dark Gray Cardigan with Light Gray Longsleeve Shirt      605
Light Gray Cardigan with Beige Longsleeve Shirt          605
Dark Gray Cardigan with Beige Longsleeve Shirt           521
Light Gray Cardigan with Tan Longsleeve Shirt            504
Light Gray Cardigan with Light Gray Oxford Shirt         472
Dark Gray Cardigan with Tan Longsleeve Shirt             436
Olive Cardigan with Light Gray Longsleeve Shirt          410
Dark Gray Cardigan with Light Gray Oxford Shirt          404
Light Gray Cardigan with Beige Oxford Shirt              402
Olive Cardigan with Beige Longsleeve Shirt               357
Dark Gray Cardigan with Beige Oxford Shirt               347
Light Gray Cardigan with Tan Oxford Shirt                343
Brown Cardigan with Light Gray Longsleeve Shirt          307
Dark Gray Cardigan with Tan Oxford Shirt                 292
Olve Cardigan with Tan Longsleeve Shirt                  289
Olive Cardigan with Light Gray Oxford Shirt              264
Brown Cardigan with Beige Longsleeve Shirt               261
Olive Cardigan with Beige Oxford Shirt                   225
Brown Cardigan with Tan Longsleeve Shirt                 220
Brown Cardigan with Light Gray Oxford Shirt              207
Light Gray Cardigan with Off-White Longsleeve Shirt      203
Olive Cardigan with Tan Oxford Shirt                     194
Dark Gray Cardigan with Off-White Longsleeve Shirt       180
Brown Cardigan with Beigse Oxford Shirt                  174
Brown Cardigan with Tan Oxford Shirt                     144
Light Gray Cardigan with Off-White Oxford Shirt          136
Dark Gray Cardigan with Off-White Oxford Shirt           118
Olive Cardigan with Off-White Longsleeve Shirt           117
Brown Cardigan with Off-White Longsleeve Shirt            90
Olive Cardigan with Off-White Oxford Shirt                75
Brown Cardigan with Off-White Oxford Shirt                59
Name: Top, dtype: int64
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
Light Gray Longsleeve                                   0.070147
Charcoal Blazer with Light Blue Shirt and No Tie        0.062732
Blue Longsleeve                                         0.059857
Navy Blazer with Striped Shirt and No Tie               0.054107
Navy Oxford with Buttons                                0.043073
Charcoal Blazer with Light Blue Shirt and Black Tie     0.041728
Dark Gray Longsleeve                                    0.040001
Olive Oxford with Buttons                               0.036557
Navy Blazer with Striped Shirt and Navy Tie             0.036206
Gray Blazer with Black Shirt and No Tie                 0.036009
Navy Oxford with Tie                                    0.030725
Navy Oxford with Pocket                                 0.030642
Red Longsleeve                                          0.030332
Tan Blazer with Off-White Shirt and No Tie              0.027302
Olive Oxford with Pocket                                0.026112
Olive Oxford with Tie                                   0.026102
Khaki Oxford with Buttons                               0.024448
Gray Blazer with Black Shirt and Gray Tie               0.023910
Gray Oxford with Buttons                                0.018449
Navy Oxford with Tie and Pocket                         0.018253
Tan Blazer with Off-White Shirt and Tan Tie             0.017994
Khaki Oxford with Tie                                   0.017581
Navy Jumpsuit                                           0.017560
Khaki Oxford with Pocket                                0.017488
Olive Oxford with Tie and Pocket                        0.015771
Denim Jumpsuit                                          0.014944
Gray Oxford with Pocket                                 0.013227
Gray Oxford with Tie                                    0.012937
Khaki Oxford with Tie and Pocket                        0.010497
Gray Jumpsuit                                           0.009980
Gray Oxford with Tie and Pocket                         0.007901
Khaki Jumpsuit                                          0.007446
Light Gray Cardigan with Light Gray Longsleeve Shirt    0.007311
Dark Gray Cardigan with Light Gray Longsleeve Shirt     0.006257
Light Gray Cardigan with Beige Longsleeve Shirt         0.006257
Dark Gray Cardigan with Beige Longsleeve Shirt          0.005388
Light Gray Cardigan with Tan Longsleeve Shirt           0.005212
Light Gray Cardigan with Light Gray Oxford Shirt        0.004881
Dark Gray Cardigan with Tan Longsleeve Shirt            0.004509
Olive Cardigan with Light Gray Longsleeve Shirt         0.004240
Dark Gray Cardigan with Light Gray Oxford Shirt         0.004178
Light Gray Cardigan with Beige Oxford Shirt             0.004157
Olive Cardigan with Beige Longsleeve Shirt              0.003692
Dark Gray Cardigan with Beige Oxford Shirt              0.003589
Light Gray Cardigan with Tan Oxford Shirt               0.003547
Brown Cardigan with Light Gray Longsleeve Shirt         0.003175
Dark Gray Cardigan with Tan Oxford Shirt                0.003020
Olve Cardigan with Tan Longsleeve Shirt                 0.002989
Olive Cardigan with Light Gray Oxford Shirt             0.002730
Brown Cardigan with Beige Longsleeve Shirt              0.002699
Olive Cardigan with Beige Oxford Shirt                  0.002327
Brown Cardigan with Tan Longsleeve Shirt                0.002275
Brown Cardigan with Light Gray Oxford Shirt             0.002141
Light Gray Cardigan with Off-White Longsleeve Shirt     0.002099
Olive Cardigan with Tan Oxford Shirt                    0.002006
Dark Gray Cardigan with Off-White Longsleeve Shirt      0.001861
Brown Cardigan with Beigse Oxford Shirt                 0.001799
Brown Cardigan with Tan Oxford Shirt                    0.001489
Light Gray Cardigan with Off-White Oxford Shirt         0.001406
Dark Gray Cardigan with Off-White Oxford Shirt          0.001220
Olive Cardigan with Off-White Longsleeve Shirt          0.001210
Brown Cardigan with Off-White Longsleeve Shirt          0.000931
Olive Cardigan with Off-White Oxford Shirt              0.000776
Brown Cardigan with Off-White Oxford Shirt              0.000610
Name: Top, dtype: float64
=====================================================
=====================================================
5
Charcoal Slacks     21178
Navy Slacks         18133
Gray Slacks         12055
Dark-Wash Denim     11006
Light-Wash Denim     9436
Khaki Slacks         9061
Blue Denim           6300
Khaki                4700
Name: Bottom, dtype: int64
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
Charcoal Slacks     0.230524
Navy Slacks         0.197379
Gray Slacks         0.131219
Dark-Wash Denim     0.119801
Light-Wash Denim    0.102711
Khaki Slacks        0.098630
Blue Denim          0.068576
Khaki               0.051160
Name: Bottom, dtype: float64
=====================================================
=====================================================
6
Brown Leather Shoes with Laces               20326
White Canvas Sneaker with White Sole         17374
Black Suede Chelseas with Brown Sole         14525
Black Leather Shoes with Laces               13573
Tan Suede Workboot with Tan Sole             11620
White Leather Sneaker with Grey Sole         11540
Redbrown Leather Workboot with Brown Sole     7724
Black Leather Chelsea with Blue Sole            15
Name: Footwear, dtype: int64
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
Brown Leather Shoes with Laces               0.210203
White Canvas Sneaker with White Sole         0.179675
Black Suede Chelseas with Brown Sole         0.150211
Black Leather Shoes with Laces               0.140366
Tan Suede Workboot with Tan Sole             0.120169
White Leather Sneaker with Grey Sole         0.119342
Redbrown Leather Workboot with Brown Sole    0.079878
Black Leather Chelsea with Blue Sole         0.000155
Name: Footwear, dtype: float64
=====================================================
=====================================================
7
Two Rings        13552
Ring One Blue      974
Name: Ring, dtype: int64
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
Two Rings        0.932948
Ring One Blue    0.067052
Name: Ring, dtype: float64
=====================================================
=====================================================
8
Tan Workers Cap          6274
Navy Blue Workers Cap    2422
Purple Workers Cap        973
Name: Headwear, dtype: int64
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
Tan Workers Cap          0.648878
Navy Blue Workers Cap    0.250491
Purple Workers Cap       0.100631
Name: Headwear, dtype: float64
=====================================================
=====================================================
9
Black Books          19340
Silver Aviators       9427
Rosegold Aviators     5055
3D Glasses              20
Blue Books              19
Name: Glasses, dtype: int64
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
Black Books          0.571159
Silver Aviators      0.278403
Rosegold Aviators    0.149287
3D Glasses           0.000591
Blue Books           0.000561
Name: Glasses, dtype: float64
=====================================================
=====================================================
10
Stud Earring    9650
Name: Piercings, dtype: int64
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
Stud Earring    1.0
Name: Piercings, dtype: float64
=====================================================
=====================================================
11
Black Smartphone           21238
Brown Leather Briefcase    17393
Black Leather Briefcase    13506
Lunchbox                    9686
Blue Lunchbox               1950
Light Blue Smartphone        947
Name: Accessories, dtype: int64
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
Black Smartphone           0.328152
Brown Leather Briefcase    0.268742
Black Leather Briefcase    0.208684
Lunchbox                   0.149660
Blue Lunchbox              0.030130
Light Blue Smartphone      0.014632
Name: Accessories, dtype: float64
=====================================================
=====================================================


```