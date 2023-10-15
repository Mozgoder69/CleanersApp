""" models.py """
from django.db import models


class Account(models.Model):
    """ Account """
    employee = models.OneToOneField('Employee', models.DO_NOTHING, primary_key=True)
    username = models.TextField(unique=True)
    password = models.TextField(blank=True, null=True)

    class Meta:
        """ Account Meta """
        managed = False
        db_table = 'account'
        db_table_comment = 'employee private info'


class Address(models.Model):
    """ Address """
    address_id = models.AutoField(primary_key=True)
    region = models.TextField()
    locality = models.TextField()
    district = models.TextField()
    street = models.TextField()
    house = models.TextField()

    class Meta:
        """ Address Meta """
        managed = False
        db_table = 'address'


class Branch(models.Model):
    """ Branch """
    address = models.OneToOneField(Address, models.DO_NOTHING, primary_key=True)
    name = models.TextField(unique=True)
    is_active = models.BooleanField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    class Meta:
        """ Branch Meta """
        managed = False
        db_table = 'branch'


class Catalyst(models.Model):
    """ Catalyst """
    stage = models.ForeignKey('Stage', models.DO_NOTHING)
    factor = models.ForeignKey('Factor', models.DO_NOTHING)
    catalyst_id = models.IntegerField(primary_key=True)

    class Meta:
        """ Catalyst Meta """
        managed = False
        db_table = 'catalyst'
        unique_together = (('stage', 'factor'),)
        db_table_comment = 'relation: stage - factor'


class Category(models.Model):
    """ Category """
    category_id = models.AutoField(primary_key=True)
    purpose = models.TextField()  # This field type is a guess.
    cost_base = models.DecimalField(max_digits=65535, decimal_places=65535)
    name = models.TextField(unique=True)
    is_active = models.BooleanField()
    term_rate = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        """ Category Meta """
        managed = False
        db_table = 'category'


class Customer(models.Model):
    """ Customer """
    first_name = models.TextField()
    last_name = models.TextField()
    birth_date = models.DateField()
    customer_id = models.AutoField(primary_key=True)

    class Meta:
        """ Customer Meta """
        managed = False
        db_table = 'customer'
        unique_together = (('first_name', 'last_name'),)


class CustomerEmail(models.Model):
    """ CustomerEmail """
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    contact = models.TextField(unique=True)
    is_active = models.BooleanField()
    email_id = models.IntegerField(primary_key=True)

    class Meta:
        """ CustomerEmail Meta """
        managed = False
        db_table = 'customer_email'


class CustomerPhone(models.Model):
    """ CustomerPhone """
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    contact = models.TextField(unique=True)
    is_active = models.BooleanField()
    phone_id = models.IntegerField(primary_key=True)

    class Meta:
        """ CustomerPhone Meta """
        managed = False
        db_table = 'customer_phone'


class Employee(models.Model):
    """ Employee """
    employee_id = models.AutoField(primary_key=True)
    position = models.TextField()  # This field type is a guess.
    signup_date = models.DateField()
    is_active = models.BooleanField()
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)

    class Meta:
        """ Employee Meta """
        managed = False
        db_table = 'employee'
        db_table_comment = 'relation: customer - branch'


class Factor(models.Model):
    """ Factor """
    factor_id = models.AutoField(primary_key=True)
    name = models.TextField(unique=True)
    is_active = models.BooleanField()

    class Meta:
        """ Factor Meta """
        managed = False
        db_table = 'factor'


class HarmfulFactor(models.Model):
    """ HarmfulFactor """
    material = models.ForeignKey('Material', models.DO_NOTHING)
    factor = models.ForeignKey(Factor, models.DO_NOTHING)
    harmful_id = models.IntegerField(primary_key=True)

    class Meta:
        """ HarmfulFactor Meta """
        managed = False
        db_table = 'harmful_factor'
        unique_together = (('material', 'factor'),)


class HelpfulFactor(models.Model):
    """ HelpfulFactor """
    pollution = models.ForeignKey('Pollution', models.DO_NOTHING)
    factor = models.ForeignKey(Factor, models.DO_NOTHING)
    helpful_id = models.IntegerField(primary_key=True)

    class Meta:
        """ HelpfulFactor Meta """
        managed = False
        db_table = 'helpful_factor'
        unique_together = (('pollution', 'factor'),)


class Journey(models.Model):
    """ Journey """
    order = models.ForeignKey('Order', models.DO_NOTHING)
    address = models.ForeignKey(Address, models.DO_NOTHING)
    process = models.ForeignKey('Process', models.DO_NOTHING)
    journey_id = models.IntegerField(primary_key=True)

    class Meta:
        """ Journey Meta """
        managed = False
        db_table = 'journey'
        unique_together = (('order', 'address'),)
        db_table_comment = 'relation: order/address'


