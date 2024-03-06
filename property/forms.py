from django import forms
from .models import Property


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'
        widgets = {
            'project': forms.Select(attrs={'class': 'form-control'}),
            'agent': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'property_slug': forms.TextInput(attrs={'class': 'form-control'}),
            'SEO_title': forms.TextInput(attrs={'class': 'form-control'}),
            'SEO_description': forms.TextInput(attrs={'class': 'form-control'}),
            'external_property_id': forms.TextInput(attrs={'class': 'form-control'}),
            'listing_type': forms.Select(attrs={'class': 'form-control'}),
            'property_type': forms.Select(attrs={'class': 'form-control'}),
            'property_name': forms.TextInput(attrs={'class': 'form-control'}),
            'area': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'bedrooms': forms.Select(attrs={'class': 'form-control'}),
            'bathrooms': forms.Select(attrs={'class': 'form-control'}),
            'buildings': forms.NumberInput(attrs={'class': 'form-control'}),
            'property_size': forms.NumberInput(attrs={'class': 'form-control'}),
            'outdoor_area_size': forms.TextInput(attrs={'class': 'form-control'}),
            'land_size': forms.TextInput(attrs={'class': 'form-control'}),
            'price_per_sqm': forms.NumberInput(attrs={'class': 'form-control'}),
            'unit_number': forms.TextInput(attrs={'class': 'form-control'}),
            'floor_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'num_of_storeys': forms.NumberInput(attrs={'class': 'form-control'}),
            'furnishing': forms.Select(attrs={'class': 'form-control'}),
            'num_of_parking_spaces': forms.NumberInput(attrs={'class': 'form-control'}),
            'monthly_maintenance_fee': forms.NumberInput(attrs={'class': 'form-control'}),
            'ownership_type': forms.Select(attrs={'class': 'form-control'}),
            'land_ownership_type': forms.Select(attrs={'class': 'form-control'}),
            'land_title_deed': forms.Select(attrs={'class': 'form-control'}),
            'purchase_year_month': forms.DateInput(attrs={'class': 'form-control'}),
            'construction_completed': forms.DateInput(attrs={'class': 'form-control'}),
            'property_features': forms.Textarea(attrs={'class': 'form-control'}),
            'property_outdoor_features': forms.Textarea(attrs={'class': 'form-control'}),
            'unit_view': forms.Select(attrs={'class': 'form-control'}),
            'photo_name': forms.TextInput(attrs={'class': 'form-control'}),
            'photo_links': forms.Textarea(attrs={'class': 'form-control'}),
            'video': forms.URLInput(attrs={'class': 'form-control'}),
            'virtual_tour': forms.URLInput(attrs={'class': 'form-control'}),
            'floor_plan': forms.URLInput(attrs={'class': 'form-control'}),
            'listing_title_for_sale': forms.TextInput(attrs={'class': 'form-control'}),
            'listing_title_for_rent': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'for_sale_occupation_status': forms.TextInput(attrs={'class': 'form-control'}),
            'for_sale_contract_expiry_date': forms.DateInput(attrs={'class': 'form-control'}),
            'for_rent_occupation_status': forms.TextInput(attrs={'class': 'form-control'}),
            'for_rent_available_date': forms.DateInput(attrs={'class': 'form-control'}),
            'sales_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'rental_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'rental_price_frequency': forms.Select(attrs={'class': 'form-control'}),
            'rental_price_conditions': forms.Textarea(attrs={'class': 'form-control'}),
            'commission_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'listing_status': forms.Select(attrs={'class': 'form-control'}),
            'created_at': forms.DateTimeInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'updated_at': forms.DateTimeInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'discounted_sales_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'discounted_rental_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'sold_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'sold_date': forms.DateInput(attrs={'class': 'form-control'}),
            'rent_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'rent_date': forms.DateInput(attrs={'class': 'form-control'}),
            'available_date': forms.DateInput(attrs={'class': 'form-control'}),
            'hidden_private_info_form': forms.Textarea(attrs={'class': 'form-control'}),
            'owner_name': forms.TextInput(attrs={'class': 'form-control'}),
            'owner_phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'owner_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'owner_social_accounts': forms.Textarea(attrs={'class': 'form-control'}),
            'owner_info_display': forms.TextInput(attrs={'class': 'form-control'}),
            'featured_property': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'bold_property': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'latitude': forms.TextInput(attrs={'class': 'form-control'}),
            'longitude': forms.TextInput(attrs={'class': 'form-control'}),
        }



class ContactForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control simple'})
    )
    email = forms.EmailField(
        label='Email',
        max_length=100,
        required=False,
        widget=forms.EmailInput(attrs={'class': 'form-control simple'})
    )
    subject = forms.CharField(
        label='Subject',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control simple'})
    )
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={'class': 'form-control simple'}),
        required=False
    )
