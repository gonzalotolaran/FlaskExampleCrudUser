from datetime import datetime

horallegada = datetime.now()
horaentrada = horallegada.replace(hour=9, minute=0, second=0)
diferencia = horallegada - horaentrada

days, seconds = diferencia.days, diferencia.seconds
hours = days * 24 + seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60
"""
if horallegada > horaentrada:
	print("El empleado llego: " + str(hours) +" hora(s) " + "y " + str(minutes) + " minuto(s) tarde")
	print(hours*60 + minutes)
"""
if horallegada > horaentrada:
		#print("El empleado llego: " + str(hours) +" hora(s) " + "y " + str(minutes) + " minuto(s) tarde")
	print (hours*60 + minutes)
else:
	print (0)