from colorama import Fore
print(f"{Fore.MAGENTA}Starting Wildfire Predictor...", flush=True)

import argparse
import joblib
import os
import colorama
import time
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

colorama.init(autoreset=True)

if os.path.exists("Wildfire_Predictor.pkl"):
    print(f"{Fore.YELLOW}Loading existing Model...\n")
    time.sleep(2)

parser = argparse.ArgumentParser(description='Wildfire Predictor')
parser.add_argument("--temp", type = float, required = True)
parser.add_argument("--humidity", type = float, required = True)
parser.add_argument("--wind", type = float, required = True)
parser.add_argument("--rain", type = float, required = True)
args = parser.parse_args()

if os.path.exists("Wildfire_Predictor.pkl"):
    model = joblib.load("Wildfire_Predictor.pkl")
else:
    while True:
        print(f"{Fore.YELLOW}Reading Data...")
        time.sleep(2)
        df = pd.read_csv("Wildfire_Data.csv")
        X = df[['temperature', 'humidity', 'wind', 'rain']]
        Y = df['fire']
        print(f"{Fore.YELLOW}Training Model...")
        time.sleep(2)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3)
        model = RandomForestClassifier(random_state=42)
        model.fit(X_train, Y_train)
        if model.score(X_test, Y_test) >= 0.85:
            joblib.dump(model, 'Wildfire_Predictor.pkl')
            accuracy = model.score(X_test, Y_test)
            print(f"{Fore.GREEN}Model Trained.\n")
            print(f'{Fore.YELLOW}Model accuracy: {accuracy * 100:.2f}%\n')
            time.sleep(2)
            break
        else: continue

new_input = pd.DataFrame([[args.temp, args.humidity, args.wind, args.rain]], columns = ['temperature', 'humidity', 'wind', 'rain'])
prediction = model.predict(new_input)[0]

if prediction == 1:
    print(f"{Fore.RED}High Risk of wildfire!")
else:
    print(f"{Fore.GREEN}Low Risk of wildfire!")

print(f"{Fore.RED}Disclaimer: Do not use this to predict actual wildfire, they depend on more than just these three variables. obviously.")