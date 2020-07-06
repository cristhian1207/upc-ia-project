from User import User
from UserService import UserService
from AttendaceService import AttendaceService

def createUser():
  print('Insertar Dni:')
  dni = input().strip()

  print('Insertar Nombre:')
  name = input().strip().upper()

  print('Insertar Apellido Paterno:')
  patLastname = input().strip().upper()

  print('Insertar Apellido Materno:')
  matLastname = input().strip().upper()

  user = User(dni, name, patLastname, matLastname, None, None)
  userService = UserService()
  userService.insert(user)
  userService.commit()
  userService.close()
  return dni

def markAttendance(dni):
  attendaceService = AttendaceService()
  attendaceService.insert(dni)
  attendaceService.commit()
  attendaceService.close()
  print('\a')