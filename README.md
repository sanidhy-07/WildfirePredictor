# 🔥 Wildfire Predictor

Predict the risk of wildfires using real environmental data!

---

## Overview

This Python command-line tool predicts wildfire risk based on **temperature**, **humidity**, and **wind speed**.  
The model is trained on real wildfire data to give you a quick and reliable risk assessment.

---

## Usage

Run the script with these **command-line arguments** in this order:

```bash
python Wildfire_Predictor.py --temp <temperature> --humidity <humidity> --wind <wind_speed>
```
--temp — Temperature (°C)

--humidity — Humidity (%)

--wind — Wind Speed (km/h)


Example:

```bash
python Wildfire_Predictor.py --temp 42 --humidity 13 --wind 12
```
The program will output:
```bash
"High Risk!!!"
```
or 
```bash
"Low Risk."
```
followed by:
```bash
Model accuracy: Percentage accuracy of the prediction model.
```
Future Plans:

- Allow for saving of accurate models
- Improve model accuracy with more data and features 
- Build a Tkinter GUI for easier use
