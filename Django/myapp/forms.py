from django import forms
#esto es para enviar formularios al html 
#gracias a esto lo que podemos hacer es enviar un tipo de formualtio a html
#donde facilitara la entrada de datos 
#en este caso asociamos al models para saber que estamos creando 


class create_taskss(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    description = forms.CharField(label='Description', widget=forms.Textarea)
    project = forms.ModelChoiceField(
        label='Proyecto',
        queryset=None,  # Lo estableceremos en la vista
        empty_label="Selecciona un proyecto"
    )

class create_projectss(forms.Form):
    name = forms.CharField(label ='Name Project', max_length=100)