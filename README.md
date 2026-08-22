
# SimpleCRM

A simple multi-user Customer Relationship Management (CRM) system built with Django.

SimpleCRM is designed for small businesses and sales teams that need a centralized place to manage potential customers, existing customers, sales activities, and deals.

The project demonstrates how a real-world business workflow can be implemented using Django's traditional server-rendered architecture, Django ORM, authentication, authorization, database relationships, and business logic.

---

## 📌 What is SimpleCRM?

A CRM (Customer Relationship Management) system helps a company organize and manage its relationships with potential and existing customers.

Without a CRM, sales information can become scattered across:

- Spreadsheets
- WhatsApp conversations
- Emails
- Notes
- Personal reminders
- Different employees' individual records

This makes it difficult to answer questions such as:

- Who are our current leads?
- Who needs a follow-up?
- Which leads are qualified?
- Which salesperson owns a lead?
- Which customers are active?
- What deals are currently being negotiated?
- How much revenue has been generated?
- What happened during the last customer interaction?

SimpleCRM brings this information into one centralized system.

---

# 🎯 Main Purpose

The purpose of this project is to manage the complete journey of a sales opportunity:

```text
Potential Customer
       ↓
      Lead
       ↓
   Contacted
       ↓
   Qualified
       ↓
Convert to Customer
       ↓
    Customer
       ↓
      Deal
       ↓
    Proposal
       ↓
  Negotiation
       ↓
   Won / Lost
````

At the same time, salespeople can record calls, meetings, notes, and follow-ups throughout the process.

---

# 👥 Who Uses SimpleCRM?

SimpleCRM is designed for a company where multiple people are involved in sales.

## Salesperson

A salesperson uses the CRM on a daily basis.

They can:

* Create leads
* Manage their leads
* Contact potential customers
* Record calls
* Schedule follow-ups
* Add notes
* Qualify leads
* Convert qualified leads into customers
* Manage their customers
* Create deals
* Track negotiations
* Mark deals as won or lost
* Monitor their own sales activity

A salesperson only works with the CRM records assigned to them.

---

## Manager

A sales manager oversees the sales team.

A manager can monitor broader team information such as:

* Leads
* Customers
* Deals
* Activities
* Sales pipeline
* Revenue

For example:

```text
Sales Team

Rahul
├── 15 Leads
├── 8 Customers
└── ₹4,50,000 Pipeline

Amit
├── 21 Leads
├── 11 Customers
└── ₹6,20,000 Pipeline
```

The manager can use this information to understand how the sales team is performing.

---

## Administrator

The administrator manages the CRM system and users.

The administrator can use Django Admin to manage:

* Users
* CRM records
* System data
* Administrative information

---

# 🔄 Complete CRM Business Flow

The core business flow of SimpleCRM is:

```text
                    NEW INQUIRY
                         │
                         ▼
                       LEAD
                         │
                         ▼
                    CONTACTED
                         │
                         ▼
                     QUALIFIED
                         │
                         ▼
                CONVERT TO CUSTOMER
                         │
                         ▼
                     CUSTOMER
                         │
                ┌────────┴────────┐
                │                 │
                ▼                 ▼
            ACTIVITIES           DEAL
                │                 │
          ┌─────┼─────┐           ▼
          │     │     │        PROPOSAL
         Call Meeting Note         │
          │     │     │            ▼
          └─────┼─────┘       NEGOTIATION
                │                 │
                │           ┌─────┴─────┐
                │           ▼           ▼
                │         WON          LOST
                │
                ▼
         CUSTOMER HISTORY
```

---

# 🧑‍💼 Real-World Example

Imagine a web development company that builds websites for businesses.

A restaurant owner named **Rahul Sharma** contacts the company and says:

> "I need a website for my restaurant."

The sales team can manage the entire relationship through SimpleCRM.

---

## Step 1 — Create a Lead

A salesperson receives the inquiry.

They create:

```text
Name: Rahul Sharma
Company: Rahul's Restaurant
Email: rahul@gmail.com
Phone: 9876543210
Source: Website
Status: New
```

The CRM now knows:

```text
Rahul Sharma
      ↓
    LEAD
      ↓
Owner: Salesperson
```

Rahul is not a customer yet.

He is a potential customer.

---

# Step 2 — Contact the Lead

The salesperson calls Rahul.

They discuss:

* Website requirements
* Number of pages
* Restaurant menu
* Photo gallery
* Online booking
* Estimated budget

The salesperson records the call:

```text
Activity Type:
Call

Lead:
Rahul Sharma

Description:
Discussed restaurant website requirements.

Completed:
Yes
```

The CRM now contains a record of the interaction.

---

# Step 3 — Create a Follow-up

The salesperson tells Rahul:

> "I'll send you a proposal tomorrow."

Instead of relying on memory, the salesperson creates a follow-up:

```text
Activity Type:
Follow-up

Lead:
Rahul Sharma

Description:
Send restaurant website proposal.

Due Date:
Tomorrow

