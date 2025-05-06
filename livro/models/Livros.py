class Livros:
    def __init__(self, titulo, autor, editora, paginas, ano, pagina_atual):
        self.titulo = titulo
        self.editora = editora
        self.autor = autor
        self.paginas = paginas
        self.ano = ano
        self.pagina_atual = pagina_atual
        
    def avancar_pagina(self):
        if self.pagina_atual <= self.paginas:
            self.pagina_atual = self.pagina_atual + 1
            print("Você está na página", self.pagina_atual)

    def voltar_pagina(self):
        if self.pagina_atual < 1:
            print("Livro não iniciado")
        else:
            self.pagina_atual = self.pagina_atual -1
            print("Você está na página:", self.pagina_atual)

    def exibir_informacoes(self):
        print("Você está lendo o livro",self.titulo,", autoral de", self.autor,"feito pela editora",self.editora,", com",self.paginas,"páginas e do ano", self.ano)

    