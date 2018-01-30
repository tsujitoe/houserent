from devhouse.models import Devinfo

infos = Devinfo.objects.all()

for info in infos:
	try:
		info.dev_pattern.replace("(室)","")
		info.save()
		print('更改成功')
	except:
		print('更改失敗')
