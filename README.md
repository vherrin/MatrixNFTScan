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


</br>

 # matrix-red-contract</br>
## Updated on 2022-01-21</br>
- [Sorted by Nifty ID using addition method](./data/matrix-red-contract/full_a_sorted_niftyID.html) </br>
 - [Sorted by Ranking ID using addition method](./data/matrix-red-contract/full_a_sorted_rankingID.html) </br>
 - [Sorted by Nifty ID using multiplication method](./data/matrix-red-contract/full_m_sorted_niftyID.html) </br>
 - [Sorted by Ranking ID using multiplication method](./data/matrix-red-contract/full_m_sorted_rankingID.html) </br>
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
      <td>5090</td>
      <td>10743.61</td>
    </tr>
    <tr>
      <td>2</td>
      <td>96220</td>
      <td>10740.38</td>
    </tr>
    <tr>
      <td>3</td>
      <td>81743</td>
      <td>10674.31</td>
    </tr>
    <tr>
      <td>4</td>
      <td>41904</td>
      <td>10668.41</td>
    </tr>
    <tr>
      <td>5</td>
      <td>52958</td>
      <td>10660.69</td>
    </tr>
    <tr>
      <td>6</td>
      <td>84328</td>
      <td>10649.29</td>
    </tr>
    <tr>
      <td>7</td>
      <td>61440</td>
      <td>10637.72</td>
    </tr>
    <tr>
      <td>8</td>
      <td>51080</td>
      <td>10632.81</td>
    </tr>
    <tr>
      <td>9</td>
      <td>86889</td>
      <td>10631.87</td>
    </tr>
    <tr>
      <td>10</td>
      <td>86839</td>
      <td>10620.24</td>
    </tr>
    <tr>
      <td>11</td>
      <td>72688</td>
      <td>10616.38</td>
    </tr>
    <tr>
      <td>12</td>
      <td>88042</td>
      <td>10593.65</td>
    </tr>
    <tr>
      <td>13</td>
      <td>51216</td>
      <td>10592.44</td>
    </tr>
    <tr>
      <td>14</td>
      <td>74323</td>
      <td>10583.18</td>
    </tr>
    <tr>
      <td>15</td>
      <td>12530</td>
      <td>10582.27</td>
    </tr>
    <tr>
      <td>16</td>
      <td>31653</td>
      <td>10579.03</td>
    </tr>
    <tr>
      <td>17</td>
      <td>41240</td>
      <td>10571.99</td>
    </tr>
    <tr>
      <td>18</td>
      <td>89892</td>
      <td>10566.08</td>
    </tr>
    <tr>
      <td>19</td>
      <td>80020</td>
      <td>10564.64</td>
    </tr>
    <tr>
      <td>20</td>
      <td>61378</td>
      <td>10557.67</td>
    </tr>
    <tr>
      <td>21</td>
      <td>39160</td>
      <td>10553.49</td>
    </tr>
    <tr>
      <td>22</td>
      <td>1373</td>
      <td>10545.82</td>
    </tr>
    <tr>
      <td>23</td>
      <td>69853</td>
      <td>10545.55</td>
    </tr>
    <tr>
      <td>24</td>
      <td>81243</td>
      <td>10544.11</td>
    </tr>
    <tr>
      <td>25</td>
      <td>18763</td>
      <td>10542.28</td>
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
      <td>40588</td>
      <td>133</td>
      <td>33.44</td>
    </tr>
    <tr>
      <td>40587</td>
      <td>11569</td>
      <td>33.64</td>
    </tr>
    <tr>
      <td>40586</td>
      <td>24874</td>
      <td>35.76</td>
    </tr>
    <tr>
      <td>40585</td>
      <td>21376</td>
      <td>37.19</td>
    </tr>
    <tr>
      <td>40584</td>
      <td>87275</td>
      <td>37.36</td>
    </tr>
    <tr>
      <td>40583</td>
      <td>51412</td>
      <td>37.56</td>
    </tr>
    <tr>
      <td>40582</td>
      <td>80475</td>
      <td>37.73</td>
    </tr>
    <tr>
      <td>40581</td>
      <td>77362</td>
      <td>38.21</td>
    </tr>
    <tr>
      <td>40580</td>
      <td>55061</td>
      <td>38.23</td>
    </tr>
    <tr>
      <td>40579</td>
      <td>96113</td>
      <td>38.25</td>
    </tr>
    <tr>
      <td>40578</td>
      <td>83276</td>
      <td>38.50</td>
    </tr>
    <tr>
      <td>40577</td>
      <td>90304</td>
      <td>39.14</td>
    </tr>
    <tr>
      <td>40576</td>
      <td>4367</td>
      <td>39.21</td>
    </tr>
    <tr>
      <td>40575</td>
      <td>20534</td>
      <td>39.29</td>
    </tr>
    <tr>
      <td>40574</td>
      <td>57932</td>
      <td>39.31</td>
    </tr>
    <tr>
      <td>40573</td>
      <td>65129</td>
      <td>39.49</td>
    </tr>
    <tr>
      <td>40572</td>
      <td>86248</td>
      <td>39.58</td>
    </tr>
    <tr>
      <td>40571</td>
      <td>47364</td>
      <td>39.87</td>
    </tr>
    <tr>
      <td>40570</td>
      <td>31178</td>
      <td>39.87</td>
    </tr>
    <tr>
      <td>40569</td>
      <td>27989</td>
      <td>40.82</td>
    </tr>
    <tr>
      <td>40568</td>
      <td>67644</td>
      <td>41.07</td>
    </tr>
    <tr>
      <td>40567</td>
      <td>7959</td>
      <td>41.29</td>
    </tr>
    <tr>
      <td>40566</td>
      <td>11909</td>
      <td>41.40</td>
    </tr>
    <tr>
      <td>40565</td>
      <td>48954</td>
      <td>41.43</td>
    </tr>
    <tr>
      <td>40564</td>
      <td>11216</td>
      <td>41.46</td>
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
      <td>71216</td>
      <td>487106.27</td>
    </tr>
    <tr>
      <td>2</td>
      <td>19706</td>
      <td>270481.18</td>
    </tr>
    <tr>
      <td>3</td>
      <td>88736</td>
      <td>209048.43</td>
    </tr>
    <tr>
      <td>4</td>
      <td>12012</td>
      <td>144417.32</td>
    </tr>
    <tr>
      <td>5</td>
      <td>21728</td>
      <td>134025.91</td>
    </tr>
    <tr>
      <td>6</td>
      <td>12682</td>
      <td>132132.97</td>
    </tr>
    <tr>
      <td>7</td>
      <td>48088</td>
      <td>111925.65</td>
    </tr>
    <tr>
      <td>8</td>
      <td>11092</td>
      <td>92873.05</td>
    </tr>
    <tr>
      <td>9</td>
      <td>54604</td>
      <td>78351.30</td>
    </tr>
    <tr>
      <td>10</td>
      <td>66091</td>
      <td>64626.14</td>
    </tr>
    <tr>
      <td>11</td>
      <td>34221</td>
      <td>63403.08</td>
    </tr>
    <tr>
      <td>12</td>
      <td>73288</td>
      <td>56724.80</td>
    </tr>
    <tr>
      <td>13</td>
      <td>41685</td>
      <td>56295.50</td>
    </tr>
    <tr>
      <td>14</td>
      <td>86400</td>
      <td>55885.27</td>
    </tr>
    <tr>
      <td>15</td>
      <td>65611</td>
      <td>55454.42</td>
    </tr>
    <tr>
      <td>16</td>
      <td>66344</td>
      <td>52300.55</td>
    </tr>
    <tr>
      <td>17</td>
      <td>506</td>
      <td>50207.58</td>
    </tr>
    <tr>
      <td>18</td>
      <td>69107</td>
      <td>47234.74</td>
    </tr>
    <tr>
      <td>19</td>
      <td>63363</td>
      <td>46337.51</td>
    </tr>
    <tr>
      <td>20</td>
      <td>43625</td>
      <td>46189.85</td>
    </tr>
    <tr>
      <td>21</td>
      <td>66661</td>
      <td>46088.85</td>
    </tr>
    <tr>
      <td>22</td>
      <td>81249</td>
      <td>45898.55</td>
    </tr>
    <tr>
      <td>23</td>
      <td>75064</td>
      <td>43483.64</td>
    </tr>
    <tr>
      <td>24</td>
      <td>71947</td>
      <td>43473.93</td>
    </tr>
    <tr>
      <td>25</td>
      <td>43562</td>
      <td>43432.63</td>
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
      <td>40588</td>
      <td>21376</td>
      <td>0.93</td>
    </tr>
    <tr>
      <td>40587</td>
      <td>11569</td>
      <td>0.97</td>
    </tr>
    <tr>
      <td>40586</td>
      <td>133</td>
      <td>1.06</td>
    </tr>
    <tr>
      <td>40585</td>
      <td>87275</td>
      <td>1.08</td>
    </tr>
    <tr>
      <td>40584</td>
      <td>27989</td>
      <td>1.08</td>
    </tr>
    <tr>
      <td>40583</td>
      <td>96113</td>
      <td>1.17</td>
    </tr>
    <tr>
      <td>40582</td>
      <td>83460</td>
      <td>1.19</td>
    </tr>
    <tr>
      <td>40581</td>
      <td>80475</td>
      <td>1.23</td>
    </tr>
    <tr>
      <td>40580</td>
      <td>24874</td>
      <td>1.27</td>
    </tr>
    <tr>
      <td>40579</td>
      <td>40952</td>
      <td>1.31</td>
    </tr>
    <tr>
      <td>40578</td>
      <td>28851</td>
      <td>1.32</td>
    </tr>
    <tr>
      <td>40577</td>
      <td>438</td>
      <td>1.39</td>
    </tr>
    <tr>
      <td>40576</td>
      <td>57932</td>
      <td>1.39</td>
    </tr>
    <tr>
      <td>40575</td>
      <td>20534</td>
      <td>1.40</td>
    </tr>
    <tr>
      <td>40574</td>
      <td>20320</td>
      <td>1.45</td>
    </tr>
    <tr>
      <td>40573</td>
      <td>79071</td>
      <td>1.45</td>
    </tr>
    <tr>
      <td>40572</td>
      <td>77362</td>
      <td>1.45</td>
    </tr>
    <tr>
      <td>40571</td>
      <td>37222</td>
      <td>1.46</td>
    </tr>
    <tr>
      <td>40570</td>
      <td>44695</td>
      <td>1.48</td>
    </tr>
    <tr>
      <td>40569</td>
      <td>48006</td>
      <td>1.49</td>
    </tr>
    <tr>
      <td>40568</td>
      <td>79469</td>
      <td>1.52</td>
    </tr>
    <tr>
      <td>40567</td>
      <td>17343</td>
      <td>1.52</td>
    </tr>
    <tr>
      <td>40566</td>
      <td>73327</td>
      <td>1.54</td>
    </tr>
    <tr>
      <td>40565</td>
      <td>83276</td>
      <td>1.55</td>
    </tr>
    <tr>
      <td>40564</td>
      <td>55061</td>
      <td>1.63</td>
    </tr>
  </tbody>
