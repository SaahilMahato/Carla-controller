import eel
eel.init("Core")

@eel.expose
def exportfile(filename,loglist):
    file = open(filename,"w+")
    for i in range(len(loglist)):
        logtext = loglist[i] + "\n"
        file.write(logtext)
    file.close()

eel.start('main.html',size=(1366,768), mode='chrome')
