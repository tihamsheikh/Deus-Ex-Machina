# This is a simple query bot
# Just like wikipedia but better
# It uses googles gemini language model

# import google-genai and flask
from google import genai    # google-genai 1.3.0
from flask import Flask, render_template, request, redirect
import const    # for api key. Use your own as a variable
import asyncio

# object initialization
app = Flask(__name__)

# global variable for the answer
answer = ""

# function to get response
def get_info(prompt):
    # language model needs this for some reason
    # don't know why and don't question it. It just works
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    # api call
    client = genai.Client(api_key=const.key)

    # getting answer
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"""
        {str(prompt)}
        """
    )
    # returning answer
    return response.text

# response editing
@app.route("/text", methods=["POST"])
def text():
    global answer

    # submission form
    form = request.form
    query = form.get("question-box", "")

    # manual query filtering
    if query == "":
        answer = "That's empty my dude"
    else:
        answer = get_info(query).split("\n")

    return redirect("/")

# main page
@app.route("/")
def index():
    global answer
    # returns main page directly
    return render_template("index.html", answer = answer)


# object runner. Runs in a ip address
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True,port=204)
