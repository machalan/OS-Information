import wmi
import socket
import platform
import os
import sys
import requests
from requests import get
import json

# Préparation des variables
 
c = wmi.WMI()
uname = platform.uname()   
my_system = c.Win32_ComputerSystem()[0]
info_bios = c.Win32_BIOS()[0]
carte_mere = c.Win32_BaseBoard ()[0]
processeur = c.Win32_Processor()[0]
memoire_vive_1 = c.Win32_PhysicalMemory ()[0]
memoire_vive_2 = c.Win32_PhysicalMemory ()[1]
#memoire_vive_3 = c.Win32_PhysicalMemory ()[2]
#memoire_vive_4 = c.Win32_PhysicalMemory ()[3]
disques_1 = c.Win32_DiskDrive ()[0]
disques_2 = c.Win32_DiskDrive ()[1]
adaptateur_resaux_1 = c.Win32_NetworkAdapter ()[0]
adaptateur_resaux_2 = c.Win32_NetworkAdapter ()[1]
adaptateur_resaux_3 = c.Win32_NetworkAdapter ()[2]
adaptateur_resaux_4 = c.Win32_NetworkAdapter ()[3]





print("")
print("="*20, "Information sur la machine", "="*20)
print("")

# Qui a fabriqué le poste

print("")
print("="*20, "Qui a fabriqué le poste ?", "="*20)
print("")
 
print(f"Manufacturer: {my_system.Manufacturer}")
print(f"Marque: {info_bios.Version}")
print(f"Modele: {my_system.Model}")
print("")


# Qui je suis ? (Le poste)

print("")
print("="*20, "Qui je suis ? (Le poste)", "="*20)
print("")

print(f"Hostname: {my_system.Name}")
print(f"Numéro de série: {info_bios.SerialNumber}")
print("")


# Quelle est mon OS ?

print("")
print("="*20, "Quelle est mon OS ?", "="*20)
print("")

print(f"System: {uname.system}")           #  Returns the system/OS name
print(f"Windows: {uname.release}")          # Returns the system’s release
print(f"Version de Windows: {uname.version}")        #  Returns the system’s release version, e.
print(f"Architecture Machine: {uname.machine}")               #  Returns the machine type, e.g. 'i386'.
print(f"SystemFamily: {my_system.SystemFamily}")
print(f"SystemType: {my_system.SystemType}")
print ("Pocessor: " +platform.processor())
print("")

# Quelles sont mes processeurs ?

print("")
print("="*20, "Quelles sont mes processeurs ?", "="*20)
print("")

print(f"Nom du processeur: {processeur.Name}")
print(f"NumberOfProcessors: {my_system.NumberOfProcessors}")
print(f"Nbr processeur logique: {processeur.NumberOfLogicalProcessors}")
print("")

# Quelles est la taille de ma RAM ?

print("")
print("="*20, "Quelles est la taille de ma RAM ?", "="*20)
print("")

print(f"Taille total de la RAM: {my_system.TotalPhysicalMemory}")
print("")
print(f"RAM-1 Taille: {memoire_vive_1.Capacity}")
print(f"RAM-1 Vitesse: {memoire_vive_1.ConfiguredClockSpeed}")
print(f"RAM-1 Fabricant ou code Fabricant: {memoire_vive_1.Manufacturer}")
print(f"RAM-1 Numéro de serie : {memoire_vive_1.SerialNumber}")
print(f"RAM-1 Tag : {memoire_vive_1.Tag}")
print("")
print(f"RAM-2 Taille: {memoire_vive_2.Capacity}")
print(f"RAM-2 Vitesse: {memoire_vive_2.ConfiguredClockSpeed}")
print(f"RAM-2 Fabricant ou code Fabricant: {memoire_vive_2.Manufacturer}")
print(f"RAM-2 Numéro de serie : {memoire_vive_2.SerialNumber}")
print(f"RAM-2 Tag : {memoire_vive_2.Tag}")
print("")



# Quelles est la taille de mon ou mes disques ?

print("")
print("="*20, "Quelles est la taille de mon ou mes disques ?", "="*20)
print("")

