from flask import Flask, render_template
from post import Post

app = Flask(__name__)
post = Post()
data = post.fetch_post()

@app.route('/')
def home(posts = data):
    return render_template("index.html", posts = posts)

@app.route('/post/<num>')
def post(num, posts= data):
    return render_template('post.html', posts = posts, num=num)

if __name__ == "__main__":
    app.run(debug=True)