class Material(models.Model):
    """ Material """
    material_id = models.AutoField(primary_key=True)
    source = models.TextField()  # This field type is a guess.
    name = models.TextField(unique=True)
    is_active = models.BooleanField()

    class Meta:
        """ Material Meta """
        managed = False
        db_table = 'material'


class Message(models.Model):
    """ Message """
    message_id = models.AutoField(primary_key=True)
    is_password = models.BooleanField()
    subject = models.TextField()
    event_time = models.DateTimeField()
    customer = models.ForeignKey(Customer, models.DO_NOTHING)

    class Meta:
        """ Message Meta """
        managed = False
        db_table = 'message'


class Method(models.Model):
    """ Method """
    method_id = models.AutoField(primary_key=True)
    term_base = models.IntegerField()
    cost_rate = models.DecimalField(max_digits=4, decimal_places=2)
    name = models.TextField(unique=True)
    is_active = models.BooleanField()
    stage = models.ForeignKey('Stage', models.DO_NOTHING)

    class Meta:
        """ Method Meta """
        managed = False
        db_table = 'method'


class MethodChem(models.Model):
    """ MethodChem """
    items_count = models.IntegerField()
    chem = models.OneToOneField(Method, models.DO_NOTHING, primary_key=True)

    class Meta:
        """ MethodChem Meta """
        managed = False
        db_table = 'method_chem'


class MethodMech(models.Model):
    """ MethodMech """
    is_occupied = models.BooleanField()
    mech = models.OneToOneField(Method, models.DO_NOTHING, primary_key=True)

    class Meta:
        """ MethodMech Meta """
        managed = False
        db_table = 'method_mech'


class Order(models.Model):
    """ Order """
    order_id = models.AutoField(primary_key=True)
    process = models.OneToOneField('Process', models.DO_NOTHING)
    paymethod = models.TextField()  # This field type is a guess.
    customer = models.ForeignKey(Customer, models.DO_NOTHING)

    class Meta:
        """ Order Meta """
        managed = False
        db_table = 'order'
        db_table_comment = 'relation (intgl): customer - process'


class Package(models.Model):
    """ Package """
    product = models.ForeignKey('Product', models.DO_NOTHING)
    order = models.ForeignKey(Order, models.DO_NOTHING)
    items_count = models.IntegerField()
    package_id = models.IntegerField(primary_key=True)

    class Meta:
        """ Package Meta """
        managed = False
        db_table = 'package'
        unique_together = (('order', 'product'),)
        db_table_comment = 'relation: order - product'


class Pollution(models.Model):
    """ Pollution """
    pollution_id = models.AutoField(primary_key=True)
    source = models.TextField()  # This field type is a guess.
    name = models.TextField(unique=True)
    is_active = models.BooleanField()

    class Meta:
        """ Pollution Meta """
        managed = False
        db_table = 'pollution'


class Premises(models.Model):
    """ Premises """
    address = models.OneToOneField(Address, models.DO_NOTHING, primary_key=True)
    floor_num = models.IntegerField()
    flat_num = models.IntegerField()
    rooms_count = models.IntegerField()
    size = models.TextField()  # This field type is a guess.
    condition = models.TextField()  # This field type is a guess.

    class Meta:
        """ Premises Meta """
        managed = False
        db_table = 'premises'


class Problem(models.Model):
    """ Problem """
    product = models.ForeignKey('Product', models.DO_NOTHING)
    pollution = models.ForeignKey(Pollution, models.DO_NOTHING)
    is_old = models.BooleanField()
    is_removed = models.BooleanField()
    problem_id = models.IntegerField(primary_key=True)

    class Meta:
        """ Problem Meta """
        managed = False
        db_table = 'problem'
        unique_together = (('product', 'pollution'),)


class Process(models.Model):
    """ Process """
    process_id = models.AutoField(primary_key=True)
    opened_by = models.ForeignKey(Employee, models.DO_NOTHING, db_column='opened_by')
    opened_at = models.DateTimeField()
    status = models.TextField()  # This field type is a guess.

    class Meta:
        """ Process Meta """
        managed = False
        db_table = 'process'


class Product(models.Model):
    """ Product """
    product_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    agreed_price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    color = models.TextField()  # This field type is a guess.
    size = models.TextField()  # This field type is a guess.
    condition = models.TextField()  # This field type is a guess.

    class Meta:
        """ Product Meta """
        managed = False
        db_table = 'product'


