#Importamos los paquetes necesarios
import os
import sys
#Obtenemos el link del primer parámetro
ytdlUrl = sys.argv[1]
#Si la plataforma es windows, ejecutamos el comando correspondiente en windows para descargar la canción
#  y después cerramos la terminal una vez termina con \k
if(sys.platform == "windows"):
   os.system('cmd \k "'+sys.path[0]+"\yt-dlp.exe -x --audio-format mp3 "+ytdlUrl+'"')
#Si la plataforma es linux, ejecutamos el comando bash correspondiente y
#  salimos del programa una vez termina
elif(sys.platform== "linux"):
    os.system('yt-dlp --extract-audio --audio-format mp3 '+ytdlUrl)
    exit()