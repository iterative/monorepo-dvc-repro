# How to test

1. Run `bash generate_projects.bash N` with `N` replaced by the number of projects you want to generate (to see the issue in effect choose a large `N`, to see the logs clearly, choose a small `N`)
1. Go to one of the project subdirectories, run
    ```
    time dvc exp run -vvv
    ```
    and observe how DVC still crawls through the whole monorepo (all projects). This slows things down considerably for large monorepos. The same issue appears with `dvc repro`, except that it does a bit less. Explicitly providing the target `dvc.yaml` file to `dvc repro` does not affect this.