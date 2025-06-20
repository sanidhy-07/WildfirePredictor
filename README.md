# 🔥 Wildfire Predictor

Predict the risk of wildfires using real environmental data!

---

## Overview

This Python command-line tool predicts wildfire risk based on **temperature**, **humidity**, **wind speed**, and **rain**.
The model is trained on real wildfire data to give you a quick and reliable risk assessment.

---

## Usage

Run the script with these **command-line arguments** in this order:

```bash
python Wildfire_Predictor.py --temp <temperature> --humidity <humidity> --wind <wind_speed> --rain <rain_intensity>
```
--temp — Temperature (°C) [Training data is from 2°C to 35°C]

--humidity — Humidity (%) [Training data is from 15% to 100%]

--wind — Wind Speed (km/h) [Training data is from 0.4km/h to 9.4km/h]

--rain — Rain Intensity (mm) [Training data is from 0mm to 6.4mm]

Example:

```bash
python Wildfire_Predictor.py --temp 42 --humidity 13 --wind 12 --rain 3.4
```
The program will output:
```bash
"High Risk!!!"
```
or 
```bash
"Low Risk."
```

Note:
If a created model has a low accuracy, delete the newly created Wildfire_Predictor.pkl file, and run the command again to create a new model (hopefully, with a higher accuracy)

# Future Plans:
- Build a Tkinter GUI for easier use
