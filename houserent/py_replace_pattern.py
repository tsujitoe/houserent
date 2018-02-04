from devhouse.models import Devinfo

pattern_word = {
	"(室)":" ",  # 針對好房網
	"3坪":"套房", # 以下針對591套房
	"4坪":"套房",
	"5坪":"套房",
	"6坪":"套房",
	"7坪":"套房",
	"8坪":"套房",
	"9坪":"套房",
	"10坪":"套房",
	"11坪":"套房",
	"12坪":"套房",
	"13坪":"套房",
	"14坪":"套房",
	"15坪":"套房",
	"16坪":"套房",
	"17坪":"套房",
	"18坪":"套房",
	"19坪":"套房",
	"20坪":"套房",
	"21坪":"套房",
	"22坪":"套房",
	"23坪":"套房",
	"24坪":"套房",
	"25坪":"套房",
}


infos = Devinfo.objects.all()

for info in infos:
	try:
		pattern = info.dev_pattern
		for word, change_word in pattern_word.items():
			pattern = pattern.replace(word, change_word)
			info.dev_pattern = pattern
		info.save()
		print('更改成功-%s' % info.dev_address)
	except:
		print('更改失敗-%s' % info.dev_address)
