from django import forms

class login(forms.Form):
    username = forms.CharField(label='Nombre de usuario',
                             max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput() , label='Contraseña', required=True, max_length=10)

class signup(forms.Form):
    nombreEmpleado = forms.CharField(label='Ingrese nombre empleado',max_length=50, required=True)
    edad = forms.CharField(widget=forms.NumberInput(attrs={
        'max': '90',    # For maximum number
        'min': '18',    # For minimum number
    }), label='Edad empleado', required=True)