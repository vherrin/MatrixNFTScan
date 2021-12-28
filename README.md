# MatrixNTFScan

## Overview


Below shows the rarity and count of all the publicly known attributes for Niftys Matrix NFTs.  

There are two jupyter notebooks with one what scrapes the Nifty Matrix site and pulls the attributes per NTF then writes it out to a file.  The second then aggregates the files together into a dataframe then displays count and percentages

Please note this is a work in progress and I will update the attribute files periodically based on changes I see in on Nifty's site.  Also, this site is for informational purposes only.

My daughter and I are excited about 2022 and what this Matrix NFT journey will entail so hence the reason to discover this information 

Lastly, if you find this information useful then buy me a coffee @ vinceherrin.eth or like my matrix nft's here https://niftys.com/vinceherrin

Thanks for reading this and I hope this information is useful 

Rarity ranking calculation article [Ranking Rarity: Understanding Rarity Calculation Methods](https://raritytools.medium.com/ranking-rarity-understanding-rarity-calculation-methods-86ceaeb9b98c).


# Metrics

Please note that I'm using two different methods for calculating rarity with one using rarity-tools link above and the other is multiplication method 
</br>
</br>
## Addition Method:
</br>
Rarity Score for a Trait Value = 1 / (Number of Items with that Trait Value / Total Number of Items in Collection)

The total Rarity Score for an NFT is the sum of the Rarity Score of all of it’s trait values.
</br>
</br>
## Multiplication Method:
</br>
Rarity Score for a Trait Value = √√ (1 / (Number of Items with that Trait Value / Total Number of Items in Collection))
</br>
</br>

## Full 100k listings
- [Sorted by Nifty ID using addition method](./full_a_sorted_niftyID.html) </br>
- [Sorted by Ranking ID using addition method](./full_a_sorted_rankingID.html) </br>
- [Sorted by Nifty ID using multiplication method](./full_m_sorted_niftyID.html) </br>
- [Sorted by Ranking ID using multiplication method](./full_m_sorted_rankingID.html) </br>

</br>

 ### Top 25 (rarity using addition)
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th style="min-width: 80px;">rankingID</th>
      <th style="min-width: 80px;">niftyID</th>
      <th style="min-width: 80px;">aRarity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>11621</td>
      <td>11526.5988</td>
    </tr>
    <tr>
      <td>2</td>
      <td>29795</td>
      <td>6988.4026</td>
    </tr>
    <tr>
      <td>3</td>
      <td>63467</td>
      <td>6760.9120</td>
    </tr>
    <tr>
      <td>4</td>
      <td>86373</td>
      <td>6679.5724</td>
    </tr>
    <tr>
      <td>5</td>
      <td>53836</td>
      <td>6632.4023</td>
    </tr>
    <tr>
      <td>6</td>
      <td>49110</td>
      <td>6620.8614</td>
    </tr>
    <tr>
      <td>7</td>
      <td>83101</td>
      <td>6613.3474</td>
    </tr>
    <tr>
      <td>8</td>
      <td>68770</td>
      <td>6598.3764</td>
    </tr>
    <tr>
      <td>9</td>
      <td>5135</td>
      <td>6569.6922</td>
    </tr>
    <tr>
      <td>10</td>
      <td>22889</td>
      <td>6533.3190</td>
    </tr>
    <tr>
      <td>11</td>
      <td>2942</td>
      <td>6528.0594</td>
    </tr>
    <tr>
      <td>12</td>
      <td>93728</td>
      <td>6522.2826</td>
    </tr>
    <tr>
      <td>13</td>
      <td>38379</td>
      <td>6521.2416</td>
    </tr>
    <tr>
      <td>14</td>
      <td>63775</td>
      <td>6516.4288</td>
    </tr>
    <tr>
      <td>15</td>
      <td>750</td>
      <td>6504.6630</td>
    </tr>
    <tr>
      <td>16</td>
      <td>17313</td>
      <td>5372.9618</td>
    </tr>
    <tr>
      <td>17</td>
      <td>81747</td>
      <td>5265.4597</td>
    </tr>
    <tr>
      <td>18</td>
      <td>47263</td>
      <td>5119.1217</td>
    </tr>
    <tr>
      <td>19</td>
      <td>39591</td>
      <td>5030.0987</td>
    </tr>
    <tr>
      <td>20</td>
      <td>62311</td>
      <td>4980.3959</td>
    </tr>
    <tr>
      <td>21</td>
      <td>44625</td>
      <td>4976.4545</td>
    </tr>
    <tr>
      <td>22</td>
      <td>37120</td>
      <td>4973.3525</td>
    </tr>
    <tr>
      <td>23</td>
      <td>52344</td>
      <td>4973.3503</td>
    </tr>
    <tr>
      <td>24</td>
      <td>59977</td>
      <td>4971.2298</td>
    </tr>
    <tr>
      <td>25</td>
      <td>74825</td>
      <td>4968.8889</td>
    </tr>
  </tbody>
</table></br>

### Bottom 25 (rarity using addition)

Please notice the reverse order  <table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th style="min-width: 80px;">rankingID</th>
      <th style="min-width: 80px;">niftyID</th>
      <th style="min-width: 80px;">aRarity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>96934</td>
      <td>15504</td>
      <td>29.4959</td>
    </tr>
    <tr>
      <td>96933</td>
      <td>29479</td>
      <td>29.9026</td>
    </tr>
    <tr>
      <td>96932</td>
      <td>70646</td>
      <td>29.9415</td>
    </tr>
    <tr>
      <td>96931</td>
      <td>88333</td>
      <td>30.2892</td>
    </tr>
    <tr>
      <td>96930</td>
      <td>23442</td>
      <td>30.8032</td>
    </tr>
    <tr>
      <td>96929</td>
      <td>1189</td>
      <td>31.4783</td>
    </tr>
    <tr>
      <td>96928</td>
      <td>12840</td>
      <td>31.5034</td>
    </tr>
    <tr>
      <td>96927</td>
      <td>471</td>
      <td>31.5437</td>
    </tr>
    <tr>
      <td>96926</td>
      <td>31021</td>
      <td>31.5863</td>
    </tr>
    <tr>
      <td>96925</td>
      <td>69174</td>
      <td>31.8040</td>
    </tr>
    <tr>
      <td>96924</td>
      <td>67863</td>
      <td>32.1306</td>
    </tr>
    <tr>
      <td>96923</td>
      <td>22942</td>
      <td>32.1806</td>
    </tr>
    <tr>
      <td>96922</td>
      <td>57198</td>
      <td>32.2735</td>
    </tr>
    <tr>
      <td>96921</td>
      <td>12197</td>
      <td>32.3123</td>
    </tr>
    <tr>
      <td>96920</td>
      <td>94080</td>
      <td>32.3793</td>
    </tr>
    <tr>
      <td>96919</td>
      <td>94640</td>
      <td>32.8031</td>
    </tr>
    <tr>
      <td>96918</td>
      <td>17248</td>
      <td>32.8031</td>
    </tr>
    <tr>
      <td>96917</td>
      <td>2654</td>
      <td>32.8992</td>
    </tr>
    <tr>
      <td>96916</td>
      <td>53827</td>
      <td>33.0421</td>
    </tr>
    <tr>
      <td>96915</td>
      <td>30386</td>
      <td>33.1726</td>
    </tr>
    <tr>
      <td>96914</td>
      <td>84020</td>
      <td>33.2129</td>
    </tr>
    <tr>
      <td>96913</td>
      <td>16765</td>
      <td>33.3539</td>
    </tr>
    <tr>
      <td>96912</td>
      <td>89747</td>
      <td>33.5265</td>
    </tr>
    <tr>
      <td>96911</td>
      <td>59463</td>
      <td>33.7038</td>
    </tr>
    <tr>
      <td>96910</td>
      <td>38555</td>
      <td>33.7288</td>
    </tr>
  </tbody>
</table></br>  </br>

 ### Top 25 (rarity using multiplication)
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th style="min-width: 80px;">rankingID</th>
      <th style="min-width: 80px;">niftyID</th>
      <th style="min-width: 80px;">mRarity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>11621</td>
      <td>4700.1846</td>
    </tr>
    <tr>
      <td>2</td>
      <td>81747</td>
      <td>3956.9145</td>
    </tr>
    <tr>
      <td>3</td>
      <td>47263</td>
      <td>1410.4392</td>
    </tr>
    <tr>
      <td>4</td>
      <td>37120</td>
      <td>1020.4555</td>
    </tr>
    <tr>
      <td>5</td>
      <td>74532</td>
      <td>926.6603</td>
    </tr>
    <tr>
      <td>6</td>
      <td>33380</td>
      <td>909.4168</td>
    </tr>
    <tr>
      <td>7</td>
      <td>46837</td>
      <td>831.1293</td>
    </tr>
    <tr>
      <td>8</td>
      <td>74825</td>
      <td>807.2481</td>
    </tr>
    <tr>
      <td>9</td>
      <td>17313</td>
      <td>801.4360</td>
    </tr>
    <tr>
      <td>10</td>
      <td>69912</td>
      <td>785.0074</td>
    </tr>
    <tr>
      <td>11</td>
      <td>43530</td>
      <td>780.6974</td>
    </tr>
    <tr>
      <td>12</td>
      <td>39591</td>
      <td>751.3014</td>
    </tr>
    <tr>
      <td>13</td>
      <td>49110</td>
      <td>745.6505</td>
    </tr>
    <tr>
      <td>14</td>
      <td>5311</td>
      <td>726.1983</td>
    </tr>
    <tr>
      <td>15</td>
      <td>62769</td>
      <td>722.3062</td>
    </tr>
    <tr>
      <td>16</td>
      <td>10200</td>
      <td>702.9221</td>
    </tr>
    <tr>
      <td>17</td>
      <td>26019</td>
      <td>701.4431</td>
    </tr>
    <tr>
      <td>18</td>
      <td>44766</td>
      <td>701.3217</td>
    </tr>
    <tr>
      <td>19</td>
      <td>1367</td>
      <td>694.3080</td>
    </tr>
    <tr>
      <td>20</td>
      <td>29795</td>
      <td>671.1420</td>
    </tr>
    <tr>
      <td>21</td>
      <td>53215</td>
      <td>668.0605</td>
    </tr>
    <tr>
      <td>22</td>
      <td>83101</td>
      <td>664.6471</td>
    </tr>
    <tr>
      <td>23</td>
      <td>70187</td>
      <td>662.3367</td>
    </tr>
    <tr>
      <td>24</td>
      <td>70442</td>
      <td>653.1730</td>
    </tr>
    <tr>
      <td>25</td>
      <td>16555</td>
      <td>640.8446</td>
    </tr>
  </tbody>
</table></br>

### Bottom 25 (rarity using multiplication)

Please notice the reverse order  <table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th style="min-width: 80px;">rankingID</th>
      <th style="min-width: 80px;">niftyID</th>
      <th style="min-width: 80px;">mRarity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>96934</td>
      <td>71614</td>
      <td>5.9637</td>
    </tr>
    <tr>
      <td>96933</td>
      <td>67863</td>
      <td>6.0476</td>
    </tr>
    <tr>
      <td>96932</td>
      <td>15504</td>
      <td>6.1293</td>
    </tr>
    <tr>
      <td>96931</td>
      <td>8415</td>
      <td>6.1624</td>
    </tr>
    <tr>
      <td>96930</td>
      <td>88333</td>
      <td>6.2717</td>
    </tr>
    <tr>
      <td>96929</td>
      <td>2654</td>
      <td>6.2875</td>
    </tr>
    <tr>
      <td>96928</td>
      <td>23442</td>
      <td>6.2985</td>
    </tr>
    <tr>
      <td>96927</td>
      <td>48794</td>
      <td>6.3168</td>
    </tr>
    <tr>
      <td>96926</td>
      <td>48815</td>
      <td>6.3168</td>
    </tr>
    <tr>
      <td>96925</td>
      <td>29479</td>
      <td>6.3696</td>
    </tr>
    <tr>
      <td>96924</td>
      <td>70646</td>
      <td>6.3715</td>
    </tr>
    <tr>
      <td>96923</td>
      <td>31021</td>
      <td>6.3745</td>
    </tr>
    <tr>
      <td>96922</td>
      <td>57198</td>
      <td>6.4155</td>
    </tr>
    <tr>
      <td>96921</td>
      <td>1189</td>
      <td>6.5183</td>
    </tr>
    <tr>
      <td>96920</td>
      <td>471</td>
      <td>6.5311</td>
    </tr>
    <tr>
      <td>96919</td>
      <td>35298</td>
      <td>6.6318</td>
    </tr>
    <tr>
      <td>96918</td>
      <td>19115</td>
      <td>6.6584</td>
    </tr>
    <tr>
      <td>96917</td>
      <td>56777</td>
      <td>6.6604</td>
    </tr>
    <tr>
      <td>96916</td>
      <td>9827</td>
      <td>6.6604</td>
    </tr>
    <tr>
      <td>96915</td>
      <td>53827</td>
      <td>6.6700</td>
    </tr>
    <tr>
      <td>96914</td>
      <td>20364</td>
      <td>6.6961</td>
    </tr>
    <tr>
      <td>96913</td>
      <td>92937</td>
      <td>6.7120</td>
    </tr>
    <tr>
      <td>96912</td>
      <td>84020</td>
      <td>6.7143</td>
    </tr>
    <tr>
      <td>96911</td>
      <td>12840</td>
      <td>6.7780</td>
    </tr>
    <tr>
      <td>96910</td>
      <td>20504</td>
      <td>6.7849</td>
    </tr>
  </tbody>
</table></br>  