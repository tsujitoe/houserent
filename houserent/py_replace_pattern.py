from devhouse.models import Devinfo

infos = Devinfo.objects.all()

for info in infos:
	try:
		pattern = info.dev_pattern
		info.dev_pattern = pattern.replace("房","嘿嘿嘿")
		info.save()
		print('更改成功')
	except:
		print('更改失敗')
