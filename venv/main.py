import os
import datetime

mensagem = "Quarta-feira é feriado. A"
file = open("contatos.txt", "r")

# for line in file:
#     line = line.replace("-","")
#     line = line.replace("+","")
#     line = line.replace(" ","")
os.system("yowsup-cli demos -s {} \"{}\" -c config.txt".format(+553288317580, mensagem))

file.close()
