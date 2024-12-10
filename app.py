import streamlit as st # フロントエンドを扱うstreamlitの機能をインポート
from dotenv import load_dotenv
import base64
import os
from openai import OpenAI

# .envファイルを読み込む
load_dotenv()

client = OpenAI()
# 環境変数からAPIキーを取得
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

st.title("（仮）画像認識アプリ") # タイトル表示
explanation = "ここに画像をアップロードしてください。"
file_upload = st.file_uploader(explanation,type=["png","jpg","gif"]) # tesseractが認識できるpngとjpgだけを許可するアップローダーの設置

# アップロードされたらfile_uploadがNoneではなくなるので、実行される
if (file_upload !=None):

    st.image(file_upload) # 画像分析する画像を表示

    # Function to encode the image
    def encode_image(file_upload):
            return base64.b64encode(file_upload.read()).decode('utf-8')

    # Getting the base64 string
    base64_image = encode_image(file_upload)

    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "この写真に合うアルコール飲料を教えて下さい",
            },
            {
            "type": "image_url",
            "image_url": {
                "url":  f"data:image/jpeg;base64,{base64_image}"
            },
            },
        ],
        }
    ],
    )

    st.write(response.choices[0].message.content)

