from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("inactive", "Inactive"),
    ]

    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    company = models.CharField(max_length=150, blank=True)
    notes = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="active"
    )
    
    owner = models.ForeignKey(
    User,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="customers",
    )   

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Lead(models.Model):
    STATUS_CHOICES = [
        ("new", "New"),
        ("contacted", "Contacted"),
        ("qualified", "Qualified"),
        ("converted", "Converted"),
        ("lost", "Lost"),
    ]

    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    company = models.CharField(max_length=150, blank=True)
    source = models.CharField(max_length=100, blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new"
    )

    notes = models.TextField(blank=True)

    converted_customer = models.OneToOneField(
        "Customer",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="converted_lead",
    )
    
    owner = models.ForeignKey(
    User,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="leads",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Deal(models.Model):
    STAGE_CHOICES = [
        ("proposal", "Proposal"),
        ("negotiation", "Negotiation"),
        ("won", "Won"),
        ("lost", "Lost"),
    ]

    name = models.CharField(max_length=150)

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="deals"
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    stage = models.CharField(
        max_length=20,
        choices=STAGE_CHOICES,
        default="proposal"
    )
    
    owner = models.ForeignKey(
    User,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="deals",
    )

    expected_close_date = models.DateField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# class Activity(models.Model):
#     TYPE_CHOICES = [
#         ("call", "Call"),
#         ("meeting", "Meeting"),
#         ("note", "Note"),
#         ("followup", "Follow-up"),
#     ]

#     customer = models.ForeignKey(
#         Customer,
#         on_delete=models.CASCADE,
#         related_name="activities"
#     )

#     activity_type = models.CharField(
#         max_length=20,
#         choices=TYPE_CHOICES
#     )

#     description = models.TextField()

#     due_date = models.DateTimeField(
#         null=True,
#         blank=True
#     )

#     completed = models.BooleanField(default=False)

#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.customer.name} - {self.activity_type}"

class Activity(models.Model):
    TYPE_CHOICES = [
        ("call", "Call"),
        ("meeting", "Meeting"),
        ("note", "Note"),
        ("followup", "Follow-up"),
    ]

    lead = models.ForeignKey(
        Lead,
        on_delete=models.CASCADE,
        related_name="activities",
        null=True,
        blank=True,
    )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="activities",
        null=True,
        blank=True,
    )

    activity_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES
    )

    description = models.TextField()

    due_date = models.DateTimeField(
        null=True,
        blank=True
    )
    
    owner = models.ForeignKey(
    User,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="activities",
    )

    completed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.lead:
            return f"{self.lead.name} - {self.activity_type}"

        if self.customer:
            return f"{self.customer.name} - {self.activity_type}"

        return self.activity_type

