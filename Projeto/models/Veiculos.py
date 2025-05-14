class Veiculos:
    """
    Classe com as principais funcionalidades do sistem de veículos.
    """
    def __init__(self, placa: float, modelo: str, marca: str, ano: int, cor:str, valor_fipe: float)-> None:
        #Construtor da classe Veículos:
        self.__placa = placa
        self.__modelo: modelo
        self.__marca = marca
        self.__ano = ano
        self.__cor = cor
        self.__valor_fipe = valor_fipe

    def __str__(self) -> str:
        #retorna uma string com as informações do veículo
        infos = f"Placa:{self._placa}\n"
        infos += f"Modelo{self._modelo}\n"
        infos += f"Marca: {self.__marca}\n"
        infos += f"Ano: {self.__ano}\n"
        infos += f"Cor: {self.__cor}\n"
        pass

    def getplaca(self) -> str:
        #retorna a placa do veículo
        