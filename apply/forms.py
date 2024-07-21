from django import forms

from apply.models import Apply


class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['checkbox']

    def __init__(self, *args, **kwargs):
        super(ApplyForm, self).__init__(*args, **kwargs)
        self.fields['checkbox'].required = True
        self.fields['checkbox'].label = 'I agree to the terms and conditions'
