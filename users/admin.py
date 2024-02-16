from django import forms
from django.contrib import admin
from .models import CustomUser


class CustomUserAdminForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Make certain fields optional for administrators
        if self.instance and self.instance.is_staff:
            self.fields["cv"].required = False
            self.fields["resume"].required = False
            self.fields["role"].required = False


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    form = CustomUserAdminForm
    readonly_fields = ("password",)
