## shovel
Tools suite for DevOps, build by Python

[TOC]


### feature list

- VSC tools
  - [x] p4 integrate by job
  - [ ] initial import git repository from p4 export
  - [ ] auto sync from p4 to git
- elasticsearch tools
  - [x] data compare between indices
  - [ ] data reindex migration from index to another
- file tools
  - [x] transform csv to json
  - [x] transform json to csv
- monitor tools
  - [ ] cron job manage
- mail tools
  - [ ] new mail receive trigger
- others
  - ...


### Build Guide

#### how to install

- install requirements: `python2 -m pip install -r requirements.txt`
- install shovel: `python2 setup.py install`
- create tar.gz: `python2 setup.py sdist --formats=gztar`
- create zip: `python2 setup.py sdist --formats=zip`
- install from zip: `python2 -m pip install shovel-0.0.1.zip`

#### how to Unit Testing
- run all tests: `python -m unittest discover tests "Test*.py"`
- run specific tests: `python tests/TestFileTransform.py`

### Usage Guide

#### create your configuration file

configuration items are locate in configuration file `shovel_config.yaml`. 

init your own configuration, follow steps:
1. copy `shovel_config_template.yaml` as `shovel_config.yaml`
    - Linux `cp shovel_config_template.yaml shovel_config.yaml`
    - Windows `copy shovel_config_template.yaml shovel_config.yaml`
2. set configuration value in `shovel_config.yaml`

#### tools usage samples

- `python2 scripts/p4integratebyjob.py -j MyP4JobId`
- `python2 scripts/elasticsearchcompare.py --leftIndex=codeworks_2018.*  --rightIndex=codeworks_compare_2018.* --queryStmtFile=samples/es-query-stmt-sample.json --keyFields=timestamp,user_email`
- `python2 scripts/csv2json.py --source=a.csv --target=a.json`
- `python2 scripts/json2csv.py --source=b.json --target=b.csv`

---

### references

- [The Hitchhiker’s Guide to Python -- Structuring Your Project](https://docs.python-guide.org/writing/structure/)
- [P4Python API Scripting Guide (2017.2)](https://www.perforce.com/perforce/doc.current/manuals/p4python/index.html)
- [P4Python Classes](https://www.perforce.com/perforce/doc.current/manuals/p4python/index.html#P4Python/python.classes.html%3FTocPath%3DP4Python%7CP4Python%2520Classes%7C_____0)
- [GitPython Tutorial](https://gitpython.readthedocs.io/en/stable/tutorial.html)
- [git-p4 Import from and submit to Perforce repositories](https://git-scm.com/docs/git-p4)
- [Python2 argparse](https://docs.python.org/2/library/argparse.html)
