from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Lead, Deal, Activity
from django.contrib.auth.decorators import login_required



def is_manager_or_admin(user):
    return user.is_superuser or user.is_staff



@login_required
def dashboard(request):

    if is_manager_or_admin(request.user):

        customers = Customer.objects.all()
        leads = Lead.objects.all()
        deals = Deal.objects.all()
        activities = Activity.objects.all()

    else:

        customers = Customer.objects.filter(
            owner=request.user
        )

        leads = Lead.objects.filter(
            owner=request.user
        )

        deals = Deal.objects.filter(
            owner=request.user
        )

        activities = Activity.objects.filter(
            owner=request.user
        )

    context = {
        "customer_count": customers.count(),

        "lead_count": leads.count(),

        "deal_count": deals.count(),

        "open_deals": deals.exclude(
            stage__in=["won", "lost"]
        ).count(),

        "total_revenue": sum(
            deal.amount
            for deal in deals.filter(stage="won")
        ),

        "recent_activities": activities.select_related(
            "customer",
            "lead"
        ).order_by("-created_at")[:5],
    }

    return render(
        request,
        "crm/dashboard.html",
        context
    )


@login_required
def customer_list(request):

    if is_manager_or_admin(request.user):
        customers = Customer.objects.all()
    else:
        customers = Customer.objects.filter(
            owner=request.user
        )

    customers = customers.order_by("-created_at")

    search = request.GET.get("search", "")

    if search:
        customers = customers.filter(
            name__icontains=search
        ) | customers.filter(
            company__icontains=search
        ) | customers.filter(
            email__icontains=search
        )

    return render(
        request,
        "crm/customers/list.html",
        {
            "customers": customers,
            "search": search,
        }
    )


@login_required
def customer_detail(request, pk):

    if is_manager_or_admin(request.user):

        customer = get_object_or_404(
            Customer,
            pk=pk
        )

    else:

        customer = get_object_or_404(
            Customer,
            pk=pk,
            owner=request.user
        )

    return render(
        request,
        "crm/customers/detail.html",
        {"customer": customer}
    )


@login_required
def customer_create(request):

    if request.method == "POST":

        Customer.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            company=request.POST.get("company"),
            notes=request.POST.get("notes"),
            status=request.POST.get("status"),
            owner=request.user,
        )

        return redirect("customer_list")

    return render(
        request,
        "crm/customers/form.html"
    )


@login_required
def customer_edit(request, pk):

    if is_manager_or_admin(request.user):

        customer = get_object_or_404(
            Customer,
            pk=pk
        )

    else:

        customer = get_object_or_404(
            Customer,
            pk=pk,
            owner=request.user
        )

    if request.method == "POST":

        customer.name = request.POST.get("name")
        customer.email = request.POST.get("email")
        customer.phone = request.POST.get("phone")
        customer.company = request.POST.get("company")
        customer.notes = request.POST.get("notes")
        customer.status = request.POST.get("status")

        customer.save()

        return redirect(
            "customer_detail",
            pk=customer.pk
        )

    return render(
        request,
        "crm/customers/form.html",
        {"customer": customer}
    )


@login_required
def customer_delete(request, pk):

    if is_manager_or_admin(request.user):

        customer = get_object_or_404(
            Customer,
            pk=pk
        )

    else:

        customer = get_object_or_404(
            Customer,
            pk=pk,
            owner=request.user
        )

    if request.method == "POST":

        customer.delete()

        return redirect("customer_list")

    return render(
        request,
        "crm/customers/delete.html",
        {"customer": customer}
    )
    
    
@login_required
def lead_list(request):

    if is_manager_or_admin(request.user):
        leads = Lead.objects.all()
    else:
        leads = Lead.objects.filter(
            owner=request.user
        )

    leads = leads.order_by("-created_at")

    search = request.GET.get("search", "")
    status = request.GET.get("status", "")

    if search:
        leads = leads.filter(
            name__icontains=search
        ) | leads.filter(
            company__icontains=search
        ) | leads.filter(
            email__icontains=search
        )

    if status:
        leads = leads.filter(
            status=status
        )

    return render(
        request,
        "crm/leads/list.html",
        {
            "leads": leads,
            "search": search,
            "status": status,
        }
    )


