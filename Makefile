.PHONY:	setup run clean deploy decision_logs oauth_logs

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

decision_logs:
	sls logs -t --function decision_handler

oauth_logs:
	sls logs -t --function oauth_handler

clean:
	rm	-rf	__pycache__
	rm	-rf	$(VENV)

