from anotacao import AnotacaoModel


class GerenciadorAnotacoes:
    def __init__(self):
        self.anotacoes = []

    def adicionar_anotacao(self, title, conteudo):
        anotacao_file = AnotacaoModel(title, conteudo)
        self.anotacoes.append(anotacao_file)
        with open('anotacoes.txt', 'a') as file:
            file.write(str(anotacao_file) + '\n')

    def listar_anotacoes(self):
        for anotacao in self.anotacoes:
            print(anotacao)

    def listar_anotacoes_no_arquivo(self):
        with open('anotacoes.txt', 'r') as file:
            for line in file:
                print(line.strip())


service = GerenciadorAnotacoes()
service.adicionar_anotacao('Anotação 1', 'Conteúdo da anotação 1')
service.adicionar_anotacao('Anotação 2', 'Conteúdo da anotação 2')
#service.listar_anotacoes()
service.listar_anotacoes_no_arquivo()
