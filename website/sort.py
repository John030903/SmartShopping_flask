import joblib

def sort_items(items):
    # Load the model from file
    reg_model, scaler = joblib.load("model.sav")

    # Scale the price feature
    items['price_scaled'] = scaler.transform(items[['price']])

    # Define the features
    features = ['star_average', 'sold', 'price_scaled']

    # Use the loaded model to make predictions
    predictions = reg_model.predict(items[features])

    # Add the predictions to the new DataFrame
    items['quality_score'] = predictions

    # Sort the DataFrame by quality_score
    items.sort_values('quality_score', ascending=False, inplace=True)
    items.reset_index(drop=True, inplace=True)
    
    # Remove the quality_score column
    items.drop(columns=['quality_score','price_scaled'], inplace=True)
    print("Ran")

    return items

