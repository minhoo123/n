# app.py

from flask import Flask, jsonify
from flask_cors import CORS
from crawler.news_scraper import get_news

app = Flask(__name__)

# 1) 특정 도메인(React dev server)만 허용 (예: localhost:3000)
#    여러 곳 허용하려면 리스트 내 여러 문자열
CORS(app, resources={
    r"/api/*": {"origins": ["http://127.0.0.1:3000", "http://localhost:3000"]}
})

@app.route("/api/news")
def news():
    return jsonify(get_news())

if __name__ == "__main__":
    # 2) 포트 지정 (예: 5000), debug=True 유지
    app.run(host="0.0.0.0", port=5000, debug=True)
