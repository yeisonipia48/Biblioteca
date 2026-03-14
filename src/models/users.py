class User:
    def __init__(self,id_user,name_user, lastname_user):
        self.id_user=id_user
        self.name_user=name_user
        self.lastname_user=lastname_user
        self.libros_prestados=[]

    def __str__(self):
        return f"User: [{self.id_user}] {self.name_user} - {self.lastname_user}"
        