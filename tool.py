from data import user

def Find_Login_Users(nome_usuario, senha):
    for usuario in user:
        if usuario["nome"] == nome_usuario and usuario["senha"] == senha:
            return True
    return False

def Find_User(TypeScreth,name):
        for usuario in user:
            if name == usuario["nome"]:
                return usuario[TypeScreth]
        return False


