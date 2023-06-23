usuario = "test"
contraseña = "test"

def CheckearLogin(user,passw):
    if(usuario == user) and (contraseña == passw):
        return True
    return False