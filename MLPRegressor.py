import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import SGDRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import VotingRegressor

data = pd.read_csv('Asthma Dataset - 2022 (1).csv')
X = data.iloc[:,1:8 ].values
y = data.iloc[:, 8].values
print(X.shape)
print(y.shape)

def MLP(X_train, X_test, y_train, y_test):
    regressor = MLPRegressor(hidden_layer_sizes=(64, 64, 64, 64, 64, 64), max_iter=2000, random_state= 42)
    regressor.fit(X_train,y_train)
    y_pred = regressor.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test,y_pred))
    #print("MLP RMSE", rmse)  
    # print("MLP", y_pred)
    return y_pred

def decision_tree(X_train, X_test, y_train, y_test):
    regressor = DecisionTreeRegressor(random_state= 42)
    regressor.fit(X_train,y_train)
    y_pred = regressor.predict(X_test)
    rmse = (mean_squared_error(y_test,y_pred))
    #print("Decision Tree", rmse )  
    # print("Decision Tree", y_pred)
    return y_pred

def svr_code(X_train, X_test, y_train, y_test, kernel='rbf', C=1.0, epsilon = 0.1, random_state = None):
    regressor = SVR(kernel=kernel, C=C, epsilon=epsilon)
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_test)
    rmse = (mean_squared_error(y_test, y_pred))
    #print("SVR",  rmse)
    # print("SVR" , y_pred)
    return y_pred

def SGD(X_train, X_test, y_train, y_test, loss = 'squared_loss', alpha = 0.0001, max_iter=1000, random_state=None):
    regressor = SGDRegressor(loss='squared_error', alpha=alpha, max_iter=max_iter, random_state=random_state)
    regressor.fit(X_train, y_train) 
    y_pred = regressor.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    #print("SGD", rmse)
    # print("SGD" , y_pred)
    return y_pred

def rf(X_train, X_test, y_train, y_test, n_estimators=300, max_depth=None, random_state=None):
    regressor = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth, random_state=random_state)
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
   #print("Random Forest" , rmse)
    # print("Random Forest" , y_pred)
    return y_pred

def gbr(X_train, X_test, y_train, y_test, n_estimators=100, learning_rate=0.1, max_depth=3, random_state=None):
    regressor = GradientBoostingRegressor(n_estimators=n_estimators, learning_rate=learning_rate, max_depth=max_depth, random_state=random_state)
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    #print("GBR", rmse)
    # print("GBR" , y_pred)
    return y_pred

y_predictions = {
    "Actual": [],
    "Multi-Layer Perceptron": [],
    "Decision Tree": [],
    "Support Vector Machine": [],
    "Stochastic Gradient Descent": [],
    "Random Forest": [],
    "Gradient Boost": []
}
for i in range(X.shape[0]):
    print("Progress:", i, "of", X.shape[0])
    X_test = X[i: i + 1]
    X_train = np.concatenate((X[0:i], X[i+1:]))

    y_test = y[i: i + 1]
    y_train = np.concatenate((y[0:i], y[i+1:]))

    # run each regressor and add to the results dictionary
    y_predictions["Actual"].append(y_test[0])
    y_predictions["Multi-Layer Perceptron"].append(MLP(X_train, X_test, y_train, y_test)[0])
    y_predictions["Decision Tree"].append(decision_tree(X_train, X_test, y_train, y_test)[0])
    y_predictions["Support Vector Machine"].append(svr_code(X_train, X_test, y_train, y_test, kernel='rbf', C=1.0, epsilon = 0.1, random_state = 42)[0])
    y_predictions["Stochastic Gradient Descent"].append(SGD(X_train, X_test, y_train, y_test, loss = 'squared_loss', alpha = 0.0001, max_iter=1000, random_state=42)[0])
    y_predictions["Random Forest"].append(rf(X_train, X_test, y_train, y_test, n_estimators=300, max_depth=None, random_state=42)[0])
    y_predictions["Gradient Boost"].append(gbr(X_train, X_test, y_train, y_test, n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)[0])

# display the results
print()
print(",".join(y_predictions.keys()))
for i in range(len(y_predictions["Actual"])):
    print(",".join([str(y_predictions[x][i]) for x in y_predictions]))


# display the RMSE values
print()
print("RMSE:")
for key in y_predictions:
    print(key, np.sqrt(mean_squared_error(y_pred=y_predictions[key], y_true=y_predictions["Actual"])))


