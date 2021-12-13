#DINO
#site: chrome://dino/
Runner.instance_.gameOver = () => {} 

#INTERFACE GRÁFICA
#Biblioteca de interfaces gráficas
from PySimpleGUI import PySimpleGUI as sg
#Instalar via terminal > pip install PySimpleGUI

#layout
sg.theme('Reddit') #um  dos temas disponíveis
layout = [
    [sg.Text('Usuário'), sg.Input(key='Usuário', size=(20,1))],
    [sg.Text('Senha'), sg.Input(key='senha',  password_char='*',size=(20,1))],
    [sg.Checkbox('Salvar o loguin?')],
    [sg.Button('Entrar')],
]    
#janela
janela= sg.Window('Tela de Loguin', layout)
#ler os eventos
while True: #verificando a senha #loop infinito
    eventos, valores = janela.read() #unpacking
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar': #verificando se a user/senha estão corretos
        if valores['Usuário'] == 'Helen' and valores['senha']== '12345':
            print('Bem-vindo!')
            
#IPHONE PRICE
#Plotando  gráfico dos dados
import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv('iphone_price.csv', sep=';')
plt.scatter(data['version'], data['price'])
plt.show()            

#Predizendo valor 
import pandas
from sklearn.linear_model import LinearRegression

data = pandas.read_csv('iphone_price.csv', sep=';')


model = LinearRegression()
model.fit(data[['version']], data[['price']])
print(model.predict([[17]]))


#APITWITTER
#criar conta de desenvolvedor: https://medium.com/programadores-ajudando-programadores/api-do-twitter-criando-o-app-e-obtendo-os-tokens-28ef3e2a281c
### K: Documentação: https://docs.tweepy.org/en/stable/

import tweepy #implementa api do tt
import pandas as pd #lendo dados

pd.set_option('display.width', 1000) #s/ quebrar linhas
pd.set_option('display.max_columns', None)


api_key        = 'jYLj0LECk3XNy5vHFbiI126G1'
api_secret     = 'wSFuaMdVt97jh61njukPEs4oEBCeCnbnJSwdo4Jg4JQ9s42t5D'
access_token        =  '4872810941-kXnVOV1mvouDOQSn7Rcw7406kKbhzK7bHqFnkE1' 
access_token_secret = 'eggylPd3ukygGbPdCrwgBUcVVo1CM3W7lIqMaKTLEgl3q' 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #identificando quem esta requisitando
auth.set_access_token(access_token, access_token_secret) #passando as chaves
api = tweepy.API(auth) #api autenticado
### K: https://docs.tweepy.org/en/stable/api.html#api-reference


user_id = 'BarackObama'
tweets = api.user_timeline(screen_name=user_id, 
                           count=10, #qtd de tweets ### K: Max 200.
                           include_rts=False,
                           tweet_mode='extended' #mais de 140 caracteres
                           )

print ('Tweets do {}\n'.format(user_id))
for tweet in tweets[:5]: #1° tweets
     print('ID: {}'.format(tweet.id))
     print(tweet.created_at)
     print(tweet.full_text, '\n')
     
        

#Análise de dados abertos
https://colab.research.google.com/drive/1ZdE78TTWu_RoPiZyt8hZEBPJbTXsmctA?usp=sharing

#Jogo
import pygame
from random import randint
pygame.init()

x=315 #415LD 280LE
y=100

pos_x = 280
pos_y = 800

pos_x_a=315
pos_y_a=800

velocidade=2
velocidade_outros= 8

fundo  = pygame.image.load('estrada00.png')
carro  = pygame.image.load('carro.png')
carro1 = pygame.image.load('carro1.png')
carro2 = pygame.image.load('carro2.png')



janela=pygame.display.set_mode((800,600))

pygame.display.set_caption("Jogo no Python")

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
            
    if comandos[pygame.K_RIGHT] and x<=400: 
        x+=velocidade           
    if comandos[pygame.K_LEFT] and x>=280:
        x-=velocidade


    
    if (pos_y<=-80):
        pos_y = randint(800,1000)

    if (pos_y_a <=-80):    
        pos_y_a= randint(1200,2000)


  

    pos_y -= velocidade_outros 
    pos_y_a -= velocidade_outros - 3

    janela.blit(fundo, (0,0))
    janela.blit(carro,(x,y))
    janela.blit(carro1,(pos_x,pos_y))
    janela.blit(carro2,(pos_x_a, pos_y_a))

    

    pygame.display.update()          

pygame.quit()  