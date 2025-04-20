from django import forms
from todo.models import Todo
from django.core.exceptions import ValidationError
import imghdr

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'status', 'photo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def clean_photo(self):
        photo = self.cleaned_data.get('photo', False)
        if photo:
            # Check if the uploaded file is a valid image
            valid_image_types = ['jpeg', 'png', 'gif']
            file_type = imghdr.what(photo)
            if file_type not in valid_image_types:
                raise ValidationError("Only JPEG, PNG, and GIF files are allowed.")
        return photo