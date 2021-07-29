def validate_pdf(value):
    """
    Validate File using it extension
    :param value: Given File
    :return: Validation Error if has a not valid Extension
    """
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    if ext.lower() != '.pdf':
        raise ValidationError('Unsupported file extension.')


def validate_pic(value):
    """
        Validate File using it extension
        :param value: Given File
        :return: Validation Error if has a not valid Extension
    """
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.png', '.jpeg', '.svg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
