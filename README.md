# slack-team-decisions

This is a simple Slack application built using serverless framework in AWS written in Python which handles creation and listing of team decisions in Slack channels.

## About the project

This simple Python serverless app is aimed to solve the problem of teams making decisions in Slack and are not able to easily find and use those decisions. It makes use of Slack search API and command to create decision messages and also be able to get a list of those messages sorted.

### Built with

The code is written in Python using Serverless Framework.

### Required packages

Make sure `Node.js` and `python3` and `make` are installed.

### Development

Use `make setup` to install dependencies and setup Python virtual env. Then use `make run` to run the application using `serverless offline` plugin.

### Deploy to AWS

Make sure AWS is configured and IAM user has necessary permissions to create Cloudformation stack as well as Lambda functions and AWS API Gateway. Run:

```sh
$ make deploy
```

The deployment creates 2 API endpoints with below function names:

```
decision_handler
oauth_handler
```

`oauth_handler` is used for Slack's OAuth2 flow.