Completed:
No
```

The activity remains pending until the salesperson completes it.

---

# Step 4 — Complete the Follow-up

The next day, the salesperson sends the proposal.

They open the activity and mark it:

```text
Completed: Yes
```

The CRM now has a record that the follow-up was completed.

---

# Step 5 — Change Lead Status

Rahul responds:

> "I'm interested. Let's discuss the project."

The salesperson changes the lead status:

```text
New
 ↓
Contacted
```

After discussing the requirements and confirming that Rahul is a serious potential buyer:

```text
Contacted
 ↓
Qualified
```

Now the lead is ready to become a customer.

---

# Step 6 — Convert Lead into Customer

The salesperson clicks:

```text
Convert to Customer
```

SimpleCRM creates a Customer using the lead's information.

```text
CUSTOMER

Rahul Sharma
Rahul's Restaurant

Email:
rahul@gmail.com

Phone:
9876543210

Status:
Active
```

The original Lead becomes:

```text
Converted
```

The relationship is maintained:

```text
Lead
  │
  └── Converted Customer
```

The customer also remains owned by the same salesperson.

---

# Step 7 — Continue Customer Activities

Now Rahul is a customer.

The salesperson has a meeting with him to discuss the final design.

They record:

```text
Activity Type:
Meeting

Customer:
Rahul Sharma

Description:
Discussed final website design,
pricing and delivery timeline.

Completed:
Yes
```

The CRM now contains the customer's interaction history.

---

# Step 8 — Create a Deal

Rahul agrees to move forward with the project.

The salesperson creates:

```text
Deal:

Name:
Restaurant Website

Customer:
Rahul Sharma

Amount:
₹50,000

Stage:
Proposal
```

The deal represents the actual sales opportunity.

---

# Step 9 — Negotiation

Rahul asks:

> "Can you do it for ₹45,000?"

The salesperson updates the deal:

```text
Amount:
₹45,000

Stage:
Negotiation
```

The manager can now see that the salesperson has a ₹45,000 opportunity in negotiation.

---

# Step 10 — Deal Won

Rahul accepts the proposal.

The salesperson changes:

```text
Negotiation
     ↓
    Won
```

The CRM now records:

```text
Restaurant Website
₹45,000
Won
```

The entire customer journey is preserved in the CRM.

---

# 🧠 Why This Workflow Matters

The CRM doesn't simply store customer names.

It records the **entire sales journey**.

For example:

```text
Rahul contacted the company
        ↓
Salesperson called Rahul
        ↓
Follow-up was scheduled
        ↓
Follow-up completed
        ↓
Lead became qualified
        ↓
Lead became customer
        ↓
Customer meeting happened
        ↓
Deal created
        ↓
Deal negotiated
        ↓
Deal won
```

This gives the company context about what happened before, what is happening now, and what needs to happen next.

---

# 👥 Multi-User Architecture

SimpleCRM supports multiple salespeople working inside the same application.

Each CRM record has an owner.

```text
User
 │
 ├── Leads
 ├── Customers
 ├── Deals
 └── Activities
```

For example:

```text
Salesperson 1
│
├── Lead A
├── Customer A
├── Deal A
└── Activities A


Salesperson 2
│
├── Lead B
├── Customer B
├── Deal B
└── Activities B
```

Salesperson 1 does not automatically see Salesperson 2's records.

---

# 🔐 Authentication & Authorization

SimpleCRM uses Django's authentication system.

The general flow is:

```text
User
 ↓
Login
 ↓
Django Authentication
 ↓
Identify User
 ↓
Check Ownership / Access
 ↓
Show Appropriate CRM Data
```

A normal salesperson sees their own records.

Managers/Admins can access broader information according to their access level.

---

# 🗂️ Record Ownership

The major CRM models contain an owner relationship.

Conceptually:

```text
Lead
 └── owner → User

Customer
 └── owner → User

Deal
 └── owner → User

Activity
 └── owner → User
```

When a salesperson creates a record:

```text
Logged-in User
      ↓
Create Record
      ↓
owner = request.user
```

This allows the application to determine who is responsible for each sales record.

---

# 🔗 Database Relationships

The main relationships are:

```text
                     USER
                      │
          ┌───────────┼───────────┐
          │           │           │
          ▼           ▼           ▼
         LEAD      CUSTOMER      DEAL
          │           │           │
          │           └─────┬─────┘
          │                 │
          └───────┐         │
                  ▼         ▼
               ACTIVITY   DEAL
```

More specifically:

```text
Lead
 │
 └── converted_customer → Customer

Customer
 │
 ├── Deals
 └── Activities

Lead
 │
 └── Activities

User
 │
 ├── Leads
 ├── Customers
 ├── Deals
 └── Activities
```

These relationships allow the CRM to maintain the context of a customer's sales journey.

---

# 📊 Dashboard

The dashboard provides a quick overview of sales information.

Depending on the user's access level, it can show:

* Total leads
* Total customers
* Total deals
* Open deals
* Won revenue
* Recent activities

For a salesperson:

```text
MY SALES

