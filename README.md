# WebApp_11

GPTアプリについて

WebApp_11というリポジトリに入れました。

1.ファイル構成
WebApp_11/
│
├── .env
├── .gitignore
├── app.py
└── requirements.txt　（一旦不要）

・プロジェクトのルートディレクトリに .env ファイルを作成し、以下のようにAPIキーを設定します。
	API_KEY=（APIキーをいれて）
	
・.env ファイルがGitリポジトリに含まれないように .gitignore に追加します。
	# 環境変数ファイル
	.env
　
2.インストール
稼働させるために、以下のインストールが必要です。

  pip install openai
  pip install python-dotenv
