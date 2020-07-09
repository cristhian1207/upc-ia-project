class DatabaseConnection():
  def __init__(self):
    import mysql_connection as connection
    self.connection = connection.get_connection()

  def commit(self):
    self.connection.commit()

  def rollback(self):
    self.connection.rollback()

  def close(self):
    self.connection.close()