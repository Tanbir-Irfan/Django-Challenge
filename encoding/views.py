from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import redirect, render

from encoding.input import EncodedForm
import json
def home(request: HttpRequest)-> HttpResponse:
    if request.method == 'POST':
        form = EncodedForm(request.POST, auto_id=True)
        if form.is_valid(): 
            data = form.cleaned_data['encoded_string']
            split_input = data.split("111")    
            first_name = split_input[0] # take first value seperated by delimeter (111) as first names
            last_name = split_input[1] # take second value seperated by delimeter (111) as last name
            if len(split_input) > 3: # if split_input length is grater than 3 that means there are more than 2 delimeters so I will assumme rest of the delimeters are the parts of id
                id = split_input[2] # take first one and then add rest of the parts including delimter
                for i in range(len(split_input)):
                    if(i>2):
                        id += '111'+split_input[i] # adding rest of the parts as id with delimeter
            else:
                id = split_input[2] # in case there are only two delimeters
            json_data = json.loads('{"firstname": "'+first_name+'", "lastname": "'+last_name+'", "id": '+str(id)+'}')
            form = EncodedForm(None)
        else:
            json_data = {}
    else:
        form = EncodedForm(auto_id=True)
        json_data = {}
        
    context = {'form': form, 'data': json_data}
    return render(request, 'encoding/home.html', context)
