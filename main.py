import max30100
from matplotlib import pyplot as plt
import time
from datetime import datetime


mx30 = max30100.MAX30100()

mx30.set_mode(max30100.MODE_SPO2)

for i in range(1000):
    mx30.read_sensor()  

signal_ir = []
#time_ir = []
lst_ir = []

signal_red = []
#time_red = []
lst_red = []

start = time.time()
for i in range(5000):
    mx30.read_sensor()                                            
    signal_ir.append(mx30.ir)
    #time_ir.append(str(datetime.now().time()))
    lst_ir.append( (str(datetime.now().time())).replace('.',':')+','+str(mx30.ir) )
    
    signal_red.append(mx30.red)
    #time_red.append(datetime.now().time())
    lst_red.append( (str(datetime.now().time())).replace('.',':')+','+str(mx30.red) )

    
print(time.time() - start)
#print(lst_ir)
#print(signal_ir)
#print(lst_red)
#print(signal_red)
plt.plot(range(len(signal_ir)), signal_ir)
plt.plot(range(len(signal_red)), signal_red)
plt.show()


with open ('Lex_' + str(datetime.today().strftime("%X_%d.%m.%Y")) + '_red.txt', 'w') as f:
    for i in lst_red:
        f.write("%s\n" % i)
        
with open ('Lex_' + str(datetime.today().strftime("%X_%d.%m.%Y")) + '_ir.txt', 'w') as f:
    for i in lst_ir:
        f.write("%s\n" % i)
    
#new_signal = butter_filter_bandpass(signal, 0.1, 50, , 5)
