[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/4x4sqhyD)
## Checkpoint

### INFORMAÇÕES DOS INTEGRANTES

Nome1: Pedro Yuzo Maeda Goyos 
RM: 84553

Nome2: Bruno Kenji Sakimoto
RM: 87217

LINK DO VIDEO: ____________________

## Visão Computacional para Assistência ao Motorista

Nesta checkpoint, vamos desenvolver um projeto de visão computacional voltado para a assistência ao motorista, utilizando um vídeo de um carro em uma rodovia. O objetivo é realizar a segmentação das faixas da estrada e gerar uma indicação visual no vídeo para alertar o motorista sobre a presença de veículos à frente, curvas na pista, entre outros aspectos relevantes para a segurança na direção.

## Informações importantes Entrega

A solução deve estar funcionando de acordo com a rubrica na data defina na programação de aulas.

Faça um vídeo mostrando a execução do seu programa e adicione o `link` do vídeo no README.md do seu repositório.

Checkpoint em dupla

## Instruções gerais 

O vídeo: o vídeo está no repositório 

A estrutura básica para executar o vídeo é formecida no arquivo `cp1.py` use esse arquivo para realizar o projeto.

## Como executar 

Primeiramente, garanta que as bibliotecas estão instaladas. No CMD/terminal digite: (esse comando so precisa ser executado uma única vez.)

```bash
pip install -r requirements.txt
```

Para executar os testes localmente (em sua maquina). No CMD/terminal dentro do diretorio do seu projeto digite:

```bash
python cp1.py
``` 

Faça `commit` e `push` para o repositório do seu projeto regularmente.

```bash
git add .
git commit -m "seu commit"
git push
``` 



## Rubrica - Critérios de entrega e avaliação para nota:

- R1 - NOTA 4: Use o vídeo fornecido para implementar um código que:

    - Realize a segmentação das faixas da rodovia no vídeo (em praticamente todos os frames), utilizando técnicas de processamento de imagem que achar mais apropriada e exiba o resultado. (`máx 4 pontos`).

- R2 - NOTA 7: Faça o R1 e:

    - Implemente a detecção de curvas (dirieta ou esquerda) na pista e exiba uma indicação visual no vídeo quando o veículo estiver se aproximando de uma curva. (`máx 1,5 pontos`)

    - Indique ao motorista a intensidade da curva (suave ou acentuada). (`máx 1,5 pontos`)

- R3 - NOTA 10: Faça o R2 e:

Adicione funcionalidades extras ao seu projeto, como a detecção de faixas contínuas e tracejadas (`máx 1,5 pontos`) e deteção de outros veiculos (`máx 1,5 pontos`) e exiba uma indicação visual no vídeo.

R4 - BÔNUS (2 pontos extras): Faça o R3 e:

Integre o seu sistema de assistência ao motorista com algum simulador de direção ou jogo de corrida, de forma que os alertas visuais sejam refletidos no comportamento do veículo no simulador. (`máx 2 pontos`)


## Como executar 

Primeiramente, garanta que as bibliotecas estão instaladas. No CMD/terminal digite:

```bash
pip install -r requirements.txt
```



### Dicas Importantes

- **Não altere os nomes dos arquivos ou funções**: Isso pode fazer com que os testes automáticos falhem, mesmo que sua solução esteja correta.
- **Leia os erros com atenção**: Eles podem fornecer dicas sobre o que está errado em seu código.
- **Peça ajuda**: Se estiver tendo dificuldades, não hesite em pedir ajuda ao professor ou colegas.


Bom trabalho!