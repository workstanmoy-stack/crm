from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.dashboard,
        name="dashboard"
    ),

    path(
        "customers/",
        views.customer_list,
        name="customer_list"
    ),

    path(
        "customers/add/",
        views.customer_create,
        name="customer_create"
    ),

    path(
        "customers/<int:pk>/",
        views.customer_detail,
        name="customer_detail"
    ),

    path(
        "customers/<int:pk>/edit/",
        views.customer_edit,
        name="customer_edit"
    ),

    path(
        "customers/<int:pk>/delete/",
        views.customer_delete,
        name="customer_delete"
    ),
    path(
    "leads/",
    views.lead_list,
    name="lead_list"
),

path(
    "leads/add/",
    views.lead_create,
    name="lead_create"
),

path(
    "leads/<int:pk>/",
    views.lead_detail,
    name="lead_detail"
),

path(
    "leads/<int:pk>/edit/",
    views.lead_edit,
    name="lead_edit"
),

path(
    "leads/<int:pk>/delete/",
    views.lead_delete,
    name="lead_delete"
),
path(
    "deals/",
    views.deal_list,
    name="deal_list"
),

path(
    "deals/add/",
    views.deal_create,
    name="deal_create"
),

path(
    "deals/<int:pk>/",
    views.deal_detail,
    name="deal_detail"
),

path(
    "deals/<int:pk>/edit/",
    views.deal_edit,
    name="deal_edit"
),

path(
    "deals/<int:pk>/delete/",
    views.deal_delete,
    name="deal_delete"
),
path(
    "activities/",
    views.activity_list,
    name="activity_list"
),

path(
    "activities/add/",
    views.activity_create,
    name="activity_create"
),

path(
    "activities/<int:pk>/edit/",
    views.activity_edit,
    name="activity_edit"
),

path(
    "activities/<int:pk>/delete/",
    views.activity_delete,
    name="activity_delete"
),
path(
    "leads/<int:pk>/convert/",
    views.lead_convert,
    name="lead_convert"
),
]