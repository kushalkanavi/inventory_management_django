from django.conf.urls import url
from my_app.views import index, main, saveInventory, inventorySearch, editInventory, approveInventory, addInventoryPermission, managerPermissions, assistantPermissions, acceptPermissions, rejectPermissions, editInventoryPermission, acceptEditPermissions, rejectEditPermissions
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^login/$', auth_views.login, {'template_name': 'my_app/login_user.html'}, name='login'),
	url(r'^logout/$', auth_views.logout, {'template_name': 'my_app/logged_out.html'}, name='logout'),

	url(r'^main/$', main.as_view(),name='main'),
	url(r'^saveInventory/$', saveInventory.as_view(), name='saveInventory'),
	url(r'^inventorySearch/$', inventorySearch, name='inventorySearch'),
	url(r'^editInventory/(?P<id>\d+)/$', editInventory.as_view(), name='editInventory'),
	url(r'^approveInventory/(?P<id>\d+)/$', approveInventory.as_view(), name='approveInventory'),
	url(r'^managerPermissions/$', managerPermissions.as_view(), name='managerPermissions'),
	url(r'^acceptPermissions/(?P<id>\d+)/$', acceptPermissions.as_view(), name='acceptPermissions'),
	url(r'^rejectPermissions/(?P<id>\d+)/$', rejectPermissions.as_view(), name='rejectPermissions'),

	url(r'^addInventoryPermission/$', addInventoryPermission.as_view(), name='addInventoryPermission'),
	url(r'^assistantPermissions/$', assistantPermissions.as_view(), name='assistantPermissions'),
	url(r'^editInventoryPermission/(?P<id>\d+)/$', editInventoryPermission.as_view(), name='editInventoryPermission'),
	url(r'^acceptEditPermissions/(?P<id>\d+)/$', acceptEditPermissions.as_view(), name='acceptEditPermissions'),
	url(r'^rejectEditPermissions/(?P<id>\d+)/$', rejectEditPermissions.as_view(), name='rejectEditPermissions'),
	
    url(r'^$', index.as_view(), name='index'),
]