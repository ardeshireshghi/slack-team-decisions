.PHONY:	setup run clean deploy decision_logs oauth_logs

VENV	=	venv
PYTHON	=	$(VENV)/bin/python3
PIP	=	$(VENV)/bin/pip
DEPLOY_ENV	=	dev

setup:
	./scripts/setup.sh

run:
	.	$(VENV)/bin/activate
	sls	offline	--stage $(DEPLOY_ENV) start

deploy:
	sls	deploy --stage $(DEPLOY_ENV) --aws-s3-accelerate

decision_logs:
	sls logs --stage $(DEPLOY_ENV) -t --startTime 30m --function decision_handler

oauth_logs:
	sls logs --stage $(DEPLOY_ENV) -t --startTime 30m --function oauth_handler

clean:
	rm	-rf	__pycache__
	rm	-rf	$(VENV)

