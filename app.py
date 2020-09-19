from flask import Flask, render_template, request
from script import InstagramScraper

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hashtag', methods=['POST'])
def search():
    k = InstagramScraper()
    hashtag = request.form['hashtag']
    results = k.profile_page_recent_posts('https://www.instagram.com/explore/tags/'+hashtag)
    return '<div>' +str(results) +'</div>'


if __name__ == "__main__":
    app.run(debug=True)