✨ Todo アプリ（Django）

Django を使って作成した Todo リスト管理アプリです。
Railway にデプロイしており、Web 上で動作します。

🔗 デプロイ先URL

https://web-production-f57be.up.railway.app/list/

🛠️ 使用技術

Python 3

Django 5

HTML / CSS (Django Template)

Railway（デプロイ）

Gunicorn / Whitenoise

PostgreSQL（Railway）

📌 主な機能

Todo 一覧表示

Todo の新規作成

Todo の編集

Todo の削除

Django の Class-Based View を使用

🚀 セットアップ方法（開発環境向け）
git clone https://github.com/ryo033141/todoproject.git
cd todoproject

# 仮想環境
python -m venv venv
source venv/bin/activate  # Windows は venv\Scripts\activate

pip install -r requirements.txt

# マイグレーションと起動
python manage.py migrate
python manage.py runserver

📂 フォルダ構成
todoproject/
 ├── todo/
 │    ├── views.py
 │    ├── models.py
 │    ├── templates/
 ├── todoproject/
 │    ├── settings.py
 │    ├── urls.py
 ├── staticfiles/
 ├── Procfile
 └── requirements.txt

📝 今後の改善予定

ユーザーログイン機能の追加

Bootstrap を使った UI 改善

独自ドメインの設定
