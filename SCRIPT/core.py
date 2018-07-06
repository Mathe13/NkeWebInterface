import os
import requests
import json
import subprocess
import sys
import signal
import time
# import pyautogui
# from threading import Timer,
# Api/salvar
apiURL = "http://localhost/NkeWebInterface/API/"


# class Alarm(Exception):
#     pass


# def alarm_handler(signum, frame):
#     raise Alarm


# signal.signal(signal.SIGALRM, alarm_handler)



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

def compile():
    comando = "cd nke/NKE0.7e/Placa && make clean && make &&  make ispu"
    a = os.popen(comando).read()
    print(a)
    f=open('compile_log.txt','w')
    f.write(a)

def run(tempo):
    proc = subprocess.Popen(
        ["nke/NKE0.7e/terminal64", "--plot"], shell=False)
    time.sleep(tempo)
    proc.send_signal(signal.SIGINT)
    # proc.communicate(input='Ctrl+c')
    # time.sleep(2)
    # pyautogui.keyDown('ctrl')
    # pyautogui.keyDown('c')
    # pyautogui.keyUp('ctrl')
    # pyautogui.keyUp('ctrl')


    
    
def prepareOutput(fileName):
    # os.system('mv plot.txt run_log.txt')
    # os.system('zip '+fileName+' plot.txt compile_log.txt')
    a=open('compile_log.txt','r').read()+open('plot.txt','r').read()
    return a
    return

def clean():
    os.system('rm compile_log.txt')
    os.system('rm plot.txt')
    os.system('rm -R nke/NKE0.7e')

def submit(req,saida):
    uploadUrl = "http://localhost/NkeWebInterface/API/index.php/Api/resultado"
    # fileUrl = "http://localhost/NkeWebInterface/API/index.php/Api/file_resultado"
    payload={"id_req":req['id'],"saida":saida}
    payload=json.dumps(payload)
    a=requests.put(
        "http://localhost/NkeWebInterface/API/index.php/Api/requisicao"
        ,json.dumps({"id":req['id'],"status":"concluido"}))
    # file_ = {'file': ('file', open(req['arquivo'], 'rb'))}
    r = requests.post(uploadUrl, data=payload)
    print(a.text)
