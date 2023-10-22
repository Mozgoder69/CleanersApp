from django import forms

class ApproveCategoryForm(forms.Form):
    category_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Название категории")
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label="Описание")
    icon = forms.ImageField(label="Иконка/Изображение", required=False)
    approve = forms.ChoiceField(choices=[('approve', 'Утвердить'), ('deny', 'Отклонить')], widget=forms.RadioSelect, label="Решение")

class ApproveMaterialDeletionForm(forms.Form):
    material_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}), label="Название материала")
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'readonly': 'readonly'}), label="Описание")
    approve = forms.ChoiceField(choices=[('approve', 'Утвердить'), ('deny', 'Отклонить')], widget=forms.RadioSelect, label="Решение")