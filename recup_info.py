import wmi
import platform
import socket
import os
import sys



 
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
print("="*20, "Information a retravailler", "="*20)
print("")

print  ("Name: " +socket.gethostname())
print ("FQDN: " +socket.getfqdn())
print ("System Platform: "+sys.platform)
print ("Machine: " +platform.machine())
print ("Node " +platform.node())
print ("Platform: "+platform.platform())
print ("Pocessor: " +platform.processor())
print ("System OS: "+platform.system())
print ("Release: " +platform.release())
print ("Version: " +platform.version())


print("")
print("="*20, "Information sur la machine", "="*20)
print("")

# Qui a fabriqué le poste
 
print(f"Manufacturer: {my_system.Manufacturer}")
print(f"Marque: {info_bios.Version}")
print(f"Modele: {my_system.Model}")
print("")
# Qui je suis ? (Le poste)

print(f"Hostname: {my_system.Name}")
print(f"Numéro de série: {info_bios.SerialNumber}")
print("")
# Quelle est mon OS ?
print(f"System: {uname.system}")           #  Returns the system/OS name
print(f"Windows: {uname.release}")          # Returns the system’s release
print(f"Version de Windows: {uname.version}")        #  Returns the system’s release version, e.
print(f"Architecture Machine: {uname.machine}")               #  Returns the machine type, e.g. 'i386'.
print(f"SystemFamily: {my_system.SystemFamily}")
print(f"SystemType: {my_system.SystemType}")
print("")

# Quelles sont mes processeurs ?

print(f"Nom du processeur: {processeur.Name}")
print(f"NumberOfProcessors: {my_system.NumberOfProcessors}")
print(f"Nbr processeur logique: {processeur.NumberOfLogicalProcessors}")
print("")

# Quelles est la taille de ma RAM ?

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

print(f"Nom de domaine: {my_system.Domain}")
print("")
# Qui je suis ? (User)

print(f"Nom de l'utilisateur actuel: {my_system.UserName}")
print("")

# Quelle est ma carte mere ?

print(f"Type de carte Mere: {carte_mere.Caption}")
print(f"Fabricant de la carte mere: {carte_mere.Manufacturer}")
print(f"Carte mere remplacable: {carte_mere.Replaceable}")
print(f"Numéro de serie de la carte mere: {carte_mere.SerialNumber}")
print("")

# Mes cartes réseaux ?

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













# Pour afficher la totalité des infos lister dans le tableau
#c = wmi.WMI ()
#for s in c.Win32_ComputerSystem ():
#  print (s)




