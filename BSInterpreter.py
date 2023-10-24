class BSInterpreter:
    def __init__(self, sourceFilePath = None, sourceCode = "", inputs = None, outputToString = False):
        self.__treeFilePath = sourceFilePath[:-2] + "json" if sourceFilePath != None else "./CodeTree.json"

        self.__inputs = inputs
        self.__outputs = []
        self.__outputToString = outputToString

        self.__currentWordIndex = 0
        self.__variables = []

        if sourceFilePath != None:
            with open(sourceFilePath, "r") as sourceFile:
                sourceCode = sourceFile.readline()

        if sourceCode[-1] == " ":
            sourceCode = sourceCode[:-1]

        self.__words = sourceCode.split(" ")
        self.__codeTree = self.__BuildCodeTree()

    def __BuildCodeBranch(self):
        self.__currentWordIndex += 1
        lastWord = self.__words[self.__currentWordIndex - 1]

        while self.__currentWordIndex < len(self.__words):
            if self.__words[self.__currentWordIndex] == ".":# End of a statement
                return {
                    "type": "constant",
                    "value": lastWord
                }
            elif self.__words[self.__currentWordIndex] == "..":# Start of a body of statements
                body = []
                next = self.__BuildCodeBranch()
                while next["type"] != "endOfBody":
                    body.append(next)
                    next = self.__BuildCodeBranch()
                return body
            elif self.__words[self.__currentWordIndex] == "...":# End of a body of statements
                return { "type": "endOfBody" }
            elif self.__words[self.__currentWordIndex] == "ingual":# Assignment of a variable
                return {
                    "type": "assignment",
                    "name": lastWord,
                    "value": self.__BuildCodeBranch()
                }
            elif self.__words[self.__currentWordIndex] == "engual":# Comparison between values (==)
                return {
                    "type": "comparison",
                    "op": "=",
                    "left": {
                        "type": "constant",
                        "value": lastWord,
                    },
                    "right": self.__BuildCodeBranch()
                }
            elif self.__words[self.__currentWordIndex] == "naoengual":# Comparison between values (!=)
                return {
                    "type": "comparison",
                    "op": "!",
                    "left": {
                        "type": "constant",
                        "value": lastWord,
                    },
                    "right": self.__BuildCodeBranch()
                }
            elif self.__words[self.__currentWordIndex] == "maioque":# Comparison between values (>)
                return {
                    "type": "comparison",
                    "op": ">",
                    "left": {
                        "type": "constant",
                        "value": lastWord,
                    },
                    "right": self.__BuildCodeBranch()
                }
            elif self.__words[self.__currentWordIndex] == "menoque":# Comparison between values (<)
                return {
                    "type": "comparison",
                    "op": "<",
                    "left": {
                        "type": "constant",
                        "value": lastWord,
                    },
                    "right": self.__BuildCodeBranch()
                }
            elif self.__words[self.__currentWordIndex] == "se":# Condition declaration (if)
                return {
                    "type": "if",
                    "condition": self.__BuildCodeBranch(),
                    "body": self.__BuildCodeBranch()
                }
            elif self.__words[self.__currentWordIndex] == "enquando":# Loop declatarion (while)
                return {
                    "type": "loop",
                    "condition": self.__BuildCodeBranch(),
                    "body": self.__BuildCodeBranch()
                }
            elif self.__words[self.__currentWordIndex] == "i":# Comparison between values (and))
                return {
                    "type": "and",
                    "left": {
                        "type": "constant",
                        "value": lastWord,
                    },
                    "right": self.__BuildCodeBranch()
                }
            elif self.__words[self.__currentWordIndex] == "o":# Comparison between values (or)
                return {
                    "type": "or",
                    "left": {
                        "type": "constant",
                        "value": lastWord,
                    },
                    "right": self.__BuildCodeBranch()
                }
            elif self.__words[self.__currentWordIndex] == "mas":# Operation between values (+)
                return {
                    "type": "operator",
                    "op": "+",
                    "left": {
                        "type": "constant",
                        "value": lastWord,
                    },
                    "right": self.__BuildCodeBranch()
                }
            elif self.__words[self.__currentWordIndex] == "menus":# Operation between values (-)
                return {
                    "type": "operator",
                    "op": "-",
                    "left": {
                        "type": "constant",
                        "value": lastWord,
                    },
                    "right": self.__BuildCodeBranch()
                }
            elif self.__words[self.__currentWordIndex] == "mutiprica":# Operation between values (*)
                return {
                    "type": "operator",
                    "op": "*",
                    "left": {
                        "type": "constant",
                        "value": lastWord,
                    },
                    "right": self.__BuildCodeBranch()
                }
            elif self.__words[self.__currentWordIndex] == "cortaem":# Operation between values (/)
                return {
                    "type": "operator",
                    "op": "/",
                    "left": {
                        "type": "constant",
                        "value": lastWord,
                    },
                    "right": self.__BuildCodeBranch()
                }
            elif self.__words[self.__currentWordIndex] == "sobrah":# Operation between values (%)
                return {
                    "type": "operator",
                    "op": "%",
                    "left": {
                        "type": "constant",
                        "value": lastWord,
                    },
                    "right": self.__BuildCodeBranch()
                }
            elif self.__words[self.__currentWordIndex] == "falah":# Declaration of a text constant (")
                lastWord = self.__words[self.__currentWordIndex]
                self.__currentWordIndex += 1

                string = []
                while self.__words[self.__currentWordIndex] != "falah":
                    string.append(self.__words[self.__currentWordIndex])
                    lastWord = self.__words[self.__currentWordIndex]
                    self.__currentWordIndex += 1
                
                lastWord = self.__words[self.__currentWordIndex + 1]
                self.__currentWordIndex += 1
                    
                return {
                    "type": "constant",
                    "value": " ".join(string)
                }
            elif self.__words[self.__currentWordIndex] == "gozpe":# Outputs value to the console
                return {
                    "type": "output",
                    "value": self.__BuildCodeBranch()
                }
            elif self.__words[self.__currentWordIndex] == "pega":# Gets an input from the console
                lastWord = self.__words[self.__currentWordIndex]
                self.__currentWordIndex += 1
                return { "type": "input" }

            lastWord = self.__words[self.__currentWordIndex]
            self.__currentWordIndex += 1

    def __BuildCodeTree(self):
        tree = []
        while self.__currentWordIndex < len(self.__words):
            branch = self.__BuildCodeBranch()
            if branch != None:
                tree.append(branch)
        return tree

    def SaveToJson(self, jsonPath = None):
        import json
        with open(self.__treeFilePath if jsonPath == None else jsonPath, "w") as jsonFile:
            jsonFile.write(json.dumps({ "program": self.__codeTree }))

    def __AssignVar(self, name, value):
        val = None
        try: val = float(value)
        except: val = value

        for v in self.__variables:
            if v["name"] == name:
                v["value"] = val
                return
        
        self.__variables.append({
            "name": name,
            "value": val
        })

    def __ConstToVar(self, name):
        for v in self.__variables:
            if v["name"] == name:
                return v["value"]
        return name

    def __RunBranch(self, branch):
        if type(branch) != dict:
            return branch

        if branch["type"] == "assignment":
            self.__AssignVar(branch["name"], self.__RunBranch(branch["value"]))
        elif branch["type"] == "comparison":
            left = self.__RunBranch(branch["left"])

            if branch["op"] == "=":
                return left == self.__RunBranch(branch["right"])
            elif branch["op"] == "!":
                return left != self.__RunBranch(branch["right"])
            elif branch["op"] == ">":
                return left > self.__RunBranch(branch["right"])
            elif branch["op"] == "<":
                return left < self.__RunBranch(branch["right"])
            
            raise Exception("Invalid comparison operator")
        elif branch["type"] == "operator":
            left = self.__RunBranch(branch["left"])
            right = self.__RunBranch(branch["right"])

            if branch["op"] == "+":
                return left + right
            elif branch["op"] == "-":
                return left - right
            elif branch["op"] == "*":
                return left * right
            elif branch["op"] == "/":
                return left / right
            elif branch["op"] == "%":
                return left % right
            
            raise Exception("Invalid math operator")
        elif branch["type"] == "constant":
            value = self.__RunBranch(branch["value"])
            val = None
            try: val = float(value)
            except: val = self.__ConstToVar(value)
            return val
        elif branch["type"] == "if":
            if self.__RunBranch(branch["condition"]):
                for b in branch["body"]:
                    self.__RunBranch(b)
        elif branch["type"] == "loop":
            while self.__RunBranch(branch["condition"]):
                for b in branch["body"]:
                    self.__RunBranch(b)
        elif branch["type"] == "and":
            return branch["left"] and self.__RunBranch(branch["right"])
        elif branch["type"] == "or":
            return branch["left"] or self.__RunBranch(branch["right"])
        elif branch["type"] == "output":
            output = self.__RunBranch(branch["value"])
            if self.__outputToString:
                self.__outputs.append(str(output))
            else: print(output)
        elif branch["type"] == "input":
            inp = self.__inputs.pop(0) if self.__inputs else input()
            
            val = None
            try: val = float(inp)
            except: val = inp
            return val

    def Run(self):
        try:
            for branch in self.__codeTree:
                self.__RunBranch(branch)
        except Exception as e:
            print(e)

    def GetOutputString(self):
        return "\n".join(self.__outputs)
