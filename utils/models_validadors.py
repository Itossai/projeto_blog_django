from django.core.exceptions import ValidationError

def validate_png(image):
    if not image.name.lower().endswith('.png'):
        raise ValidationError("O arquivo deve ser uma imagem do tipo PNG!")