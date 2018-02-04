from devhouse.models import Devinfo

infos = Devinfo.objects.all()

for info in infos:
	try:
		pattern = info.dev_pattern
		info.dev_pattern = pattern.replace("(室)","")
		info.dev_pattern = pattern.replace("3坪","")
		info.dev_pattern = pattern.replace("4坪","")
		info.dev_pattern = pattern.replace("5坪","")
		info.dev_pattern = pattern.replace("6坪","")
		info.dev_pattern = pattern.replace("7坪","")
		info.dev_pattern = pattern.replace("8坪","")
		info.dev_pattern = pattern.replace("9坪","")
		info.dev_pattern = pattern.replace("10坪","")
		#info.dev_pattern = pattern.replace("11坪","")
		#info.dev_pattern = pattern.replace("12坪","")
		#info.dev_pattern = pattern.replace("13坪","")
		info.save()
		print('更改成功')
	except:
		print('更改失敗')
