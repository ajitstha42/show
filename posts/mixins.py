from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from .models import CustomUser


class RecruiterAccessMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.role != CustomUser.RECRUITER

    def handle_no_permission(self):
        raise PermissionDenied("You do not have permission to access this page.")
