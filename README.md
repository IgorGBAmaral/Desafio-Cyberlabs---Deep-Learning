# Desafio Cyberlabs - Deep-Learning

### Como usar:

- Faça download do repositório e abra o **DesafioDeepLearningCyberlabs.ipynb** usando o Google Colab
- Faça download das imagens para treino no link: https://drive.google.com/open?id=1sJwUVLNkTNI4m6_UfWt727tfpLkmX0n2
- Crie uma nova pasta no seu Drive pessoal e altere os endereços no Colab para o endereço da pasta do seu Drive (Há mais detalhes por lá)
- Rode as linhas de código do Colab
- Na última parte, altere o endereço para o da imagem especifica que quer testar

### Processo de Treinamento:

- Comecei extremamente perdido, pois nem sabia muito sobre os conceitos, apenas as capacidades da AI e que eu iria gostar de aprender pois já gosto de programar
- Iniciei buscando mais conhecimento teórico e explicações sobre o que realmente é AI, Machine Learning, Deep Learning, Visão Computacional, enfim, todos os termos relacionados a eles também
- Quanto mais eu aprendia, mais foi aparecendo para aprender, e fui me aprofundando em conhecimentos cada vez mais especificos, porém, muitas vezes me perdi estudando coisas que não seriam aplicadas nesse projeto
- Como no material passado possuia bastante coisa sobre o OpenCV, comecei a fazer um tutorial ensinando a usá-lo, e na lista de vídeos tinha um vídeo sobre reconhecimento de imagens, então continuei seguindo em frente. Porém, quando cheguei nessa etapa, eu precisava de um modelo já pré definido, e eu não tinha, e não queria usar modelos pré treinados pois queria ter a experiência de fazer o meu e entender melhor como isso funcionava
- Então fui buscar como fazer, e comecei a estudar o Tensorflow, só que tive diversos problemas durante a instalação, o que me fez perder boas horas tentando entender como tudo funcionava e consegui resolver os problemas, com a instalação concluída, fui buscando mais informação sobre o Tensor flow até achar tutoriais sobre a criação de um modelo para finalmente fazer meu classificador
- Daqui, quis ter 100 imagens em média de cada empresa aérea para poder fazer meu modelo, para isso precisava de uma forma mais eficiente de baixar as imagens
- Encontrei uma extensão do chrome chamada "Image Downloads" que me permitia baixar cada imagem com um clique, o que ficou bem fácil para juntar minhas imagens
- Com as imagens baixadas tentei seguir alguns tutoriais mais eles novamente me encaminhavam para um modelo já pré treinado, mas no processo fui baixando diversas bibliotecas e pacotes, e aprendendo mais sobre diversas formas de usar o tensorflow
- Depois disso, comecei a pesquisar no site towardsdatascience.com artigos que poderiam me encaminhar para o que eu queria e lá consegui achar artigos onde aprendi ainda mais e que me direcionavam para o caminho que eu queria
- Encontrei alguns artigos que explicavam bem os conceitos e como isso se traduzia em código, a partir dai fui lendo e entendendo os códigos e comecei um projeto no PyCharm onde fui comentando o que fui fazendo e entendendo, até me deparar com alguns problemas de execução, que fiquei um bom tempo tentando resolver, mas, meu prazo estava acabando e fui testar o código no Colab, e funcionou, por isso acabei finalizando meu projeto por lá mesmo.
- Até hoje, nunca tinha feito um projeto com tanto conceito que eu nunca tinha ouvido falar, foi bem desafiador, mas fiquei satisfeito com o resultado, queria poder melhorar e implementar ele em alguma outra plataforma, para que ele seja de fácil acesso (android por exemplo)
- O que me deixou mais satisfeito, é que se eu quiser treinar novas classes, é bem simples de adaptar esse código
- Também fiquei feliz pois aprendi a buscar conhecimento em lugares que eu não costumava buscar, e com certeza me tornei um programador melhor, estou empolgado e quero aprender ainda mais

### Arquitetura

- Tensorflow
- Keras
- Numpy

### Processamento de imagem
O processamento foi feito reduzindo o tamanho da imagem(para ter um treinamento mais rápido) e a transformando em um tensor, que era usado no treinamento
