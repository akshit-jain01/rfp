from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple, EmailField, CharField, ValidationError

from django.core.validators import EmailValidator

from .validators import *

from .models import Vendor, RequestForProposal, Category

def quantity_check(quantity):
    if not quantity.isdigit():
        raise ValidationError(code='invalid',
            message="quantity should be numeric"
        )

class RegisterAdminForm(ModelForm):

    class Meta:
        model = Vendor
        fields = ['email','password']

class VendorForm(ModelForm):

    category = ModelMultipleChoiceField(
    label = 'category',
    queryset=Category.objects.all(),
    widget=CheckboxSelectMultiple
    )

    email = EmailField(validators=[EmailValidator()])

    

    class Meta:
        model = Vendor
        fields = ['firstname','lastname','email','password','revenue','no_of_employees','category','gst_no','pancard_no','mobile']

class AddRfpForm(ModelForm):

    categories = ModelMultipleChoiceField(
    label = 'Categories',
    queryset=Category.objects.all(),
    widget=CheckboxSelectMultiple
    )

    vendor = ModelMultipleChoiceField(
    label = 'Vendors',
    queryset=Vendor.objects.all(),
    widget=CheckboxSelectMultiple
    )

    quantity = CharField(validators=[quantity_check])
    

    class Meta:
        model = RequestForProposal
        fields = '__all__'
        exclude = ['status']

class AddCategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = '__all__'