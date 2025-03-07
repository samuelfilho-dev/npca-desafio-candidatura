class AnotacaoModel:
    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo

    def __str__(self):
        return f'Título: {self.titulo}\nConteúdo: {self.conteudo}'