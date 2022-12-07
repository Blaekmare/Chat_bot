from funktion import *

class Searcher:

##Инициация экземпляра класса

    def __int__(self):
        self.names = None
        self.numbers = None
        self.full_names = None

##поиск имен по тексту что вводит пользователь
    def parse_query(self, text: str) -> list:
        ##вывод из базы данных списка всех лекарств
        namesis = list(DID_COMMAND_INDB("select neme from medicin"))
        name = list()
        for i in namesis:
            name.append(convert_tuple(i))
        self.names = name
        val = text.upper().strip()
        name = list()
        for i in range(len(self.names)):
            if val in self.names[i]:
                name.append(self.names[i])
        return name

##вывод итоговых данных
    def get_prices(self, name: list) -> list:
        ##вывод цен из базы данных списка всех лекарств
        numbe = list(DID_COMMAND_INDB("select bought from medicin"))
        ##вывод полных имен из базы данных списка всех лекарств
        full_names = list(DID_COMMAND_INDB("select full_name from medicin"))
        number = list()
        full_name = list()
        for i in numbe:
            number.append(convert_tuple_int(i))
        for i in full_names:
            full_name.append(convert_tuple_int(i))
        self.numbers = number
        self.full_names = full_name
        for i in range(len(self.names)):
            for nam in name:
                if self.names[i] == nam:
                    numbr = self.numbers[i]
                    funam = self.full_names[i]
                    print(nam, numbr, funam)
                    yield nam, numbr, funam
