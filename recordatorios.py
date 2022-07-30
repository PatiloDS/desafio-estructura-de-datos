#Patricio Carrasco
import sys

recordatorios = [['2021-01-01', '11:00', "levantarse y ejercitar"],
['2021-05-01', "15:00", "no trabajar"],
['2021-07-15', "13:00", "no hacer nada, es feriado"],
['2021-09-18', "16:00", "ramadas"],
['2021-12-25', "00:00", "navidad"]]

recordatorios.insert(1,['2021-01-02',"06:00","empezar año nuevo"])
recordatorios.remove(['2021-07-15', "13:00", "no hacer nada, es feriado"])
recordatorios.insert(2,['2021-07-16',"13:00", "no hacer nada, es feriado"])
recordatorios.pop(3)
recordatorios.insert(4,['2021-12-24', '22:00', 'cena navidad'])
recordatorios.append(['2021-12-31', '22:00', 'cena año nuevo'])

print("los recordatorios son: \n{}".format(recordatorios))
