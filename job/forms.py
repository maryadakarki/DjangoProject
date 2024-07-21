from datetime import date

from django.forms import ModelForm, DateInput, DateField, ModelChoiceField
from job.models import Job, Category


class JobForm(ModelForm):
    # job_validity = DateField(
    #     widget=DateInput(attrs={'type': 'date', 'min': date.today().isoformat()})
    # )

    class Meta:
        model = Job
        fields = ['category', 'job_title', 'job_description', 'job_validity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['job_title'].widget.attrs.update(
            {'class': 'form-control mt-1'}
        )
        self.fields['job_description'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please add a proper description.'}
        )
        self.fields['category'].widget.attrs.update(
            {'class': 'form-control'}
        )
        self.fields['job_validity'].widget.attrs.update(
            {'class': 'form-control'}
        )


