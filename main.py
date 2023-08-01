from flask import Flask, render_template, request
from requests import request
from utils import radio, get_index

TOKEN = "6173435069:AAEw84qHT0KRrrDVSRNwk93Q9PgyUqTtXHA"
CHAT_ID = 250765796

app = Flask(__name__)


def send_message(name, number, text_redio):
    text_messege = f"{name}\n{number}\n{text_redio}"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text_messege}"
    import requests
    requests.get(url).json()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=['GET', 'POST'])
def post_index():
    if request.method == 'POST':
        items = request.form.items()
        index = get_index(items)
        name = request.form.get('name')  # Фамилия и имя
        number = request.form.get('number')  # номер
        text_radio = radio(index)
        send_message(name, number, text_radio)
        return render_template("done.html")


if __name__ == "__main__":
    app.run(debug=True)
