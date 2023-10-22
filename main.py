from BSInterpreter import BSInterpreter

while True:
    path = input("Caminho do arquivo .bs: ")
    interpreter = BSInterpreter(path)
    # interpreter.SaveToJson()
    print(f"{path}:")
    interpreter.Run()