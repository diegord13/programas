from datetime import datetime

fechayhora = datetime.now()

print(fechayhora)

año = fechayhora.year
mes = fechayhora.month
dia = fechayhora.day

hora = fechayhora.hour
minutos = fechayhora.minute
segundo = fechayhora.second
microsegundo = fechayhora.microsecond

print("La hora es {}:{}:{}".format(hora,minutos,segundo))