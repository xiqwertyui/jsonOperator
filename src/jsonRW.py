import os
import json
import subprocess

# https://stackoverflow.com/questions/8689964/why-do-some-functions-have-underscores-before-and-after-the-function-name



class jsonRW:
    def __init__(self, jsonPath = None) -> None:
        self.initPrompt = ['init', 'clear']
        self.readPrompt = ['read', 'view']
        self.readAllPrompt = ['readAll', 'print', 'viewAll']
        self.readAllPrettyPrompt = ['readAllPretty', 'printPretty', 'viewAllPretty']
        self.writePrompt = ['write', 'add']
        self.helpPrompt = ['help']
        self.quitPrompt = ['q']
        self.javascriptPath = globals()['__file__'].replace(os.path.basename(globals()['__file__']), 'jsonPrintPretty.js')
        self.jsonPath = jsonPath
        if jsonPath == None:
            self.jsonPath = self.pathConfig()


    def colorfulPrint(self, msg, colorDigit):
        print('\033[{}m'.format(colorDigit)+msg+'\033[0m')

    def pathConfig(self):
        while True:
            path = input('JSON FILE PATH: ')
            if path in self.quitPrompt:
                break
            elif os.path.isfile(path):
                return path
            else:
                self.colorfulPrint('NOT A FILE PATH', 91)

    def readJson(self):
        with open(self.jsonPath, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except Exception as err:
                print(err)

    def writeJson(self, jsonContent):
        with open(self.jsonPath, 'w', encoding='utf-8') as f:
            try:
                json.dump(jsonContent, f)
            except Exception as err:
                print(err)

    def clearEntry(self):
        self.writeJson({})

    def addEntry(self, key, value):
        jsonContent = self.readJson()
        jsonContent[key] = value
        self.writeJson(jsonContent)

    def deleteEntry(self, key):
        jsonContent = self.readJson()
        del jsonContent[key]
        self.writeJson(jsonContent)

    def viewEntry(self, key):
        jsonContent = self.readJson()
        try:
            print(jsonContent[key])
        except Exception as err:
            print(err)
        
    def viewJson(self):
        jsonContent = self.readJson()
        try:
            print(jsonContent)
        except Exception as err:
            print(err)
       

    def viewJsonPretty(self):
        proc = subprocess.Popen(["node", "-v"], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        if out != b'':
            os.system('node {} {}'.format(self.javascriptPath, self.jsonPath))
        else:
            self.colorfulPrint('You computer is not support viewJsonPretty, please install nodejs first', 91)

    def usage(self):
        pass

    def prompt(self):
        while True:
            prompt = input('Prompt: ')
            if prompt in self.quitPrompt:
                exit()
            elif prompt in self.initPrompt:
                self.clearEntry()
                self.viewJson()
            elif prompt in self.readPrompt:
                key = input('KEY: ')
                self.viewEntry(key)
                self.viewJson()
            elif prompt in self.writePrompt:
                key = input('KEY: ')
                value = input('VALUE: ')
                self.addEntry(key, value)
                self.viewJson()
            elif prompt in self.readAllPrompt:
                self.viewJson()
            elif prompt in self.readAllPrettyPrompt:
                self.viewJsonPretty()
            elif prompt in self.helpPrompt:
                self.usage()
            else:
                self.colorfulPrint('unrecognised command, type "help" to view command', 91)

    def main(self):
        self.prompt()

if __name__ == '__main__':
    controler = jsonRW('../target.json')
    controler.main()