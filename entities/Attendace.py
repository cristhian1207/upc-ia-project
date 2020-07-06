class Attendace(object):
  def __init__(self, ID, DNI, ATTENDACE_TIME):
    self.ID = ID
    self.DNI = DNI
    self.ATTENDACE_TIME = ATTENDACE_TIME

  def __str__(self):
    obj_str='{'
    obj_str+=f'"ID": "ID",'
    obj_str+=f'"DNI": "DNI",'
    obj_str+=f'"ATTENDACE_TIME": "ATTENDACE_TIME"'
    obj_str+='}'
    return obj_str