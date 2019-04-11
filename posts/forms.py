from django import forms
from .models import Post

class PostModelForm(forms.ModelForm):
    
    # 1. 어떤 input 필드를 가지는지
    """
    label : human-friendly label for this fields
            content : [         Form        ] 이런식으로 넣어지는것임.
                => 기본적으로 Placeholder는 label값을 따로 상속받음
    widget : Django's representation of an HTML input element
            1. Rendering of the HTML
            2. Extraction of data from a GET/POST dictionary that corresponds
            to the widget
            (https://docs.djangoproject.com/en/2.1/ref/forms/widgets/#base-widget-classes)
            
            widget
            - 생성자
                - attrs : HTML 속성들을 담는 딕셔너리
    """
    content = forms.CharField(label="content", widget=forms.Textarea(
        # 조절하고 싶은 html attribute들을 넣어주면됨.
            attrs = {
                'placeholder' : "오늘은 무엇을 하셨나요?"
            }
        ))
    # 2. 해당 input 필드의 속성을 추가 & 어떤 모델을 조작할지
    class Meta:
        model = Post
        fields = ['content','image']
        # __all__ 이라고 하면 모든 컬럼을 받을 수 있는데,
        # 단점도 있음 (ex, created_at, updated_at같은건 받으면 안되니까)
        
    """
    우리가 만든 TextField에 바로
    Bootstrap을 먹일 수 있는 패키지가 있음!
            django-bootstrap4
    """
        