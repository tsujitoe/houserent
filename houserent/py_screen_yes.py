from devhouse.models import Devinfo

infos = Devinfo.objects.all()

for info in infos:
	info.dev_screenshot_yes = True