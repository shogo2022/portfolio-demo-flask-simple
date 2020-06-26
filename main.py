from flask import Flask, render_template, json, jsonify, request, redirect, url_for

import logic
from models.settings import session


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/meme', methods=['POST'])
def process_meme():
    meme = logic.get_test_meme()
    return_json = {
        'meme_desc': meme.description,
        'meme_image': meme.image_path
    }
    return jsonify(ResultSet=json.dumps(return_json))



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)