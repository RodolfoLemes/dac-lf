$(eval $(shell test -f .env  || touch .env))
include .env
$(eval export $(shell sed -ne 's/ *#.*$$//; /./ s/=.*$$// p' .env))

## Config values from .env file
########################################################################################################################

export TF_VAR_web_domain_name = $(WEB_DOMAIN_NAME)
export TF_VAR_aws_access_key_id = $(AWS_ACCESS_KEY_ID)
export TF_VAR_aws_secret_access_key = $(AWS_SECRET_ACCESS_KEY)
export TF_VAR_region = $(REGION)

export AWS_DEFAULT_REGION = $(TF_VAR_region)

deploy:
	bin/deploy.sh