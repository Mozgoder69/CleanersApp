""" tables.py """
import django_tables2 as tables
from general.core.models import Account, Address, Branch, Catalyst, Category, Customer, CustomerEmail, CustomerPhone, Employee, Factor, HarmfulFactor, HelpfulFactor, Journey, Material, Message, Method, MethodChem, MethodMech, Order, Package, Pollution, Premises, Problem, Process, Product, Referral, Request, Scenario, ScenarioOffsite, ScenarioOnsite, Solution, Stage, Symbol, Texture, Workflow

class AccountTable(tables.Table):
    class Meta:
        model = Account
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'

class AddressTable(tables.Table):
    class Meta:
        model = Address
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'

class BranchTable(tables.Table):
    class Meta:
        model = Branch
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'

class CatalystTable(tables.Table):
    class Meta:
        model = Catalyst
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'

class CategoryTable(tables.Table):
    class Meta:
        model = Category
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'

class CustomerTable(tables.Table):
    class Meta:
        model = Customer
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'

class CustomerEmailTable(tables.Table):
    class Meta:
        model = CustomerEmail
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'

class CustomerPhoneTable(tables.Table):
    class Meta:
        model = CustomerPhone
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'

class EmployeeTable(tables.Table):
    class Meta:
        model = Employee
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'

class FactorTable(tables.Table):
    class Meta:
        model = Factor
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'

class HarmfulFactorTable(tables.Table):
    class Meta:
        model = HarmfulFactor
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'

class HelpfulFactorTable(tables.Table):
    class Meta:
        model = HelpfulFactor
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'

class JourneyTable(tables.Table):
    class Meta:
        model = Journey
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'

class MaterialTable(tables.Table):
    class Meta:
        model = Material
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'

class MessageTable(tables.Table):
    class Meta:
        model = Message
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'

class MethodTable(tables.Table):
    class Meta:
        model = Method
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'

class MethodChemTable(tables.Table):
    class Meta:
        model = MethodChem
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'

class MethodMechTable(tables.Table):
    class Meta:
        model = MethodMech
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'

class OrderTable(tables.Table):
    class Meta:
        model = Order
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'

class PackageTable(tables.Table):
    class Meta:
        model = Package
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'

class PollutionTable(tables.Table):
    class Meta:
        model = Pollution
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'

class PremisesTable(tables.Table):
    class Meta:
        model = Premises
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'

class ProblemTable(tables.Table):
    class Meta:
        model = Problem
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'

class ProcessTable(tables.Table):
    class Meta:
        model = Process
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'

class ProductTable(tables.Table):
    class Meta:
        model = Product
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'

class ReferralTable(tables.Table):
    class Meta:
        model = Referral
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'

class RequestTable(tables.Table):
    class Meta:
        model = Request
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'

class ScenarioTable(tables.Table):
    class Meta:
        model = Scenario
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'

class ScenarioOffsiteTable(tables.Table):
    class Meta:
        model = ScenarioOffsite
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'

class ScenarioOnsiteTable(tables.Table):
    class Meta:
        model = ScenarioOnsite
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'

class SolutionTable(tables.Table):
    class Meta:
        model = Solution
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'

class StageTable(tables.Table):
    class Meta:
        model = Stage
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'

class SymbolTable(tables.Table):
    class Meta:
        model = Symbol
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'

class TextureTable(tables.Table):
    class Meta:
        model = Texture
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'

class WorkflowTable(tables.Table):
    class Meta:
        model = Workflow
        template_name = "django_tables2/bootstrap4.html"
        fields = '__all__'
