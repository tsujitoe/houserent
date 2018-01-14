from django.shortcuts import render, redirect
from .forms import TenantForm
from .models import Tenant

# Create your views here.


def get_tenant(request):
	if request.method == 'POST':
		form = TenantForm(request.POST, submit_title='建立')
		if form.is_valid():
			tenant = form.save()
			return redirect(tenant.get_absolute_url())
	else:
		form = TenantForm(submit_title='建立')
	return render(request, 'tenant_create.html', {'form': form})


def list_tenant(request, pk):
	try:
		tenant = Tenant.objects.get(pk=pk)
	except Tenant.DoesNotExist:
		raise Http404
	return render(request, 'tenant_list.html', {'tenant': tenant})
