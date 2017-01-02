all:
	@echo downloading python nltk tagger
	@python2 -c "import nltk; nltk.download('averaged_perceptron_tagger')"
	@echo
	@echo please create a file called credentials with the following data:
	@echo "oatoken = 'yourOAuthToken'"
	@echo "oasecret = 'yourOAuthSecret'"
	@echo "conskey = 'yourConsumerKey'"
	@echo "conssecret = 'yourConsSecret'"
	@echo
	@echo you can get these by creating a twitter app
