run:
	py main.py 

1:
	py main.py < stdin1.txt


clean:
	find . -name '*.pyc' -exec rm -v {} \;

c:
	find . -name '*.pyc' -exec rm -v {} \;

loc:
	find . -name '*.py' -type f -exec grep . {} \; | wc -l
