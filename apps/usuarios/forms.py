from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import Usuario, Asesor

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            'first_name', 'last_name', 'email', 'documento',
            'role', 'telefono', 'direccion'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'documento': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-select'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar widgets de contraseña
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        
        # Personalizar mensajes de ayuda
        self.fields['password1'].help_text = 'La contraseña debe tener al menos 8 caracteres.'
        self.fields['password2'].help_text = 'Ingresa la misma contraseña para verificación.'
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exclude(pk=self.instance.pk if self.instance else None).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado.')
        return email
    
    def clean_documento(self):
        documento = self.cleaned_data.get('documento')
        if Usuario.objects.filter(documento=documento).exclude(pk=self.instance.pk if self.instance else None).exists():
            raise forms.ValidationError('Este documento ya está registrado.')
        return documento

class SolicitarRecuperacionForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu correo'}))

class CodigoRecuperacionForm(forms.Form):
    codigo = forms.CharField(label='Código de recuperación', max_length=6, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código de 6 dígitos'}))

class NuevaContrasenaForm(forms.Form):
    nueva_contrasena = forms.CharField(label='Nueva contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Nueva contraseña'}))
    confirmar_contrasena = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirma la contraseña'}))

    def clean(self):
        cleaned_data = super().clean()
        nueva = cleaned_data.get('nueva_contrasena')
        confirmar = cleaned_data.get('confirmar_contrasena')
        if nueva and confirmar and nueva != confirmar:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return cleaned_data

class PerfilAprendizForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'telefono', 'direccion', 'imagen_perfil']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'imagen_perfil': forms.FileInput(attrs={'class': 'form-control'})
        }
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo electrónico',
            'telefono': 'Teléfono',
            'direccion': 'Dirección',
            'imagen_perfil': 'Foto de perfil'
        }

class AsesorRegistroForm(UsuarioForm):
    trimestre = forms.ChoiceField(
        choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')],
        label='Trimestre',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta(UsuarioForm.Meta):
        fields = UsuarioForm.Meta.fields + ['trimestre'] 