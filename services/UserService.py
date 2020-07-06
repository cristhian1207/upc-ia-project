from DatabaseConnection import DatabaseConnection
import user_dao

class UserService(object):

  def __init__(self):
    self.db_conn = DatabaseConnection().connection

  def insert(self, user):
    user_dao.insert(user, self.db_conn)

  def commit(self):
    self.db_conn.commit()

  def rollback(self):
    self.db_conn.rollback()

  def close(self):
    self.db_conn.close()