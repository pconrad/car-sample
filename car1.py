from flask import Flask, render_template
import json
from json import loads

app = Flask(__name__)

json_file = open('cars.json')
json_str = json_file.read()
json_data = json.loads(json_str)


#cars = json_data['Engine Information']

for item in json_data:
    name = item.get("Engine Information")

print (name)


#{ d['Horsepower'] for d in loads(json_data)['Engine Information']}

#data =  json.dumps(json_data, indent=4)


@app.route("/")
def index():
    return "hello"


@app.route("/test")
def test():
    return render_template('range_slider.html')


if __name__ == "__main__":
    app.run(debug=True)

