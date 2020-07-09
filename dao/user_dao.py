def insert(user, conn):
  userId = None
  query="""
    INSERT INTO USERS (DNI, NAME, PAT_LASTNAME, MAT_LASTNAME) 
    VALUES (%s, %s, %s, %s)
  """
  c = conn.cursor()
  args = (
    user.DNI,
    user.NAME,
    user.PAT_LASTNAME,
    user.MAT_LASTNAME
  )
  c.execute(query, args)