@login_required
def lead_detail(request, pk):

    if is_manager_or_admin(request.user):

        lead = get_object_or_404(
            Lead,
            pk=pk
        )

    else:

        lead = get_object_or_404(
            Lead,
            pk=pk,
            owner=request.user
        )

    return render(
        request,
        "crm/leads/detail.html",
        {"lead": lead}
    )


@login_required
def lead_create(request):

    if request.method == "POST":

        Lead.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            company=request.POST.get("company"),
            source=request.POST.get("source"),
            status=request.POST.get("status"),
            notes=request.POST.get("notes"),
            owner=request.user,
        )

        return redirect("lead_list")

    return render(
        request,
        "crm/leads/form.html"
    )

@login_required
def lead_edit(request, pk):

    if is_manager_or_admin(request.user):
        lead = get_object_or_404(
            Lead,
            pk=pk
        )
    else:
        lead = get_object_or_404(
            Lead,
            pk=pk,
            owner=request.user
        )


    if request.method == "POST":

        lead.name = request.POST.get("name")
        lead.email = request.POST.get("email")
        lead.phone = request.POST.get("phone")
        lead.company = request.POST.get("company")
        lead.source = request.POST.get("source")
        lead.status = request.POST.get("status")
        lead.notes = request.POST.get("notes")

        lead.save()

        return redirect("lead_detail", pk=lead.pk)

    return render(
        request,
        "crm/leads/form.html",
        {"lead": lead}
    )

@login_required
def lead_delete(request, pk):

    if is_manager_or_admin(request.user):
        lead = get_object_or_404(
            Lead,
            pk=pk
        )
    else:
        lead = get_object_or_404(
            Lead,
            pk=pk,
            owner=request.user
        )

    if request.method == "POST":
        lead.delete()
        return redirect("lead_list")

    return render(
        request,
        "crm/leads/delete.html",
        {"lead": lead}
    )

@login_required
def deal_list(request):

    if is_manager_or_admin(request.user):
        deals = Deal.objects.select_related("customer").all()
    else:
        deals = Deal.objects.select_related("customer").filter(
            owner=request.user
        )

    search = request.GET.get("search", "")
    stage = request.GET.get("stage", "")

    if search:
        deals = deals.filter(
            name__icontains=search
        ) | deals.filter(
            customer__name__icontains=search
        )

    if stage:
        deals = deals.filter(stage=stage)

    deals = deals.order_by("-created_at")

    return render(
        request,
        "crm/deals/list.html",
        {
            "deals": deals,
            "search": search,
            "stage": stage,
        }
    )


@login_required
def deal_detail(request, pk):

    if is_manager_or_admin(request.user):
        deal = get_object_or_404(
            Deal.objects.select_related("customer"),
            pk=pk
        )
    else:
        deal = get_object_or_404(
            Deal.objects.select_related("customer"),
            pk=pk,
            owner=request.user
        )

    return render(
        request,
        "crm/deals/detail.html",
        {"deal": deal}
    )


@login_required
def deal_create(request):

    if request.method == "POST":

        Deal.objects.create(
        name=request.POST.get("name"),
        customer_id=request.POST.get("customer"),
        amount=request.POST.get("amount"),
        stage=request.POST.get("stage"),
        expected_close_date=request.POST.get(
            "expected_close_date"
        ) or None,
        owner=request.user,
    )

        return redirect("deal_list")

    if is_manager_or_admin(request.user):
        customers = Customer.objects.filter(
            status="active"
        ).order_by("name")
    else:
        customers = Customer.objects.filter(
            status="active",
            owner=request.user
        ).order_by("name")

    return render(
        request,
        "crm/deals/form.html",
        {"customers": customers}
    )

