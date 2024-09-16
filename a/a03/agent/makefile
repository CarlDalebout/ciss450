run:
	python main.py 

1:
	python main.py < stdin1.txt


clean:
	find . -name '*.pyc' -exec rm -v {} \;

c:
	find . -name '*.pyc' -exec rm -v {} \;

loc:
	find . -name '*.py' -type f -exec grep . {} \; | wc -l
