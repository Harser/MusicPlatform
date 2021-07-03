from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from backend.models import Album, Track


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('title', 'creator', 'cover_url')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))


class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ('title', 'lyrics')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
