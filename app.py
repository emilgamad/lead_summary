from flask import Flask, request, redirect
from flask import render_template
import json, requests
app = Flask(__name__)


@app.route('/index', methods=['GET', 'POST'])
def create_lead():
    
    if request.method == 'POST':
        response = submit_lead_summary(request)
        return render_template('create_lead.html', response=response)
    elif request.method == 'GET':
        return render_template('create_lead.html', name=create_lead)

def submit_lead_summary(request):
    empty = ""
    try:
        firstname = request.form.get('username', empty)
        lastname = request.form('lastname', empty) #Required
        email = request.form('email', empty)
        phone = request.form('phone', empty)
        websource = request.form('websource', empty)
        description = request.form('description', empty)
    except:
        firstname = empty
        lastname = "asd"
        email = empty
        phone = empty
        websource = empty
        description = empty
    
    url = "https://shapiro.secure.force.com/api/services/apexrest/litify_pm/api/v1/intake/create"

    payload = {
        "firstName":firstname,
        "lastName":lastname,
        "email": email,
        "phone": phone,
        "websource": websource,
        "description": description
    }

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data = json.dumps(payload))
    if response.status_c = 200
    return response.text

def hello():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)