from flask import Flask
import threading

app = Flask(__name__)

@app.route("/")
def health_check():
    return "Bot is running!", 200  

def start_health_check():
    app.run(host="0.0.0.0", port=8080)

if __name__ == "__main__":
    start_health_check()
