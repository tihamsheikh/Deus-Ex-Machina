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
    print(form['question-box'])

    if form['question-box'] == "":
        ans = 404
        return redirect("/")
        
    response = getInfo(form['question-box'])

    print(response)
    
    ans = response.split("\n")
    
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
        page += "<p>Your answer will apper here</p>"

    elif ans == 404:
        page += "<p>Do not submit empty form!</p>"
    else:
        for paragraph in ans:
            page += f"<p>{paragraph.strip()}</p>"

    page += """
    </div>
        </div>
        <script src="script.js"></script>
    </body>
    </html>
    """

    return page


app.run(host="0.0.0.0", port=81)
