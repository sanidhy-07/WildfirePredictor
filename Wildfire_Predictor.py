import argparse

import colorama
import pandas as pd
from colorama import Fore
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

colorama.init(autoreset=True)

parser = argparse.ArgumentParser(description='Wildfire Predictor')
parser.add_argument("--temp", type = float, required = True)
parser.add_argument("--humidity", type = float, required = True)
parser.add_argument("--wind", type = float, required = True)

args = parser.parse_args()

df = pd.read_csv("Wildfire_Data.csv")

X = df[['temperature', 'humidity', 'wind']]
Y = df['fire']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state = 42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, Y_train)

new_input = pd.DataFrame([[args.temp, args.humidity, args.wind]], columns = ['temperature', 'humidity', 'wind'])
prediction = model.predict(new_input)[0]

if prediction == 1:
    print(f"{Fore.RED}High Risk!!!")
else:
    print(f"{Fore.GREEN}Low Risk!!!")

accuracy = model.score(X_test, Y_test)
print(f'{Fore.YELLOW}Model accuracy: {accuracy * 100:.2f}%')
