#!/usr/bin/env python3

import json 

def http_get_json( url, headers, params=None, cookies=None):
	try:
		response = requests.get(url, headers=headers, cookies=cookies, params=params)
	except Exception as e:
		Log.get_logger().exception(e)
		raise
	return response.status_code, response.json()

def http_post( url, headers, data=None, cookies=None):
	try:
		response = requests.post(url, headers=headers, cookies=cookies, data=data)
	except Exception as e:
		Log.get_logger().exception(e)
		raise
	return response.status_code, response.json()
		
	
def get_request_data( fid, pz, pn):
	page_json = {"fid": fid, "pz": pz, "type": "WEB_FRIEND", "pn": pn}
	return  {"p": json.dumps(page_json), "requestToken": requestToken, "_rtk": _rtk}
	

def parse_cookie(cookie):
	cookies_list = cookie.split(';')
	cookie_dict = {}
	for cookie in cookies_list:
		k, v = cookie.split('=', 1)
		cookie_dict[k.strip()] = v
	return cookie_dict
	
		
request_url = "http://friend.renren.com/friend/api/getotherfriendsdata"

CHROM_HEADER = {
	"Accept": "application/json, text/javascript, */*; q=0.01",
	"Accept - Encoding": "gzip, deflate",
	"Accept - Language": "zh - CN, zh;q = 0.9",
	"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
	"Connection": "close",
	"Host": "friend.renren.com",
	"Origin": "http: // friend.renren.com",
	"X - Requested - With": "XMLHttpRequest"
}

cookie = "anonymid=jpqzhzn3mjrbm0; _r01_=1; _de=085C0D6D57D8483C5BF7EAB63017E04A; ln_uact=yxba_02@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn221/20141225/2040/main_OfDO_747d00029c29195a.jpg; jebe_key=d50226be-ce36-4b8a-931f-afa380c6b0e2%7Cf38044e0b216ea6d1642d82816df489c%7C1544972724578%7C1%7C1544972723629; __utma=10481322.905640354.1544972381.1544972381.1545065307.2; __utmz=10481322.1545065307.2.2.utmcsr=photo.renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/photo/68184877/albumlist/v7; depovince=SX; jebecookies=76a0bfa5-321f-4f02-89ab-3b29a0a2c53b|||||; ick_login=8b71b82e-db5e-4e48-99ec-1501601ad066; p=b19f097b366de7de96eff958319697107; first_login_flag=1; t=961a8d66d4a81c335757c45257ca71307; societyguester=961a8d66d4a81c335757c45257ca71307; id=102747867; xnsid=2973e83f; loginfrom=syshome; ch_id=10016; wp_fold=0; jebe_key=d50226be-ce36-4b8a-931f-afa380c6b0e2%7Cf38044e0b216ea6d1642d82816df489c%7C1544972724578%7C1%7C1545492773174"
requestToken= "-711138180"
_rtk = "a15de2d6"

def main():
	cookie_dict = parse_cookie(cookie)
	code, res = http_post(request_url, CHROM_HEADER, get_request_data(73802339, 100, 0), cookie_dict)
	
	print(code)
	print(res)
	
	
	
	
	
	
if __name__ == '__main__':
	main()