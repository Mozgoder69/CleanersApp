""" forms.py """
from django import forms
from general.core.models import Account, Address, Branch, Catalyst, Category, Customer, CustomerEmail, CustomerPhone, Employee, Factor, HarmfulFactor, HelpfulFactor, Journey, Material, Message, Method, MethodChem, MethodMech, Order, Package, Pollution, Premises, Problem, Process, Product, Referral, Request, Scenario, ScenarioOffsite, ScenarioOnsite, Solution, Stage, Symbol, Texture, Workflow

# ['field1', 'field2', 'field3', 'field4', 'field5', 'field6', 'field7', 'field8']
class AccountForm(forms.ModelForm):
    """ AccountForm """
    class Meta:
        """ ['employee', 'username', 'password'] """
        model = Account
        fields = '__all__'

class AddressForm(forms.ModelForm):
    """ AddressForm """
    class Meta:
        """ ['address_id', 'region', 'locality', 'District', 'street', 'house'] """
        model = Address
        fields = '__all__'

class BranchForm(forms.ModelForm):
    """ BranchForm """
    class Meta:
        """ ['address', 'name', 'is_active', 'opening_time', 'closing_time'] """
        model = Branch
        fields = '__all__'

class CatalystForm(forms.ModelForm):
    """ CatalystForm """
    class Meta:
        """ ['catalyst_id', 'username', 'factor'] """
        model = Catalyst
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    """ CategoryForm """
    class Meta:
        """ ['category_id', 'purpose', 'name', 'is_active', 'cost_base', 'term_rate'] """
        model = Category
        fields = '__all__'

class CustomerForm(forms.ModelForm):
    """ CustomerForm """
    class Meta:
        """ ['customer_id', 'first_name', 'last_name', 'birth_date'] """
        model = Customer
        fields = '__all__'

class CustomerEmailForm(forms.ModelForm):
    """ CustomerEmailForm """
    class Meta:
        """ ['email_id', 'customer', 'contact', 'is_active'] """
        model = CustomerEmail
        fields = '__all__'

class CustomerPhoneForm(forms.ModelForm):
    """ CustomerPhoneForm """
    class Meta:
        """ ['phone_id', 'customer', 'contact', 'is_active'] """
        model = CustomerPhone
        fields = '__all__'

class EmployeeForm(forms.ModelForm):
    """ EmployeeForm """
    class Meta:
        """ ['employee_id', 'customer', 'branch', 'position', 'signup_date', 'is_active'] """
        model = Employee
        fields = '__all__'

class FactorForm(forms.ModelForm):
    """ FactorForm """
    class Meta:
        """ ['factor_id', 'name', 'is_active'] """
        model = Factor
        fields = '__all__'

class HarmfulFactorForm(forms.ModelForm):
    """ HarmfulFactorForm """
    class Meta:
        """ ['harmful_id', 'material', 'factor'] """
        model = HarmfulFactor
        fields = '__all__'

class HelpfulFactorForm(forms.ModelForm):
    """ HelpfulFactorForm """
    class Meta:
        """ ['helpful_id', 'pollution', 'factor'] """
        model = HelpfulFactor
        fields = '__all__'

class JourneyForm(forms.ModelForm):
    """ JourneyForm """
    class Meta:
        """ ['journey_id', 'order', 'address', 'process'] """
        model = Journey
        fields = '__all__'

class MaterialForm(forms.ModelForm):
    """ MaterialForm """
    class Meta:
        """ ['material_id', 'source', 'name', 'is_active'] """
        model = Material
        fields = '__all__'

class MessageForm(forms.ModelForm):
    """ MessageForm """
    class Meta:
        """ ['message_id', 'customer', 'is_password', 'subject', 'event_time'] """
        model = Message
        fields = '__all__'

class MethodForm(forms.ModelForm):
    """ MethodForm """
    class Meta:
        """ ['method_id', 'stage', 'name', 'term_base', 'cost_rate', 'is_active'] """
        model = Method
        fields = '__all__'

