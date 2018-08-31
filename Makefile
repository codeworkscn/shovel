init:
    python2 -m pip install -r requirements.txt

test:
    python2 py.test tests

.PHONY: init test
