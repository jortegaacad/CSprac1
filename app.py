from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
   r = lambda: random.randint(0,255)
   return render_template('index.html', bgcolor=f"rgb({r()},{r()},{r()})")

if __name__ == '__main__':
   app.run(debug=True)
