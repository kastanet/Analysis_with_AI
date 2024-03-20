from flask import Flask, render_template, request
from google.cloud import vision
import os

app = Flask(__name__)

# Google Cloud Vision APIの認証情報のパスを設定
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\s1280\\OneDrive\\デスクトップ\\prefab-isotope-401211-70acce0fd29e.json"


# クライアントのインスタンスを作成
client = vision.ImageAnnotatorClient()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        # アップロードされたファイルを取得
        uploaded_file = request.files['file']
        
        # ファイル内容を読み込んでVision APIに送信
        content = uploaded_file.read()
        image = vision.Image(content=content)

        # Vision APIでラベル検出を実行
        response = client.label_detection(image=image)
        labels = response.label_annotations

        # 検出されたラベルを表示
        label_descriptions = [label.description for label in labels]

        return render_template('result.html', labels=label_descriptions)
    else:
        return "Method Not Allowed", 405

if __name__ == '__main__':
    app.run(debug=True)

