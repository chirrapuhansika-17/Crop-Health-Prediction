import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load data
data = pd.read_csv("data.csv")

# Inputs and output
X = data[['temperature', 'humidity', 'soil_moisture', 'pest_level']]
y = data['crop_health']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Prediction function
def predict(data_input):
    return model.predict([data_input])