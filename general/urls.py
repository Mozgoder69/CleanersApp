""" urls.py """
from django.contrib import admin
from django.urls import path, include
from general.core import views as core_views
from general.core.views import AccountCreateView, AddressCreateView, BranchCreateView, CatalystCreateView, CategoryCreateView, CustomerCreateView, CustomerEmailCreateView,  CustomerPhoneCreateView,  EmployeeCreateView, FactorCreateView, HarmfulFactorCreateView,  HelpfulFactorCreateView,  JourneyCreateView,  MessageCreateView,  MaterialCreateView, MethodCreateView, MethodChemCreateView, MethodMechCreateView, OrderCreateView,  PackageCreateView,  PollutionCreateView,  PremisesCreateView, ProblemCreateView,  ProcessCreateView,  ProductCreateView,  ReferralCreateView, RequestCreateView,  ScenarioCreateView, ScenarioOffsiteCreateView,  ScenarioOnsiteCreateView, SolutionCreateView, StageCreateView,  SymbolCreateView, TextureCreateView,  WorkflowCreateView
from general.core.tabviews  import AccountListView, AddressListView, BranchListView, CatalystListView, CategoryListView, CustomerListView, CustomerEmailListView,  CustomerPhoneListView,  EmployeeListView, FactorListView, HarmfulFactorListView,  HelpfulFactorListView,  JourneyListView,  MaterialListView, MessageListView,  MethodListView, MethodChemListView, MethodMechListView, OrderListView,  PackageListView,  PollutionListView,  PremisesListView, ProblemListView,  ProcessListView,  ProductListView,  ReferralListView, RequestListView,  ScenarioListView, ScenarioOffsiteListView,  ScenarioOnsiteListView, SolutionListView, StageListView,  SymbolListView, TextureListView,  WorkflowListView

