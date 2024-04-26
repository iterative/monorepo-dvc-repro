# path to the shared DVC cache used by all projects
DVC_SHARED_CACHE_PATH=../dvc_shared_cache
# URL of the DVC remote used in all projects in the monorepo
DVC_REMOTE_URL=gs://dvc-cse/example-tempus

.PHONY: help venv dvc_project

# HELP
# This will output the help for each task
# thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-z%A-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

venv: ## set up a simple python virtual environment and install requirements
	python3 -m venv .venv \
	&& source .venv/bin/activate \
	&& python3 -m pip install --upgrade pip wheel \
	&& python3 -m pip install -r requirements.txt

dvc_project: ## creates and initializes a dvc project, links it to a shared cache and a DVC remote, call by `projectdir=<name of your project directory> make dvc_project`
	source .venv/bin/activate \
	&& mkdir -p $(projectdir) \
	&& cd $(projectdir) \
	&& dvc init --subdir \
	&& dvc cache dir $(DVC_SHARED_CACHE_PATH) \
	&& dvc config cache.shared group \
	&& dvc config cache.type symlink \
	&& dvc remote add -d myremote $(DVC_REMOTE_URL)