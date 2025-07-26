import requests
import plotly.graph_objects as go

def fetch_covid_data():
    url = "https://disease.sh/v3/covid-19/historical/all?lastdays=30"
    response = requests.get(url)
    data = response.json()
    return data


def plot_Covid_trends(data):
    dates = list(data['cases'].keys())
    cases = list(data['cases'].values())
    deaths = list(data['deaths'].values())
    recovered = list(data['recovered'].values())
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=cases ,mode="lines+markers", name='Cases'))
    fig.add_trace(go.Scatter(x=dates, y=deaths, mode="lines+markers", name="Deaths"))
    fig.add_trace(go.Scatter(x=dates, y=recovered,mode="lines+markers", name= "Recovered" ))
    
    fig.update_layout(
        title= "Global COVID-19 Trends (Last 30 Days)",
        xaxis_title = "Date",
        yaxis_title = "No of People",
        hovermode = "x unified"
    )
    fig.show()
    
if __name__ == "__main__":
    covid_data = fetch_covid_data()
    plot_Covid_trends(covid_data)

