from data import load_data, get_plot_data
from flask import Flask, render_template, request, jsonify

df = load_data()    # Clean & load dataset
df.to_csv("data/cleaned.csv", index=False)   # Export dataset

app = Flask(__name__)

# Dashboard endpoint
@app.route('/')
def index():
    countries = df['country'].unique()
    return render_template('index.html', countries=countries)


# Plotly JSON endpoint
@app.route('/data')
def get_data():
    country = request.args.get('country', 'Canada')
    metric = request.args.get('metric', 'new_cases')
    
    df_country = get_plot_data(df, country, metric)
    return jsonify(df_country.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)