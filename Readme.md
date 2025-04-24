# Conversor de temperatura

## Descrição: 
O presente arquivo apresenta um projeto particular de conversor de temperatura feito em python utilizando estrutura OOP e o framework Custom Tkinter para GUI.

## Objetivo: 
Resolvi fazer esse projeto para rever e aprimorar minhas habilidades em programação, além de conhecer mais a fundo a biblioteca Custom Tkinter.

## O que é um conversor de temperatura CFK?
O nome "conversor de temperatura" é suficiente. CFK se refere as temperaturas Celsius (°C), Fahrenheit (°F) e Kelvin (K).
A medida Celsius é a mais usada; Kelvin é uma medida científica; e Fahrenheit é mais utilizada nos EUA. Elas são converdidas pelas seguintes fórmulas:

C/5 = (F-32)/9 = (K-273)/5

Onde:  
C = temperatura em gruas celsius  
F = temperatura em graus farenheit  
K = temperatura em kelvin  

## Detalhes:
O primeiro modelo desse programa foi feito apenas com uma interface simples de terminal e sem orientação a objeto. A única coisa que precisei fazer a mais foi pesquisar as fórmulas de conversão novamente. Nesse ponto, o aprendizado foi ficar mais atento com as excessões, mas o programa foi rápido de fazer. Veja o post no LinkedIn referente a ele [aqui](https://www.linkedin.com/posts/mateusmagalhaes_python-programaaexaeto-activity-7310782971374927872-E5eY?utm_source=share&utm_medium=member_desktop&rcm=ACoAACexfIABu0_IIQtlHmH2oveguEC-MuBYeqA).  

O arquivo "ConversorCFT_CTK.py" é o programa com interface gráfica e totalmente funcional. Além de fazer a conversão, ele também tem um tratamento de erro onde, caso o usuário escreva algo que não possa ser identificado como um número, o programa não faz a conversão e muda a cor do texto para vermelho.  

## Observações e melhorias
Podemos dizer que o programa em si está completo, ou seja, está funcionando sem erros e cumpre seu propósito. Entretanto, podemos melhorá-lo.

- A escala Kelvin não tem números negativos, mas o programa permite que isso ocorra.  
- Apesar de eu ter posto um arredondamento com duas casas decimais nas respostas, você consegue escrever um número com mais casas. Não vejo problema nisso visto que a resposta ainda terá duas casas decimais - mas pode ser uma melhoria.  
- Colocar um ícone informativo que explique minimamente o funcionamento do programa ou a conversão pode ser interessante.  
- Mudar os ícones da janela e do programa pode ser interessante, ao invés de deixar as imagens padrões do Custom Tkinter e do python.  
- Precisei usar duas funções na conversão. Será que tem como simplificar e colocar uma única função sem comprometer a legibilidade?  
- Eu não mudei muito o estilo da interface pois meu objetivo não era criar um app bonito, mas sim funcional.  
- O aplicativo não está no formato executável. Farei isso assim que puder.  

## Conclusão
Apesar das observações acima, o aprendizado foi muito bom. Entendi melhor o processo de criação de uma interface gráfica com uma estrutura de OOP e me sinto preparado para criar outros aplicativos.

## Referência

Pense em Python - Allen B. Downey  
Curso de Física Básica, Vol 2 - Moysés Nussenzveig  
[Site do CustomTkinter](https://customtkinter.tomschimansky.com/)  