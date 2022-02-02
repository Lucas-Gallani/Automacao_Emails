// Bibliotecas utilizadas
import yagmail
from time import sleep

# Contador do laço
cont = 0

# Lista de E-mails destinatários, substitua e adicione quantos forem nescessários
emails = ['email_1_@gmail.com', 'email_2_@gmail.com', 'email_3_@gmail.com']

# Laço de repetição para o envio
while cont < len(emails):

    # Variável que irá pegar os e-mail da lista pelos seus indices atravez de cada repetição
    destino = emails[cont]
    
    corpo = ('''Aqui você pode adicionar o corpo do E-mail.

Podendo adicionar quebras de texto, desde que aja aspas triplas no começo e fim do texto: ''' '''
                                                                                
Lembrando que toda e qualquer identação também será levada em consideração''', 'Meu_Arquivo.md') # Após a virgula do texto do corpo,
                                                                                                 # pode se adiconar um anexo aos e-mails
                                                                                                 # O arquivo utlizado é apenas para métodos
                                                                                                 # de exemplo, está disponivel no github tbm

    # Área para efetuar o seu login
    remetente = yagmail.SMTP('O  seu e-mail vai aqui', 'A sua senha vai aqui')
    
    # Área de Envio dos e-mail
    # to = A variável dos e-mails de destinatário
    # subject = O assunto do E-mail adicione abaixo
    # contents = A variável do corpo do e-mail
    remetente.send(to=destino, subject='''Adicione o assunto do e-mail aqui''', contents=corpo)
    
    # Apenas um print para indicar sucesso no envio dos  e-mails
    print(f'E-mail para {emails[cont]}, enviado com sucesso')

    # Soma do contador para prosseguir pela lista
    cont += 1

    # utilização da biblioteca time para esperar 30 segundos antes do envio do proximo E-mail
    sleep(30)


# Fim do programa
print('Programa finalizado com sucesso, E-mails enviados com êxito')


