from DatabaseConnection import DatabaseConnection
import attendace_dao

class AttendaceService(object):

  def __init__(self):
    self.db_conn = DatabaseConnection().connection

  def insert(self, dni):
    attendace_dao.insert(dni, self.db_conn)

  def commit(self):
    self.db_conn.commit()

  def rollback(self):
    self.db_conn.rollback()

  def close(self):
    self.db_conn.close()