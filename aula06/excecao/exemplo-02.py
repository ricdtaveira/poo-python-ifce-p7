

try:
  f = open("demofil.txt","r")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Não pode gravar!")
  finally:
    f.close()
except:
  print("Arquivo inexistente!")
