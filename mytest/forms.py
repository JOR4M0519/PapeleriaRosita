from django import forms

class CreateProduct(forms.Form):
    nombre_producto = forms.CharField(label="Nombre",max_length=50)
    valor_compra = forms.IntegerField(label="Valor_Compra")
    valor_venta = forms.IntegerField(label="Valor_venta")
    valor_ganancia = forms.IntegerField(label="Ganancia")
    stock = forms.IntegerField(label="Cantidad")