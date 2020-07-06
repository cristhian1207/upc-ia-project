def insert(dni, conn):
  attendaceId = None
  query="""
    INSERT INTO ATTENDANCES (DNI) 
    VALUES (%s)
  """
  with conn.cursor() as c:
    c.execute(query, [dni])
    attendaceId = c.lastrowid
  return attendaceId