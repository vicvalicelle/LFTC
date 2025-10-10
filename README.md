# Trabalho 1

## Conversor de AFND-ε em AFND

Este projeto consiste em um script Python que converte um Autômato Finito Não Determinístico com transições épsilon (AFND-ε) para um Autômato Finito Não Determinístico sem transições épsilon (AFND). O processo de conversão remove as transições épsilon e, em seguida, otimiza o autômato resultante eliminando quaisquer estados que se tornem inalcançáveis a partir do estado inicial.

### Funcionalidades

-   **Conversão de AFND-ε para AFND**: Implementa um algoritmo iterativo para absorver o comportamento das transições épsilon nas transições regulares.
-   **Leitura de Arquivo**: O autômato é lido a partir de um arquivo de texto (`automato.txt`), que suporta legendas e comentários (linhas iniciadas com `#`) para facilitar a edição e a compreensão.

### Formato do Arquivo de Entrada ('automato.txt')

A ordem das seções de dados é importante:

1.  **Linha 1 (dados)**: Lista de todos os estados, separados por espaço.
2.  **Linha 2 (dados)**: O alfabeto do autômato. Use `e` para representar a transição épsilon (ε).
3.  **Linha 3 (dados)**: O estado inicial.
4.  **Linha 4 (dados)**: Lista dos estados finais, separados por espaço.
5.  **Linhas seguintes (dados)**: As transições, uma por linha, no formato `estado_origem simbolo estado_destino`.

# Trabalho 2

## Conversor de GLC para APND

Este projeto consiste em um script Python que converte uma Gramática Livre de Contexto para um Autômato de Pilha Não-Determinístico equivalente.

### Funcionalidades

  - **Conversão de GLC para APND**: Implementa o algoritmo de conversão baseado em duas regras principais:
    1.  **Expansão de Não-Terminais**: Para cada regra de produção, gera uma transição épsilon (`ε`) que substitui um não-terminal no topo da pilha pelo corpo da sua regra.
    2.  **Casamento de Terminais**: Para cada símbolo terminal da gramática, gera uma transição que o consome da fita de entrada se ele corresponder ao topo da pilha.
  - **Leitura de Arquivo**: A gramática é lida a partir de um arquivo de texto (`gramatica.txt`), que suporta comentários (linhas iniciadas com `#`) para facilitar a edição e a compreensão.

### Formato do Arquivo de Entrada (`gcl.txt`)

Para que o script funcione corretamente, o arquivo de entrada deve seguir as seguintes convenções:

1.  **Uma Regra por Linha**: Cada linha do arquivo deve conter apenas uma regra de produção.
2.  **Símbolo de Produção**: Utilize `->` para separar o não-terminal (cabeça) do corpo da regra.
3.  **Separação de Símbolos**: Os símbolos no corpo da regra devem ser separados por espaços.
      - **Correto**: `S -> a S b`
      - **Incorreto**: `S -> aSb`
4.  **Transição Vazia (Épsilon)**: Use a palavra-chave `e` para representar a produção vazia (`ε`).
5.  **Convenção de Nomenclatura**:
      - **Não-Terminais**: Devem começar com uma letra maiúscula.
      - **Terminais**: Devem começar com uma letra minúscula.
6.  **Comentários**: Linhas que começam com `#` são ignoradas, permitindo adicionar anotações ao arquivo.