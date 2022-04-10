.PHONY:	setup	run	clean

VENV	=	venv
PYTHON	=	$(VENV)/bin/python3
PIP	=	$(VENV)/bin/pip

setup:
	./scripts/setup.sh

run:
	.	$(VENV)/bin/activate
	sls	offline	start

deploy:
	sls	deploy

clean:
	rm	-rf	__pycache__
	rm	-rf	$(VENV)