Leads:          18
Customers:     12
Open Deals:     7
Won Revenue: ₹2,40,000
```

For a manager/admin, the dashboard can represent broader team/company information.

---

# 🧩 Main Modules

## Leads

Used to manage potential customers.

```text
Create
View
Edit
Delete
Search
Filter
Qualify
Convert
```

---

## Customers

Used to manage active customers.

```text
Create
View
Edit
Delete
Search
```

Customers can be connected to activities and deals.

---

## Activities

Used to record interactions and tasks.

```text
Call
Meeting
Note
Follow-up
```

Activities can be associated with:

```text
Lead
or
Customer
```

---

## Deals

Used to track sales opportunities.

A deal contains information such as:

```text
Deal Name
Customer
Amount
Stage
Expected Close Date
Owner
```

Stages represent the progress of a sale.

---

## Dashboard

Provides a high-level overview of sales activity and performance.

---

# 🏗️ Technical Architecture

SimpleCRM uses Django's traditional server-rendered architecture.

```text
                BROWSER
                   │
                   ▼
                 URLS
                   │
                   ▼
                VIEWS
                   │
                   ▼
           BUSINESS LOGIC
                   │
                   ▼
              DJANGO ORM
                   │
                   ▼
               DATABASE
                   │
                   ▼
               TEMPLATES
                   │
                   ▼
                 HTML
                   │
                   ▼
                BROWSER
```

The project does not use Django REST Framework.

The application uses Django's server-side rendering approach.

---

# 🛠️ Technology Stack

### Backend

* Python
* Django
* Django ORM

### Frontend

* Django Templates
* HTML
* Tailwind CSS

### Database

* SQLite for development

### Authentication

* Django Authentication

### Architecture

* Django MVT / traditional MVC-style application structure

---

# 📁 Project Structure

```text
crm/
│
├── crm/
│   ├── migrations/
│   ├── templates/
│   │
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🚀 Running the Project Locally

## 1. Clone the repository

```bash
git clone https://github.com/workstanmoy-stack/crm.git
```

Move into the project:

```bash
cd crm
```

---

## 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run database migrations

```bash
python manage.py migrate
```

---

## 5. Create an administrator

```bash
python manage.py createsuperuser
```

Follow Django's prompts to create the admin account.

---

## 6. Start the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

Admin panel:

```text
http://127.0.0.1:8000/admin/
```

---

# 🧪 Example Test Scenario

To test the multi-user functionality:

### User 1

Create:

```text
salesman1
```

Log in and create:

```text
Lead:
ABC Restaurant
```

### User 2

Create:

```text
salesman2
```

Log in as User 2.

User 2 should not see User 1's private CRM records.

This demonstrates record ownership and multi-user separation.

---

# 🔒 Security Model

The application uses Django authentication and ownership-based filtering.

The basic concept is:

```text
Salesperson
     ↓
Authenticated User
     ↓
Own CRM Records
```

The application checks ownership when accessing CRM records rather than relying only on the visibility of UI elements.

This prevents users from simply accessing another user's records by manually changing URLs.

---

# 📈 What This Project Demonstrates

This project demonstrates practical Django development concepts including:

* Django project structure
* Django models
* Database relationships
* Django ORM
* CRUD operations
* Server-rendered templates
* URL routing
* Form handling
* Authentication
* Authorization
* User ownership
* Business logic
* Query filtering
* Lead lifecycle management
* Customer management
* Sales pipeline management
* Multi-user applications
* Dashboard development

---

# 🚧 Future Improvements

SimpleCRM is intentionally kept as a simple CRM MVP.

Possible future improvements include:

* Advanced role and permission management
* Manager/team management interface
* Email notifications
* Automated follow-up reminders
* Calendar integration
* File attachments
* Import/export
* Pagination
* Advanced reporting
* Sales charts
* Audit logs
* Customer communication history
* Email integration
* REST API
* Mobile application
* Production deployment
* PostgreSQL support
* Automated backups

These features are outside the current MVP scope.

---

# 📌 Project Status

## SimpleCRM — MVP Complete

The current application implements the core CRM business workflow:

```text
Lead
 ↓
Contact
 ↓
Qualification
 ↓
Customer
 ↓
Activity
 ↓
Deal
 ↓
Negotiation
 ↓
Won / Lost
```

It also supports:

```text
Authentication
      +
Multi-user ownership
      +
CRM business logic
      +
Sales workflow
      +
Dashboard
```

---

# 🎓 Why This Project Was Built

SimpleCRM was built as a practical Django project to demonstrate how a business application can be designed around real-world workflows rather than simply creating isolated CRUD pages.

The goal was to understand how:

```text
Users
  ↓
Business Rules
  ↓
Database Relationships
  ↓
Permissions
  ↓
Sales Workflow
  ↓
User Interface
```

come together to form a complete business application.

This version is much better for a **GitHub portfolio** because someone who has never seen the project can understand the problem, the users, the complete sales lifecycle, the database relationships, the permissions model, the technical architecture, and the real-world use case just by reading the repository.
