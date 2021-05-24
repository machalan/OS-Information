
# Importer les librairies

import wmi
import socket
import platform
import os
import sys
import requests
from requests import get
import json

# Définir les fonctions


def mes_infos():
	c = wmi.WMI()
	uname = platform.uname()   
	my_system = c.Win32_ComputerSystem()[0]
	info_bios = c.Win32_BIOS()[0]
	carte_mere = c.Win32_BaseBoard()[0]
	processeur = c.Win32_Processor()[0]
	memoire_vive = c.Win32_PhysicalMemory()
	mes_disques = c.Win32_DiskDrive()
	mes_cartes_reseaux = c.Win32_NetworkAdapter()
	ip_local = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	ip_local.connect(("8.8.8.8", 80))
	mon_ip_local = ip_local.getsockname()[0]
	ip_local.close()
	ip2 = requests.get('https://checkip.amazonaws.com').text.strip()
	info_du_poste = {}
	RAM = {}
	disque = {}
	cartes_reseaux = {}
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
	info_du_poste["Nom de domaine:"] = my_system.Domain
	info_du_poste["Nom de l'utilisateur actuel:"] = my_system.UserName
	info_du_poste["Type de carte Mere:"] = carte_mere.Caption
	info_du_poste["Fabricant de la carte mere:"] = carte_mere.Manufacturer
	info_du_poste["Carte mere remplacable:"] = carte_mere.Replaceable
	info_du_poste["Numero de serie de la carte mere:"] = carte_mere.SerialNumber
	with open('C:\sources\data.json', 'w') as fp:
		  fp.write(json.dumps(info_du_poste, indent=4))
	
	for memoire_vive in memoire_vive:
		print(memoire_vive.Capacity)
		memoire_vive_1_Go = (int(memoire_vive.Capacity)/1073741824)
		RAM["RAM Taille:"] = (round(memoire_vive_1_Go))
		RAM["RAM Vitesse:"] = memoire_vive.ConfiguredClockSpeed
		RAM["RAM Fabricant ou code Fabricant:"] = memoire_vive.Manufacturer
		RAM["RAM Numero de serie :"] = memoire_vive.SerialNumber
		RAM["RAM Tag :"] = memoire_vive.Tag
		with open('C:\sources\data.json', 'a+') as fp:
			fp.write(json.dumps(RAM, indent=4))

	for mes_disques in mes_disques:
		print(mes_disques.Model)
		disques_1_taille_Go = (int(mes_disques.Size)/1073741824)
		disque["Disque - Taille du disque :"] = round(disques_1_taille_Go)
		disque["Disque - OK ou defaillant :"] = mes_disques.Status
		disque["Disque - Model du disque :"] = mes_disques.Model
		disque["Disque - Type interface :"] = mes_disques.InterfaceType
		disque["Disque - Numero de serie :"] = mes_disques.SerialNumber
		with open('C:\sources\data.json', 'a+') as fp:
			fp.write(json.dumps(disque, indent=4))

	for mes_cartes_reseaux in mes_cartes_reseaux:
		print(mes_cartes_reseaux.Description)
		cartes_reseaux["Carte reseaux :"] = mes_cartes_reseaux.AdapterType
		cartes_reseaux["Carte reseaux - Description :"] = mes_cartes_reseaux.Description
		cartes_reseaux["Carte reseaux - MACAddress :"] = mes_cartes_reseaux.MACAddress
		with open('C:\sources\data.json', 'a+') as fp:
			fp.write(json.dumps(cartes_reseaux, indent=4))









# Executer mon script

# Lancer la collecte, afficher la collect, attendre 45s et recommencer
i = 1
#while i <= 5:
mes_infos()

print ("voila!")   



