from rest_framework.permissions import BasePermission
from datetime import datetime

class WorkingHoursPermission(BasePermission):
    message = "Ish vaqtimiz 09:00 dan 18:00 gacha"

    def has_permission(self, request, view):
        now = datetime.now().time()
        start = datetime.strptime("09:00", "%H:%M").time()
        end = datetime.strptime("18:00", "%H:%M").time()
        return start <= now <= end


class WeekdayPermission(BasePermission):
    message = "Bu faqat chorshanba va juma kunlari ishlaydi."

    def has_permission(self, request, view):
        today = datetime.today().weekday()
        return today in [2, 5]