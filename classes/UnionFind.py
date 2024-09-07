class UnioFind:
    def __init__(self, pessoa):
        self.Pessoa = pessoa
        self.Amigos = []
    
    def makeFriend(self, amigo):
        self.Amigos.append[amigo]
        amigo.Amigos.append[self]
    
    def dropFriend(self, amigo):
        pass

    def buscarFriend(self, amigo):
        for i in self.Amigos:
            if i.Pessoa.nome == amigo:
                return amigo