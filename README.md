# 🏙Bangalore weather stats streamlit ☁ [![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![](https://img.shields.io/badge/Prateek-Ralhan-brightgreen.svg?colorB=ff0000)](https://prateekralhan.github.io/)
A simple streamlit based webapp to display weather statistics of my city for quick reference which autorefreshes every 5 seconds ! 😉

![demo](https://user-images.githubusercontent.com/29462447/205502125-3da98938-2454-4362-8b4f-96808de82ef6.gif)


## Installation:
* Simply run the command ***pip install -r requirements.txt*** to install the necessary dependencies.
* Ensure you get your API Key from [openweathermap](https://openweathermap.org/).

## Usage:
1. Create a new folder `.streamlit` and create a file titled `secrets.toml` within it.
2. Enter your API Key in this file as `API_Key = "XXXXXXXXXXXX"` and save the details.
3. Simply run the command: 
```
streamlit run app.py
```
4. Navigate to http://localhost:8501 in your web-browser, and your webapp shall spin up!

![1](https://user-images.githubusercontent.com/29462447/205502823-9f4c9d3b-f6b8-41ce-8ace-b7848d651241.png)

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

