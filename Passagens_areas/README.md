ENUNCIADO DO DESAFIO 
AfroCodigos - Venda de passagens

Crie um sistema de venda de passagens aéreas, projetado para facilitar a reserva de voos para os clientes. Eles podem comprar passagens aéreas para viagens entre diferentes cidades.
Descrição Técnica
Cadastro de Passagens Aéreas:

Os usuários podem comprar passagens aéreas, inserindo informações como origem, destino e preço da passagem. Cada passagem é representada por um objeto da classe PassagemAerea, que armazena essas informações.
Gerenciamento de Passagens:

O gerenciamento de passagens é realizado pela classe PassagensAereasManager, que mantém uma lista de todas as passagens compradas. Os usuários podem adicionar passagens à lista por meio do método adicionar_passagem().
Exibição de Passagens:

As passagens compradas podem ser listadas para visualização. O método listar_passagens() da classe PassagensAereasManager é responsável por exibir as informações de todas as passagens compradas.
Menu de Opções:

O programa oferece um menu com opções para comprar passagens, listar passagens compradas e sair do programa.
Encerramento do Programa:
Os usuários têm a opção de sair do programa a qualquer momento, encerrando a execução.