import os, requests, json
from flask import Flask, request, redirect

global ans
ans = ""

app = Flask(__name__, static_url_path="/static")

apiKey = os.environ['geminiai']

def getInfo(promt):    
    promt = str(promt)
    headers = {"Content-Type": "application/json", "x-goog-api-key": apiKey}

    data = {"contents": [{"role": "user", "parts": [{"text": promt}]}]}

    url = "https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent"

    response = requests.post(url, json=data, headers=headers)
    result = response.json()
    return result['candidates'][0]['content']['parts'][0]['text']



@app.route("/text", methods=['POST'])
def text():
    global ans

    form = request.form
    # print(form['question-box'])

    ans = getInfo(form['question-box'])
    # print("text ans: ",ans)

    return redirect("/")
    

@app.route("/")
def index():
    global ans

    # print("in index: ", form)
    page = ""
    with open("page.html") as f:
        page = f.read()
    # print("in index 2: ", request.form)
    # print("index ans: ", ans)

    if ans == "":
        page = page.replace("Your answer will apper here", "Your answer will apper here")
    elif "gemini" in ans.lower():    
        page = page.replace("Your answer will apper here", "You know, you should not pry into other people's life.")
    else:
        page = page.replace("Your answer will apper here", ans)
    

    return page

# print(getInfo(promt))

app.run(host="0.0.0.0", port=81)
