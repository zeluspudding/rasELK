#!/usr/bin/env python

import os

# Return CPU temperature as a character string
def getCPUtemperature_value():
 res = os.popen('vcgencmd measure_temp').readline()
 return(res.replace("temp=","").replace("'C\n",""))

def getCPUtemperature():
 return float(getCPUtemperature_value())


#temp2= 9.0/5.0*temp1+32
#print temp1,"C", "\n",  temp2,"F"
