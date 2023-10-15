""" views.py """
from django.shortcuts import render
# from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Account,     Address,     Branch,     Catalyst,     Category,     Customer,     CustomerEmail,      CustomerPhone,      Employee,     Factor,     HarmfulFactor,      HelpfulFactor,      Journey,      Material,     Message,      Method,     MethodChem,     MethodMech,     Order,      Package,      Pollution,      Premises,     Problem,      Process,      Product,      Referral,     Request,      Scenario,     ScenarioOffsite,      ScenarioOnsite,     Solution,     Stage,      Symbol,     Texture,      Workflow
from .forms import  AccountForm, AddressForm, BranchForm, CatalystForm, CategoryForm, CustomerForm, CustomerEmailForm,  CustomerPhoneForm,  EmployeeForm, FactorForm, HarmfulFactorForm,  HelpfulFactorForm,  JourneyForm,  MaterialForm, MessageForm,  MethodForm, MethodChemForm, MethodMechForm, OrderForm,  PackageForm,  PollutionForm,  PremisesForm, ProblemForm,  ProcessForm,  ProductForm,  ReferralForm, RequestForm,  ScenarioForm, ScenarioOffsiteForm,  ScenarioOnsiteForm, SolutionForm, StageForm,  SymbolForm, TextureForm,  WorkflowForm

def index(request):
    """ index """
    return render(request, 'main/index.html')

def about(request):
    """ about """
    return render(request, 'main/about.html')

class AccountCreateView(CreateView):
    """ AccountCreateView """
    model = Account
    form_class = AccountForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')

class AddressCreateView(CreateView):
    """ AddressCreateView """
    model = Address
    form_class = AddressForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')

class BranchCreateView(CreateView):
    """ BranchCreateView """
    model = Branch
    form_class = BranchForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')

class CatalystCreateView(CreateView):
    """ CatalystCreateView """
    model = Catalyst
    form_class = CatalystForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')

class CategoryCreateView(CreateView):
    """ CategoryCreateView """
    model = Category
    form_class = CategoryForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')

class CustomerCreateView(CreateView):
    """ CustomerCreateView """
    model = Customer
    form_class = CustomerForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')

class CustomerEmailCreateView(CreateView):
    """ CustomerEmailCreateView """
    model = CustomerEmail
    form_class = CustomerEmailForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')

class CustomerPhoneCreateView(CreateView):
    """ CustomerPhoneCreateView """
    model = CustomerPhone
    form_class = CustomerPhoneForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')

class EmployeeCreateView(CreateView):
    """ EmployeeCreateView """
    model = Employee
    form_class = EmployeeForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')

class FactorCreateView(CreateView):
    """ FactorCreateView """
    model = Factor
    form_class = FactorForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')

class HarmfulFactorCreateView(CreateView):
    """ HarmfulFactorCreateView """
    model = HarmfulFactor
    form_class = HarmfulFactorForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')

class HelpfulFactorCreateView(CreateView):
    """ HelpfulFactorCreateView """
    model = HelpfulFactor
    form_class = HelpfulFactorForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')

class JourneyCreateView(CreateView):
    """ JourneyCreateView """
    model = Journey
    form_class = JourneyForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')

class MaterialCreateView(CreateView):
    """ MaterialCreateView """
    model = Material
    form_class = MaterialForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')

class MessageCreateView(CreateView):
    """ MessageCreateView """
    model = Message
    form_class = MessageForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')

class MethodCreateView(CreateView):
    """ MethodCreateView """
    model = Method
    form_class = MethodForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')

class MethodChemCreateView(CreateView):
    """ MethodChemCreateView """
    model = MethodChem
    form_class = MethodChemForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')

class MethodMechCreateView(CreateView):
    """ MethodMechCreateView """
    model = MethodMech
    form_class = MethodMechForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')

class OrderCreateView(CreateView):
    """ OrderCreateView """
    model = Order
    form_class = OrderForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')

class PackageCreateView(CreateView):
    """ PackageCreateView """
    model = Package
    form_class = PackageForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')

class PollutionCreateView(CreateView):
    """ PollutionCreateView """
    model = Pollution
    form_class = PollutionForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')

class PremisesCreateView(CreateView):
    """ PremisesCreateView """
    model = Premises
    form_class = PremisesForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')

class ProblemCreateView(CreateView):
    """ ProblemCreateView """
    model = Problem
    form_class = ProblemForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')

class ProcessCreateView(CreateView):
    """ ProcessCreateView """
    model = Process
    form_class = ProcessForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')

class ProductCreateView(CreateView):
    """ ProductCreateView """
    model = Product
    form_class = ProductForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')

class ReferralCreateView(CreateView):
    """ ReferralCreateView """
    model = Referral
    form_class = ReferralForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')

class RequestCreateView(CreateView):
    """ RequestCreateView """
    model = Request
    form_class = RequestForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')

class ScenarioCreateView(CreateView):
    """ ScenarioCreateView """
    model = Scenario
    form_class = ScenarioForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')

class ScenarioOffsiteCreateView(CreateView):
    """ ScenarioOffsiteCreateView """
    model = ScenarioOffsite
    form_class = ScenarioOffsiteForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')

class ScenarioOnsiteCreateView(CreateView):
    """ ScenarioOnsiteCreateView """
    model = ScenarioOnsite
    form_class = ScenarioOnsiteForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')

class SolutionCreateView(CreateView):
    """ SolutionCreateView """
    model = Solution
    form_class = SolutionForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')

class StageCreateView(CreateView):
    """ StageCreateView """
    model = Stage
    form_class = StageForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')

class SymbolCreateView(CreateView):
    """ SymbolCreateView """
    model = Symbol
    form_class = SymbolForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')

class TextureCreateView(CreateView):
    """ TextureCreateView """
    model = Texture
    form_class = TextureForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')

class WorkflowCreateView(CreateView):
    """ WorkflowCreateView """
    model = Workflow
    form_class = WorkflowForm
    template_name = 'main/entity_form.html'
    success_url = reverse_lazy('success_page')
