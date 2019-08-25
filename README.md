# modeling-project

```
1. Amazon Review Classification
2. NYC Taxi Fare
3. Credit Card Transaction Fraud
4. Journal Paper Classification
```

```
The data has been cleaned up somewhat; for example:

The dataset is comprised of only English reviews.
All text has been converted to lowercase.
There is white space around punctuation like periods, commas, and brackets.
Text has been split into one sentence per line.

After unzipping the file, you will have a directory called “txt_sentoken” with two sub-directories containing the text “neg” and “pos” for negative and positive reviews. Reviews are stored one per file with a naming convention cv000 to cv999 for each neg and pos.

Data Preparation
In this section, we will look at 3 things:

Separation of data into training and test sets.
Loading and cleaning the data to remove punctuation and numbers.
Prepare all reviews and save to file.

```


>GitHub Tricks: Upload Images & Live Demos

http://solutionoptimist.com/2013/12/28/awesome-github-tricks/

>Jupyter Lab project setup

https://florianwilhelm.info/2018/11/working_efficiently_with_jupyter_lab/

>Neural Network Projects with Python

https://github.com/PacktPublishing/Neural-Network-Projects-with-Python

>How to delete condo envs

```
$ conda info --envs
$ conda remove --name modeling_project --all
```

>How to create project

```
$ conda create -n modeling_project python=3.6 jupyterlab pandas scikit-learn seaborn
$ conda activate modeling_project

$ conda install -c conda-forge pyscaffold
$ putup modeling_project

$ cd modeling_project

$ python setup.py develop
```
