

# **Estimators from Scratch**
This project provides Python implementations of various estimators from scratch, without relying on external libraries such as scikit-learn. The purpose of this project is to understand how these models work under the hood.

## Estimators Implemented
So far, this project includes the following Estimator models:

Linear Regression: Open in Colab->[![Colab](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Google_Colaboratory_SVG_Logo.svg/32px-Google_Colaboratory_SVG_Logo.svg.png)](https://colab.research.google.com/drive/1hYe7LsNkZaODpGAQlEgLeCc5aBYSWrxo?usp=sharing)
<br>
Logistic Regression: 
<br>
Decision Trees: Open in Colab->[![Colab](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Google_Colaboratory_SVG_Logo.svg/32px-Google_Colaboratory_SVG_Logo.svg.png)](https://colab.research.google.com/drive/17CN_GwgMRPQBNEDd-kvL2VVa_EeYBX2K?usp=sharing)
<br>
Naive Bayes: 
<br>
k-Nearest Neighbors: 
<br>
Support Vector Machines: 
<br>
Artificial Neural Networks: 
<br>
Stochastic Gradient Descent: Open in Colab->[![Colab](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Google_Colaboratory_SVG_Logo.svg/32px-Google_Colaboratory_SVG_Logo.svg.png)](https://colab.research.google.com/drive/15qgScy7xpwhuWwLLBe0bDl--KLqJQjT6?usp=sharing)

## Usage
Each model implementation is contained in its own Python file and includes a `fit` method for training the model and a `predict` method for making predictions on new data. The `utils.py` file contains helper functions for loading and preprocessing data.

To use a model, simply import the relevant Python file and create an instance of the model class. Then, call the `fit` method with your training data and labels, and the `predict` method with your test data.

For example, to use the linear regression model:

```
from linear_regression import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

## Contributing
Contributions to this project are welcome! If you notice a bug or would like to add a new model implementation, please create a pull request.









