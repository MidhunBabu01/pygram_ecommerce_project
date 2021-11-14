from django import forms
from fashion_hub_app.models import Products




class AdminProductsForms(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('name','subcategory','desc','img1','img2','img3','price','stock')
        widgets ={
            'desc': forms.TextInput(attrs={'class':'form-control'}),
            # 'name': forms.TextInput(attrs={'class':'form-control'}),
            # 'price': forms.TextInput(attrs={'class':'form-control'}),
            # 'stock': forms.TextInput(attrs={'class':'form-control'})
            
        }