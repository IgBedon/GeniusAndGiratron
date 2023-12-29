class Player:

    def __init__(self, nickname, cpf):
        self.__nickname = nickname
        self.__cpf = cpf
        self.__stage = 0

    
    def get_name(self):
        return self.__nickname
    

    def get_cpf(self):
        return self.__cpf
    

    def get_stage(self):
        return self.__stage


    def set_stage(self, stage):
        self.__stage = stage
