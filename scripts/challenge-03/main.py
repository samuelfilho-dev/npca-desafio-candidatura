import numpy as np
import csv


class Fila:
    def __init__(self):

        self.capacidade = self.contar_linhas_arquivo()
        self.inicio = 0
        self.final = -1
        self.numeros_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=object)

        with open('dados.csv', newline='') as file:
            reader = csv.reader(file, delimiter=',')

            next(reader)
            for row in reader:
                self.valores[self.numeros_elementos] = row
                self.numeros_elementos += 1

            if self.__verificar_cabecalho():
                fieldnames = ["nome", "quantidade", "valor"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                self.numeros_elementos += 1

    def __fila_vazia(self):
        with open('dados.csv', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row:
                    return False
            return True

    def __fila_cheia(self):
        return self.numeros_elementos == self.capacidade

    def enfileirar(self, nome, quantidade, valor):
        if self.__fila_cheia(): return print('A Fila está Cheia')

        with open('dados.csv', 'a', newline='') as file:
            fieldnames = ['nome', 'quantidade', 'valor']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'nome': nome, 'quantidade': quantidade, 'valor': valor})

    def desenfileirar(self):
        if self.__fila_vazia(): return print('A Fila Já esta Vazia')

        temp = self.valores[self.inicio]
        self.inicio += 1

        if self.inicio == self.capacidade - 1:
            self.inicio = 0
        self.numeros_elementos -= 1

        with open('dados.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for i in range(self.numeros_elementos):
                writer.writerow([self.valores[i][0], self.valores[i][1], self.valores[i][2]])

        return temp

    def primeiro_elemento(self):
        if self.__fila_vazia(): return -1
        return self.valores[self.inicio]

    def valor_total(self):
        with open('dados.csv', 'r') as file:
            reader = csv.reader(file)
            total = 0
            for row in reader:
                total += int(row[1]) * float(row[2])
            print(f'O valor total da Fila é: {total}')

    @staticmethod
    def contar_linhas_arquivo():
        with open('dados.csv', 'r') as file:
            reader = csv.reader(file)
            return sum(1 for _ in reader)

    def __verificar_cabecalho(self):
        with open('dados.csv', 'r') as file:
            if file.readline().strip() != 'nome,quantidade,valor':
                return False


service = Fila()
# service.enfileirar('leite', 10, 3)
# service.desenfileirar()
service.valor_total()
print(service.primeiro_elemento())
