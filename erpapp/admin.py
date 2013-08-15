from django.contrib import admin 
from .models import ERPInquiry,OpenERPModules,ErpCustomers,ErpDemo

admin.site.register(ERPInquiry)
admin.site.register(ErpCustomers)
admin.site.register(OpenERPModules)
admin.site.register(ErpDemo)
