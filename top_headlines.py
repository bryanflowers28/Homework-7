from flask import Flask, render_template
import requests
import secret

app = Flask(__name__)

@app.route('/name/<nm>')
def hello_name(nm):
    return render_template('headlines.html', name = nm)

@app.route('/headlines/<nm>')
def page(nm):
    requestUrl = "https://api.nytimes.com/svc/topstories/v2/technology.json?api-key=" + str(secret.api_key)
    requestHeaders = {

    "Accept": "application/json"

    }
    request = requests.get(requestUrl, headers=requestHeaders)
    result = request.json()

    headline1 = result['results'][0]['title']
    headline2 = result['results'][1]['title']
    headline3 = result['results'][2]['title']
    headline4 = result['results'][3]['title']
    headline5 = result['results'][4]['title']

    return render_template('headlines.html',  headline1 = headline1,  headline2 = headline2,  headline3 = headline3,  headline4 = headline4,  headline5 = headline5, name = nm )

if __name__ == '__main__':
    print("starting Flask app", app.name)
    app.run(debug=True)
