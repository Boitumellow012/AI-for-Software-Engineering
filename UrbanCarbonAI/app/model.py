import os
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

def train_model(X, y, model_save_path="carbon_emission_model.pkl", plot_save_path="static/feature_importance.jpg"):
    # Ensure the directory for plot exists
    os.makedirs(os.path.dirname(plot_save_path), exist_ok=True)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(n_estimators=200, max_depth=10, min_samples_split=5, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    print(f"MAE: {mean_absolute_error(y_test, y_pred):.2f}")
    print(f"R² Score: {r2_score(y_test, y_pred):.2f}")

    # Feature importance plot
    feature_imp = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=feature_imp, y=feature_imp.index)
    plt.title("Most Important Features for Emission Prediction")
    plt.xlabel("Relative Importance")
    plt.tight_layout()
    plt.savefig(plot_save_path)
    plt.close()

    joblib.dump(model, model_save_path)
    return model
