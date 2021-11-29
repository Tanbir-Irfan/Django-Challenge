from django import forms
import re

class EncodedForm(forms.Form):
    encoded_string = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    def clean_encoded_string(self)->str:
        data = self.cleaned_data['encoded_string']
        if data == "": # check emptiness of the passing argument value
            raise forms.ValidationError("The input can not be empty")
        elif len(data) <10 or len(data) > 200: # check the size of passing arguments as expected let's assume the size needs to be between 10 and 40
            raise forms.ValidationError("The input's length has to be between 10 and 200 (inclusive)")
        elif not re.search("^[a-zA-Z]+111[a-zA-Z]+111\d+$", data): # check valid encoded string with correct format using regex
            raise forms.ValidationError("The input needs to contain valid encoded alphanumeric* characters with correct format ex: 'firstname(alphabetic)<111>lastname(alphabetic)<111>id(int)'")
        return str(data)
    
    