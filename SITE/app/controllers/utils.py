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
    reqs=json.loads(r.text)
    # return json.dumps(reqs)
    a=includeResultados(reqs)
    return json.dumps(a)

def cadReq(data):
    data=json.dumps(data)
    requests.post(urlApi+'requisicao',data)

def includeResultados(reqs):
    fullReqs=[]
    print(reqs)
    if(reqs):
        for req in reqs:
            if(req['status'] == 'concluido'):
                link = urlApi+'/Api/resultado?id_req='+req['id']
                print('link quebrado'+link)
                resultado = requests.get(link)
                req['resultado']=json.loads(resultado.text)
            fullReqs.append(req)    
    return fullReqs
