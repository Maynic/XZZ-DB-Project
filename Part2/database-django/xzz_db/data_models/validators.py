


from django.core.exceptions import ValidationError



def validate_zip(value):
    if len(value) != 5:
        raise ValidationError(
            _("%(value)s is not an valid zip"),
            params={"value": value},
        )
    for i in value:
        if i not in "0123456789":
            raise ValidationError(
                _("%(value)s is not an valid zip"),
                params={"value": value},
            )


def validate_cvv(value):
    if len(value) != 3 and len(value) != 4:
        raise ValidationError(
            _("%(value)s is not an valid cvv"),
            params={"value": value},
        )
    for i in value:
        if i not in "0123456789":
            raise ValidationError(
                _("%(value)s is not an valid cvv"),
                params={"value": value},
            )


def validate_card(value):
    for i in value:
        if i not in "0123456789":
            raise ValidationError(
                _("%(value)s is not an valid card number"),
                params={"value": value},
            )