</table></br>  </br>

 # matrix-blue-contract</br>
## Updated on 2022-01-21</br>
- [Sorted by Nifty ID using addition method](./data/matrix-blue-contract/full_a_sorted_niftyID.html) </br>
 - [Sorted by Ranking ID using addition method](./data/matrix-blue-contract/full_a_sorted_rankingID.html) </br>
 - [Sorted by Nifty ID using multiplication method](./data/matrix-blue-contract/full_m_sorted_niftyID.html) </br>
 - [Sorted by Ranking ID using multiplication method](./data/matrix-blue-contract/full_m_sorted_rankingID.html) </br>
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
      <td>47036</td>
      <td>21767.53</td>
    </tr>
    <tr>
      <td>2</td>
      <td>55898</td>
      <td>16002.03</td>
    </tr>
    <tr>
      <td>3</td>
      <td>55194</td>
      <td>15927.90</td>
    </tr>
    <tr>
      <td>4</td>
      <td>13009</td>
      <td>12759.71</td>
    </tr>
    <tr>
      <td>5</td>
      <td>71381</td>
      <td>10918.97</td>
    </tr>
    <tr>
      <td>6</td>
      <td>27567</td>
      <td>10861.53</td>
    </tr>
    <tr>
      <td>7</td>
      <td>79979</td>
      <td>10738.88</td>
    </tr>
    <tr>
      <td>8</td>
      <td>13626</td>
      <td>7643.87</td>
    </tr>
    <tr>
      <td>9</td>
      <td>76582</td>
      <td>7230.30</td>
    </tr>
    <tr>
      <td>10</td>
      <td>45395</td>
      <td>7201.16</td>
    </tr>
    <tr>
      <td>11</td>
      <td>11621</td>
      <td>5485.17</td>
    </tr>
    <tr>
      <td>12</td>
      <td>7510</td>
      <td>4587.55</td>
    </tr>
    <tr>
      <td>13</td>
      <td>68164</td>
      <td>4554.78</td>
    </tr>
    <tr>
      <td>14</td>
      <td>74966</td>
      <td>4503.01</td>
    </tr>
    <tr>
      <td>15</td>
      <td>8779</td>
      <td>4389.46</td>
    </tr>
    <tr>
      <td>16</td>
      <td>47495</td>
      <td>4388.80</td>
    </tr>
    <tr>
      <td>17</td>
      <td>71447</td>
      <td>4348.80</td>
    </tr>
    <tr>
      <td>18</td>
      <td>55079</td>
      <td>4014.62</td>
    </tr>
    <tr>
      <td>19</td>
      <td>60553</td>
      <td>3840.23</td>
    </tr>
    <tr>
      <td>20</td>
      <td>92345</td>
      <td>3702.46</td>
    </tr>
    <tr>
      <td>21</td>
      <td>33754</td>
      <td>3686.30</td>
    </tr>
    <tr>
      <td>22</td>
      <td>62291</td>
      <td>3668.81</td>
    </tr>
    <tr>
      <td>23</td>
      <td>59354</td>
      <td>3633.22</td>
    </tr>
    <tr>
      <td>24</td>
      <td>83101</td>
      <td>3318.94</td>
    </tr>
    <tr>
      <td>25</td>
      <td>77787</td>
      <td>3109.60</td>
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
      <td>10442</td>
      <td>55147</td>
      <td>126.31</td>
    </tr>
    <tr>
      <td>10441</td>
      <td>9710</td>
      <td>131.46</td>
    </tr>
    <tr>
      <td>10440</td>
      <td>67484</td>
      <td>138.38</td>
    </tr>
    <tr>
      <td>10439</td>
      <td>57833</td>
      <td>139.44</td>
    </tr>
    <tr>
      <td>10438</td>
      <td>3854</td>
      <td>142.29</td>
    </tr>
    <tr>
      <td>10437</td>
      <td>31010</td>
      <td>144.63</td>
    </tr>
    <tr>
      <td>10436</td>
      <td>89282</td>
      <td>145.33</td>
    </tr>
    <tr>
      <td>10435</td>
      <td>37366</td>
      <td>145.41</td>
    </tr>
    <tr>
      <td>10434</td>
      <td>74676</td>
      <td>147.18</td>
    </tr>
    <tr>
      <td>10433</td>
      <td>71129</td>
      <td>147.26</td>
    </tr>
    <tr>
      <td>10432</td>
      <td>72078</td>
      <td>147.75</td>
    </tr>
    <tr>
      <td>10431</td>
      <td>9525</td>
      <td>148.33</td>
    </tr>
    <tr>
      <td>10430</td>
      <td>69477</td>
      <td>148.80</td>
    </tr>
    <tr>
      <td>10429</td>
      <td>31223</td>
      <td>148.96</td>
    </tr>
    <tr>
      <td>10428</td>
      <td>44241</td>
      <td>150.39</td>
    </tr>
    <tr>
      <td>10427</td>
      <td>74923</td>
      <td>151.28</td>
    </tr>
    <tr>
      <td>10426</td>
      <td>40873</td>
      <td>152.07</td>
    </tr>
    <tr>
      <td>10425</td>
      <td>84109</td>
      <td>152.14</td>
    </tr>
    <tr>
      <td>10424</td>
      <td>84016</td>
      <td>152.24</td>
    </tr>
    <tr>
      <td>10423</td>
      <td>3057</td>
      <td>152.25</td>
    </tr>
    <tr>
      <td>10422</td>
      <td>76584</td>
      <td>152.31</td>
    </tr>
    <tr>
      <td>10421</td>
      <td>56633</td>
      <td>152.38</td>
    </tr>
    <tr>
      <td>10420</td>
      <td>62728</td>
      <td>152.39</td>
    </tr>
    <tr>
      <td>10419</td>
      <td>78351</td>
      <td>152.79</td>
    </tr>
    <tr>
      <td>10418</td>
      <td>18412</td>
      <td>152.80</td>
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
      <td>17601</td>
      <td>58272648.79</td>
    </tr>
    <tr>
      <td>2</td>
      <td>47036</td>
      <td>47335396.14</td>
    </tr>
    <tr>
      <td>3</td>
      <td>21677</td>
      <td>42162065.10</td>
    </tr>
    <tr>
      <td>4</td>
      <td>55898</td>
      <td>21133046.64</td>
    </tr>
    <tr>
      <td>5</td>
      <td>9260</td>
      <td>20061894.95</td>
    </tr>
    <tr>
      <td>6</td>
      <td>90190</td>
      <td>18558117.34</td>
    </tr>
    <tr>
      <td>7</td>
      <td>32839</td>
      <td>16256343.09</td>
    </tr>
    <tr>
      <td>8</td>
      <td>1319</td>
      <td>16066410.76</td>
    </tr>
    <tr>
      <td>9</td>
      <td>1884</td>
      <td>11490308.47</td>
    </tr>
    <tr>
      <td>10</td>
      <td>21133</td>
      <td>11376530.93</td>
    </tr>
    <tr>
      <td>11</td>
      <td>77787</td>
      <td>11087130.55</td>
    </tr>
    <tr>
      <td>12</td>
      <td>16294</td>
      <td>10748875.33</td>
    </tr>
    <tr>
      <td>13</td>
      <td>21454</td>
      <td>10565143.77</td>
    </tr>
    <tr>
      <td>14</td>
      <td>79308</td>
      <td>10537801.08</td>
    </tr>
    <tr>
      <td>15</td>
      <td>71381</td>
      <td>10368309.54</td>
    </tr>
    <tr>
      <td>16</td>
      <td>17085</td>
      <td>9999688.11</td>
    </tr>
    <tr>
      <td>17</td>
      <td>95783</td>
      <td>9706599.18</td>
    </tr>
    <tr>
      <td>18</td>
      <td>95331</td>
      <td>9610449.58</td>
    </tr>
    <tr>
      <td>19</td>
      <td>21218</td>
      <td>9462000.48</td>
    </tr>
    <tr>
      <td>20</td>
      <td>60553</td>
      <td>9275376.38</td>
    </tr>
    <tr>
      <td>21</td>
      <td>66967</td>
      <td>9264751.40</td>
    </tr>
    <tr>
      <td>22</td>
      <td>92398</td>
      <td>9127130.68</td>
    </tr>
    <tr>
      <td>23</td>
      <td>3651</td>
      <td>8942643.81</td>
    </tr>
    <tr>
      <td>24</td>
      <td>48839</td>
      <td>8444807.63</td>
    </tr>
    <tr>
      <td>25</td>
      <td>18717</td>
      <td>8055920.03</td>
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
      <td>10442</td>
      <td>57833</td>
      <td>3138.10</td>
    </tr>
    <tr>
      <td>10441</td>
      <td>55147</td>
      <td>3491.97</td>
    </tr>
    <tr>
      <td>10440</td>
      <td>9710</td>
      <td>4236.21</td>
    </tr>
    <tr>
      <td>10439</td>
      <td>18412</td>
      <td>4283.05</td>
    </tr>
    <tr>
      <td>10438</td>
      <td>3434</td>
      <td>4606.39</td>
    </tr>
    <tr>
      <td>10437</td>
      <td>23916</td>
      <td>4637.53</td>
    </tr>
    <tr>
      <td>10436</td>
      <td>67484</td>
      <td>4864.97</td>
    </tr>
    <tr>
      <td>10435</td>
      <td>44241</td>
      <td>5108.44</td>
    </tr>
    <tr>
      <td>10434</td>
      <td>33173</td>
      <td>5156.99</td>
    </tr>
    <tr>
      <td>10433</td>
      <td>12216</td>
      <td>5159.93</td>
    </tr>
    <tr>
      <td>10432</td>
      <td>71389</td>
      <td>5169.13</td>
    </tr>
    <tr>
      <td>10431</td>
      <td>87903</td>
      <td>5192.70</td>
    </tr>
    <tr>
      <td>10430</td>
      <td>20700</td>
      <td>5313.51</td>
    </tr>
    <tr>
      <td>10429</td>
      <td>37366</td>
      <td>5526.39</td>
    </tr>
    <tr>
      <td>10428</td>
      <td>31010</td>
      <td>5696.48</td>
    </tr>
    <tr>
      <td>10427</td>
      <td>6524</td>
      <td>5961.52</td>
    </tr>
    <tr>
      <td>10426</td>
      <td>75314</td>
      <td>5989.07</td>
    </tr>
    <tr>
      <td>10425</td>
      <td>5220</td>
      <td>6029.60</td>
    </tr>
    <tr>
      <td>10424</td>
      <td>2654</td>
      <td>6082.20</td>
    </tr>
    <tr>
      <td>10423</td>
      <td>67896</td>
      <td>6257.29</td>
    </tr>
    <tr>
      <td>10422</td>
      <td>26654</td>
      <td>6415.40</td>
    </tr>
    <tr>
      <td>10421</td>
      <td>70405</td>
      <td>6465.90</td>
    </tr>
    <tr>
      <td>10420</td>
      <td>43507</td>
      <td>6474.94</td>
    </tr>
    <tr>
      <td>10419</td>
      <td>9525</td>
      <td>6483.40</td>
    </tr>
    <tr>
      <td>10418</td>
      <td>78605</td>
      <td>6571.67</td>
    </tr>
  </tbody>
</table></br>  