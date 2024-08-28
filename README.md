# Data Science Project

## Research Question:

What is the impact on overall weight loss from the combined effect of
reducing calories and increasing exercise? Is there a synergistic
effect?

## Executive Summary

This project explores an individual's weight loss journey, focusing on
the effects of calorie intake and exercise over several months. Through
data analysis, the study identifies key patterns in weight changes
related to diet and physical activity.

Using regression analysis and forecasting, the study predicts future
weight trends and provides insights into effective weight management
strategies. The findings reveal that regular exercise and controlled
calorie intake are critical for sustainable weight loss.

## 

## Introduction

This project delves into an individual's weight loss journey, focusing
on the effects of calorie intake and exercise over a period of a few
months. By analysing these factors, this study aims to provide

valuable insights into the relationship between diet, physical activity,
and weight management. The findings will offer evidence-based strategies
for individuals dedicated to achieving effective and sustainable weight
loss.

## 

## Methods

### Data Collection

**Source**: This dataset was found from Kaggle [Calorie, Exercise and Weight Changes](https://www.kaggle.com/datasets/chrisbow/2018-calorie-exercise-and-weight-changes)

**Variables**: Critical variables include date, weight in oz, calories,
walk, run, weight.

**Data Prep/Cleaning**: Changed the format from American to English for
dates, added in additional columns for:

- **Weight in grams:** A unified weight metric in grams was created to
  standardise and aggregate measurements originally recorded in stones,
  pounds, and ounces, facilitating easier analysis and comparison.

- **Exercise indicator:** The dataset originally included three separate
  columns to capture exercise activity. These were consolidated into a
  single column indicating whether any exercise was performed each day,
  improving data consistency and reducing redundancy.

- **Daily weight change in ounces (weight_dif_in_oz):** This feature
  represents the difference in weight (in ounces) between consecutive
  days, calculated as the current day's weight in ounces minus the
  previous day's weight in ounces.

- **Daily weight change in grams (weight_dif_in_g):** This metric
  calculates the daily change in weight in grams by subtracting the
  previous day's weight from the current day's weight, both in grams.

- **Weight loss per 100 calories consumed:** A new column was added to
  quantify weight loss in grams per 100 calories consumed. This metric
  enables an analysis of weight changes relative to caloric intake,
  helping to assess the efficiency of weight loss against calorie
  consumption.

- **Week number:** A week number attribute was added to segment the data
  by week, aiding in time series analysis by grouping observations into
  weekly periods.

![](images/Figure%201.%20Original%20data%20%20(unedited).png)Figure 1 - Original data -- unedited

![](images/Figure%202.%20Data%20after%20cleaning%20and%20prepping.png)Figure 2 - Data after cleaning & prepping

### 

### Data Analysis

**Techniques used:** Time series analysis for identifying weight loss
over time, and regression analysis.

**Justification of methods:** These methods were used for their
effectiveness in prediction and the ability to provide clear insights.
Regression analysis can be used to see how much weight change can be
attributed to calorie intake and exercise and can also be used for
predicting future weight changes. Using Power BI for the time series
analysis (or forecast) enables us to understand and see the individual's
weight changes throughout the 5 months. Having the seasonality set to 12
(to indicate the number of months in a year) and the confidence interval
to 95% as I am certain the individual's weight will fall between the
grey areas.

Originally, I was planning to use a t-test to provide some insight into
the data and to see if it was random that the person was losing weight,
unfortunately I couldn't preform a t-test as I only have the one set of
data and it would have been too complicated to include a second.

### Results

**Data communication tools:** Visualisations were created using Power BI
and Python.

**Screenshots and narratives:**

![](images/Figure%203.%20Time%20Series%20Analysis%20on%20weight%20in%20g%20over%20a%20period%20of%20time.png)Figure 3 - Time Series Analysis on weight in g over a period of time



Figure 3: The trend line indicates a steady increase in individuals'
weight over time, with a future prediction suggesting a gradual
decrease. This is significant because, although the person may
ultimately lose weight, the fluctuations during this process are not
ideal for health. Without more precise data, many factors could
contribute to weight loss, such as hydration levels, calorie
expenditure, and meal timing. Each of these variables can affect an
individual's weight loss journey.



![](images/Figure%204.%20Weight%20difference,%20Time%20Series%20Analysis.png)Figure 4 - Weight difference - Time Series Analysis



Figure 4 illustrates the fluctuations in weight difference (either
positive or negative), measured in grams, that the individual has
experienced over time. Like Figure 3, the weight changes are quite
erratic. For instance, the data shows that the individual lost 3 kg just
after Christmas but then gained 1 kg back. These fluctuations could be
attributed to factors such as hydration levels and calorie intake, but
such significant variations are not conducive to healthy weight
management.



![](images/Figure%205.%20Weight%20loss%20in%20grams,%20per%20100%20calories%20consumed.png)Figure 5 - Weight loss in grams, per 100 calories consumed



Figure 5 provides a detailed analysis of how much weight the individual
gains or loses per 100 kcal consumed. This approach offers a
standardised method for comparing weight loss relative to calorie intake
and helps determine whether weight loss through diet alone is feasible.



![](images/Figure%206.%20Python%20script%20in%20Notepad%2B%2B.png)Figure 6 - Python script in Notepad++



Using Notepad++, I created a Python script to generate a scatter plot
with a regression line. The script begins by importing necessary
modules, like pandas and statsmodels, and then loads data from
"dietdata.csv." It performs some preprocessing steps, such as
converting dates to a datetime format and changing any true/false values
to 1 or 0. It also has the independent and dependent variables listed
within the script.

For this project, I chose Ordinary Least Squares (OLS) regression, which
is the simplest and most widely used method for linear regression. The
objective of OLS regression is to find the best-fitting line that
minimises the errors between the observed data points and the predicted
values.

After running the Python script shown in Figure 6, we produce the output
displayed in Figure 7 and the graph presented in Figure 8. Explanations
for both are provided below each figure.



![](images/Figure%207.%20Python%20output,%20summary%20of%20prediction%20model%20OLS%20%28Ordinary%20Least%20Squares%29.png)Figure 7 - Python output -- summary of prediction model OLS (Ordinary
Least Squares)



The figure above provides a detailed summary of the OLS regression model
applied to the data. This summary, generated using the statsmodels
library, offers valuable insights into the model's performance, the
relationships between the independent and dependent variables, and the
statistical significance of the results. A few key points to note are
that the overall model is not statistically significant (p-value >
0.05), indicating it may not be a reliable predictor of weight
differences. Among all the predictors, only "walk" shows a
statistically significant relationship with weight difference. This
analysis highlights that while the model offers some useful insights,
particularly regarding the significance of walking, it also has
limitations that could impact its predictive accuracy and reliability.



![](images/Figure%208.%20Scatterplot%20regression%20model%20showing%20actual%20vs%20predicted%20weight%20difference.png)Figure 8 - Scatterplot regression model showing actual vs predicted
weight difference



Finally, a scatter plot with a regression line is created using
matplotlib to visualise the actual versus predicted weight differences
over time. In the graph, the blue line represents the actual weight
difference, which fluctuates consistently above and below zero. The red
line shows the predicted weight difference as determined by the OLS
regression model, which displays significantly fewer fluctuations and
spikes.

This indicates that the predicted values do not capture the extreme
variations seen in the actual weight difference. This could suggest that
the model is missing some important variables related to the
individual's weight loss, as discussed further in the recommendations
section. The graph also shows signs of underfitting, as the predicted
and actual lines differ considerably, suggesting that the OLS regression
was too simplistic for this data. A more advanced model, such as
polynomial regression, might have been more appropriate.

### 

### Recommendations

- Using OLS regression has its limitations; the model does not account
  for any interactions between variables, which OLS cannot capture
  without additional modelling techniques.

- There are also missing variables that could provide more insight, such
  as data from more advanced scales that measure BMI, water retention,
  muscle mass, etc. Additionally, we lack information on factors like
  the individual's sleep patterns, stress levels, metabolism, and
  genetics---all of which can significantly influence weight loss and
  gain.

- Given our small sample size, I suggest collecting more data,
  potentially across different seasons, to determine if weight changes
  are influenced by seasonal variations.

- With additional time and data, we could consider using polynomial
  regression, which might provide a better fit by capturing non-linear
  relationships between independent and dependent variables (for
  example, if the relationship between calorie intake and exercise is
  non-linear, a polynomial regression model could better represent
  this).

# 

# Bibliography

ChrisBow (2018).* 2018 calorie, exercise and weight changes. [online]
Kaggle.com.* Available at: [2018 calorie, exercise and weight changes | Kaggle](https://www.kaggle.com/datasets/chrisbow/2018-calorie-exercise-and-weight-changes) Accessed 01 July 2024).

*For anyone who is confused about the chi-squared stuff*. Available at: [For anyone who is confused about the Chi-Squared stuff](https://www.marksmath.org/classes/Summer2018Stat185/mathstatHWDiscuss/t/for-anyone-who-is-confused-about-the-chi-squared-stuff/130/) (Accessed: 08 July 2024).

Bevans, R. (2023) *An introduction to T tests: Definitions, formula and
examples*, *Scribbr*. Available at: [An Introduction to t Tests | Definitions, Formula and Examples](https://www.scribbr.com/statistics/t-test/) (Accessed: 01 July 2024).

Chip (2023) *Understanding time-series analysis in power bi*, *QuantHub*. Available at: [Understanding Time-Series Analysis in Power BI | QuantHub](https://www.quanthub.com/power-bi-time-series-analysis/) (Accessed: 01
July 2024).

GeeksforGeeks. (2020). *Ordinary Least Squares (OLS) using statsmodels*.
[online] Available at: [Ordinary Least Squares (OLS) using statsmodels - GeeksforGeeks](https://www.geeksforgeeks.org/ordinary-least-squares-ols-using-statsmodels/) (Accessed: 20 August 2024).

Zach (2022). *How to Perform OLS Regression in Python (With Example)*.
[online] Statology. Available at: [How to Perform OLS Regression in Python (With Example)](https://www.statology.org/ols-regression-python/) (Accessed: 20 August
2024).

GeeksforGeeks. (2018). *Python | Implementation of Polynomial
Regression - GeeksforGeeks*. [online] Available at: [Implementation of Polynomial Regression - GeeksforGeeks](https://www.geeksforgeeks.org/python-implementation-of-polynomial-regression/) (Accessed: 20 August 2024).