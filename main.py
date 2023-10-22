from BSInterpreter import BSInterpreter

print("***************************")
print("* BS Programming Language *")
print("*       by Rafael Silva   *")
print("***************************")
while True:
    path = input("Caminho do arquivo .BS: ")
    interpreter = BSInterpreter(path)
    interpreter.SaveToJson()
    print(f"{path}:")
    interpreter.Run()
