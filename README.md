1. Create environment and activate it
2. Create requirements.txt and put required packages and install it using below command
```
pip install -r requirements.txt

```
3. Create data folder in the root of project
4. Create template.py to create structure of the project 
5. Create a data_given folder and put data file there
6. Make a repo on Github and keep on pushing the code wherever required
``` 
git init
dvc init
dvc add data_given/data_file
git add . && git commit -m "firs
t commit" 
git branch -M main
git remote add origin https://gi
thub.com/swatishayna/airqualitymlops.git
git push origin main

```
7. Stage1: Get the data: create afile inside src directory to get the data from data_given folder and add this stage in dvc.yaml
8. Stage2: load the data: create afile inside src directory to load the data and add this stage in dvc.yaml
9. Run in Terminal
```
dvc repro
```

 # This will generate dvc.lock file

10. Stage3:Perform train test split: Create a file in src folder and add this stage in dvc.yaml
11. Stage4: Train and Evaluate Model: Create a file in src folder and add this stage in dvc.yaml
12.Create directory report and add two files params.json and scores.json
    ```
    dvc repro
    dvc metrics show
    dvc metrics diff```
     

    
13. Make tox.ini file which will generate virtualenv and test ommand line tool
```
https://tox.readthedocs.io/en/latest/index.html

```
14. tox commands
```
tox
```
for rebuilding
```
tox -r
```
15. pytest commands
```
pytest-v
```
16. setup commands
```
pip install -e .
```
17. build package commands
```
python setup.py sdist bdist_wheel
```