print("")
print(f"disk 1 - Model du disque : {disques_1.Model}")
print(f"disk 1 - Type interface : {disques_1.InterfaceType}")
print(f"disk 1 - Numéro de série : {disques_1.SerialNumber}")
print(f"disk 1 - Taille du disque : {disques_1.Size}")
print(f"disk 1 - OK ou défaillant : {disques_1.Status}")
print("")
print(f"disk 2 - Model du disque : {disques_2.Model}")
print(f"disk 2 - Type interface : {disques_2.InterfaceType}")
print(f"disk 2 - Numéro de série : {disques_2.SerialNumber}")
print(f"disk 2 - Taille du disque : {disques_2.Size}")
print(f"disk 2 - OK ou défaillant : {disques_2.Status}")
print("")




# Quelles est mon nom domaine

print("")
print("="*20, "Quelle est mon nom domaine ?", "="*20)
print("")

print(f"Nom de domaine: {my_system.Domain}")
print("")
# Qui je suis ? (User)

print("")
print("="*20, "Qui je suis ?", "="*20)
print("")

print(f"Nom de l'utilisateur actuel: {my_system.UserName}")
print("")

# Quelle est ma carte mere ?

print("")
print("="*20, "Quelle est ma carte mere ?", "="*20)
print("")

print(f"Type de carte Mere: {carte_mere.Caption}")
print(f"Fabricant de la carte mere: {carte_mere.Manufacturer}")
print(f"Carte mere remplacable: {carte_mere.Replaceable}")
print(f"Numéro de serie de la carte mere: {carte_mere.SerialNumber}")
print("")

# Mes cartes réseaux ?

print("")
print("="*20, "Quelle sont mes cartes réseaux ?", "="*20)
print("")

print(f"Carte réseaux-1 : {adaptateur_resaux_1.AdapterType}")
print(f"Carte réseaux-1 - Description : {adaptateur_resaux_1.Description}")
print(f"Carte réseaux-1 - MACAddress : {adaptateur_resaux_1.MACAddress}")
print("")
print(f"Carte réseaux-2 : {adaptateur_resaux_2.AdapterType}")
print(f"Carte réseaux-2 - Description : {adaptateur_resaux_2.Description}")
print(f"Carte réseaux-2 - MACAddress : {adaptateur_resaux_2.MACAddress}")
print("")
print(f"Carte réseaux-3 : {adaptateur_resaux_3.AdapterType}")
print(f"Carte réseaux-3 - Description : {adaptateur_resaux_3.Description}")
print(f"Carte réseaux-3 - MACAddress : {adaptateur_resaux_3.MACAddress}")
print("")
print(f"Carte réseaux-4 : {adaptateur_resaux_4.AdapterType}")
print(f"Carte réseaux-4 - Description : {adaptateur_resaux_4.Description}")
print(f"Carte réseaux-4 - MACAddress : {adaptateur_resaux_4.MACAddress}")
print("")


# Mon IP local avec laquelle je vais sur internet

print("")
print("="*20, "Quelle est mon ip local ?", "="*20)
print("")


ip_local = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_local.connect(("8.8.8.8", 80))
mon_ip_local = ip_local.getsockname()[0]
ip_local.close()

print("Mon IP Local est : " +mon_ip_local)
print("")

# Mon IP public

print("")
print("="*20, "Quelle est mon ip Public ?", "="*20)
print("")

ip2 = requests.get('https://checkip.amazonaws.com').text.strip()
print("Mon IP Public est : " +ip2)
print("")




# Pour afficher la totalité des infos lister dans le tableau
#c = wmi.WMI ()
#for s in c.Win32_ComputerSystem ():
#  print (s)

# Pour afficher la totalité des infos lister dans le tableau
#c = socket.socket ()
#for s in c.Win32_ComputerSystem ():
#  print (s)


# Création du dictionnaire

info_du_poste = {}

