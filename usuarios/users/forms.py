from django import forms

from .models import User

class UserRegisterForm(forms.ModelForm):
    """Form definition for UserRegisterForm."""

    # Para la contraseña
    password1 = forms.CharField(
        label="Password", 
        required=True, 
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )

    password2 = forms.CharField(
        label="Password", 
        required=True, 
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir Contraseña'
            }
        )
    )



    class Meta:
        """Meta definition for UserRegisterFormform."""

        model = User
        fields = ('username', 'email','nombres', 'apellidos', 'genero') 


    # Funcion para la vaidacion de las conraseñas
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:

            # Enviamos error; decimos en que campo y que error saldra
            self.add_error('password2', 'Las contaseñas no son iguales')
        


    def clean_password1(self):
        if len(self.cleaned_data['password1']) < 5:
            self.add_error('password1', 'La contraseña debe tener mas de 5 caracteres')