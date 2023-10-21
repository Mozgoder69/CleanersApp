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
        widgets = {
            'employee': forms.Select(attrs={'class': 'form-select'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'})
        }

class AddressForm(forms.ModelForm):
    """ AddressForm """
    class Meta:
        """ ['address_id', 'region', 'locality', 'district', 'street', 'house'] """
        model = Address
        fields = '__all__'
        widgets = {
            # 'address_id': forms.Select(attrs={'class': 'form-select'}),
            'region': forms.TextInput(attrs={'class': 'form-control'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'house': forms.TextInput(attrs={'class': 'form-control'})
        }

class BranchForm(forms.ModelForm):
    """ BranchForm """
    class Meta:
        """ ['address', 'name', 'is_active', 'opening_time', 'closing_time'] """
        model = Branch
        fields = '__all__'
        widgets = {
            'address': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'opening_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'closing_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

class CatalystForm(forms.ModelForm):
    """ CatalystForm """
    class Meta:
        """ ['catalyst_id', 'stage', 'factor'] """
        model = Catalyst
        fields = '__all__'
        widgets = {
            # 'catalyst_id': forms.Select(attrs={'class': 'form-select'}),
            'stage': forms.Select(attrs={'class': 'form-select'}),
            'factor': forms.Select(attrs={'class': 'form-select'})
        }

class CategoryForm(forms.ModelForm):
    """ CategoryForm """
    class Meta:
        """ ['category_id', 'purpose', 'name', 'is_active', 'cost_base', 'term_rate'] """
        model = Category
        fields = '__all__'
        widgets = {
            # 'category_id': forms.Select(attrs={'class': 'form-select'}),
            'purpose': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'cost_base': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'term_rate': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-control'})
        }

class CustomerForm(forms.ModelForm):
    """ CustomerForm """
    class Meta:
        """ ['customer_id', 'first_name', 'last_name', 'birth_date'] """
        model = Customer
        fields = '__all__'
        widgets = {
            # 'customer_id': forms.Select(attrs={'class': 'form-select'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }

class CustomerEmailForm(forms.ModelForm):
    """ CustomerEmailForm """
    class Meta:
        """ ['email_id', 'customer', 'contact', 'is_active'] """
        model = CustomerEmail
        fields = '__all__'
        widgets = {
            # 'email_id': forms.Select(attrs={'class': 'form-select'}),
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-control'})
        }

class CustomerPhoneForm(forms.ModelForm):
    """ CustomerPhoneForm """
    class Meta:
        """ ['phone_id', 'customer', 'contact', 'is_active'] """
        model = CustomerPhone
        fields = '__all__'
        widgets = {
            # 'phone_id': forms.Select(attrs={'class': 'form-select'}),
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-control'})
        }

class EmployeeForm(forms.ModelForm):
    """ EmployeeForm """
    class Meta:
        """ ['employee_id', 'customer', 'branch', 'position', 'signup_date', 'is_active'] """
        model = Employee
        fields = '__all__'
        widgets = {
            # 'employee_id': forms.Select(attrs={'class': 'form-select'}),
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'branch': forms.Select(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'signup_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }

class FactorForm(forms.ModelForm):
    """ FactorForm """
    class Meta:
        """ ['factor_id', 'name', 'is_active'] """
        model = Factor
        fields = '__all__'
        widgets = {
            # 'factor_id': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-control'})
        }

class HarmfulFactorForm(forms.ModelForm):
    """ HarmfulFactorForm """
    class Meta:
        """ ['harmful_id', 'material', 'factor'] """
        model = HarmfulFactor
        fields = '__all__'
        widgets = {
            # 'harmful_id': forms.Select(attrs={'class': 'form-select'}),
            'material': forms.Select(attrs={'class': 'form-control'}),
            'factor': forms.Select(attrs={'class': 'form-control'})
        }

class HelpfulFactorForm(forms.ModelForm):
    """ HelpfulFactorForm """
    class Meta:
        """ ['helpful_id', 'pollution', 'factor'] """
        model = HelpfulFactor
        fields = '__all__'
        widgets = {
            # 'helpful_id': forms.Select(attrs={'class': 'form-select'}),
            'pollution': forms.Select(attrs={'class': 'form-control'}),
            'factor': forms.Select(attrs={'class': 'form-control'})
        }

class JourneyForm(forms.ModelForm):
    """ JourneyForm """
    class Meta:
        """ ['journey_id', 'order', 'address', 'process'] """
        model = Journey
        fields = '__all__'
        widgets = {
            # 'journey_id': forms.Select(attrs={'class': 'form-select'}),
            'order': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.Select(attrs={'class': 'form-control'}),
            'process': forms.Select(attrs={'class': 'form-control'})
        }

class MaterialForm(forms.ModelForm):
    """ MaterialForm """
    class Meta:
        """ ['material_id', 'source', 'name', 'is_active'] """
        model = Material
        fields = '__all__'
        widgets = {
            # 'material_id': forms.Select(attrs={'class': 'form-select'}),
            'source': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-control'})
        }

class MessageForm(forms.ModelForm):
    """ MessageForm """
    class Meta:
        """ ['message_id', 'customer', 'is_password', 'subject', 'event_time'] """
        model = Message
        fields = '__all__'
        widgets = {
            # 'message_id': forms.Select(attrs={'class': 'form-select'}),
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'is_password': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'event_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'event_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'})
        }

class MethodForm(forms.ModelForm):
    """ MethodForm """
    class Meta:
        """ ['method_id', 'stage', 'name', 'term_base', 'cost_rate', 'is_active'] """
        model = Method
        fields = '__all__'
        widgets = {
            # 'method_id': forms.Select(attrs={'class': 'form-select'}),
            'stage': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'term_base': forms.NumberInput(attrs={'class': 'form-control'}),
            'cost_rate': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-control'})
        }

class MethodChemForm(forms.ModelForm):
    """ MethodChemForm """
    class Meta:
        """ ['chem_id', 'items_count'] """
        model = MethodChem
        fields = '__all__'
        widgets = {
            # 'chem_id': forms.Select(attrs={'class': 'form-select'}),
            'items_count': forms.NumberInput(attrs={'class': 'form-control'})
        }

class MethodMechForm(forms.ModelForm):
    """ MethodMechForm """
    class Meta:
        """ ['mech_id', 'is_occupied'] """
        model = MethodMech
        fields = '__all__'
        widgets = {
            # 'mech_id': forms.Select(attrs={'class': 'form-select'}),
            'is_occupied': forms.CheckboxInput(attrs={'class': 'form-control'})
        }

class OrderForm(forms.ModelForm):
    """ OrderForm """
    class Meta:
        """ ['order_id', 'customer', 'process', 'paymethod'] """
        model = Order
        fields = '__all__'
        widgets = {
            # 'order_id': forms.Select(attrs={'class': 'form-select'}),
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'process': forms.Select(attrs={'class': 'form-control'}),
            'paymethod': forms.TextInput(attrs={'class': 'form-control'})
        }

class PackageForm(forms.ModelForm):
    """ PackageForm """
    class Meta:
        """ ['package_id', 'order', 'product', 'items_count'] """
        model = Package
        fields = '__all__'
        widgets = {
            # 'package_id': forms.Select(attrs={'class': 'form-select'}),
            'order': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'items_count': forms.NumberInput(attrs={'class': 'form-control'})
        }

class PollutionForm(forms.ModelForm):
    """ PollutionForm """
    class Meta:
        """ ['pollution_id', 'source', 'name', 'is_active'] """
        model = Pollution
        fields = '__all__'
        widgets = {
            # 'pollution_id': forms.Select(attrs={'class': 'form-select'}),
            'source': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-control'})
        }

class PremisesForm(forms.ModelForm):
    """ PremisesForm """
    class Meta:
        """ ['address', 'floor_num', 'flat_num', 'rooms_count', 'size', 'condition'] """
        model = Premises
        fields = '__all__'
        widgets = {
            # 'address': forms.Select(attrs={'class': 'form-select'}),
            'floor_num': forms.NumberInput(attrs={'class': 'form-control'}),
            'flat_num': forms.NumberInput(attrs={'class': 'form-control'}),
            'rooms_count': forms.NumberInput(attrs={'class': 'form-control'}),
            'size': forms.TextInput(attrs={'class': 'form-control'}),
            'condition': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProblemForm(forms.ModelForm):
    """ ProblemForm """
    class Meta:
        """ ['problem_id', 'product', 'pollution', 'is_old', 'is_removed'] """
        model = Problem
        fields = '__all__'
        widgets = {
            # 'problem_id': forms.Select(attrs={'class': 'form-select'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'pollution': forms.Select(attrs={'class': 'form-control'}),
            'is_old': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'is_removed': forms.CheckboxInput(attrs={'class': 'form-control'})
        }

class ProcessForm(forms.ModelForm):
    """ ProcessForm """
    class Meta:
        """ ['process_id', 'opened_by', 'opened_at', 'status'] """
        model = Process
        fields = '__all__'
        widgets = {
            # 'process_id': forms.Select(attrs={'class': 'form-select'}),
            'opened_by': forms.Select(attrs={'class': 'form-control'}),
            'opened_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'opened_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'status': forms.TextInput(attrs={'class': 'form-control'})
        }

class ProductForm(forms.ModelForm):
    """ ProductForm """
    class Meta:
        """ ['product_id', 'category', 'agreed_price', 'color', 'size', 'condition'] """
        model = Product
        fields = '__all__'
        widgets = {
            # 'product_id': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'agreed_price': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.TextInput(attrs={'class': 'form-control'}),
            'condition': forms.TextInput(attrs={'class': 'form-control'})
        }

class ReferralForm(forms.ModelForm):
    """ ReferralForm """
    class Meta:
        """ ['referral_id', 'product', 'symbol', 'is_crossedout', 'is_underlined', 'temperature'] """
        model = Referral
        fields = '__all__'
        widgets = {
            # 'referral_id': forms.Select(attrs={'class': 'form-select'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'symbol': forms.Select(attrs={'class': 'form-control'}),
            'is_crossedout': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'is_underlined': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'temperature': forms.TextInput(attrs={'class': 'form-control'})
        }

class RequestForm(forms.ModelForm):
    """ RequestForm """
    class Meta:
        """ ['request_id', 'process', 'action', 'object', 'subject'] """
        model = Request
        fields = '__all__'
        widgets = {
            # 'request_id': forms.Select(attrs={'class': 'form-select'}),
            'process': forms.Select(attrs={'class': 'form-control'}),
            'action': forms.TextInput(attrs={'class': 'form-control'}),
            'object': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'})
        }

class ScenarioForm(forms.ModelForm):
    """ ScenarioForm """
    class Meta:
        """ ['scenario_id', 'purpose', 'name', 'is_active'] """
        model = Scenario
        fields = '__all__'
        widgets = {
            # 'scenario_id': forms.Select(attrs={'class': 'form-select'}),
            'purpose': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-control'})
        }

class ScenarioOffsiteForm(forms.ModelForm):
    """ ScenarioOffsiteForm """
    class Meta:
        """ ['offsite_id', 'premises', 'scenario', 'rooms_left'] """
        model = ScenarioOffsite
        fields = '__all__'
        widgets = {
            # 'offsite_id': forms.Select(attrs={'class': 'form-select'}),
            'premises': forms.Select(attrs={'class': 'form-control'}),
            'scenario': forms.Select(attrs={'class': 'form-control'}),
            'rooms_left': forms.NumberInput(attrs={'class': 'form-control'})
        }

class ScenarioOnsiteForm(forms.ModelForm):
    """ ScenarioOnsiteForm """
    class Meta:
        """ ['onsite_id', 'product', 'scenario', 'current_stage'] """
        model = ScenarioOnsite
        fields = '__all__'
        widgets = {
            # 'onsite_id': forms.Select(attrs={'class': 'form-select'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'scenario': forms.Select(attrs={'class': 'form-control'}),
            'current_stage': forms.Select(attrs={'class': 'form-control'})
        }

class SolutionForm(forms.ModelForm):
    """ SolutionForm """
    class Meta:
        """ ['solution_id', 'scenario', 'method'] """
        model = Solution
        fields = '__all__'
        widgets = {
            # 'solution_id': forms.Select(attrs={'class': 'form-select'}),
            'scenario': forms.Select(attrs={'class': 'form-control'}),
            'method': forms.Select(attrs={'class': 'form-control'})
        }

class StageForm(forms.ModelForm):
    """ StageForm """
    class Meta:
        """ ['stage_id', 'priority', 'type', 'mode', 'name', 'is_active'] """
        model = Stage
        fields = '__all__'
        widgets = {
            # 'stage_id': forms.Select(attrs={'class': 'form-select'}),
            'priority': forms.NumberInput(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'mode': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }

class SymbolForm(forms.ModelForm):
    """ SymbolForm """
    class Meta:
        """ ['symbol_id', 'stage', 'specifics', 'is_active'] """
        model = Symbol
        fields = '__all__'
        widgets = {
            # 'symbol_id': forms.Select(attrs={'class': 'form-select'}),
            'stage': forms.Select(attrs={'class': 'form-control'}),
            'specifics': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-control'})
        }

class TextureForm(forms.ModelForm):
    """ TextureForm """
    class Meta:
        """ ['texture_id', 'product', 'material', 'density', 'is_mix'] """
        model = Texture
        fields = '__all__'
        widgets = {
            # 'texture_id': forms.Select(attrs={'class': 'form-select'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'material': forms.Select(attrs={'class': 'form-control'}),
            'density': forms.TextInput(attrs={'class': 'form-control'}),
            'is_mix': forms.CheckboxInput(attrs={'class': 'form-control'})
        }

class WorkflowForm(forms.ModelForm):
    """ WorkflowForm """
    class Meta:
        """ ['workflow_id', 'process', 'employee', 'event_time', 'result_status'] """
        model = Workflow
        fields = '__all__'
        widgets = {
            # 'workflow_id': forms.Select(attrs={'class': 'form-select'}),
            'process': forms.Select(attrs={'class': 'form-control'}),
            'employee': forms.Select(attrs={'class': 'form-control'}),
            'event_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'event_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'result_status': forms.TextInput(attrs={'class': 'form-control'})
        }
