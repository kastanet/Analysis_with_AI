<<<<<<< HEAD
def detect_labels():
    import io
    import os
    # Imports the Google Cloud client library
    from google.cloud import vision
    # Instantiates a client
    client = vision.ImageAnnotatorClient()
    # The name of the image file to annotate
    file_name = os.path.abspath('./wakeupcat.jpg')
    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')
    for label in labels:
        print(label.description)
detect_labels()
=======
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

>>>>>>> e74b6bb846009a32926ca175c6b42303a9e03496