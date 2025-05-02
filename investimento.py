TAXA_ANUAL = 14.15
TAXA_MESES = TAXA_ANUAL / 12


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class IOF:
    """
    Classe responsável por calcular o Imposto sobre Operações Financeiras (IOF).
    """

    # Tabela de alíquotas do IOF por dia.
    tabela_de_imposto = {
        1: 0.96,
        2: 0.93,
        3: 0.90,
        4: 0.86,
        5: 0.83,
        6: 0.80,
        7: 0.76,
        8: 0.73,
        9: 0.70,
        10: 0.66,
        11: 0.63,
        12: 0.60,
        13: 0.56,
        14: 0.53,
        15: 0.50,
        16: 0.46,
        17: 0.43,
        18: 0.40,
        19: 0.36,
        20: 0.33,
        21: 0.30,
        22: 0.26,
        23: 0.23,
        24: 0.20,
        25: 0.16,
        26: 0.13,
        27: 0.10,
        28: 0.06,
        29: 0.03,
    }

    @classmethod
    def desconto(cls, tempo_aplicacao: int, rendimento: float) -> float:
        """
        Calcula o desconto do IOF sobre o rendimento.

        Args:
            tempo_aplicacao (int): O tempo de aplicação em dias.
            rendimento (float): O valor do rendimento bruto.

        Returns:
            float: O rendimento com o desconto do IOF aplicado.
        """

        if tempo_aplicacao > 29:
            return rendimento # Sem IOF após 29 dias.
        return rendimento * cls.tabela_de_imposto[tempo_aplicacao]


class IR:
    """
    Classe responsável por calcular o Imposto de Renda (IR) sobre o rendimento.
    """

    # Tabela de alíquotas do IR por período.
    tabela_de_imposto = {
        180: 0.225,
        360: 0.2,
        720: 0.175,
        float("inf"): 0.15,
    }

    @classmethod
    def desconto(cls, tempo_aplicacao: int, rendimento: float) -> float:
        """
        Calcula o desconto do IR sobre o rendimento.

        Args:
            tempo_aplicacao (int): O tempo de aplicação em dias.
            rendimento (float): O valor do rendimento já descontado do IOF.

        Returns:
            float: O rendimento com o desconto do IR aplicado.
        """

        for limite, aliquota in sorted(cls.tabela_de_imposto.items()):
            if tempo_aplicacao <= limite:
                return rendimento * aliquota
        return rendimento # Caso algo inesperado aconteça.


class Investimento:
    """
    Calcula o rendimento de um investidor(a), descontando o valor do investimento sobre o percentual do imposto baseado na tabela IOF e também sobre Imposto de Renda - IR
    
    """

    def __init__(self, valor: float, tempo_aplicacao: int) -> object:
        """
        Inicializa um objeto de investimento.

        Args:
            valor (float): O valor inicial do investimento.
            tempo_aplicacao (int): O tempo de aplicação em dias.
        """

        self.valor = valor
        self.tempo_aplicacao = tempo_aplicacao
        self.rendimento = 0

    @classmethod
    def get(cls): 
        """
        Obtém os dados do investimento do usuário através da entrada de texto.

        Returns:
            Investimento: Uma instância da classe Investimento com os dados fornecidos.
        """

        print(f"Olá, é um prazer ter você aqui em nossa Instituição Financeira!\nAqui, em nossa IF, a aplicação na Caixinha Super Cofrinho é: {bcolors.OKGREEN}14,15% a.a (1,18% a.m){bcolors.ENDC})!\n")

        valor: float = float(input("Valor de investimento: R$"))
        tempo_aplicacao: int = int(input("Tempo da aplicação (dias): "))

        return cls(valor, tempo_aplicacao)

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor: float):
        """
        Define o valor do investimento, validando se é um valor numérico positivo.

        Args:
            valor (float): O valor a ser definido para o investimento.

        Raises:
            ValueError: Se o valor não for especificado.
            TypeError: Se o valor inserido não for do tipo float.
        """

        if not valor:
            raise ValueError(f"{bcolors.WARNING}Você não especificou o valor do investimento!{bcolors.ENDC}")

        if not isinstance(valor, float):
            raise TypeError(f"{bcolors.WARNING}Valor inserido inválido!{bcolors.ENDC}")

        self._valor = valor # Define o valor do investimento.

    @property
    def tempo_aplicacao(self):
        return self._tempo_aplicacao

    @tempo_aplicacao.setter
    def tempo_aplicacao(self, tempo_aplicacao: int):
        """
        Define o tempo de aplicação, validando se é um número inteiro positivo.

        Args:
            tempo_aplicacao (int): O tempo de aplicação em dias.

        Raises:
            TypeError: Se o valor inserido não for do tipo int.
        """

        if not isinstance(tempo_aplicacao, int):
            raise TypeError(f"{bcolors.WARNING}Valor inserido inválido!{bcolors.ENDC}")

        self._tempo_aplicacao = tempo_aplicacao # Define o tempo de aplicação.

    @property
    def rendimento(self) -> float:
        return self._rendimento

    @rendimento.setter
    def rendimento(self, *args):
        """
        Calcula e define o rendimento líquido do investimento, aplicando IOF e IR.
        """
        
        self._rendimento = self.valor * (TAXA_MESES * (self.tempo_aplicacao / 30)) # Calcula o rendimento bruto.
        self._rendimento = IOF.desconto(self.tempo_aplicacao, self._rendimento) # Aplica o desconto do IOF.
        self._rendimento = IR.desconto(self.tempo_aplicacao, self._rendimento) # Aplica o desconto do IR.


if __name__ == "__main__":
    
    investidor = Investimento.get() # Obtém os dados do investimento do investidor(a).
    print(f"Seu rendimento é de: {bcolors.OKGREEN}R${investidor.rendimento:.2f}{bcolors.ENDC}") # Exibe o rendimento final.