from django.contrib import admin
from .models import Customer, Lead, Deal, Activity


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "company",
        "email",
        "phone",
        "status",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "company",
        "phone",
    )

    list_filter = ("status",)


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "company",
        "email",
        "source",
        "status",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "company",
    )

    list_filter = (
        "status",
        "source",
    )


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "customer",
        "amount",
        "stage",
        "expected_close_date",
    )

    search_fields = (
        "name",
        "customer__name",
    )

    list_filter = ("stage",)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = (
        "customer",
        "activity_type",
        "due_date",
        "completed",
        "created_at",
    )

    search_fields = (
        "customer__name",
        "description",
    )

    list_filter = (
        "activity_type",
        "completed",
    )