# How to test

1. Edit the `DVC_REMOTE_URL` variable in the `Makefile` to change the URL of your DVC remote (the example uses a bucket from Iterative GCS which is not publicly accessible)
1. make sure that you have dvc installed globally (with pipx for instance) or you are using an environment where it is installed (`make dvc_project` assumes that DVC is installed)
1. Run `bash generate_projects.bash N` with `N` replaced by the number of projects you want to generate. This will create a number of projects which are set up with DVC initialized and a shared cache. The projects will each contain a randomized `params.yaml` file and copies of `script_template.py` and a `dvc_template.yaml` called `script.py` and `dvc.yaml`, respectively.
