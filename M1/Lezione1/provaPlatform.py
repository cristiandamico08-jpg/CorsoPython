import platform

print(platform.platform())  # restituisce le informazioni sul sistema operativo

print(platform.platform(0, 1))  # restituisce solo il tipo di sistema oprativo e la major version

print(platform.machine())    # restitutisce il nome generico della CPU
print(platform.processor())  # restituisce il tipo di CPU

print(platform.system()) # restituisce solo il tipo di sistema operativo

print(platform.version()) # restitutisce solo la versione del sistema operativo

print(platform.python_implementation())  # restitutisce il tipo di "python" scaricato (in questo caso sviluppato in linguaggio C)

for i in platform.python_version_tuple():  # restituisce la versione di python scaricata
    print(i)