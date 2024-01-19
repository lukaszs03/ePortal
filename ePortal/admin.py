from django.contrib import admin
from .models import Notification
from .models import PhoneNumber, Address, JobTitle, PersonalInfo, EtatInfo, PayList

admin.site.register(Notification)

class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ['user', 'number']
    search_fields = ['user__username', 'number']
    list_filter = ['user']

    def save_model(self, request, obj, form, change):
        # Automatyczne przypisanie aktualnie zalogowanego użytkownika jako właściciela numeru telefonu
        if not change:  # Jeśli to jest nowy obiekt (nie edycja istniejącego)
            obj.user = request.user
        super().save_model(request, obj, form, change)

admin.site.register(PhoneNumber, PhoneNumberAdmin)

class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'address']
    search_fields = ['user__username', 'address']
    list_filter = ['user']

    def save_model(self, request, obj, form, change):
        # Automatyczne przypisanie aktualnie zalogowanego użytkownika jako właściciela adresu
        if not change:  # Jeśli to jest nowy obiekt (nie edycja istniejącego)
            obj.user = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Address, AddressAdmin)

class JobTitleAdmin(admin.ModelAdmin):
    list_display = ['user', 'job_title']
    search_fields = ['user__username', 'job_title']
    list_filter = ['user']

    def save_model(self, request, obj, form, change):
        # Automatyczne przypisanie aktualnie zalogowanego użytkownika jako właściciela job_title
        if not change:  # Jeśli to jest nowy obiekt (nie edycja istniejącego)
            obj.user = request.user
        super().save_model(request, obj, form, change)

admin.site.register(JobTitle, JobTitleAdmin)

class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'pesel', 'birth_date']
    search_fields = ['user__username', 'pesel', 'birth_date']
    list_filter = ['user']

    def save_model(self, request, obj, form, change):
        # Automatyczne przypisanie aktualnie zalogowanego użytkownika jako właściciela 
        if not change:  # Jeśli to jest nowy obiekt (nie edycja istniejącego)
            obj.user = request.user
        super().save_model(request, obj, form, change)

admin.site.register(PersonalInfo, PersonalInfoAdmin)

class EtatInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'etat', 'etat_to', 'etat_form']
    search_fields = ['user__username', 'etat', 'etat_to', 'etat_form']
    list_filter = ['user']

    def save_model(self, request, obj, form, change):
        # Automatyczne przypisanie aktualnie zalogowanego użytkownika jako właściciela 
        if not change:  # Jeśli to jest nowy obiekt (nie edycja istniejącego)
            obj.user = request.user
        super().save_model(request, obj, form, change)

admin.site.register(EtatInfo, EtatInfoAdmin)

class PayListAdmin(admin.ModelAdmin):
    list_display = ['user', 'korekta', 'kwota', 'data_wyp']
    search_fields = ['user__username', 'korekta', 'kwota', 'data_wyp']
    list_filter = ['user']

    def save_model(self, request, obj, form, change):
        # Automatyczne przypisanie aktualnie zalogowanego użytkownika jako właściciela 
        if not change:  # Jeśli to jest nowy obiekt (nie edycja istniejącego)
            obj.user = request.user
        super().save_model(request, obj, form, change)

admin.site.register(PayList, PayListAdmin)





