""" tabviews.py """
from django_tables2 import SingleTableView
from general.core.models import Account,     Address,     Branch,     Catalyst,     Category,     Customer,     CustomerEmail,      CustomerPhone,      Employee,     Factor,     HarmfulFactor,      HelpfulFactor,      Journey,      Material,     Message,      Method,     MethodChem,     MethodMech,     Order,      Package,      Pollution,      Premises,     Problem,      Process,      Product,      Referral,     Request,      Scenario,     ScenarioOffsite,      ScenarioOnsite,     Solution,     Stage,      Symbol,     Texture,      Workflow
from general.core.tables  import AccountTable, AddressTable, BranchTable, CatalystTable, CategoryTable, CustomerTable, CustomerEmailTable,  CustomerPhoneTable,  EmployeeTable, FactorTable, HarmfulFactorTable,  HelpfulFactorTable,  JourneyTable,  MaterialTable, MessageTable,  MethodTable, MethodChemTable, MethodMechTable, OrderTable,  PackageTable,  PollutionTable,  PremisesTable, ProblemTable,  ProcessTable,  ProductTable,  ReferralTable, RequestTable,  ScenarioTable, ScenarioOffsiteTable,  ScenarioOnsiteTable, SolutionTable, StageTable,  SymbolTable, TextureTable,  WorkflowTable

class AccountListView(SingleTableView):
    model = Account
    table_class = AccountTable
    template_name = 'table_form.html'

class AddressListView(SingleTableView):
    model = Address
    table_class = AddressTable
    template_name = 'table_form.html'

class BranchListView(SingleTableView):
    model = Branch
    table_class = BranchTable
    template_name = 'table_form.html'

class CatalystListView(SingleTableView):
    model = Catalyst
    table_class = CatalystTable
    template_name = 'table_form.html'

class CategoryListView(SingleTableView):
    model = Category
    table_class = CategoryTable
    template_name = 'table_form.html'

class CustomerListView(SingleTableView):
    model = Customer
    table_class = CustomerTable
    template_name = 'table_form.html'

class CustomerEmailListView(SingleTableView):
    model = CustomerEmail
    table_class = CustomerEmailTable
    template_name = 'table_form.html'

class CustomerPhoneListView(SingleTableView):
    model = CustomerPhone
    table_class = CustomerPhoneTable
    template_name = 'table_form.html'

class EmployeeListView(SingleTableView):
    model = Employee
    table_class = EmployeeTable
    template_name = 'table_form.html'

class FactorListView(SingleTableView):
    model = Factor
    table_class = FactorTable
    template_name = 'table_form.html'

class HarmfulFactorListView(SingleTableView):
    model = HarmfulFactor
    table_class = HarmfulFactorTable
    template_name = 'table_form.html'

class HelpfulFactorListView(SingleTableView):
    model = HelpfulFactor
    table_class = HelpfulFactorTable
    template_name = 'table_form.html'

class JourneyListView(SingleTableView):
    model = Journey
    table_class = JourneyTable
    template_name = 'table_form.html'

class MaterialListView(SingleTableView):
    model = Material
    table_class = MaterialTable
    template_name = 'table_form.html'

class MessageListView(SingleTableView):
    model = Message
    table_class = MessageTable
    template_name = 'table_form.html'

class MethodListView(SingleTableView):
    model = Method
    table_class = MethodTable
    template_name = 'table_form.html'

class MethodChemListView(SingleTableView):
    model = MethodChem
    table_class = MethodChemTable
    template_name = 'table_form.html'

class MethodMechListView(SingleTableView):
    model = MethodMech
    table_class = MethodMechTable
    template_name = 'table_form.html'

class OrderListView(SingleTableView):
    model = Order
    table_class = OrderTable
    template_name = 'table_form.html'

class PackageListView(SingleTableView):
    model = Package
    table_class = PackageTable
    template_name = 'table_form.html'

class PollutionListView(SingleTableView):
    model = Pollution
    table_class = PollutionTable
    template_name = 'table_form.html'

class PremisesListView(SingleTableView):
    model = Premises
    table_class = PremisesTable
    template_name = 'table_form.html'

class ProblemListView(SingleTableView):
    model = Problem
    table_class = ProblemTable
    template_name = 'table_form.html'

class ProcessListView(SingleTableView):
    model = Process
    table_class = ProcessTable
    template_name = 'table_form.html'

class ProductListView(SingleTableView):
    model = Product
    table_class = ProductTable
    template_name = 'table_form.html'

class ReferralListView(SingleTableView):
    model = Referral
    table_class = ReferralTable
    template_name = 'table_form.html'

class RequestListView(SingleTableView):
    model = Request
    table_class = RequestTable
    template_name = 'table_form.html'

class ScenarioListView(SingleTableView):
    model = Scenario
    table_class = ScenarioTable
    template_name = 'table_form.html'

class ScenarioOffsiteListView(SingleTableView):
    model = ScenarioOffsite
    table_class = ScenarioOffsiteTable
    template_name = 'table_form.html'

class ScenarioOnsiteListView(SingleTableView):
    model = ScenarioOnsite
    table_class = ScenarioOnsiteTable
    template_name = 'table_form.html'

class SolutionListView(SingleTableView):
    model = Solution
    table_class = SolutionTable
    template_name = 'table_form.html'

class StageListView(SingleTableView):
    model = Stage
    table_class = StageTable
    template_name = 'table_form.html'

class SymbolListView(SingleTableView):
    model = Symbol
    table_class = SymbolTable
    template_name = 'table_form.html'

class TextureListView(SingleTableView):
    model = Texture
    table_class = TextureTable
    template_name = 'table_form.html'

class WorkflowListView(SingleTableView):
    model = Workflow
    table_class = WorkflowTable
    template_name = 'table_form.html'

