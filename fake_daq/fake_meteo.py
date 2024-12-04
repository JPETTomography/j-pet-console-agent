import time
import math 
from setup import *


ts = time.time()
P_ATM = 5*math.sin(2*math.pi*ts/14400)+1000
P_1 = 0.0001*math.sin(2*math.pi*ts/3600)+0.0004
P_2 = 0.05*math.cos(2*math.pi*ts/7200)+0.45
T_1 = 2*math.sin(2*math.pi*ts/7200)+25
T_2 = 1.5*math.cos(2*math.pi*ts/3600)+22
H_1 = 10*math.sin(2*math.pi*ts/3600)+50
H_2 = 8*math.cos(2*math.pi*ts/5400)+50

with open(METEO_LOG_DIR+METEO_LOG, "a") as log_file:
  log_file.write("Timestamp "+str(round(ts,1)))
  log_file.write(" Atmospheric pressure "+str(round(P_ATM, 2))+" [hPa] ")
  log_file.write(" Turbo pump pressure "+str(round(P_1, 5))+" [hPa] ")
  log_file.write(" Rotary pump pressure "+str(round(P_2, 3))+" [hPa] ")
  log_file.write(" Temperature 1 "+str(round(T_1, 1))+" [C] ")
  log_file.write(" Temperature 2 "+str(round(T_2, 1))+" [C] ")
  log_file.write(" Humidity 1 "+str(round(H_1, 1))+" [%] ")
  log_file.write(" Humidity 2 "+str(round(H_2, 1))+" [%] \n")
