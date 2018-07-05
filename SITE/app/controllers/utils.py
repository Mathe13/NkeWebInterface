import json
import requests
urlApi = 'http://localhost/NkeWebInterface/API/index.php/'


def getReqs(campo, valor):
    # print('teste getReqs',id)
    r=''
    if(campo=='id'):
        r=requests.get(urlApi+'requisicao?id='+str(valor))
    if(campo=='email'):
        r = requests.get(urlApi+'requisicao?email='+str(valor))
    return r.text

def cadReq(data):
    data=json.dumps(data)
    requests.post(urlApi+'requisicao',data)
