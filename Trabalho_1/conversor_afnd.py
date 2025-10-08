from collections import defaultdict

class AFND:
    def __init__(self, estados, alfabeto, transicoes, inicial, finais):
        self.estados = set(estados)
        self.alfabeto = set(alfabeto)
        self.transicoes = transicoes
        self.estado_inicial = inicial
        self.estados_finais = set(finais)

    def imprimir(self):
        print(f"Estados: {', '.join(sorted(list(self.estados)))}")
        alfabeto_sem_e = sorted(list(self.alfabeto - {'e'}))
        print(f"Alfabeto: {', '.join(alfabeto_sem_e)}")
        print(f"Estado Inicial: {self.estado_inicial}")
        print(f"Estados Finais: {', '.join(sorted(list(self.estados_finais)))}")
        print("Transições:")
        for (origem, simbolo), destinos in sorted(self.transicoes.items()):
            if simbolo != 'e':
                print(f"  δ({origem}, {simbolo}) -> {{{', '.join(sorted(list(destinos)))}}}")


def converter(automato):
    novas_transicoes = defaultdict(set)
    for (origem, simbolo), destinos in automato.transicoes.items():
        if simbolo != 'e':
            novas_transicoes[(origem, simbolo)] = destinos.copy()

    novos_finais = automato.estados_finais.copy()

    houve_mudanca = True
    while houve_mudanca:
        houve_mudanca = False
        
        transicoes_epsilon = [
            (origem, next(iter(destinos))) for (origem, simbolo), destinos in automato.transicoes.items() 
            if simbolo == 'e'
        ]

        for p1, p2 in transicoes_epsilon:
            for (origem_trans, a), destinos_q in list(novas_transicoes.items()):
                if origem_trans == p2:
                    for q in destinos_q:
                        if q not in novas_transicoes.get((p1, a), set()):
                            novas_transicoes[(p1, a)].add(q)
                            houve_mudanca = True

            if p2 in novos_finais and p1 not in novos_finais:
                novos_finais.add(p1)
                houve_mudanca = True

    novo_alfabeto = automato.alfabeto - {'e'}
    return AFND(
        automato.estados,
        novo_alfabeto,
        novas_transicoes,
        automato.estado_inicial,
        novos_finais
    )


def ler_automato(arquivo):
    try:
        with open(arquivo, 'r') as f:
            linhas = f.readlines()
            dados = []
            for linha in linhas:
                linha_limpa = linha.strip()
                if linha_limpa and not linha_limpa.startswith('#'):
                    dados.append(linha_limpa)

            if len(dados) < 4:
                print("Erro: O arquivo não contém dados suficientes (estados, alfabeto, inicial, finais).")
                return None

            estados = dados[0].split()
            alfabeto = dados[1].split()
            inicial = dados[2]
            finais = dados[3].split()
            
            transicoes = defaultdict(set)
            for linha in dados[4:]:
                partes = linha.split()
                if len(partes) == 3:
                    origem, simbolo, destino = partes
                    transicoes[(origem, simbolo)].add(destino)

            return AFND(estados, alfabeto, transicoes, inicial, finais)
            
    except FileNotFoundError:
        print(f"Erro: O arquivo não foi encontrado.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro ao processar o arquivo: {e}")
        return None

# Execução
afnd_com_epsilon = ler_automato("automato.txt")

if afnd_com_epsilon:
    print("\nAutômato lido do arquivo:\n")
    print(f"Estados: {afnd_com_epsilon.estados}")
    print(f"Alfabeto: {afnd_com_epsilon.alfabeto}")
    print(f"Estado Inicial: {afnd_com_epsilon.estado_inicial}")
    print(f"Estados Finais: {afnd_com_epsilon.estados_finais}")
    
    afnd_sem_epsilon = converter(afnd_com_epsilon)
    
    print("\nAutômato Convertido:\n")
    afnd_sem_epsilon.imprimir()
