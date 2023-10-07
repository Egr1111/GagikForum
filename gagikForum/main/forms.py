from .models import *
from django.forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from phonenumber_field.formfields import PhoneNumberField


class UserCreateForm(UserCreationForm):
    username = CharField(
        label="Введите свой псевдоним",
        max_length=255,
        widget=TextInput(
            attrs={
                "class": "form-control col-xxl-3 col-lg-5 col-md-8 col-sm-12",
            }
        ),
    )
    phone_number = PhoneNumberField(
        label="Введите свой номер",
        widget=TextInput(
            attrs={
                "class": "form-control col-xxl-3 col-lg-5 col-md-8 col-sm-12",
                "placeholder": "+...",
                "type": "number",
            }
        ),
    )
    gender = TypedChoiceField(
        label="Введите свой пол",
        choices=GENDER_CHOICE,
        widget=RadioSelect(attrs={"class": "flex-row"}),
        coerce=str,
    )

    education = TypedChoiceField(
        label="Введите свое нынешнее образование",
        choices=EDUCATION_CHOICE,
        widget=RadioSelect(
            attrs={
                "class": "col",
            }
        ),
    )

    email = CharField(
        label="Введите свою электронную почту",
        max_length=255,
        widget=(
            TextInput(
                attrs={
                    "class": "form-control col-xxl-3 col-lg-5 col-md-8 col-sm-12",
                }
            )
        ),
    )
    wasBorn = DateField(
        label="Введите свою дату рождения",
        widget=(
            DateInput(
                attrs={
                    "class": "form-control col-xxl-3 col-lg-5 col-md-8 col-sm-12",
                    "type": "date",
                }
            )
        ),
    )

    password1 = CharField(
        label="Введите пароль",
        max_length=255,
        widget=TextInput(
            attrs={
                "class": "form-control col-xxl-3 col-lg-5 col-md-8 col-sm-12",
                "type": "password",
            }
        ),
    )

    password2 = CharField(
        label="Повторите пароль",
        max_length=255,
        widget=TextInput(
            attrs={
                "class": "form-control col-xxl-3 col-lg-5 col-md-8 col-sm-12",
                "type": "password",
            }
        ),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "password1",
            "password2",
            "email",
            "gender",
            "phone_number",
            "wasBorn",
            "education",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"autofocus": False})
        self.fields["password1"].widget.attrs.update({"autofocus": False})
        self.fields["password2"].widget.attrs.update({"autofocus": False})
        self.fields["email"].widget.attrs.update({"autofocus": False})
        self.fields["wasBorn"].widget.attrs.update({"autofocus": False})
        self.fields["education"].widget.attrs.update({"autofocus": False})
        self.fields["gender"].widget.attrs.update({"autofocus": False})
        self.fields["phone_number"].widget.attrs.update({"autofocus": False})

    # def clean(self):
    #     cleaned_data = super(UserCreateForm, self).clean()

    # print(cleaned_data)
    # num = [f"{i}" for i in range(9)]
    # sim = ["@", "+", "-", "_"] + num
    # for i in username:
    #     if not i.isalpha() and i not in sim:
    #         self.add_error(
    #             "username",
    #             "Введите правильное имя пользователя. Оно может содержать только буквы, цифры и знаки @/+/-/_.",
    #         )
    #         break
    # return cleaned_data


class UserLoginForm(AuthenticationForm):
    username = CharField(
        label="Введите свой псевдоним",
        max_length=255,
        widget=TextInput(
            attrs={
                "class": "form-control col-xxl-3 col-lg-5 col-md-8 col-sm-12",
            }
        ),
    )
    password = CharField(
        label="Введите пароль",
        max_length=255,
        widget=TextInput(
            attrs={
                "class": "form-control col-xxl-3 col-lg-5 col-md-8 col-sm-12",
                "type": "password",
            }
        ),
    )

    class Meta:
        models = User
        fields = ("username", "password")

class UserForm(ModelForm):
    username = CharField(
        label="Введите свой псевдоним",
        max_length=255,
        widget=TextInput(
            attrs={
                "class": "form-control col-xxl-3 col-lg-5 col-md-8 col-sm-12",
            }
        ),
    )
    my_story = CharField(
        label="Расскажите о себе",
        required=False,
        widget=Textarea(
            attrs={
                "class": "form-control col-xxl-3 col-lg-5 col-md-8 col-sm-12",
            }
        ),
    )

    phone_number = PhoneNumberField(
        label="Введите свой номер",
        widget=TextInput(
            attrs={
                "class": "form-control col-xxl-3 col-lg-5 col-md-8 col-sm-12",
                "placeholder": "+...",
                "type": "number",
            }
        ),
    )
    gender = TypedChoiceField(
        label="Введите свой пол",
        choices=GENDER_CHOICE,
        widget=RadioSelect(attrs={"class": "flex-row"}),
        coerce=str,
    )

    education = TypedChoiceField(
        label="Введите свое нынешнее образование",
        choices=EDUCATION_CHOICE,
        widget=RadioSelect(
            attrs={
                "class": "col",
            }
        ),
    )

    email = CharField(
        label="Введите свою электронную почту",
        max_length=255,
        widget=(
            TextInput(
                attrs={
                    "class": "form-control col-xxl-3 col-lg-5 col-md-8 col-sm-12",
                }
            )
        ),
    )
    wasBorn = DateField(
        label="Введите свою дату рождения",
        required=False,
        widget=(
            DateInput(
                attrs={
                    "class": "form-control col-xxl-3 col-lg-5 col-md-8 col-sm-12",
                    "type": "date",
                }
            )
        ),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "image",
            "my_story",
            "email",
            "gender",
            "phone_number",
            "wasBorn",
            "education",
        )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"autofocus": False})
        self.fields["email"].widget.attrs.update({"autofocus": False})
        self.fields["wasBorn"].widget.attrs.update({"autofocus": False})
        
        self.fields["education"].widget.attrs.update({"autofocus": False})
        self.fields["gender"].widget.attrs.update({"autofocus": False})
        self.fields["phone_number"].widget.attrs.update({"autofocus": False})