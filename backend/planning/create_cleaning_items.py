
from .models import CleaningListItem
import django

django.setup()


def clear_daily_items():
    CleaningListItem.objects.filter(frequency="D").delete()


def clear_weekly_items():
    CleaningListItem.objects.filter(frequency="W").delete()


def clear_monthly_items():
    CleaningListItem.objects.filter(frequency="M").delete()
