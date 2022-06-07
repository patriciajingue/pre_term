# Pre-term risk prediction
## Welcome to my GitHub repository on using Predictive Analytics model to determine the probability of pre-term birth.
### Objective:
The repository is a learning exercise to:
* Apply the fundamental concepts of machine learning from a dataset
* Evaluate and interpret my result and justify my interpretation based on observed dataset.
##### The analysis is divided into four section
1. Identifying the problem from the raw Data
2. Exploratory Data Analysis
3. Pre-processing the data
4. Build model to predict the probability of having a preterm baby based on certain features
### file 1: Identifying the problem and getting data
##### Goal: Identify the information conatined in our data
I used python modules to import external datasets for the purpose of getting familiarize with the data an see patterns in other to solve the problem
##### Exploratory Data Analysis
Explored the variables to assess how they relate to the response variable In this notebook, I am getting familiar with the data using data exploration and visualization techniques using python libraries (Pandas, matplotlib, seaborn. Familiarity with the data is important which will provide useful knowledge for data pre-processing)
##### Pre-Processing the data
 I used feature selection to reduce high-dimension data, feature extraction and transformation for dimensionality reduction. This is essential in preparing the data before predictive models are developed.
##### Predictive model using Logistic Regression 
Constructed a predictive model using Logistic Regression learning algorithm to predict the probability of a preterm birth. The diagnosis of a preterm is a binary variable (0[full Term] or 1[preterm]). I also evaluate the model using confusion matrix and since I have an imbalance dataset i choosed the technique of undersampling as the data is not alot, which are essential in assessing and interpreting the fitted model.
