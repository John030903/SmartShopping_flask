from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
import joblib
import pandas as pd

# Load the dataset
# data = pd.read_csv('products.csv')

# Khởi tạo DataFrame
data = pd.DataFrame({'star_average': [4.8],
                   'sold': [762],
                   'price': [740000],
                   'quality_score': [71]})

# Thêm dữ liệu vào DataFrame
new_data = [[4.7,1600,515000,90],
            [4.7,970,369000,99],
            [4.8,1100,575000,87],
            [4.9,913,1539000,70],
            [4.8,2800,499000,98],
            [4.8,481,625000,79],
            [4.8,119,1092000,55],
            [4.9,556,1201000,62],
            [5,32,677000,49],
            [4.7,662,829000,68],
            [4.9,608,1819000,71],
            [4.6,129,479000,92],
            [4.8,2500,480000,100],
            [4.7,38,939000,56],
            [4.8,264,829000,70],
            [4.7,66,715000,65],
            [5,148,994000,64],
            [4.9,33,1978000,1],
            [5,29,747450,13],
            [4.8,44,397000,70],
            [4.8,168,550000,76],
            [5,61,14900,5],
            [4.8,58,559000,54],
            [4.6,30,12000,4],
            [4.8,57,679000,67],
            [5,29,787000,48],
            [4.7,55,623000,52],
            [4.8,68,1398000,4],
            [4.9,15,999000,2],
            [4.8,476,529000,61],
            [4.7,285,474000,88],
            [4.9,67,486000,70],
            [4.8,1800,489000,95],
            [4.7,228,489000,89],
            [4.6,11,275000,20],
            [4.9,35,785000,17],
            [4.9,154,1491000,47],
            [5,3,668000,0],
            [4.9,66,270750,60],
            [5,27,2250000,0],
            [4.8,290,519000,71],
            [4.9,38,1270000,2],
            [4.5,25,1400000,5],
            [4.6,72,559000,62],
            [4.7,122,549000,65],
            [4.9,57,575000,61],
            [5,52,645000,57],
            [5,14,810000,50],
            [4.2,6,695000,45],
            [5,13,459000,25],
            [4.9,61,459000,50],
            [4.4,5,311000,6],
            [5,7,480000,15],
            [4.9,57,567000,60],
            [5,5,1190000,7],
            [5,18,1144000,0],
            [4.8,98,484000,85]]

data = data.append(pd.DataFrame(new_data, columns=data.columns), ignore_index=True)

# Scale the price feature to give it higher priority
scaler = MinMaxScaler(feature_range=(0, 0.5))
data['price_scaled'] = scaler.fit_transform(data[['price']])

# Split the dataset into training and testing sets
train_data = data.sample(frac=0.8, random_state=1)
test_data = data.drop(train_data.index)

# Define the features and target variable
features = ['star_average', 'sold', 'price_scaled']
target = 'quality_score'

# Train the regression model
reg_model = LinearRegression()
reg_model.fit(train_data[features], train_data[target])

# Save the model and scaler to a file
joblib.dump((reg_model, scaler), 'model.sav')