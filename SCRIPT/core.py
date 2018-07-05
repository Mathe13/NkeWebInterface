import os
import requests
import json
import subprocess
# Api/salvar
apiURL = "http://localhost/NkeWebInterface/API/"


def getReqs():
    reqs = requests.get(apiURL+'index.php/Api/requisicao')
    return json.loads(reqs.text)


def filtraReqsStatus(listaReq,status):
    retorno = []
    # print(listaReq)
    for req in listaReq:
        # print ((req))
        if(req['status'] == status):
            retorno.append(req)
    return retorno

def downloadNke(req):
    fileName=req['arquivo']
    file=requests.get(apiURL+'files/'+fileName)
    print(apiURL+'files/'+fileName)
    tmp=open('tmp.zip','wb')
    tmp.write(file.content)

def unzip():
    print("mv tmp.zip nke/")
    print(os.system("mv tmp.zip nke/"))
    print("cd nke && unzip tmp.zip")
    print(os.system('cd nke && unzip tmp.zip'))

def run():
    comando = "cd nke/NKE0.7e/Placa && make clean && make && sudo make ispu && cd .. && sudo ./terminal64"
    print(comando)
    print(os.system(comando))
