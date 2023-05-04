# This repo contains ML models from scratch in Python using just NumPy and Pandas. 


Linear Regressor:: 
<br>
Decision Tree: 
<br>



# **ML Models from Scratch**
This project provides Python implementations of various machine learning models from scratch, without relying on external libraries such as scikit-learn or TensorFlow. The purpose of this project is to help beginners understand how these models work under the hood, and to give them a foundation for building more complex models in the future.

## Models Implemented
So far, this project includes the following machine learning models:

Linear Regression: Open in Colab->[![Colab](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Google_Colaboratory_SVG_Logo.svg/32px-Google_Colaboratory_SVG_Logo.svg.png)](https://colab.research.google.com/drive/1hYe7LsNkZaODpGAQlEgLeCc5aBYSWrxo?usp=sharing)
Logistic Regression: 
Decision Trees: Open in Colab->[![Colab](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Google_Colaboratory_SVG_Logo.svg/32px-Google_Colaboratory_SVG_Logo.svg.png)](https://colab.research.google.com/drive/17CN_GwgMRPQBNEDd-kvL2VVa_EeYBX2K?usp=sharing)
Naive Bayes: 
k-Nearest Neighbors: 
Support Vector Machines: 
Artificial Neural Networks: 

Stochastic Gradient Descent: Open in Colab->[![Colab](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Google_Colaboratory_SVG_Logo.svg/32px-Google_Colaboratory_SVG_Logo.svg.png)](https://colab.research.google.com/drive/15qgScy7xpwhuWwLLBe0bDl--KLqJQjT6?usp=sharing)

## Usage
Each model implementation is contained in its own Python file, and includes a `fit` method for training the model and a `predict` method for making predictions on new data. The `utils.py` file contains helper functions for loading and preprocessing data.

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

##License
This project is licensed under the MIT License - see the `LICENSE.md` file for details.








