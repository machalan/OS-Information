import wmi
import platform
 
c = wmi.WMI()   
my_system = c.Win32_ComputerSystem()[0]
info_bios = c.Win32_BIOS()[0]
carte_mere = c.Win32_BaseBoard ()[0]
 
print(f"Manufacturer: {my_system.Manufacturer}")
print(f"Marque: {info_bios.Version}")
print(f"Modele: {my_system. Model}")


print(f"Hostname: {my_system.Name}")
print(f"Numéro de série: {info_bios.SerialNumber}")


print(f"SystemFamily: {my_system.SystemFamily}")
print(f"SystemType: {my_system.SystemType}")


print(f"NumberOfProcessors: {my_system.NumberOfProcessors}")
print(f"Nbr processeur logique: {my_system.NumberOfLogicalProcessors}")
print(f"Taille total de la RAM: {my_system.TotalPhysicalMemory}")


print(f"Nom de domaine: {my_system.Domain}")
print(f"Nom de l'utilisateur actuel: {my_system.UserName}")



print(f"Type de carte Mere: {carte_mere.Caption}")
print(f"Fabricant de la carte mere: {carte_mere.Manufacturer}")
print(f"Carte mere remplacable: {carte_mere.Replaceable}")
print(f"Numéro de serie de la carte mere: {carte_mere.SerialNumber}")












print("")
print("="*20, "Information sur la machine", "="*20)
print("")

uname = platform.uname()
print(f"System: {uname.system}")           #  Returns the system/OS name
print(f"Node Name: {uname.node}")         #  Returns the computer’s network name
print(f"Release: {uname.release}")          # Returns the system’s release
print(f"Version: {uname.version}")        #  Returns the system’s release version, e.
print(f"Machine: {uname.machine}")               #  Returns the machine type, e.g. 'i386'.
print(f"Processor: {uname.processor}")       #  Returns the (real) processor name,


#print("="*40, "Information sur les imprimantes", "="*40)

#for s in c.Win32_Printer ():

#     print(s.Caption, s.PortName, s.PrinterStatus) 

print("")
print("="*20, "Information sur les disques", "="*20)
print("")


#c = wmi.WMI ()
#for s in c.Win32_ComputerSystem ():
#  print (s)

c = wmi.WMI ()
for s in c.Win32_BaseBoard ():
   print (s)



Win32_Processor
Win32_PhysicalMemory
Win32_NetworkAdapter
Win32_VideoController
Win32_DiskDrive
