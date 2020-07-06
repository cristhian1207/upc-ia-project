class User(object):
  def __init__(self, DNI, NAME, PAT_LASTNAME, MAT_LASTNAME, CREATED_DATE, LASTUPDATE_DATE):
    self.DNI = DNI
    self.NAME = NAME
    self.PAT_LASTNAME = PAT_LASTNAME
    self.MAT_LASTNAME = MAT_LASTNAME
    self.CREATED_DATE = CREATED_DATE
    self.LASTUPDATE_DATE = LASTUPDATE_DATE

  def __str__(self):
    obj_str='{'
    obj_str+=f'"DNI": "DNI",'
    obj_str+=f'"NAME": "NAME",'
    obj_str+=f'"PAT_LASTNAME": "PAT_LASTNAME",'
    obj_str+=f'"MAT_LASTNAME": "MAT_LASTNAME",'
    obj_str+=f'"CREATED_DATE": "CREATED_DATE",'
    obj_str+=f'"LASTUPDATE_DATE": "LASTUPDATE_DATE"'
    obj_str+='}'
    return obj_str