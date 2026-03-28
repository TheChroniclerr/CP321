# Introduction

A Flask web app that visualizes real-world COVID-19 data interactively with provided insights.

Dataset: `COVID_Country_Sample.csv`

**Flask App Directory**
```txt
project
|   app.py
|   data.py
|
+---data
|       cleaned.csv
|
+---static
|       favicon.ico
|       script.js
|       style.css
|
+---templates
|       index.html
```

# Cleaning

We choose to use a rolling means to smooths out short-term spikes and reducing the affects from outliers, allowing the visualizations to better reflect underlying trends without discarding the raw data.

For rolling means, it is generally fine to fill NaN with 0 missing values as rolling means minimizes biases caused by zero-fills. However, the NaN produced from edge values of rolling means are dropped. 

# Commands

Create, activate, and deactiavte virtual environment.
```sh
py -m venv .venv
./.venv/Scripts/activate
deactivate
```

Installing libraries for `.venv`.
```sh
py -m pip install --upgrade pip
pip install -r requirements.txt
```

Launch website (Flask automatically detects `app.py`).
```sh
flask run
```

Set `Debug mode: on` to default launch setting. This enables hot fixes.
```sh
$env:FLASK_DEBUG=1
```

Launch manually with `Debug mode: on`.
```sh
py app.py
```