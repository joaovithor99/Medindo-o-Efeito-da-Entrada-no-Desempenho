class NoAVL:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None
        self.altura = 1

class AVL:
    def __init__(self):
        self.raiz = None

    def obter_altura(self, no):
        if not no:
            return 0
        return no.altura

    def obter_fator_balanceamento(self, no):
        if not no:
            return 0
        return self.obter_altura(no.esquerda) - self.obter_altura(no.direita)

    def rotacao_direita(self, z):
        y = z.esquerda
        T3 = y.direita

        y.direita = z
        z.esquerda = T3

        z.altura = 1 + max(self.obter_altura(z.esquerda), self.obter_altura(z.direita))
        y.altura = 1 + max(self.obter_altura(y.esquerda), self.obter_altura(y.direita))

        return y

    def rotacao_esquerda(self, z):
        y = z.direita
        T2 = y.esquerda

        z.direita = T2
        y.esquerda = z

        z.altura = 1 + max(self.obter_altura(z.esquerda), self.obter_altura(z.direita))
        y.altura = 1 + max(self.obter_altura(y.esquerda), self.obter_altura(y.direita))

        return y

    def inserir(self, chave):
        self.raiz = self._inserir_recursivo(self.raiz, chave)

    def _inserir_recursivo(self, no, chave):
        if not no:
            return NoAVL(chave)

        if chave < no.chave:
            no.esquerda = self._inserir_recursivo(no.esquerda, chave)
        else:
            no.direita = self._inserir_recursivo(no.direita, chave)

        no.altura = 1 + max(self.obter_altura(no.esquerda), self.obter_altura(no.direita))

        fb = self.obter_fator_balanceamento(no)

        # Rotação Simples Direita
        if fb > 1 and chave < no.esquerda.chave:
            return self.rotacao_direita(no)

        # Rotação Simples Esquerda
        if fb < -1 and chave >= no.direita.chave:
            return self.rotacao_esquerda(no)

        # Rotação Dupla Esquerda-Direita
        if fb > 1 and chave >= no.esquerda.chave:
            no.esquerda = self.rotacao_esquerda(no.esquerda)
            return self.rotacao_direita(no)

        # Rotação Dupla Direita-Esquerda
        if fb < -1 and chave < no.direita.chave:
            no.direita = self.rotacao_direita(no.direita)
            return self.rotacao_esquerda(no)

        return no