# Conversor de teperatura

## Descrição: 
O presente arquivo apresenta um projeto particular de conversor de temperatura feito em python utilizando estrutura OOP e o framework Custom Tkinter para GUI.

## Objetivo: 
Resolvi fazer esse projeto para rever e aprimorar minhas habilidades em programação, além de conhecer mais a fundo a biblioteca Custom Tkinter.

## O que é um conversor de termperatura CFK?
O nome "conversor de temperatura" é suficiente. CFK se refere as temperaturas Celsius (°C), Fahrenheit (°F) e Kelvin (K).
A medida Celsius é a mais usada; Kelvin é uma medida científica; e Fahrenheit é mais utilizada nos EUA. Elas são converdidas pelas seguintes fórmulas:

C/5 = (F-32)/9 = (K-273)/5

Onde:
C = temperatura em gruas celsius
F = temperatura em graus farenheit
K = temperatura em kelvin

## Detalhes:
O primeiro modelo desse programa foi feito apenas com uma interface simples de terminal e sem orientação a objeto. A única coisa que precisei fazer a mais foi pesquisar as fórmulas de conversão novamente. Nesse ponto, o aprendizado foi ficar mais atento com as excessões, mas o programa foi rápido de fazer. Veja o post no LinkedIn referente a ele [aqui](https://www.linkedin.com/posts/mateusmagalhaes_python-programaaexaeto-activity-7310782971374927872-E5eY?utm_source=share&utm_medium=member_desktop&rcm=ACoAACexfIABu0_IIQtlHmH2oveguEC-MuBYeqA).
Atualmente, estou tentando implementar uma interface utilizando OOP. Para isso, tive que mudar a estrutura e transformei a conversão em função. Estou tentando me basear no modelo do conversor do Google, onde não preciso apertar o botão "calcular". Nesse modelo, preciso apenas selecionar as unidades de medida da temperatura e, ao colocar o valor de entrada, o valor de saída aparece automaticamente. Esse tem sido meu desafio atual, pois a interface em si já está estruturada. Veja arquivo "ConversorCFK_CTK.py".

## Referência

Pense em Python - Allen B. Downey
Curso de Física básica, Vol 2 - Moysés Nussenzveig
[Site do CustomTkinter](https://customtkinter.tomschimansky.com/)