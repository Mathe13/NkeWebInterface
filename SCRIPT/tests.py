import core
import os
def main():
    reqs = core.getReqs()
    # core.downloadNke(reqs[0])
    # core.unzip()
    # core.compile()
    core.run(5)
    core.submit(reqs[0], core.prepareOutput(reqs[0]['arquivo']))
    return
    while 1:
        reqs = core.getReqs()
        print(type(reqs[0]['status']))
        filaEspera = core.filtraReqsStatus(reqs, 'espera')
        for req in filaEspera:
            core.downloadNke(req)
            core.unzip()
            core.compile()
            core.run(60)
            core.prepareOutput(req['arquivo'])

    # core.getOutput()
    # os.system("cd nke/NKE0.7e && ./terminal64 --plot")

if __name__=='__main__':
    main()
