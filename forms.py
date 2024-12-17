from django import forms

class VideoUploadForm(forms.Form):

    upload_video_file = forms.FileField(label="Select Video", required=True,widget=forms.FileInput(attrs={"accept": "video/*"}))
    # upload_image_file = forms.FileField(label="Select image", required=True,widget=forms.FileInput(attrs={"accept": "image/*"}))
    sequence_length = forms.IntegerField(label="Sequence Length", required=True)
class ImageUploadForm(forms.Form):
    upload_image_file = forms.FileField(label="Select image", required=True,widget=forms.FileInput(attrs={"accept": "image/*"}))
    sequence_length = forms.IntegerField(label="Sequence Length", required=True)