## shovel
Tools suite for DevOps, build by Python

### Ho to Build

- install requirements: `python2 -m pip install -r requirements.txt`
- install shovel: `python2 setup.py install`
- create tar.gz: `python2 setup.py sdist --formats=gztar`
- create zip: `python2 setup.py sdist --formats=zip`
- install from zip: `python2 -m pip install shovel-0.0.1.zip`

### feature list

- VSC tools
  - [x] p4 integrate by job
  - [ ] initial import git repository from p4 export
  - [ ] auto sync from p4 to git
- elasticsearch tools
  - [x] data compare between indices
  - [ ] data reindex migration from index to another
  
- others
  - ...

### config guide

configuration items are locate in configuration file `shovel_config.yaml`. 

init your own configuration, follow steps:
1. copy `shovel_config_template.yaml` as `shovel_config.yaml`
    - Linux `cp shovel_config_template.yaml shovel_config.yaml`
    - Windows `copy shovel_config_template.yaml shovel_config.yaml`
1. set configuration value in `shovel_config.yaml`

### tools usage samples

- `python2 scripts/p4integratebyjob.py -j MyP4JobId`
- `python2 scripts/elasticsearchcompare.py --leftIndex=tmcas_violation_2018.09  --rightIndex=tmcas_violation_compare_2018.09 --queryStmtFile=config/ElasticCompare/es-compare-query-stmt-violation.json --keyFields=tm_violator,tm_timestamp,tm_trace_id`
- `python2 scripts/elasticsearchcompare.py --leftIndex=tmcas_quarantine_2018.09  --rightIndex=tmcas_quarantine_compare_2018.09 --queryStmtFile=config/ElasticCompare/es-compare-query-stmt-storage-quarantine.json --keyFields=tm_violator,tm_timestamp,tm_trace_id`

### references

- [P4Python API Scripting Guide (2017.2)](https://www.perforce.com/perforce/doc.current/manuals/p4python/index.html)
- [P4Python Classes](https://www.perforce.com/perforce/doc.current/manuals/p4python/index.html#P4Python/python.classes.html%3FTocPath%3DP4Python%7CP4Python%2520Classes%7C_____0)
- [GitPython Tutorial](https://gitpython.readthedocs.io/en/stable/tutorial.html)
- [git-p4 Import from and submit to Perforce repositories](https://git-scm.com/docs/git-p4)
