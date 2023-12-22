# 🏙Bangalore weather stats streamlit ☁ [![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![](https://img.shields.io/badge/Prateek-Ralhan-brightgreen.svg?colorB=ff0000)](https://prateekralhan.github.io/)
A simple streamlit based webapp to display weather statistics of my city for quick reference which autorefreshes every 5 seconds ! 😉

![demo](https://github.com/prateekralhan/weather-stats-streamlit/assets/29462447/b5e7c61b-8a3b-49bb-af71-887de0b516b3)


## Installation:
* Simply run the command ***pip install -r requirements.txt*** to install the necessary dependencies.
* Ensure you get your API Keys from [openweathermap](https://openweathermap.org/) and [AQICN](https://aqicn.org/here/).

## Usage:
1. Create a new folder `.streamlit` and create a file titled `secrets.toml` within it.
2. Enter your API Keys in this file as `OPENWEATHER_API_Key = "XXXXXXXXXXXX"` and `AQI_API_Key = "XXXXXXXXXXXX"` in 2 separate lines and save the details.
3. Simply run the command: 
```
streamlit run app.py
```
4. Navigate to http://localhost:8501 in your web-browser, and your webapp shall spin up!

![1](https://github.com/prateekralhan/weather-stats-streamlit/assets/29462447/547a91f0-8702-401c-98c6-b0e5469c99dd)

### Running the Dockerized App
1. Ensure you have Docker Installed and Setup in your OS (Windows/Mac/Linux). For detailed Instructions, please refer [this.](https://docs.docker.com/engine/install/)
2. Navigate to the folder where you have cloned this repository ( where the ***Dockerfile*** is present ).
3. Build the Docker Image (don't forget the dot!! :smile: ): 
```
docker build -f Dockerfile -t app:latest .
```
4. Run the docker:
```
docker run -p 8501:8501 app:latest
```

This will launch the dockerized app. Navigate to ***http://localhost:8501/*** in your browser to have a look at your application. You can check the status of your all available running dockers by:
```
docker ps
```

