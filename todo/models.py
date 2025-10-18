from django.db import models

CHOICE = (('danger','high'),('warning','normal'),('primary','low'))

class TodoModel(models.Model):
    # タイトルを最大100文字の文字列に定義
    title = models.CharField(max_length=100)
    # メモを長い文字列型に定義
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices=CHOICE
        )
    # 日付を日付型に定義
    duedate = models.DateField()

    # オブジェクトが作成された時に実行する関数
    def __str__(self):
        # タイトル名を返す
        return self.title