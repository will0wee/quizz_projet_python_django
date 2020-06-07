from django import forms

class ClassForm(forms.Form):
    libelle = forms.CharField(max_length=100,
                                label="Nom de la classe :",
                                widget=forms.TextInput(attrs={'class': 'form-control'}))


class addEleveForm(forms.Form):
    def __init__(self, *args, **kwargs):
        extra_fields = kwargs.pop('extra', 0)

        super(addEleveForm, self).__init__(*args, **kwargs)
        self.fields['extra_field_count'].initial = extra_fields

        for index in range(int(extra_fields)):
            # generate extra fields in the number specified via extra_fields
            self.fields['extra_field_{index}'.format(index=index)] = \
                forms.CharField()