class MethodChemForm(forms.ModelForm):
    """ MethodChemForm """
    class Meta:
        """ ['chem_id', 'items_count'] """
        model = MethodChem
        fields = '__all__'

class MethodMechForm(forms.ModelForm):
    """ MethodMechForm """
    class Meta:
        """ ['mech_id', 'is_occupied'] """
        model = MethodMech
        fields = '__all__'

class OrderForm(forms.ModelForm):
    """ OrderForm """
    class Meta:
        """ ['order_id', 'customer', 'process', 'paymethod'] """
        model = Order
        fields = '__all__'

class PackageForm(forms.ModelForm):
    """ PackageForm """
    class Meta:
        """ ['package_id', 'order', 'product', 'items_count'] """
        model = Package
        fields = '__all__'

class PollutionForm(forms.ModelForm):
    """ PollutionForm """
    class Meta:
        """ ['pollution_id', 'source', 'name', 'is_active'] """
        model = Pollution
        fields = '__all__'

class PremisesForm(forms.ModelForm):
    """ PremisesForm """
    class Meta:
        """ ['address', 'floor_num', 'flat_num', 'rooms_count', 'size', 'condition'] """
        model = Premises
        fields = '__all__'

class ProblemForm(forms.ModelForm):
    """ ProblemForm """
    class Meta:
        """ ['problem_id', 'product', 'pollution', 'is_old', 'is_removed'] """
        model = Problem
        fields = '__all__'

class ProcessForm(forms.ModelForm):
    """ ProcessForm """
    class Meta:
        """ ['process_id', 'opened_by', 'opened_at', 'status'] """
        model = Process
        fields = '__all__'

class ProductForm(forms.ModelForm):
    """ ProductForm """
    class Meta:
        """ ['product_id', 'category', 'agreed_price', 'color', 'size', 'condition'] """
        model = Product
        fields = '__all__'

class ReferralForm(forms.ModelForm):
    """ ReferralForm """
    class Meta:
        """ ['referral_id', 'product', 'symbol', 'is_crossedout', 'is_underlined', 'temperature'] """
        model = Referral
        fields = '__all__'

class RequestForm(forms.ModelForm):
    """ RequestForm """
    class Meta:
        """ ['request_id', 'process', 'action', 'object', 'subject'] """
        model = Request
        fields = '__all__'

class ScenarioForm(forms.ModelForm):
    """ ScenarioForm """
    class Meta:
        """ ['scenario_id', 'purpose', 'name', 'is_active'] """
        model = Scenario
        fields = '__all__'

class ScenarioOffsiteForm(forms.ModelForm):
    """ ScenarioOffsiteForm """
    class Meta:
        """ ['offsite_id', 'premises', 'scenario', 'rooms_left'] """
        model = ScenarioOffsite
        fields = '__all__'

class ScenarioOnsiteForm(forms.ModelForm):
    """ ScenarioOnsiteForm """
    class Meta:
        """ ['onsite_id', 'product', 'scenario', 'current_stage'] """
        model = ScenarioOnsite
        fields = '__all__'

class SolutionForm(forms.ModelForm):
    """ SolutionForm """
    class Meta:
        """ ['solution_id', 'scenario', 'method'] """
        model = Solution
        fields = '__all__'

class StageForm(forms.ModelForm):
    """ StageForm """
    class Meta:
        """ ['stage_id', 'priority', 'type', 'mode', 'name', 'is_active'] """
        model = Stage
        fields = '__all__'

class SymbolForm(forms.ModelForm):
    """ SymbolForm """
    class Meta:
        """ ['symbol_id', 'stage', 'specifics', 'is_active'] """
        model = Symbol
        fields = '__all__'

class TextureForm(forms.ModelForm):
    """ TextureForm """
    class Meta:
        """ ['texture_id', 'product', 'material', 'density', 'is_mix'] """
        model = Texture
        fields = '__all__'

class WorkflowForm(forms.ModelForm):
    """ WorkflowForm """
    class Meta:
        """ ['workflow_id', 'process', 'employee', 'event_time', 'result_status'] """
        model = Workflow
        fields = '__all__'
