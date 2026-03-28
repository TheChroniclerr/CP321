import pandas as pd

DATASET = "https://raw.githubusercontent.com/TheChroniclerr/CP321/refs/heads/main/a4/assets/COVID_Country_Sample.csv"

def load_data():
    # Load dataset
    df = pd.read_csv(DATASET)

    # Zero-fill Nan values
    df['new_vaccinations'] = df['new_vaccinations'].fillna(0)

    # Compute rolling means
    df['cases_rolling'] = df.groupby('country')['new_cases'].transform(lambda x: x.rolling(3, center=True).mean())
    df['deaths_rolling'] = df.groupby('country')['new_deaths'].transform(lambda x: x.rolling(3, center=True).mean())
    df['vacc_rolling'] = df.groupby('country')['new_vaccinations'].transform(lambda x: x.rolling(3, center=True).mean())

    # Drop edge NaN producd by rolling means
    df = df.dropna(subset=['cases_rolling', 'deaths_rolling', 'vacc_rolling'])
    return df


def get_plot_data(df, country, metric):
    # Get processed metrics from raw metrics
    metric_map = {
        'new_cases': 'cases_rolling',
        'new_deaths': 'deaths_rolling',
        'new_vaccinations': 'vacc_rolling'
    }   
    metric_proc = metric_map[metric]

    # Create new date & metric table
    df_country = df[df['country'] == country][['date', metric_proc]].copy()
    
    # Convert date to string type
    df_country['date'] = pd.to_datetime(df_country['date']).dt.strftime('%Y-%m-%d')

    # Rename metric to 'value' for consistency
    df_country = df_country.rename(columns={metric_proc: 'value'})
    return df_country
    