import requests, json, argparse

url = 'https://api.indoxploit.or.id/lookup/ip/'


#====================================== #
#       	Script By RTechS			#
#		  rusmants.public@pm.me			#
#	     Rusman Tobyakta Siregar		#
#	          @rusman_toby				#
#======================================	#


def getJson(ip):
	u = url+ip
	req = requests.get(u)
	js = json.loads(req.text)
	if 'error' in js:
		print('Harap masukkan alamat ip yang valid / coba lagi')
		exit()
	elif 'message' in js:
		if js['message'] == 'private range':
			print(f'{ip} adalah ip private range')
		elif js['message'] == 'reserved range':
			print(f'{ip} adalah ip reserved range')
		print('Masukkan alamat ip yang valid')
		exit()

	urlMap = 'https://www.google.co.id/maps/place/{},{}'.format(js['lat'],js['lon'])
	print('''
#====================================== #
#           Script By RTechS            #
#         rusmants.public@pm.me         #
#             @rusman_toby              #
#====================================== #

===================== {} =====================
Negara = {}
Kota = {}
Latitude = {}
Longtitude = {}
Kode Negara = {}
Nama ISP = {}
Wilayah = {}
Zona Waktu = {}
VPN = {}
Tor = {}
Zip = {}
Maps Url = {}
				
		'''.format(ip, js['country'], js['city'], js['lat'], js['lon'],js['countryCode'], js['isp'], js['regionName'], js['timezone'], js['active_vpn'], js['active_tor'], js['zip'], urlMap ))




parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ip", help="ip target", default='8.8.8.8')
args = parser.parse_args()
getJson(args.ip)





