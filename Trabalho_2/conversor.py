def gcl_para_apnd(arquivo):
    try:
        with open(arquivo, 'r') as f:
            linhas = f.readlines()
    except FileNotFoundError:
        print(f"ERRO: O arquivo '{arquivo}' não foi encontrado.")
        return

    terminais = set()
    regras = []
    
    for linha in linhas:
        linha = linha.strip()
        
        esquerdo, direito = linha.split('->')
        esquerdo = esquerdo.strip()
        direito = direito.strip().split()
        
        regras.append((esquerdo, direito))

        for elemento in direito:
            if elemento != 'e' and elemento.islower():
                terminais.add(elemento)

    print(f"Transições geradas a partir do arquivo '{arquivo}':\n")
    
    # A -> β:  δ(q, ε, A) = (q, β)
    for esquerdo, direito in regras:
        dir = "".join(direito) if direito != ['e'] else "ε"
        print(f"δ(q, ε, {esquerdo}) = (q, {dir})")

    # x:  δ(q, x, x) = (q, ε)
    for t in sorted(list(terminais)):
        print(f"δ(q, {t}, {t}) = (q, ε)")

if __name__ == "__main__":
    nome_do_arquivo = 'glc.txt'
    gcl_para_apnd(nome_do_arquivo)