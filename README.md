# Trabalho 1

## Conversor de AFND-ε em AFND

Este projeto consiste em um script Python que converte um Autômato Finito Não Determinístico com transições épsilon (AFND-ε) para um Autômato Finito Não Determinístico sem transições épsilon (AFND). O processo de conversão remove as transições épsilon e, em seguida, otimiza o autômato resultante eliminando quaisquer estados que se tornem inalcançáveis a partir do estado inicial.

### Funcionalidades

-   **Conversão de AFND-ε para AFND**: Implementa um algoritmo iterativo para absorver o comportamento das transições épsilon nas transições regulares.
-   **Leitura de Arquivo**: O autômato é lido a partir de um arquivo de texto (`automato.txt`), que suporta legendas e comentários (linhas iniciadas com `#`) para facilitar a edição e a compreensão.
-   **Remoção de Estados Inalcançáveis**: Após a conversão, o script realiza uma "limpeza" para remover estados que não são mais acessíveis a partir do estado inicial, resultando em um autômato final minimizado.

A ordem das seções de dados é importante:

1.  **Linha 1 (dados)**: Lista de todos os estados, separados por espaço.
2.  **Linha 2 (dados)**: O alfabeto do autômato. Use `e` para representar a transição épsilon (ε).
3.  **Linha 3 (dados)**: O estado inicial.
4.  **Linha 4 (dados)**: Lista dos estados finais, separados por espaço.
5.  **Linhas seguintes (dados)**: As transições, uma por linha, no formato `estado_origem simbolo estado_destino`.
