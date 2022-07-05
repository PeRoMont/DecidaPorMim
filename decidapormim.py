#Bibliotecas
from time import sleep #Biblioteca do temporizador
from random import choice

print('=' * 30)
print('Bem-vindo(a) ao DECIDA POR MIM')
print('=' * 30)
sleep(1.2) #Temporizador

nomeuser = str(input('Insira o seu nome: ')).strip().capitalize() #Pedir o nome do usuário
nomescript = str(input(f'Olá {nomeuser}, dê um nome para o seu robô: ')).strip().capitalize() #Dar o nome para o 'robô'
pergunta = str(input('Agora insira a sua pergunta: ')).strip().capitalize() #Inserir a pergunta

print(f'O {nomescript} está pensando...')
sleep(2) #Temporizador

respostas = ['Sim!', 'Não!', 'Acho que sim!', 'Acredito que sim.', 'Acredito que não.', 'Provavelmente não.', 'Pode ser?!', 'Não sei.', 'Você é quem sabe.', 'Não sei te responder.', 'O que você achar melhor!'] #Lista com as respostas pré-definidas

print('=' * 40)
print(f'Para a pergunta: {pergunta}\nO {nomescript} te respondeu: {choice(respostas)}') #Escolha de uma das respostas da linha 17
print('=' * 40)