urlpatterns = [
    path("", core_views.index, name='home'),
    path('about', core_views.about, name='about'),
    # path('', include('general/urls')),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),


    path('add_account/',    AccountCreateView.as_view(),            name='add_account'),
    path('add_address/',    AddressCreateView.as_view(),            name='add_address'),
    path('add_branch/',     BranchCreateView.as_view(),             name='add_branch'),

    path('add_catalyst/',   CatalystCreateView.as_view(),           name='add_catalyst'),
    path('add_category/',   CategoryCreateView.as_view(),           name='add_category'),
    path('add_customer/',   CustomerCreateView.as_view(),           name='add_customer'),
    path('add_email/',      CustomerEmailCreateView.as_view(),      name='add_email'),
    path('add_phone/',      CustomerPhoneCreateView.as_view(),      name='add_phone'),

    path('add_employee/',   EmployeeCreateView.as_view(),           name='add_employee'),
    path('add_factor/',     FactorCreateView.as_view(),             name='add_factor'),
    path('add_harmful/',    HarmfulFactorCreateView.as_view(),      name='add_harmful'),
    path('add_helpful/',    HelpfulFactorCreateView.as_view(),      name='add_helpful'),
    path('add_journey/',    JourneyCreateView.as_view(),            name='add_journey'),
    path('add_message/',    MessageCreateView.as_view(),            name='add_message'),

    path('add_material/',   MaterialCreateView.as_view(),           name='add_material'),
    path('add_method/',     MethodCreateView.as_view(),             name='add_method'),
    path('add_chem/',       MethodChemCreateView.as_view(),         name='add_chem'),
    path('add_mech/',       MethodMechCreateView.as_view(),         name='add_mech'),
    path('add_order/',      OrderCreateView.as_view(),              name='add_order'),
    path('add_package/',    PackageCreateView.as_view(),            name='add_package'),
    path('add_pollution/',  PollutionCreateView.as_view(),          name='add_pollution'),

    path('add_premises/',   PremisesCreateView.as_view(),           name='add_premises'),
    path('add_problem/',    ProblemCreateView.as_view(),            name='add_problem'),
    path('add_process/',    ProcessCreateView.as_view(),            name='add_process'),
    path('add_product/',    ProductCreateView.as_view(),            name='add_product'),
    path('add_referral/',   ReferralCreateView.as_view(),           name='add_referral'),
    path('add_request/',    RequestCreateView.as_view(),            name='add_request'),
    path('add_scenario/',   ScenarioCreateView.as_view(),           name='add_scenario'),

    path('add_offsite/',    ScenarioOffsiteCreateView.as_view(),    name='add_offsite'),
    path('add_onsite/',     ScenarioOnsiteCreateView.as_view(),     name='add_onsite'),
    path('add_solution/',   SolutionCreateView.as_view(),           name='add_solution'),
    path('add_stage/',      StageCreateView.as_view(),              name='add_stage'),
    path('add_symbol/',     SymbolCreateView.as_view(),             name='add_symbol'),
    path('add_texture/',    TextureCreateView.as_view(),            name='add_texture'),
    path('add_workflow/',   WorkflowCreateView.as_view(),           name='add_workflow'),

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    path('view_account/',   AccountListView.as_view(),            name='view_account'),
    path('view_address/',   AddressListView.as_view(),            name='view_address'),
    path('view_branch/',    BranchListView.as_view(),             name='view_branch'),

    path('view_catalyst/',  CatalystListView.as_view(),           name='view_catalyst'),
    path('view_category/',  CategoryListView.as_view(),           name='view_category'),
    path('view_customer/',  CustomerListView.as_view(),           name='view_customer'),
    path('view_email/',     CustomerEmailListView.as_view(),      name='view_email'),
    path('view_phone/',     CustomerPhoneListView.as_view(),      name='view_phone'),

    path('view_employee/',  EmployeeListView.as_view(),           name='view_employee'),
    path('view_factor/',    FactorListView.as_view(),             name='view_factor'),
    path('view_harmful/',   HarmfulFactorListView.as_view(),      name='view_harmful'),
    path('view_helpful/',   HelpfulFactorListView.as_view(),      name='view_helpful'),
    path('view_journey/',   JourneyListView.as_view(),            name='view_journey'),
    path('view_message/',   MessageListView.as_view(),            name='view_message'),

    path('view_material/',  MaterialListView.as_view(),           name='view_material'),
    path('view_method/',    MethodListView.as_view(),             name='view_method'),
    path('view_chem/',      MethodChemListView.as_view(),         name='view_chem'),
    path('view_mech/',      MethodMechListView.as_view(),         name='view_mech'),
    path('view_order/',     OrderListView.as_view(),              name='view_order'),
    path('view_package/',   PackageListView.as_view(),            name='view_package'),
    path('view_pollution/', PollutionListView.as_view(),          name='view_pollution'),

    path('view_premises/',  PremisesListView.as_view(),           name='view_premises'),
    path('view_problem/',   ProblemListView.as_view(),            name='view_problem'),
    path('view_process/',   ProcessListView.as_view(),            name='view_process'),
    path('view_product/',   ProductListView.as_view(),            name='view_product'),
    path('view_referral/',  ReferralListView.as_view(),           name='view_referral'),
    path('view_request/',   RequestListView.as_view(),            name='view_request'),
    path('view_scenario/',  ScenarioListView.as_view(),           name='view_scenario'),

    path('view_offsite/',   ScenarioOffsiteListView.as_view(),    name='view_offsite'),
    path('view_onsite/',    ScenarioOnsiteListView.as_view(),     name='view_onsite'),
    path('view_solution/',  SolutionListView.as_view(),           name='view_solution'),
    path('view_stage/',     StageListView.as_view(),              name='view_stage'),
    path('view_symbol/',    SymbolListView.as_view(),             name='view_symbol'),
    path('view_texture/',   TextureListView.as_view(),            name='view_texture'),
    path('view_workflow/',  WorkflowListView.as_view(),           name='view_workflow')
]