@login_required
def deal_edit(request, pk):

    if is_manager_or_admin(request.user):
        deal = get_object_or_404(
            Deal,
            pk=pk
        )
    else:
        deal = get_object_or_404(
            Deal,
            pk=pk,
            owner=request.user
        )

    if request.method == "POST":

        deal.name = request.POST.get("name")
        deal.customer_id = request.POST.get("customer")
        deal.amount = request.POST.get("amount")
        deal.stage = request.POST.get("stage")
        deal.expected_close_date = (
            request.POST.get("expected_close_date") or None
        )

        deal.save()

        return redirect("deal_detail", pk=deal.pk)

    if is_manager_or_admin(request.user):
        customers = Customer.objects.filter(
            status="active"
        ).order_by("name")
    else:
        customers = Customer.objects.filter(
            status="active",
            owner=request.user
        ).order_by("name")

    return render(
        request,
        "crm/deals/form.html",
        {
            "deal": deal,
            "customers": customers,
        }
    )

@login_required
def deal_delete(request, pk):

    if is_manager_or_admin(request.user):
        deal = get_object_or_404(
            Deal,
            pk=pk
        )
    else:
        deal = get_object_or_404(
            Deal,
            pk=pk,
            owner=request.user
        )

    if request.method == "POST":
        deal.delete()
        return redirect("deal_list")

    return render(
        request,
        "crm/deals/delete.html",
        {"deal": deal}
    )

# @login_required
# def activity_list(request):
#     activities = Activity.objects.select_related(
#         "lead",
#         "customer"
#     ).all().order_by("-created_at")

#     activity_type = request.GET.get("type", "")
#     completed = request.GET.get("completed", "")

#     if activity_type:
#         activities = activities.filter(
#             activity_type=activity_type
#         )

#     if completed == "yes":
#         activities = activities.filter(completed=True)

#     elif completed == "no":
#         activities = activities.filter(completed=False)

#     if is_manager_or_admin(request.user):

#         activities = Activity.objects.all()

#     else:

#         activities = Activity.objects.filter(
#             owner=request.user
#         )

#     return render(
#         request,
#         "crm/activities/list.html",
#         {
#             "activities": activities,
#             "activity_type": activity_type,
#             "completed": completed,
#         }
#     )

@login_required
def activity_list(request):

    if is_manager_or_admin(request.user):

        activities = Activity.objects.select_related(
            "lead",
            "customer"
        ).all()

    else:

        activities = Activity.objects.select_related(
            "lead",
            "customer"
        ).filter(
            owner=request.user
        )

    activity_type = request.GET.get("type", "")
    completed = request.GET.get("completed", "")

    if activity_type:
        activities = activities.filter(
            activity_type=activity_type
        )

    if completed == "yes":
        activities = activities.filter(
            completed=True
        )

    elif completed == "no":
        activities = activities.filter(
            completed=False
        )

    activities = activities.order_by("-created_at")

    return render(
        request,
        "crm/activities/list.html",
        {
            "activities": activities,
            "activity_type": activity_type,
            "completed": completed,
        }
    )

# @login_required
# def activity_create(request):
    
#     if is_manager_or_admin(request.user):

#         leads = Lead.objects.exclude(
#             status="lost"
#         ).order_by("name")

#         customers = Customer.objects.filter(
#             status="active"
#         ).order_by("name")

#     else:

#         leads = Lead.objects.filter(
#             owner=request.user
#         ).exclude(
#             status="lost"
#         ).order_by("name")

#         customers = Customer.objects.filter(
#             owner=request.user,
#             status="active"
#         ).order_by("name")

#     if request.method == "POST":

#         lead_id = request.POST.get("lead")
#         customer_id = request.POST.get("customer")

#         Activity.objects.create(
#             lead_id=lead_id or None,
#             customer_id=customer_id or None,
#             activity_type=request.POST.get("activity_type"),
#             description=request.POST.get("description"),
#             due_date=request.POST.get("due_date") or None,
#             completed=request.POST.get("completed") == "on",
#             owner=request.user,
#         )

#         return redirect("activity_list")

#     leads = Lead.objects.exclude(
#         status="lost"
#     ).order_by("name")

#     customers = Customer.objects.filter(
#         status="active"
#     ).order_by("name")

#     return render(
#         request,
#         "crm/activities/form.html",
#         {
#             "leads": leads,
#             "customers": customers,
#         }
#     )

