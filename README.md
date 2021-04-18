# PT_DS_TEST

## Running the tests:
#### First you'll need to install the requirements for the project. use the command below in your python env terminal:

pip install -r requirements.txt

#### To execute a file: 
The script runs a sex predictor alongside a script that uses an algorithm to do so.

Command: (env) python sex_predictor.py newsample.csv

the newsample.csv file needs to be  file with the same structure of the 'test_data_CANDIDATE.csv', except the 'sex' column.
## Data descriptions:
The `test_data_CANDIDATE.csv` file contains some patient's data.
- age: in years
- sex: (M = male; F = female)
- cp: chest pain type
- trestbps: resting blood pressure (in mm Hg on admission to the hospital)
- chol: serum cholesterol in mg/dl
- fbs: (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
- restecg: resting electrocardiographic results
- thalach: maximum heart rate achieved
- nar: number of arms
- exang: exercise induced angina (1 = yes; 0 = no)
- oldpeak: ST depression induced by exercise relative to rest
- slope: the slope of the peak exercise ST segment
- hc: patient's hair colour
- sk: patient's skin colour
- trf: time spent in traffic daily (in seconds)
- ca: number of major vessels (0-3) colored by flourosopy
- thal: 3 = normal; 6 = fixed defect; 7 = reversable defect