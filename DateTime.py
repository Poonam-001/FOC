
def getDate():
    import datetime# imported current date time 
    now=datetime.datetime.now#variable initialized
    print("Date: ",now().date())#print information
    return str(now().date())#return the paticular value

def getTime():
    import datetime# imported current date time
    now=datetime.datetime.now#variable initialized
    print("Time: ",now().time())#print information
    return str(now().time())#return the paticular value
