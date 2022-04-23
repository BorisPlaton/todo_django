from django.forms import models

from .models import Affair


class AffairEditingForm(models.ModelForm):
    def __init__(self, *args, **kwargs):
        """Инициализация формы. Устанавливаем стили формам"""

        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                "class": "form-control",
            })

        self.fields['is_completed'].widget.attrs.update({
            'class': 'form-check-input'
        })

    class Meta:
        model = Affair
        fields = ('title', 'text', 'is_completed')


class CreateAffairForm(models.ModelForm):

    def __init__(self, *args, **kwargs):
        """Инициализация формы. Устанавливаем стили формам"""

        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                "class": "form-control"
            })

        self.fields['text'].widget.attrs.update({
            "cols": "",
            "rows": "",
            "style": """
                width: 100%; 
                resize: none;
                height: 275px;
            """
        })

    class Meta:
        model = Affair
        fields = ('title', 'text')
