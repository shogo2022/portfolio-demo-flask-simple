from flask import Flask, render_template, json, jsonify, request, redirect, url_for

from models import dbtool


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/meme', methods=['POST'])
def process_meme():
    meme = dbtool.get_test_meme()
    return_json = {
        'meme_desc': meme['description'],
        'meme_image': meme['image_path']
    }
    return jsonify(ResultSet=json.dumps(return_json))


if __name__ == '__main__':
    app.debug = True # デバッグモード有効化
    app.run(host='0.0.0.0') # どこからでもアクセス可能に