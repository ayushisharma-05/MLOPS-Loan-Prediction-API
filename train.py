from sklearn.linear_model import LogisticRegression
import pandas as pd
import pickle

# Dummy dataset
data = pd.DataFrame({
    "income": [20000, 50000, 80000, 120000],
    "loan_amount": [5000, 20000, 30000, 40000],
    "approved": [0, 1, 1, 1]
})

X = data[["income", "loan_amount"]]
y = data["approved"]

model = LogisticRegression()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained & saved!")