from django import forms

class feedback_Form(forms.Form):
    email = forms.EmailField(label='Enter Your name', max_length=100)
    name = forms.CharField(label='Enter Your name', max_length=200)
    feedback = forms.CharField(label='Enter Your feedback', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(feedback_Form,self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"