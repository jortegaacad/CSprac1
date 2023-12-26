from flask import Flask, render_template
import git
import os

app = Flask(__name__)

@app.route('/')
def home():
   repo = git.Repo(os.getcwd(), search_parent_directories=True)
   sha = repo.head.object.hexsha
   r = int(sha[0:2], 16)
   g = int(sha[2:4], 16)
   b = int(sha[4:6], 16)
   return render_template('index.html', bgcolor=f"rgb({r},{g},{b})")

if __name__ == '__main__':
   app.run(debug=True)