info_du_poste['Mon IP local'] = mon_ip_local
info_du_poste["Mon IP public"] = ip2
info_du_poste["Fabricant:"] = my_system.Manufacturer
info_du_poste["Marque:" ] = info_bios.Version
info_du_poste["Modele:"] = my_system.Model
info_du_poste["Hostname:"] = my_system.Name
info_du_poste["Numero de serie:"] = info_bios.SerialNumber
info_du_poste["System:"] = uname.system           
info_du_poste["Windows:"] = uname.release        
info_du_poste["Version de Windows:"] = uname.version       
info_du_poste["Architecture Machine:"] = uname.machine
info_du_poste["SystemFamily:"] = my_system.SystemFamily
info_du_poste["SystemType:"] = my_system.SystemType
info_du_poste["Pocessor: "] = platform.processor()
info_du_poste["Nom du processeur:"] = processeur.Name
info_du_poste["NumberOfProcessors:"] = my_system.NumberOfProcessors
info_du_poste["Nbr processeur logique:"] = processeur.NumberOfLogicalProcessors
info_du_poste["Taille total de la RAM:"] = my_system.TotalPhysicalMemory
info_du_poste["RAM-1 Taille:"] = memoire_vive_1.Capacity
info_du_poste["RAM-1 Vitesse:"] = memoire_vive_1.ConfiguredClockSpeed
info_du_poste["RAM-1 Fabricant ou code Fabricant:"] = memoire_vive_1.Manufacturer
info_du_poste["RAM-1 Numero de serie :"] = memoire_vive_1.SerialNumber
info_du_poste["RAM-1 Tag :"] = memoire_vive_1.Tag
info_du_poste["RAM-2 Taille:"] = memoire_vive_2.Capacity
info_du_poste["RAM-2 Vitesse:"] = memoire_vive_2.ConfiguredClockSpeed
info_du_poste["RAM-2 Fabricant ou code Fabricant:"] = memoire_vive_2.Manufacturer
info_du_poste["RAM-2 Numero de serie :"] = memoire_vive_2.SerialNumber
info_du_poste["RAM-2 Tag :"] = memoire_vive_2.Tag
info_du_poste["disk 1 - Model du disque :"] = disques_1.Model
info_du_poste["disk 1 - Type interface :"] = disques_1.InterfaceType
info_du_poste["disk 1 - Numero de serie :"] = disques_1.SerialNumber
info_du_poste["disk 1 - Taille du disque :"] = disques_1.Size
info_du_poste["disk 1 - OK ou defaillant :"] = disques_1.Status
info_du_poste["disk 2 - Model du disque :"] = disques_2.Model
info_du_poste["disk 2 - Type interface :"] = disques_2.InterfaceType
info_du_poste["disk 2 - Numero de serie :"] = disques_2.SerialNumber
info_du_poste["disk 2 - Taille du disque :"] = disques_2.Size
info_du_poste["disk 2 - OK ou defaillant :"] = disques_2.Status
info_du_poste["Nom de domaine:"] = my_system.Domain
info_du_poste["Nom de l'utilisateur actuel:"] = my_system.UserName
info_du_poste["Type de carte Mere:"] = carte_mere.Caption
info_du_poste["Fabricant de la carte mere:"] = carte_mere.Manufacturer
info_du_poste["Carte mere remplacable:"] = carte_mere.Replaceable
info_du_poste["Numero de serie de la carte mere:"] = carte_mere.SerialNumber
info_du_poste["Carte reseaux-1 :"] = adaptateur_resaux_1.AdapterType
info_du_poste["Carte reseaux-1 - Description :"] = adaptateur_resaux_1.Description
info_du_poste["Carte reseaux-1 - MACAddress :"] = adaptateur_resaux_1.MACAddress
info_du_poste["Carte reseaux-2 :"] = adaptateur_resaux_2.AdapterType
info_du_poste["Carte reseaux-2 - Description : "] = adaptateur_resaux_2.Description
info_du_poste["Carte reseaux-2 - MACAddress :"] = adaptateur_resaux_2.MACAddress
info_du_poste["Carte reseaux-3 :"] = adaptateur_resaux_3.AdapterType
info_du_poste["Carte reseaux-3 - Description :"] = adaptateur_resaux_3.Description
info_du_poste["Carte reseaux-3 - MACAddress :"] = adaptateur_resaux_3.MACAddress
info_du_poste["Carte reseaux-4 :"] = adaptateur_resaux_4.AdapterType
info_du_poste["Carte reseaux-4 - Description :"] = adaptateur_resaux_4.Description
info_du_poste["Carte reseaux-4 - MACAddress :"] = adaptateur_resaux_4.MACAddress

# Création du fichier json

with open('data.json', 'w') as fp:
	  fp.write(json.dumps(info_du_poste, indent=4))



for i in info_du_poste.items():
    print(i)
