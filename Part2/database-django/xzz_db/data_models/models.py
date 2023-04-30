from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


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


#     def __str__(self):
#         return self.name

# birth_date = models.DateTimeField(auto_now=False, auto_now_add=False, **options)
# zip = models.DecimalField(..., max_digits=5, decimal_places=2)
# null=True, blank=True,
class xzz_visitor(models.Model):
    visitor_name = models.CharField("Visitor Name", max_length=60)
    email = models.EmailField("Email")
    birth_date = models.DateTimeField("Birthday")
    phone = models.CharField("Phone", max_length=10)
    address = models.CharField("Street", max_length=60)
    city = models.CharField("City", max_length=20)
    state = models.CharField("State", max_length=2)
    zip = models.CharField("ZIP Code", max_length=5, validators=[validate_zip])

    class visitor_type_choices(models.TextChoices):
        INDIVIDUAL = "IN", _("Individual")
        GROUP = "GR", _("Group")
        MEMBER = "ME", _("Member")
        STUDENT = "ST", _("Student")

    visitor_type = models.CharField("Visitor Type",
                                    max_length=2,
                                    choices=visitor_type_choices.choices,
                                    default=visitor_type_choices.INDIVIDUAL,
                                    )

    # def __str__(self):
    #     res = ''
    #     res += self.name
    #     return res


class xzz_ticket_search(models.Model):
    radio = models.CharField(max_length=100)
    ticket_date = models.CharField(max_length=100, blank=True)
    ticket_c = models.CharField(max_length=100, blank=True)
    ticket_a = models.CharField(max_length=100, blank=True)
    ticket_s = models.CharField(max_length=100, blank=True)
    show_select = models.CharField(max_length=100, blank=True)
    show_date = models.CharField(max_length=100, blank=True)
    show_c = models.CharField(max_length=100, blank=True)
    show_a = models.CharField(max_length=100, blank=True)
    show_s = models.CharField(max_length=100, blank=True)
    store_category = models.CharField(max_length=100, blank=True)
    park_place = models.CharField(max_length=100, blank=True)
    park_in_date = models.CharField(max_length=100, blank=True)
    park_in = models.CharField(max_length=100, blank=True)
    park_out_date = models.CharField(max_length=100, blank=True)
    park_out = models.CharField(max_length=100, blank=True)

