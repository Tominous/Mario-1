import flask
from flask import Flask
from threading import Thread

app = Flask("")

@app.route("/")
def index():
  return "Tutti i sistemi sono tornati operativi."

def run():
  app.run(host = "0.0.0.0", port = 8080)

def run_server():
  t = Thread(target=run)
  t.start()