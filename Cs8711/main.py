from flask import Flask, request, render_template
import requests
app=Flask(__name__)
@app.route('/',methods=["GET","POST"])
def index():
  weatherData=''
  error=0
  cityName=''
  if request.method=="POST":
    cname=request.form.get("cname")
    if cname:
      weatherApiKey= '33232a73c48ed3c163c9c5e75117bdf6'
      url="https://api.openweathermap.org/data/2.5/weather?q="+cname+"&appid=" + weatherApiKey
      weatherData = requests.get(url).json()
    else:
      error = 1
  return render_template('index.html', data = weatherData, cityName = cityName, error = error)
if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8000,debug=True)
