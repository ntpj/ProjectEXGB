from datetime import date, datetime
import os
import traceback
import uuid

global __day__
__day__ = date.today()

def logging(txt, file):
    __file__ = file
    
    if not os.path.exists(f"./log/"):
        os.makedirs(f"./log/")
    if os.path.exists(__file__):
        pass
    else:
        f = open(__file__, "a")
        f.write(""+'\r')
    txt = txt.encode('utf-8', 'ignore').decode('utf-8')
    f = open(__file__, "a")
    f.write(f"\n Log: {datetime.now()}: {txt}") # + '\r')
    f.close()
    
def logtb(txt):
    type = "normal"
    file= f"./log/{__day__}_traceback.log"
    logging(txt, file)

def log(txt):
    type = "normal"
    file = f"./log/{__day__}.log"
    logging(txt, file)