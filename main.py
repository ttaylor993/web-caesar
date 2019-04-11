from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

style_form = """
<!DOCTYPE html>
<html lang = "en">
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>

</html>

<body>
"""
caesar_form = """
    <form action="/caesar", method="post"> 
        <label for="rot">
            Rotated by:
            <input type ="text" name ="rot" value = "0">
        </label>
          </br>  
        <textarea name ="text">{0}</textarea>
        <input type="submit" value ="Submit Query">
    </form>
</body>
"""
@app.route("/")
def index():
    return caesar_form.format("")

@app.route("/caesar", methods=['POST'])
def encrypt():
    input_mess = request.form['text']
    number_input = request.form['rot']
    encrypted_mess = rotate_string(str(input_mess),int(number_input))
    return caesar_form.format(encrypted_mess)

app.run()

