"""
記事モデル
"""
from app.models.abstract import AbstractModel


class ArticleModel(AbstractModel):
    def __init__(self, config):
        super(ArticleModel, self).__init__(config)

    def fetch_recent_articles(self, limit=5):
        """
        最新の記事を取得する．デフォルトでは最新5件まで
        :param limit: 取得する記事の数
        :return:
        """
        sql = "SELECT * FROM articles ORDER BY created_at DESC LIMIT %s"
        return self.fetch_all(sql, limit)

    def fetch_article_by_id(self, article_id):
        """
        指定されたIDの記事を取得
        :param article_id: 取得したい記事のID
        :return: 指定された記事のID
        """
        sql = "SELECT * FROM articles INNER JOIN users u on articles.user_id = u.id WHERE articles.id=%s"
        return self.fetch_one(sql, article_id)

    def create_article(self, user_id, title, body, image_path):
        """
        新しく記事を作成する
        :param user_id: 投稿したユーザのOD
        :param title: 記事のタイトル
        :param body: 記事の本文
        :image_path: 画像のパス(appは含まない方が良い)
        :return: None
        """
        sql = "INSERT INTO articles(user_id, title, body, image_path) VALUE (%s, %s, %s, %s);"
        self.execute(sql, user_id, title, body, image_path)