class Referral(models.Model):
    """ Referral """
    product = models.ForeignKey(Product, models.DO_NOTHING)
    symbol = models.ForeignKey('Symbol', models.DO_NOTHING)
    is_underlined = models.BooleanField()
    is_crossedout = models.BooleanField()
    temperature = models.TextField()  # This field type is a guess.
    referral_id = models.IntegerField(primary_key=True)

    class Meta:
        """ Referral Meta """
        managed = False
        db_table = 'referral'
        unique_together = (('product', 'symbol'),)


class Request(models.Model):
    """ Request """
    request_id = models.AutoField(primary_key=True)
    process = models.OneToOneField(Process, models.DO_NOTHING)
    action = models.TextField()  # This field type is a guess.
    object = models.TextField()
    subject = models.TextField()

    class Meta:
        """ Request Meta """
        managed = False
        db_table = 'request'
        db_table_comment = 'requests to manage ctg_items and reg_int data (non-deletable records with "is_active" status column)'


class Scenario(models.Model):
    """ Scenario """
    scenario_id = models.IntegerField(primary_key=True)
    name = models.TextField(unique=True)
    is_active = models.BooleanField()
    purpose = models.TextField()  # This field type is a guess.

    class Meta:
        """ Scenario Meta """
        managed = False
        db_table = 'scenario'


class ScenarioOffsite(models.Model):
    """ ScenarioOffsite """
    premises = models.ForeignKey(Premises, models.DO_NOTHING)
    scenario = models.ForeignKey(Scenario, models.DO_NOTHING)
    rooms_left = models.IntegerField()
    offsite_id = models.IntegerField(primary_key=True)

    class Meta:
        """ ScenarioOffsite Meta """
        managed = False
        db_table = 'scenario_offsite'
        unique_together = (('scenario', 'premises'),)


class ScenarioOnsite(models.Model):
    """ ScenarioOnsite """
    product = models.ForeignKey(Product, models.DO_NOTHING)
    scenario = models.ForeignKey(Scenario, models.DO_NOTHING)
    current_stage = models.ForeignKey('Stage', models.DO_NOTHING, db_column='current_stage')
    onsite_id = models.IntegerField(primary_key=True)

    class Meta:
        """ ScenarioOnsite Meta """
        managed = False
        db_table = 'scenario_onsite'
        unique_together = (('scenario', 'product'),)


class Solution(models.Model):
    """ Solution """
    scenario = models.ForeignKey(Scenario, models.DO_NOTHING)
    method = models.ForeignKey(Method, models.DO_NOTHING)
    solution_id = models.IntegerField(primary_key=True)

    class Meta:
        """ Solution Meta """
        managed = False
        db_table = 'solution'
        unique_together = (('scenario', 'method'),)
        db_table_comment = 'relation: scenario - method'


class Stage(models.Model):
    """ Stage """
    stage_id = models.AutoField(primary_key=True)
    name = models.TextField()
    is_active = models.BooleanField()
    priority = models.IntegerField()
    type = models.TextField()  # This field type is a guess.
    mode = models.TextField()  # This field type is a guess.

    class Meta:
        """ Stage Meta """
        managed = False
        db_table = 'stage'
        unique_together = (('type', 'mode', 'name'),)


class Symbol(models.Model):
    """ Symbol """
    symbol_id = models.AutoField(primary_key=True)
    is_active = models.BooleanField()
    stage = models.ForeignKey(Stage, models.DO_NOTHING)
    specifics = models.TextField()

    class Meta:
        """ Symbol Meta """
        managed = False
        db_table = 'symbol'
        unique_together = (('stage', 'specifics'),)


class Texture(models.Model):
    """ Texture """
    product = models.ForeignKey(Product, models.DO_NOTHING)
    material = models.ForeignKey(Material, models.DO_NOTHING)
    is_mix = models.BooleanField()
    density = models.TextField()  # This field type is a guess.
    texture_id = models.IntegerField(primary_key=True)

    class Meta:
        """ Texture Meta """
        managed = False
        db_table = 'texture'
        unique_together = (('product', 'material'),)


class Workflow(models.Model):
    """ Workflow """
    workflow_id = models.AutoField(primary_key=True)
    process = models.ForeignKey(Process, models.DO_NOTHING)
    employee = models.ForeignKey(Employee, models.DO_NOTHING)
    event_time = models.DateTimeField()
    result_status = models.TextField()  # This field type is a guess.

    class Meta:
        """ Workflow Meta """
        managed = False
        db_table = 'workflow'
        db_table_comment = 'relation: process - employee'
