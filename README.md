# MatrixNTFScan

## Overview


Below shows the rarity and count of all the publicly known attributes for Niftys Matrix NFTs.  

There are two jupyter notebooks with one what scrapes the Nifty Matrix site and pulls the attributes per NTF then writes it out to a file.  The second then aggregates the files together into a dataframe then displays count and percentages

Please note this is a work in progress and I will update the attribute files periodically based on changes I see in on Nifty's site.  Also, this site is for informational purposes only.

My daughter and I are excited about 2022 and what this Matrix NFT journey will entail so hence the reason to discover this information 

Lastly, if you find this information useful then buy me a coffee @ vinceherrin.eth or like my matrix nft's here https://niftys.com/vinceherrin

Thanks for reading this and I hope this information is useful 



## Metrics

```

You can change the pull count in GetRarityFromAll.ipynb.  
Ranking is using the Rarity ranking method - 
https://raritytools.medium.com/ranking-rarity-understanding-rarity-calculation-methods-86ceaeb9b98c

Top 25
       rankingID  niftyID     rarity
               1    11621  11732.100
               2    29795   6955.348
               3    63467   6733.812
               4    86373   6653.388
               5    53836   6603.381
               6    49110   6589.774
               7    83101   6584.488
               8    68770   6569.332
               9     5135   6540.719
              10    22889   6503.229
              11     2942   6497.533
              12    93728   6494.860
              13    38379   6492.310
              14    63775   6490.522
              15      750   6478.754
              16    17313   5601.065
              17    39591   5271.307
              18    81747   5242.183
              19    52344   5228.305
              20    74825   5201.598
              21    48223   5198.745
              22     1367   5188.549
              23    26797   5176.901
              24    76137   5163.262
              25    58945   5161.794


Bottom 25 please note reverse order listing
       rankingID  niftyID  rarity
           96406    83435  47.211
           96405    55705  47.211
           96404    79953  48.017
           96403    47536  48.057
           96402    96034  48.306
           96401    16253  48.426
           96400    84987  48.426
           96399    10939  48.465
           96398    87543  48.739
           96397    18275  48.739
           96396    86363  48.739
           96395    62648  48.778
           96394    15504  48.780
           96393    90136  48.785
           96392    15596  48.785
           96391    85783  48.825
           96390    81083  48.885
           96389    13061  48.925
           96388    81036  49.073
           96387    74701  49.073
           96386    14042  49.107
           96385    84768  49.107
           96384    28742  49.107
           96383    66086  49.112
           96382    39424  49.146



Empty Count =  3594 out of 100,000

0
White    96406
Name: Background, dtype: int64
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
White    1.0
Name: Background, dtype: float64
=====================================================
=====================================================
1
None                         9649
Straight Sideswept Fringe    9644
Short Messy                  9606
Buzz Cut                     8698
Short Afro Fade              8692
Short Coil                   8666
Medium Curly Bob             7685
Long Messy                   6774
Low Ponytail                 6739
Short Pixie                  6737
Updo Bun                     4840
Short Updo                   4817
Long Straight Bangs          1935
Long Afro                    1924
Name: Hair Style, dtype: int64
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
None                         0.100087
Straight Sideswept Fringe    0.100035
Short Messy                  0.099641
Buzz Cut                     0.090223
Short Afro Fade              0.090160
Short Coil                   0.089891
Medium Curly Bob             0.079715
Long Messy                   0.070265
Low Ponytail                 0.069902
Short Pixie                  0.069882
Updo Bun                     0.050204
Short Updo                   0.049966
Long Straight Bangs          0.020071
Long Afro                    0.019957
Name: Hair Style, dtype: float64
=====================================================
=====================================================
2
Black          28935
Light Brown    21202
Dark Brown     17382
Blonde         13503
Light Grey      9621
Auburn          5763
Name: Hair Color, dtype: int64
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
Black          0.300137
Light Brown    0.219924
Dark Brown     0.180300
Blonde         0.140064
Light Grey     0.099797
Auburn         0.059778
Name: Hair Color, dtype: float64
=====================================================
=====================================================
3
None        72363
Stubble      9617
Thin         4820
Mustache     3853
Goatee       3836
Beard        1917
Name: Facial Hair, dtype: int64
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
None        0.750607
Stubble     0.099755
Thin        0.049997
Mustache    0.039966
Goatee      0.039790
Beard       0.019885
Name: Facial Hair, dtype: float64
=====================================================
=====================================================
4
Light Gray Longsleeve                                   6758
Charcoal Blazer with Light Blue Shirt and No Tie        6048
Blue Longsleeve                                         5769
Navy Blazer with Striped Shirt and No Tie               5217
Navy Oxford with Buttons                                4156
Charcoal Blazer with Light Blue Shirt and Black Tie     4026
Dark Gray Longsleeve                                    3850
Olive Oxford with Buttons                               3529
Navy Blazer with Striped Shirt and Navy Tie             3493
Gray Blazer with Black Shirt and No Tie                 3473
Navy Oxford with Tie                                    2961
Navy Oxford with Pocket                                 2952
Red Longsleeve                                          2925
Tan Blazer with Off-White Shirt and No Tie              2632
Olive Oxford with Pocket                                2517
Olive Oxford with Tie                                   2514
Khaki Oxford with Buttons                               2359
Gray Blazer with Black Shirt and Gray Tie               2305
Gray Oxford with Buttons                                1776
Navy Oxford with Tie and Pocket                         1759
Tan Blazer with Off-White Shirt and Tan Tie             1736
Khaki Oxford with Tie                                   1697
Navy Jumpsuit                                           1691
Khaki Oxford with Pocket                                1685
Olive Oxford with Tie and Pocket                        1523
Denim Jumpsuit                                          1441
Gray Oxford with Pocket                                 1275
Gray Oxford with Tie                                    1248
Khaki Oxford with Tie and Pocket                        1010
Gray Jumpsuit                                            964
Gray Oxford with Tie and Pocket                          764
Khaki Jumpsuit                                           716
Light Gray Cardigan with Light Gray Longsleeve Shirt     702
Light Gray Cardigan with Beige Longsleeve Shirt          605
Dark Gray Cardigan with Light Gray Longsleeve Shirt      603
Dark Gray Cardigan with Beige Longsleeve Shirt           519
Light Gray Cardigan with Tan Longsleeve Shirt            503
Light Gray Cardigan with Light Gray Oxford Shirt         472
Dark Gray Cardigan with Tan Longsleeve Shirt             435
Olive Cardigan with Light Gray Longsleeve Shirt          407
Dark Gray Cardigan with Light Gray Oxford Shirt          403
Light Gray Cardigan with Beige Oxford Shirt              400
Olive Cardigan with Beige Longsleeve Shirt               356
Dark Gray Cardigan with Beige Oxford Shirt               344
Light Gray Cardigan with Tan Oxford Shirt                342
Brown Cardigan with Light Gray Longsleeve Shirt          307
Dark Gray Cardigan with Tan Oxford Shirt                 292
Olve Cardigan with Tan Longsleeve Shirt                  289
Olive Cardigan with Light Gray Oxford Shirt              264
Brown Cardigan with Beige Longsleeve Shirt               260
Olive Cardigan with Beige Oxford Shirt                   223
Brown Cardigan with Tan Longsleeve Shirt                 220
Brown Cardigan with Light Gray Oxford Shirt              206
Light Gray Cardigan with Off-White Longsleeve Shirt      203
Olive Cardigan with Tan Oxford Shirt                     194
Dark Gray Cardigan with Off-White Longsleeve Shirt       179
Brown Cardigan with Beigse Oxford Shirt                  173
Brown Cardigan with Tan Oxford Shirt                     142
Light Gray Cardigan with Off-White Oxford Shirt          136
Dark Gray Cardigan with Off-White Oxford Shirt           118
Olive Cardigan with Off-White Longsleeve Shirt           117
Brown Cardigan with Off-White Longsleeve Shirt            90
Olive Cardigan with Off-White Oxford Shirt                74
Brown Cardigan with Off-White Oxford Shirt                59
Name: Top, dtype: int64
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
Light Gray Longsleeve                                   0.070099
Charcoal Blazer with Light Blue Shirt and No Tie        0.062735
Blue Longsleeve                                         0.059841
Navy Blazer with Striped Shirt and No Tie               0.054115
Navy Oxford with Buttons                                0.043109
Charcoal Blazer with Light Blue Shirt and Black Tie     0.041761
Dark Gray Longsleeve                                    0.039935
Olive Oxford with Buttons                               0.036606
Navy Blazer with Striped Shirt and Navy Tie             0.036232
Gray Blazer with Black Shirt and No Tie                 0.036025
Navy Oxford with Tie                                    0.030714
Navy Oxford with Pocket                                 0.030621
Red Longsleeve                                          0.030340
Tan Blazer with Off-White Shirt and No Tie              0.027301
Olive Oxford with Pocket                                0.026108
Olive Oxford with Tie                                   0.026077
Khaki Oxford with Buttons                               0.024469
Gray Blazer with Black Shirt and Gray Tie               0.023909
Gray Oxford with Buttons                                0.018422
Navy Oxford with Tie and Pocket                         0.018246
Tan Blazer with Off-White Shirt and Tan Tie             0.018007
Khaki Oxford with Tie                                   0.017603
Navy Jumpsuit                                           0.017540
Khaki Oxford with Pocket                                0.017478
Olive Oxford with Tie and Pocket                        0.015798
Denim Jumpsuit                                          0.014947
Gray Oxford with Pocket                                 0.013225
Gray Oxford with Tie                                    0.012945
Khaki Oxford with Tie and Pocket                        0.010477
Gray Jumpsuit                                           0.009999
Gray Oxford with Tie and Pocket                         0.007925
Khaki Jumpsuit                                          0.007427
Light Gray Cardigan with Light Gray Longsleeve Shirt    0.007282
Light Gray Cardigan with Beige Longsleeve Shirt         0.006276
Dark Gray Cardigan with Light Gray Longsleeve Shirt     0.006255
Dark Gray Cardigan with Beige Longsleeve Shirt          0.005383
Light Gray Cardigan with Tan Longsleeve Shirt           0.005218
Light Gray Cardigan with Light Gray Oxford Shirt        0.004896
Dark Gray Cardigan with Tan Longsleeve Shirt            0.004512
Olive Cardigan with Light Gray Longsleeve Shirt         0.004222
Dark Gray Cardigan with Light Gray Oxford Shirt         0.004180
Light Gray Cardigan with Beige Oxford Shirt             0.004149
Olive Cardigan with Beige Longsleeve Shirt              0.003693
Dark Gray Cardigan with Beige Oxford Shirt              0.003568
Light Gray Cardigan with Tan Oxford Shirt               0.003547
Brown Cardigan with Light Gray Longsleeve Shirt         0.003184
Dark Gray Cardigan with Tan Oxford Shirt                0.003029
Olve Cardigan with Tan Longsleeve Shirt                 0.002998
Olive Cardigan with Light Gray Oxford Shirt             0.002738
Brown Cardigan with Beige Longsleeve Shirt              0.002697
Olive Cardigan with Beige Oxford Shirt                  0.002313
Brown Cardigan with Tan Longsleeve Shirt                0.002282
Brown Cardigan with Light Gray Oxford Shirt             0.002137
Light Gray Cardigan with Off-White Longsleeve Shirt     0.002106
Olive Cardigan with Tan Oxford Shirt                    0.002012
Dark Gray Cardigan with Off-White Longsleeve Shirt      0.001857
Brown Cardigan with Beigse Oxford Shirt                 0.001794
Brown Cardigan with Tan Oxford Shirt                    0.001473
Light Gray Cardigan with Off-White Oxford Shirt         0.001411
Dark Gray Cardigan with Off-White Oxford Shirt          0.001224
Olive Cardigan with Off-White Longsleeve Shirt          0.001214
Brown Cardigan with Off-White Longsleeve Shirt          0.000934
Olive Cardigan with Off-White Oxford Shirt              0.000768
Brown Cardigan with Off-White Oxford Shirt              0.000612
Name: Top, dtype: float64
=====================================================
=====================================================
5
Charcoal Slacks     21117
Navy Slacks         18077
Gray Slacks         12019
Dark-Wash Denim     10976
Light-Wash Denim     9397
Khaki Slacks         9045
Blue Denim           6282
None                 4812
Khaki                4681
Name: Bottom, dtype: int64
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
Charcoal Slacks     0.219042
Navy Slacks         0.187509
Gray Slacks         0.124671
Dark-Wash Denim     0.113852
Light-Wash Denim    0.097473
Khaki Slacks        0.093822
Blue Denim          0.065162
None                0.049914
Khaki               0.048555
Name: Bottom, dtype: float64
=====================================================
=====================================================
6
Brown Leather Shoes with Laces               20264
White Canvas Sneaker with White Sole         17326
Black Suede Chelseas with Brown Sole         14484
Black Leather Shoes with Laces               13526
Tan Suede Workboot with Tan Sole             11585
White Leather Sneaker with Grey Sole         11504
Redbrown Leather Workboot with Brown Sole     7702
Black Leather Chelsea with Blue Sole            15
Name: Footwear, dtype: int64
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
Brown Leather Shoes with Laces               0.210194
White Canvas Sneaker with White Sole         0.179719
Black Suede Chelseas with Brown Sole         0.150240
Black Leather Shoes with Laces               0.140302
Tan Suede Workboot with Tan Sole             0.120169
White Leather Sneaker with Grey Sole         0.119329
Redbrown Leather Workboot with Brown Sole    0.079891
Black Leather Chelsea with Blue Sole         0.000156
Name: Footwear, dtype: float64
=====================================================
=====================================================
7
None             81926
Two Rings        13507
Ring One Blue      973
Name: Ring, dtype: int64
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
None             0.849802
Two Rings        0.140105
Ring One Blue    0.010093
Name: Ring, dtype: float64
=====================================================
=====================================================
8
None                     86771
Tan Workers Cap           6253
Navy Blue Workers Cap     2415
Purple Workers Cap         967
Name: Headwear, dtype: int64
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
None                     0.900058
Tan Workers Cap          0.064861
Navy Blue Workers Cap    0.025050
Purple Workers Cap       0.010030
Name: Headwear, dtype: float64
=====================================================
=====================================================
9
None                 62651
Black Books          19274
Silver Aviators       9402
Rosegold Aviators     5040
3D Glasses              20
Blue Books              19
Name: Glasses, dtype: int64
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
None                 0.649866
Black Books          0.199925
Silver Aviators      0.097525
Rosegold Aviators    0.052279
3D Glasses           0.000207
Blue Books           0.000197
Name: Glasses, dtype: float64
=====================================================
=====================================================
10
None            86791
Stud Earring     9615
Name: Piercings, dtype: int64
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
None            0.900266
Stud Earring    0.099734
Name: Piercings, dtype: float64
=====================================================
=====================================================
11
None                       31875
Black Smartphone           21177
Brown Leather Briefcase    17340
Black Leather Briefcase    13461
Lunchbox                    9658
Blue Lunchbox               1948
Light Blue Smartphone        947
Name: Accessories, dtype: int64
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
None                       0.330633
Black Smartphone           0.219665
Brown Leather Briefcase    0.179864
Black Leather Briefcase    0.139628
Lunchbox                   0.100180
Blue Lunchbox              0.020206
Light Blue Smartphone      0.009823
Name: Accessories, dtype: float64
=====================================================
=====================================================


```