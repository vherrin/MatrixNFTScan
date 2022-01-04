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
      <td>11538.91</td>
    </tr>
    <tr>
      <td>2</td>
      <td>29795</td>
      <td>6993.64</td>
    </tr>
    <tr>
      <td>3</td>
      <td>63467</td>
      <td>6768.26</td>
    </tr>
    <tr>
      <td>4</td>
      <td>86373</td>
      <td>6686.85</td>
    </tr>
    <tr>
      <td>5</td>
      <td>53836</td>
      <td>6639.36</td>
    </tr>
    <tr>
      <td>6</td>
      <td>49110</td>
      <td>6627.84</td>
    </tr>
    <tr>
      <td>7</td>
      <td>83101</td>
      <td>6620.44</td>
    </tr>
    <tr>
      <td>8</td>
      <td>68770</td>
      <td>6605.49</td>
    </tr>
    <tr>
      <td>9</td>
      <td>5135</td>
      <td>6576.79</td>
    </tr>
    <tr>
      <td>10</td>
      <td>22889</td>
      <td>6540.37</td>
    </tr>
    <tr>
      <td>11</td>
      <td>2942</td>
      <td>6535.14</td>
    </tr>
    <tr>
      <td>12</td>
      <td>93728</td>
      <td>6529.35</td>
    </tr>
    <tr>
      <td>13</td>
      <td>38379</td>
      <td>6528.32</td>
    </tr>
    <tr>
      <td>14</td>
      <td>63775</td>
      <td>6523.51</td>
    </tr>
    <tr>
      <td>15</td>
      <td>750</td>
      <td>6511.74</td>
    </tr>
    <tr>
      <td>16</td>
      <td>17313</td>
      <td>5376.45</td>
    </tr>
    <tr>
      <td>17</td>
      <td>81747</td>
      <td>5270.33</td>
    </tr>
    <tr>
      <td>18</td>
      <td>47263</td>
      <td>5124.61</td>
    </tr>
    <tr>
      <td>19</td>
      <td>39591</td>
      <td>5035.29</td>
    </tr>
    <tr>
      <td>20</td>
      <td>62311</td>
      <td>4985.29</td>
    </tr>
    <tr>
      <td>21</td>
      <td>44625</td>
      <td>4981.70</td>
    </tr>
    <tr>
      <td>22</td>
      <td>37120</td>
      <td>4978.67</td>
    </tr>
    <tr>
      <td>23</td>
      <td>52344</td>
      <td>4978.24</td>
    </tr>
    <tr>
      <td>24</td>
      <td>59977</td>
      <td>4976.56</td>
    </tr>
    <tr>
      <td>25</td>
      <td>74825</td>
      <td>4974.21</td>
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
      <td>97040</td>
      <td>15504</td>
      <td>29.49</td>
    </tr>
    <tr>
      <td>97039</td>
      <td>29479</td>
      <td>29.90</td>
    </tr>
    <tr>
      <td>97038</td>
      <td>70646</td>
      <td>29.94</td>
    </tr>
    <tr>
      <td>97037</td>
      <td>88333</td>
      <td>30.29</td>
    </tr>
    <tr>
      <td>97036</td>
      <td>23442</td>
      <td>30.80</td>
    </tr>
    <tr>
      <td>97035</td>
      <td>1189</td>
      <td>31.48</td>
    </tr>
    <tr>
      <td>97034</td>
      <td>12840</td>
      <td>31.50</td>
    </tr>
    <tr>
      <td>97033</td>
      <td>471</td>
      <td>31.54</td>
    </tr>
    <tr>
      <td>97032</td>
      <td>31021</td>
      <td>31.59</td>
    </tr>
    <tr>
      <td>97031</td>
      <td>69174</td>
      <td>31.80</td>
    </tr>
    <tr>
      <td>97030</td>
      <td>67863</td>
      <td>32.14</td>
    </tr>
    <tr>
      <td>97029</td>
      <td>22942</td>
      <td>32.18</td>
    </tr>
    <tr>
      <td>97028</td>
      <td>57198</td>
      <td>32.27</td>
    </tr>
    <tr>
      <td>97027</td>
      <td>12197</td>
      <td>32.31</td>
    </tr>
    <tr>
      <td>97026</td>
      <td>94080</td>
      <td>32.37</td>
    </tr>
    <tr>
      <td>97025</td>
      <td>94640</td>
      <td>32.80</td>
    </tr>
    <tr>
      <td>97024</td>
      <td>17248</td>
      <td>32.80</td>
    </tr>
    <tr>
      <td>97023</td>
      <td>2654</td>
      <td>32.91</td>
    </tr>
    <tr>
      <td>97022</td>
      <td>53827</td>
      <td>33.04</td>
    </tr>
    <tr>
      <td>97021</td>
      <td>30386</td>
      <td>33.17</td>
    </tr>
    <tr>
      <td>97020</td>
      <td>84020</td>
      <td>33.21</td>
    </tr>
    <tr>
      <td>97019</td>
      <td>16765</td>
      <td>33.36</td>
    </tr>
    <tr>
      <td>97018</td>
      <td>89747</td>
      <td>33.52</td>
    </tr>
    <tr>
      <td>97017</td>
      <td>59463</td>
      <td>33.70</td>
    </tr>
    <tr>
      <td>97016</td>
      <td>38555</td>
      <td>33.73</td>
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
      <td>4703.08</td>
    </tr>
    <tr>
      <td>2</td>
      <td>81747</td>
      <td>3955.62</td>
    </tr>
    <tr>
      <td>3</td>
      <td>47263</td>
      <td>1410.83</td>
    </tr>
    <tr>
      <td>4</td>
      <td>37120</td>
      <td>1021.01</td>
    </tr>
    <tr>
      <td>5</td>
      <td>74532</td>
      <td>926.12</td>
    </tr>
    <tr>
      <td>6</td>
      <td>33380</td>
      <td>909.40</td>
    </tr>
    <tr>
      <td>7</td>
      <td>46837</td>
      <td>831.74</td>
    </tr>
    <tr>
      <td>8</td>
      <td>74825</td>
      <td>807.58</td>
    </tr>
    <tr>
      <td>9</td>
      <td>17313</td>
      <td>800.97</td>
    </tr>
    <tr>
      <td>10</td>
      <td>69912</td>
      <td>784.79</td>
    </tr>
    <tr>
      <td>11</td>
      <td>43530</td>
      <td>780.36</td>
    </tr>
    <tr>
      <td>12</td>
      <td>39591</td>
      <td>751.24</td>
    </tr>
    <tr>
      <td>13</td>
      <td>49110</td>
      <td>745.77</td>
    </tr>
    <tr>
      <td>14</td>
      <td>5311</td>
      <td>726.69</td>
    </tr>
    <tr>
      <td>15</td>
      <td>62769</td>
      <td>722.29</td>
    </tr>
    <tr>
      <td>16</td>
      <td>10200</td>
      <td>702.91</td>
    </tr>
    <tr>
      <td>17</td>
      <td>26019</td>
      <td>701.65</td>
    </tr>
    <tr>
      <td>18</td>
      <td>44766</td>
      <td>700.85</td>
    </tr>
    <tr>
      <td>19</td>
      <td>1367</td>
      <td>694.40</td>
    </tr>
    <tr>
      <td>20</td>
      <td>29795</td>
      <td>670.53</td>
    </tr>
    <tr>
      <td>21</td>
      <td>53215</td>
      <td>667.91</td>
    </tr>
    <tr>
      <td>22</td>
      <td>83101</td>
      <td>664.92</td>
    </tr>
    <tr>
      <td>23</td>
      <td>70187</td>
      <td>661.67</td>
    </tr>
    <tr>
      <td>24</td>
      <td>70442</td>
      <td>652.70</td>
    </tr>
    <tr>
      <td>25</td>
      <td>16555</td>
      <td>640.65</td>
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
      <td>97040</td>
      <td>71614</td>
      <td>5.96</td>
    </tr>
    <tr>
      <td>97039</td>
      <td>67863</td>
      <td>6.05</td>
    </tr>
    <tr>
      <td>97038</td>
      <td>15504</td>
      <td>6.13</td>
    </tr>
    <tr>
      <td>97037</td>
      <td>8415</td>
      <td>6.16</td>
    </tr>
    <tr>
      <td>97036</td>
      <td>88333</td>
      <td>6.27</td>
    </tr>
    <tr>
      <td>97035</td>
      <td>2654</td>
      <td>6.29</td>
    </tr>
    <tr>
      <td>97034</td>
      <td>23442</td>
      <td>6.30</td>
    </tr>
    <tr>
      <td>97033</td>
      <td>48815</td>
      <td>6.32</td>
    </tr>
    <tr>
      <td>97032</td>
      <td>48794</td>
      <td>6.32</td>
    </tr>
    <tr>
      <td>97031</td>
      <td>29479</td>
      <td>6.37</td>
    </tr>
    <tr>
      <td>97030</td>
      <td>70646</td>
      <td>6.37</td>
    </tr>
    <tr>
      <td>97029</td>
      <td>31021</td>
      <td>6.38</td>
    </tr>
    <tr>
      <td>97028</td>
      <td>57198</td>
      <td>6.42</td>
    </tr>
    <tr>
      <td>97027</td>
      <td>1189</td>
      <td>6.52</td>
    </tr>
    <tr>
      <td>97026</td>
      <td>471</td>
      <td>6.53</td>
    </tr>
    <tr>
      <td>97025</td>
      <td>35298</td>
      <td>6.63</td>
    </tr>
    <tr>
      <td>97024</td>
      <td>9827</td>
      <td>6.66</td>
    </tr>
    <tr>
      <td>97023</td>
      <td>19115</td>
      <td>6.66</td>
    </tr>
    <tr>
      <td>97022</td>
      <td>56777</td>
      <td>6.66</td>
    </tr>
    <tr>
      <td>97021</td>
      <td>53827</td>
      <td>6.67</td>
    </tr>
    <tr>
      <td>97020</td>
      <td>20364</td>
      <td>6.70</td>
    </tr>
    <tr>
      <td>97019</td>
      <td>84020</td>
      <td>6.71</td>
    </tr>
    <tr>
      <td>97018</td>
      <td>92937</td>
      <td>6.71</td>
    </tr>
    <tr>
      <td>97017</td>
      <td>20504</td>
      <td>6.78</td>
    </tr>
    <tr>
      <td>97016</td>
      <td>12840</td>
      <td>6.78</td>
    </tr>
  </tbody>
</table></br>  