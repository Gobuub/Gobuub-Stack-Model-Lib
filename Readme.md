# Gobuub Stack Model lib

I create this little library for a personal project.

On it you can find four packages with different functions, the finally of this library is to have in a only one library 
the necessary elements to make a quickly EDA and make an easy train stack model.

- Print Correlation:
  - This function returns a correlation matrix plot.
  
- Print Scatter:
  - This function returns an scatter plot.
- Train levels:
  - This function train a list of different machine learning models, you must import it from sklearn library, and returns
  the prediction of each model on a pandas DataFrame, that it would be used to train the next level of stack model.
- Train stack model:
  - This function receive a list of predictions makes with train levels and use it to train another level of the stack 
  model, the final level only can have one model. 