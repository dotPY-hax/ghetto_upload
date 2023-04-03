import random
from flask import Flask, request
app = Flask(__name__)
@app.route('/', methods = ['POST'])
def upload_file():
    file = "/tmp/uploaded" + str(random.randint(0,69))
    with open(file, "wb") as f:
        f.write(request.get_data())
        print(f"written to {file}")
    return "fuck flask!!"

app.run(debug = False, port=80, host="0.0.0.0")
