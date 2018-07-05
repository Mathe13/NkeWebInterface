import core
if __name__=='__main__':
    reqs=core.getReqs()
    # print(type(reqs[0]['status']))
    # print(core.filtraReqsStatus(reqs,'espera'))
    core.downloadNke(reqs[0])
    core.unzip()
    core.run()
