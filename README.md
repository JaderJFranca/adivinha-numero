# Adivinhe o Número

Este é um jogo simples de adivinhação em Python, onde o objetivo é descobrir um número aleatório gerado pelo programa, com um número limitado de tentativas.

## Como funciona o jogo

1. O programa escolhe um número aleatório entre 0 e 100.
2. O jogador tem 10 chances para adivinhar o número.
3. Após cada tentativa, o programa dá uma dica se o número correto é maior ou menor do que o chute.
4. Se o jogador acertar, ele vence e o jogo termina.
5. Se as chances acabarem antes do acerto, o número correto é revelado e o jogo termina.

## Regras

- O jogador deve inserir números entre 0 e 100.
- Caso o jogador insira algo que não seja um número ou um valor fora do intervalo, o programa exibe uma mensagem de erro e o jogador perde uma tentativa.

## Como executar

Certifique-se de ter o Python instalado no seu computador. Para executar o jogo:

1. Salve o código em um arquivo com extensão `.py`, por exemplo, `adivinhe_numero.py`.
2. Abra um terminal ou prompt de comando.
3. Navegue até o diretório onde o arquivo foi salvo.
4. Execute o comando:

   ```bash
   python adivinhe_numero.py
