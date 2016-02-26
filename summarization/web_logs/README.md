#Exploring the Bentley's web logs
Provides a relatively simple interface to extract summarized info from the Bentley's server logs.

##Requirements:

* [apache-log-parser](https://github.com/rory/apache-log-parser)
* [tqdm](https://github.com/noamraph/tqdm)

##Usage

###Loading data
First, load an initial web log:
```python
parser = BentleyWebLogParser("path/to/log/file")
```

The parser will automatically remove all bot entries, as well as requests that were not to html pages (like for css, js, or image files)

You can load additional log data if you want to process data from multiple exports:
```python
parser.add_logs("path/to/new/log/file")
```

You can save a lot of future loading time by saving a parsed raw log file in json format, then loading from that instead 
in the future. All you need to make this happen is to run the ```save_log_to_json()``` method:
```python
parser.save_log_to_json()
```

This will output a .json file. You can load these directly into the parser just as you would the normal raw-text server log files:
```python
parser = BentleyWebLogParser("path/to/json/file")

parser.add_logs("path/to/json/file")
```

The json files load much faster, since the parser doesn't need to manually process each individual line.


###Summarizations
Get a count of all unique visitors:
```python
>>> parser.unique_visitor_count()
18754
```

Get a count of total page requests made:
```python
>>> parser.total_page_requests_count()
87552
```

Get a sorted list of most-searched-for search terms. Search terms are all normalized to lowercase.
```python
>>> parser.raw_search_counts(results_limit=50)  # results_limit limits the results to the top n entries
[(u'republican', 285),
 (u'john harvey kellogg', 245),
 (u'duderstadt', 235),
 (u'democratic', 234),
 (u'radio', 217),
 (u'albert kahn papers', 204),
 (...)
]
```

Get a sorted list of search terms ordered by number of unique users making that search:
```python
>>> parser.unique_users_per_search_term(results_limit=50)
[(u'keijo', 104),
 (u'albert kahn papers', 74),
 (u'bells', 40),
 (u'mercywood', 36),
 (u'albert kahn', 32),
 (u'duderstadt', 22),
 (u'william lebaron jenney', 21),
 (u'reginald malcolmson', 20),
 (...)
]
```

Get a sorted list of most-visited finding aids
```python
>>> parser.raw_finding_aid_visit_counts(results_limit=50)
[(u'umich-bhl-0420', 1925),
 (u'umich-bhl-97105', 756),
 (u'umich-bhl-943', 711),
 (u'umich-bhl-0081', 636),
 (u'umich-bhl-2014106', 541),
 (...)
]
```

Get a sorted list of finding aids ordered by number of unique visitors
```python
>>> parser.unique_users_per_finding_aid(results_limit=50)
[(u'umich-bhl-0420', 656),
 (u'umich-bhl-97105', 307),
 (u'umich-bhl-9915', 260),
 (u'umich-bhl-0081', 197),
 (u'umich-bhl-850', 179),
 (...)
]
```

Get a summary of data for a single finding aid by its identifier
```python
>>> parser.get_stats_for_single_finding_aid_by_identifier('umich-bhl-0420')
{'identifier': 'umich-bhl-0420',
 'total views': 1925,
 'unique user count': 656,
 'associated queries': [(u'albert kahn papers', 146),
                        (u'albert kahn', 86),
                        (u'willow run', 28),
                        (u'durant', 26),
                        (u'hill', 21),
                        (u'russia', 17),
                        (...)
}
```

Get a summary for a set of finding aids by a list of identifiers
```python
>>> parser.get_stats_for_multiple_finding_aids_by_identifier(['umich-bhl-0420', 'umich-bhl-2009082', 'umich-bhl-97115'])
{'identifiers': ['umich-bhl-0420', 'umich-bhl-2009082', 'umich-bhl-97115'],
 'total views': 2129,
 'unique user count': 785,
 'associated queries': [(u'albert kahn papers', 146),
                        (u'albert kahn', 86),
                        (u'willow run', 28),
                        (u'durant', 26),
                        (u'hill', 21),
                        (u'russia', 17),
                        (...)
}
```

Get a list of where our traffic is coming from:
```python
>>> parser.get_referer_counts(results_limit=50)
[(u'https://www.google.com', 8643),
 (u'http://bentley.umich.edu/legacy-support/EAD', 2977),
 (u'http://quod.lib.umich.edu/cgi/f/findaid/findaid-idx?&page=simple&c=bhlead', 1964),
 (u'http://bentley.umich.edu/legacy-support/EAD/ead_uofm.php', 1549),
 (u'http://quod.lib.umich.edu', 969),
 (u'http://bentley.umich.edu/legacy-support/EAD/ead_ab.php', 579),
 (u'http://quod.lib.umich.edu/b/bhlead?page=simple', 451),
 (u'http://quod.lib.umich.edu/cgi/f/findaid/findaid-idx?c=bhlead;page=simple', 344),
 (u'http://quod.lib.umich.edu/cgi/f/findaid/findaid-idx?c=bhlead;page=boolean', 301),
 (u'http://bentley.umich.edu/legacy-support/EAD/ead_kl.php', 298),
 (u'https://www.google.ca', 286),
 (...)
]
```