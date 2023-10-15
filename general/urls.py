""" urls.py """
from django.contrib import admin
from django.urls import path, include
from general.core import views as core_views
from general.core.views import AccountCreateView, AddressCreateView, BranchCreateView, CatalystCreateView, CategoryCreateView, CustomerCreateView, CustomerEmailCreateView,  CustomerPhoneCreateView,  EmployeeCreateView, FactorCreateView, HarmfulFactorCreateView,  HelpfulFactorCreateView,  JourneyCreateView,  MessageCreateView,  MaterialCreateView, MethodCreateView, MethodChemCreateView, MethodMechCreateView, OrderCreateView,  PackageCreateView,  PollutionCreateView,  PremisesCreateView, ProblemCreateView,  ProcessCreateView,  ProductCreateView,  ReferralCreateView, RequestCreateView,  ScenarioCreateView, ScenarioOffsiteCreateView,  ScenarioOnsiteCreateView, SolutionCreateView, StageCreateView,  SymbolCreateView, TextureCreateView,  WorkflowCreateView

urlpatterns = [
    path("", core_views.index, name='home'),
    path('about', core_views.about, name='about'),
    # path('', include('general/urls')),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),



    path('add_account/', AccountCreateView.as_view(), name='add_account'),
    path('add_address/', AddressCreateView.as_view(), name='add_address'),
    path('add_branch/', BranchCreateView.as_view(), name='add_branch'),

    path('add_catalyst/', CatalystCreateView.as_view(), name='add_catalyst'),
    path('add_category/', CategoryCreateView.as_view(), name='add_category'),
    path('add_customer/', CustomerCreateView.as_view(), name='add_customer'),
    path('add_email/', CustomerEmailCreateView.as_view(), name='add_email'),
    path('add_phone/', CustomerPhoneCreateView.as_view(), name='add_phone'),

    path('add_employee/', EmployeeCreateView.as_view(), name='add_employee'),
    path('add_factor/', FactorCreateView.as_view(), name='add_factor'),
    path('add_harmful/', HarmfulFactorCreateView.as_view(), name='add_harmful'),
    path('add_helpful/', HelpfulFactorCreateView.as_view(), name='add_helpful'),
    path('add_journey/', JourneyCreateView.as_view(), name='add_journey'),
    path('add_message/', MessageCreateView.as_view(), name='add_message'),

    path('add_material/', MaterialCreateView.as_view(), name='add_material'),
    path('add_method/', MethodCreateView.as_view(), name='add_method'),
    path('add_chem/', MethodChemCreateView.as_view(), name='add_chem'),
    path('add_mech/', MethodMechCreateView.as_view(), name='add_mech'),
    path('add_order/', OrderCreateView.as_view(), name='add_order'),
    path('add_package/', PackageCreateView.as_view(), name='add_package'),
    path('add_pollution/', PollutionCreateView.as_view(), name='add_pollution'),

    path('add_premises/', PremisesCreateView.as_view(), name='add_premises'),
    path('add_problem/', ProblemCreateView.as_view(), name='add_problem'),
    path('add_process/', ProcessCreateView.as_view(), name='add_process'),
    path('add_product/', ProductCreateView.as_view(), name='add_product'),
    path('add_referral/', ReferralCreateView.as_view(), name='add_referral'),
    path('add_request/', RequestCreateView.as_view(), name='add_request'),
    path('add_scenario/', ScenarioCreateView.as_view(), name='add_scenario'),

    path('add_offsite/', ScenarioOffsiteCreateView.as_view(), name='add_offsite'),
    path('add_onsite/', ScenarioOnsiteCreateView.as_view(), name='add_onsite'),
    path('add_solution/', SolutionCreateView.as_view(), name='add_solution'),
    path('add_stage/', StageCreateView.as_view(), name='add_stage'),
    path('add_symbol/', SymbolCreateView.as_view(), name='add_symbol'),
    path('add_texture/', TextureCreateView.as_view(), name='add_texture'),
    path('add_workflow/', WorkflowCreateView.as_view(), name='add_workflow'),
]
