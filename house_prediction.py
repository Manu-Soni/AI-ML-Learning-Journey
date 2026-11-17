
# Day 1: House Price Prediction using Machine Learning

from sklearn.linear_model import LinearRegression

# 1. Training data (house size in square feet)
X = [[500], [800], [1000], [1200], [1500]]

# 2. Correct prices (in lakh rupees)
y = [15, 24, 30, 36, 45]

# 3. Create the Machine Learning model
model = LinearRegression()

# 4. Train the model
model.fit(X, y)

# 5. Predict the price of a new house
new_house = [[1300]]

prediction = model.predict(new_house)

# 6. Display the result
print("House size:", new_house[0][0], "sq ft")
print("Predicted price:", prediction[0], "lakh rupees")