@login_required
def activity_create(request):

    if is_manager_or_admin(request.user):

        leads = Lead.objects.exclude(
            status="lost"
        ).order_by("name")

        customers = Customer.objects.filter(
            status="active"
        ).order_by("name")

    else:

        leads = Lead.objects.filter(
            owner=request.user
        ).exclude(
            status="lost"
        ).order_by("name")

        customers = Customer.objects.filter(
            owner=request.user,
            status="active"
        ).order_by("name")

    if request.method == "POST":

        lead_id = request.POST.get("lead")
        customer_id = request.POST.get("customer")

        # Validate Lead ownership
        if lead_id:

            if is_manager_or_admin(request.user):
                lead = get_object_or_404(
                    Lead,
                    pk=lead_id
                )
            else:
                lead = get_object_or_404(
                    Lead,
                    pk=lead_id,
                    owner=request.user
                )

        # Validate Customer ownership
        if customer_id:

            if is_manager_or_admin(request.user):
                customer = get_object_or_404(
                    Customer,
                    pk=customer_id
                )
            else:
                customer = get_object_or_404(
                    Customer,
                    pk=customer_id,
                    owner=request.user
                )

        Activity.objects.create(
            lead_id=lead_id or None,
            customer_id=customer_id or None,
            activity_type=request.POST.get("activity_type"),
            description=request.POST.get("description"),
            due_date=request.POST.get("due_date") or None,
            completed=request.POST.get("completed") == "on",
            owner=request.user,
        )

        return redirect("activity_list")

    return render(
        request,
        "crm/activities/form.html",
        {
            "leads": leads,
            "customers": customers,
        }
    )

@login_required
def activity_edit(request, pk):
    
    if is_manager_or_admin(request.user):
        activity = get_object_or_404(
            Activity,
            pk=pk
        )
    else:
        activity = get_object_or_404(
            Activity,
            pk=pk,
            owner=request.user
        )


    if request.method == "POST":

        lead_id = request.POST.get("lead")
        customer_id = request.POST.get("customer")

        activity.lead_id = lead_id or None
        activity.customer_id = customer_id or None
        activity.activity_type = request.POST.get("activity_type")
        activity.description = request.POST.get("description")
        activity.due_date = request.POST.get("due_date") or None
        activity.completed = request.POST.get("completed") == "on"

        activity.save()

        return redirect("activity_list")

    if is_manager_or_admin(request.user):

        leads = Lead.objects.exclude(
            status="lost"
        ).order_by("name")

        customers = Customer.objects.filter(
            status="active"
        ).order_by("name")

    else:

        leads = Lead.objects.filter(
            owner=request.user
        ).exclude(
            status="lost"
        ).order_by("name")

        customers = Customer.objects.filter(
            owner=request.user,
            status="active"
        ).order_by("name")

    return render(
        request,
        "crm/activities/form.html",
        {
            "activity": activity,
            "leads": leads,
            "customers": customers,
        }
    )

@login_required
def activity_delete(request, pk):
    
    if is_manager_or_admin(request.user):
        activity = get_object_or_404(
            Activity,
            pk=pk
        )
    else:
        activity = get_object_or_404(
            Activity,
            pk=pk,
            owner=request.user
        )


    if request.method == "POST":
        activity.delete()
        return redirect("activity_list")

    return render(
        request,
        "crm/activities/delete.html",
        {"activity": activity}
    )
    
@login_required
def lead_convert(request, pk):
    
    if is_manager_or_admin(request.user):
        lead = get_object_or_404(
            Lead,
            pk=pk
        )
    else:
        lead = get_object_or_404(
            Lead,
            pk=pk,
            owner=request.user
        )


    # Already converted
    if lead.converted_customer:
        return redirect(
            "customer_detail",
            pk=lead.converted_customer.pk
        )

    # Only qualified leads can be converted
    if lead.status != "qualified":
        return redirect("lead_detail", pk=lead.pk)

    customer = Customer.objects.create(
    name=lead.name,
    email=lead.email,
    phone=lead.phone,
    company=lead.company,
    notes=lead.notes,
    status="active",
    owner=lead.owner,
)

    lead.status = "converted"
    lead.converted_customer = customer
    lead.save()

    return redirect(
        "customer_detail",
        pk=customer.pk
    )