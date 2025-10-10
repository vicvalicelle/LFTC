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
        if not linha or linha.startswith('#'):
            continue
        
        head, body_str = linha.split('->')
        head = head.strip()
        body = body_str.strip().split()
        
        regras.append((head, body))

        for symbol in body:
            if symbol != 'e' and symbol.islower():
                terminais.add(symbol)

    print(f"Transições geradas a partir do arquivo '{arquivo}':\n")
    
    # Para cada regra A -> β, crie a transição δ(q, ε, A) = (q, β)
    for head, body in regras:
        body_formatado = "".join(body) if body != ['e'] else "ε"
        print(f"δ(q, ε, {head}) = (q, {body_formatado})")

    # Para cada terminal 'x', crie a transição δ(q, x, x) = (q, ε)
    for t in sorted(list(terminais)):
        print(f"δ(q, {t}, {t}) = (q, ε)")

# Execução
if __name__ == "__main__":
    nome_do_arquivo = 'glc.txt'
    gcl_para_apnd(nome_do_arquivo)