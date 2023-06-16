# Globals to be included into all Makefiles
# specification of the used openapi-generator-cli (see also https://github.com/ITISFoundation/openapi-generator)

REPO_ROOT               := $(realpath $(dir $(abspath $(lastword $(MAKEFILE_LIST))))/..)
SCRIPTS_DIR             := $(REPO_ROOT)/scripts
CLIENTS_DIR             := $(REPO_ROOT)/clients

OPENAPI_GENERATOR_NAME  := itisfoundation/openapi-generator-cli-openapi-generator-v4.2.3
OPENAPI_GENERATOR_TAG   := v0
OPENAPI_GENERATOR_IMAGE := $(OPENAPI_GENERATOR_NAME):$(OPENAPI_GENERATOR_TAG)

REL_API_JSON_PATH       := api/openapi.json
ABS_API_JSON_PATH       := $(API_DIR)/$(REL_API_JSON_PATH)

GIT_USER_ID := ITISFoundation
GIT_CLIENT_REPO_ID := osparc-simcore-clients
GIT_OPENAPI_REPO_ID := openapi-generator
GENERATOR_NAME := python
ADDITIONAL_PROPS := \
	generateSourceCodeOnly=false\
	hideGenerationTimestamp=true\
	library=urllib3\
	packageName=osparc\
	packageUrl=https://github.com/$(GIT_USER_ID)/${GIT_CLIENT_REPO_ID}.git\
	packageVersion=$(APP_VERSION)\
	projectName=osparc-simcore-python-api
ADDITIONAL_PROPS := $(foreach prop,$(ADDITIONAL_PROPS),$(strip $(prop)))

null  :=
space := $(null) #
comma := ,


help: ## help on rule's targets
	@awk --posix 'BEGIN {FS = ":.*?## "} /^[[:alpha:][:space:]_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

# Validate openapi specification --------------------------------------------------------------

validate-api-specification: ## validates openapi-specification
	@docker run --rm \
			--volume "$(REPO_ROOT):/local" \
			$(OPENAPI_GENERATOR_IMAGE) validate --input-spec /local/$(REL_API_JSON_PATH)