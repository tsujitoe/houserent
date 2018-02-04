from devhouse.models import Devinfo

infos = Devinfo.objects.all()

for info in infos:
	try:
		pattern = info.dev_pattern
		info.dev_pattern = pattern.replace("(室)","") # 針對好房網
		info.dev_pattern = pattern.replace("3坪","套房") # 以下針對591套房
		info.dev_pattern = pattern.replace("4坪","套房")
		info.dev_pattern = pattern.replace("5坪","套房")
		info.dev_pattern = pattern.replace("6坪","套房")
		info.dev_pattern = pattern.replace("7坪","套房")
		info.dev_pattern = pattern.replace("8坪","套房")
		info.dev_pattern = pattern.replace("9坪","套房")
		info.dev_pattern = pattern.replace("10坪","套房")
		info.dev_pattern = pattern.replace("11坪","套房")
		info.dev_pattern = pattern.replace("12坪","套房")
		info.dev_pattern = pattern.replace("13坪","套房")
		info.dev_pattern = pattern.replace("15坪","套房")
		info.dev_pattern = pattern.replace("16坪","套房")
		info.dev_pattern = pattern.replace("17坪","套房")
		info.dev_pattern = pattern.replace("18坪","套房")
		info.dev_pattern = pattern.replace("19坪","套房")
		info.dev_pattern = pattern.replace("20坪","套房")
		info.dev_pattern = pattern.replace("21坪","套房")
		info.dev_pattern = pattern.replace("22坪","套房")
		info.dev_pattern = pattern.replace("23坪","套房")
		info.dev_pattern = pattern.replace("24坪","套房")
		info.dev_pattern = pattern.replace("25坪","套房")
		info.dev_pattern = pattern.replace("26坪","套房")
		info.dev_pattern = pattern.replace("27坪","套房")
		info.dev_pattern = pattern.replace("28坪","套房")
		info.dev_pattern = pattern.replace("29坪","套房")

		info.save()
		print('更改成功')
	except:
		print('更改失敗')
