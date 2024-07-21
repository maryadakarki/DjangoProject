from django import forms

from pro.models import Pro


class ProForm(forms.ModelForm):
    # pro_certificates = forms.MultiValueField(
    #     widget=forms.FileInput(attrs={'multiple': True}))

    class Meta:
        model = Pro
        fields = ['pro_name', 'pro_pic', 'pro_dob', 'pro_number', 'pro_bio', 'pro_cv',
                  'pro_certificates']

        widgets = {
            'pro_dob': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProForm, self).__init__(*args, **kwargs)
        self.fields['pro_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['pro_pic'].widget.attrs.update({'class': 'form-control'})
        self.fields['pro_dob'].widget.attrs.update({'class': 'form-control'})
        self.fields['pro_bio'].widget.attrs.update({'class': 'form-control'})
        self.fields['pro_cv'].widget.attrs.update({'class': 'form-control'})
        self.fields['pro_certificates'].widget.attrs.update({'class': 'form-control'})

