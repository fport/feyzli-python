from datetime import datetime 

t = '27 Mayıs 2014 saat 12:34:22'

z = datetime.strptime(t,'%d %B %Y saat %H:%M:%S')
print(z)
#EROR