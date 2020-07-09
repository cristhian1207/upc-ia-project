def insert(dni, conn):
  attendaceId = None
  query="""
    INSERT INTO ATTENDANCES (DNI) 
    VALUES (%s)
  """
  c = conn.cursor()
  c.execute(query, [dni])
  attendaceId = c.lastrowid
  return attendaceId