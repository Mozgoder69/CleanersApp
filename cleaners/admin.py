""" admin.py """
from django.contrib import admin
from .models import Account, Address, Branch, Catalyst, Category, Customer, CustomerEmail, CustomerPhone, Employee, Factor, HarmfulFactor, HelpfulFactor, Journey, Material, Message, Method, MethodChem, MethodMech, Order, Package, Pollution, Premises, Problem, Process, Product, Referral, Request, Scenario, ScenarioOffsite, ScenarioOnsite, Solution, Stage, Symbol, Texture, Workflow

models = [
    Account, Address, Branch, Catalyst, Category,
    Customer, CustomerEmail, CustomerPhone, Employee,
    Factor, HarmfulFactor, HelpfulFactor, Journey, Material,
    Message, Method, MethodChem, MethodMech, Order, Package,
    Pollution, Premises, Problem, Process, Product, Referral,
    Request, Scenario, ScenarioOffsite, ScenarioOnsite,
    Solution, Stage, Symbol, Texture, Workflow ]
for model in models:
    admin.site.register(model)
