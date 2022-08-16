# Kidney-Disease-Prediction
A Chronic Disease is a major chronic disease associated with ageing, hypertension and diabetes generally affecting people 40 and more.
It affects 10% of the world population.
It does not show any symptoms and may lose up to 25% of kidney function before symptoms arise.
Kidney disease also increases the risk of having heart and blood vessel disease. These problems may happen slowly over a long time. Early detection and treatment can often keep chronic kidney disease from getting worse. When kidney disease progresses, it may eventually lead to kidney failure, which requires dialysis or a kidney transplant to maintain life.
# Existing System   
2 tests are used to detect Chronic Kidney Disease in labs
ACR (Albumin to Creatinine Ratio)
This is a urine Sample Test to check the ACR( Albumin Creatinine Ration) Albumin is Produced by the liver and it circulates in the blood. If Kidney Works Properly then Albumin should not come in our urine. Creatinine is an endogenous product of muscle metabolism.
ACR= Albumun/Creatinine
If the Value of ACR is around 30 then it means Your Kidney Works Properly because albumin does not come in your urine.
In Worst Condition, these ACR value goes to 300-400.
Albuminuria (ACR) Categories:
Category	ACR(mg/mmol)	Description
A1	<3 mg/mmol	Normal to mildly increased
A2	3-30 mg/mmol	Moderately increased (CKD)
A3	>30 mg/mmol	Severely increased (CKD)
GFR (glomerular filtration rate). GFR is a measure of kidney function and is performed through a blood test. Your GFR will determine what stage of kidney disease you have 
A GFR of 60 or higher is in the normal range. A GFR below 60 may mean kidney disease. A GFR of 15 or lower may mean kidney failure.
The disadvantage of the Existing System
Very Few systems use the available clinical data for classification purposes and even if they do, they are restricted by the large number of association rules that apply.
Detection is not possible in the early stage.
In the existing system, practical use of various collected data is time-consuming.
# Advantages of My Model
Classification is very flexible
Better Healthcare services less healthcare cost
Decrease Mortality rate
Faster result and Good Accuracy

#  Data Preprocessing 
Datasets are susceptible to missing, noisy, redundant and inconsistent data especially clinical datasets working with low-quality data lead to the low-quality result
Outlier
Outlier is an extreme value located far away from the features central tendency. Invalid outliers occur due to data entry errors which cause noise in the data
Missing Values
In real-world datasets missing data is a very common issue, especially in the medical area. Usually, every patient record and every attribute contains some missing values. Therefore the chronic Kidney Disease dataset has around 78% of its variables having missing value; around 56% of cases have at least one missing value and 10% have all values are missing.
Data Reduction
Data reduction means reducing the number of features while maintaining a good analytical result. For this purpose, the feature selection correlation types technique has been used to remove redundant information.
Data Transformation
Data is transformed into appropriate forms for modelling purposes. This includes the normalization process of scaling the values of the attributes to fall within a small specific range. It is usually applied before feature selection and modelling stages because different scales of attributes complicate the comparison of attributes and influence the ability of algorithms to learn
Feature Selection
The process of selecting the most discriminating features in a given dataset is known as feature selection. This process is enhancing the model performance, reducing overfitting and reducing the cost  of building a model 
Filter features selection methods select features that have a stronger relationship with the outcome variable independent of the learning model.
After the data preprocessing and data cleaning the next phase is to divide the data for the training and testing of our model.
Generally, the training and validation data set is split into an 80:20 ratio. The test data set remains hidden during the model training and model performance evaluation stage. 
                               
# The Algorithm I use in this model is supervised (Classification) Machine Learning.
1) Logistic Regression
3) Decision Tree
2) Random Forest
3) KNN

