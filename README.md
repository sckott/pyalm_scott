pyalm
=======

<pre>
         __      | 			|\      /|
        /  \     | 			| \    / |
       / -- \    | 			|  \  /  |
      /      \   | 			|   \/   |
     /        \  |_______ 	|        |
</pre>


**This is a port of the R wrapper to PLOS ALM called `alm`, see [here](https://github.com/ropensci/alm).**


### What it is!?

`alm` is a set of functions to access article level metrics from the Public Library of Science journals using their ALM API. 


### What is an article level metric? 

Glad you asked. The canonical URL for this is perhaps [altmetrics.org](http://altmetrics.org/manifesto/). Basically it is a metric that measures something about an article. This is in stark contrast to journal level metrics, like the Journal Impact Factor. 

### Authentication

You are required to use an API key to access the PLoS ALM API. Get your key [here](http://alm.plos.org/)

You can pass your key in to the functions.

### Tutorials and help

*Coming soon* 

<!-- alm tutorial at rOpenSci website [here](#) -->

### Quick start

#### Download and install pyalm

```bash
git clone https://github.com/SChamberlain/pyalm.git
cd pyalm
python setup.py install
```

#### Load pyalm

```python
import pyalm
```

#### Get altmetrics for two DOIs

```python
pyalm.alm(doi=['10.1371/journal.pone.0001543','10.1371/journal.pone.0040117'], key=<yourplosalmapikey>)
```

```
[                  citations  comments  groups  html  likes  pdf  shares  total
bloglines                 0       NaN     NaN   NaN    NaN  NaN     NaN      0
citeulike               NaN       NaN     NaN   NaN    NaN  NaN       0      0
connotea                  0       NaN     NaN   NaN    NaN  NaN     NaN      0
crossref                  1       NaN     NaN   NaN    NaN  NaN     NaN      1
nature                    0       NaN     NaN   NaN    NaN  NaN     NaN      0
postgenomic               0       NaN     NaN   NaN    NaN  NaN     NaN      0
pubmed                    1       NaN     NaN   NaN    NaN  NaN     NaN      1
scopus                    3       NaN     NaN   NaN    NaN  NaN     NaN      3
counter                 NaN       NaN     NaN  1158    NaN  249     NaN   1419
researchblogging          0       NaN     NaN   NaN    NaN  NaN     NaN      0
biod                    NaN       NaN     NaN   NaN    NaN  NaN     NaN      0
pmc                     NaN       NaN     NaN   181    NaN   64     NaN    245
facebook                NaN         0     NaN   NaN      0  NaN       0      0
mendeley                NaN       NaN       0   NaN    NaN  NaN       8      8
twitter                 NaN         0     NaN   NaN    NaN  NaN     NaN      0
wikipedia                 0       NaN     NaN   NaN    NaN  NaN     NaN      0
scienceseeker             0       NaN     NaN   NaN    NaN  NaN     NaN      0
relativemetric          NaN       NaN     NaN   NaN    NaN  NaN     NaN  46962
f1000                     0       NaN     NaN   NaN    NaN  NaN     NaN      0
figshare                NaN       NaN     NaN     3      0    0     NaN      3
pmceurope                 0       NaN     NaN   NaN    NaN  NaN     NaN      0
pmceuropedata             0       NaN     NaN   NaN    NaN  NaN     NaN      0
openedition               0       NaN     NaN   NaN    NaN  NaN     NaN      0
wordpress                 0       NaN     NaN   NaN    NaN  NaN     NaN      0
reddit                    0       NaN     NaN   NaN    NaN  NaN     NaN      0,
                   citations  comments  groups  html  likes  pdf  shares   total
bloglines                 0       NaN     NaN   NaN    NaN  NaN     NaN       0
citeulike               NaN       NaN     NaN   NaN    NaN  NaN       0       0
connotea                  0       NaN     NaN   NaN    NaN  NaN     NaN       0
crossref                  5       NaN     NaN   NaN    NaN  NaN     NaN       5
nature                    0       NaN     NaN   NaN    NaN  NaN     NaN       0
postgenomic               1       NaN     NaN   NaN    NaN  NaN     NaN       1
pubmed                    6       NaN     NaN   NaN    NaN  NaN     NaN       6
scopus                    7       NaN     NaN   NaN    NaN  NaN     NaN       7
counter                 NaN       NaN     NaN  2500    NaN  414     NaN    2953
researchblogging          0       NaN     NaN   NaN    NaN  NaN     NaN       0
biod                    NaN       NaN     NaN   NaN    NaN  NaN     NaN       0
pmc                     NaN       NaN     NaN   340    NaN  207     NaN     547
facebook                NaN         0     NaN   NaN      0  NaN       0       0
mendeley                NaN       NaN       0   NaN    NaN  NaN       8       8
twitter                 NaN         0     NaN   NaN    NaN  NaN     NaN       0
wikipedia                 0       NaN     NaN   NaN    NaN  NaN     NaN       0
scienceseeker             0       NaN     NaN   NaN    NaN  NaN     NaN       0
relativemetric          NaN       NaN     NaN   NaN    NaN  NaN     NaN  646087
f1000                     0       NaN     NaN   NaN    NaN  NaN     NaN       0
figshare                  0       NaN     NaN   NaN    NaN  NaN     NaN       0
pmceurope                 6       NaN     NaN   NaN    NaN  NaN     NaN       6
pmceuropedata             0       NaN     NaN   NaN    NaN  NaN     NaN       0
openedition               0       NaN     NaN   NaN    NaN  NaN     NaN       0
wordpress                 0       NaN     NaN   NaN    NaN  NaN     NaN       0
reddit                    0       NaN     NaN   NaN    NaN  NaN     NaN       0]
```


This code is released under the MIT license; please see LICENSE for more details.