# modeling-project

```
1. Amazon Review Classification
2. NYC Taxi Fare
3. Credit Card Transaction Fraud
4. Journal Paper Classification
5. EML
6. Fishing Email Detection
```

```
The data has been cleaned up somewhat; for example:

The dataset is comprised of only English reviews.
All text has been converted to lowercase.
There is white space around punctuation like periods, commas, and brackets.
Text has been split into one sentence per line.

After unzipping the file, you will have a directory called “txt_sentoken” with 
two sub-directories containing the text “neg” and “pos” for negative and 
positive reviews. Reviews are stored one per file with a naming convention 
cv000 to cv999 for each neg and pos. 

Data Preparation
In this section, we will look at 3 things:

Separation of data into training and test sets.
Loading and cleaning the data to remove punctuation and numbers.
Prepare all reviews and save to file.
```

```
Split into Train and Test Sets

After the model is developed, we will need to make predictions 
on new input data. This will require all of the same data preparation to 
be performed on those new data as is performed on the training data for the 
model.
We will ensure that this constraint is built into the evaluation of our models 
by splitting the training and test datasets prior to any data preparation. This 
means that any knowledge in the data in the test set that could help us better 
prepare the data (e.g. the words used) is unavailable in the preparation of 
data used for training the model. 
That being said, we will use the last 100 positive reviews and the last 100 
negative reviews as a test set (100 reviews) and the remaining 1,800 reviews as 
the training dataset. 
This is a 90% train, 10% split of the data.
```

```
Loading and Cleaning Reviews

Split tokens on white space.
Remove all punctuation from words.
Remove all words that are not purely comprised of alphabetical characters.
Remove all words that are known stop words.
Remove all words that have a length <= 1 character.
```


>GitHub Tricks: Upload Images & Live Demos

http://solutionoptimist.com/2013/12/28/awesome-github-tricks/

>Jupyter Lab project setup

https://florianwilhelm.info/2018/11/working_efficiently_with_jupyter_lab/

>Neural Network Projects with Python

https://github.com/PacktPublishing/Neural-Network-Projects-with-Python

>Confusion Matrix

https://www.python-course.eu/confusion_matrix.php

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
