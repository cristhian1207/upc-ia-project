import os
import MySQLdb as Database
import logging
import sqlalchemy.pool as pool
from sqlalchemy.pool import QueuePool

PoolDatabase=pool.manage(Database, poolclass=QueuePool, pool_size=2, max_overflow=3, timeout=5, recycle=119)
def get_connection():
  '''Obtener una conexión del Pool'''
  return PoolDatabase.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'mysql', 
    database = 'project_ia', 
    local_infile = 1
  )