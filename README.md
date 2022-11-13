# nsepy2

<h2>The objective</h2>
To build an OpenLibrary which can be utilised to consume stock related data available in public domain. Currently, stocks which are traded at NSE-India are only being considered.

<h2>Inspiration and Current State</h2>
As the original repo 'NSEpy' is not being actively developed, I am trying to extend the project as much as I can. Please be so kind to contribute as much as you can. Small contributions can also help.

This project is inspired from 'NSEpy' -> https://github.com/swapniljariwala/nsepy.

<h2>Phases</h2>
<ol>
  <li>Documentation for NSEpy</li>
  <li>New development</li>
  <li>Ammend Documentation</li>
 </ol>
 

<h3>Current phase: Documentation for NSEpy</h3>
At this moment I am just preparing some documentation so that it'll be easier for others to use 'NSEpy'.


<table>
 <thead>
  <tr>
    <th>Usage</th>
    <th>Functions</th>
  </tr>
  </thead>
  <tbody>
    <tr>
      <td>List of securities / scrips traded at NSE</td>
      <td>

```python

      from nsepy.symbols import *
      scrip_list = get_symbol_list()
      scrip_list.columns = ['SYMBOL', 'NAME OF COMPANY', 'SERIES', 'DATE OF LISTING','PAID UP VALUE', 'MARKET LOT', 'ISIN NUMBER', 'FACE VALUE']

```

</td>
</tr>
    <tr>
      <td>Historical EOD data, From Date until To date</td>
      <td>
```python

data_2001 = get_history(symbol="SBIN", start=date(2001,1,1), end=date(2001,12,31))


```
      
      </td>
    </tr>
  </tbody>
</table>




