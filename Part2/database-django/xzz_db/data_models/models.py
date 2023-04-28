from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator


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
    # birth_date = models.DateTimeField(auto_now=False, auto_now_add=False, **options)
    # zip = models.DecimalField(..., max_digits=5, decimal_places=2)
    # null=True, blank=True,


# Visitor
class xzz_visitor(models.Model):

    # visitor_id = models.AutoField(primary_key=True)
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

    # class Meta:
    #     db_table = 'xzz_visitor'

    def __str__(self):
        return self.visitor_name


# Attraction
class xzz_attraction(models.Model):

    location_validator = RegexValidator(
        regex=r'^Lot [A-Z]$',
        message='Location must follow the pattern "Lot [A-Z]"',
    )
    # attraction_id = models.DecimalField(max_digits=15, decimal_places=2, primary_key=True)
    attraction_name = models.CharField(max_length=60)
    attraction_description = models.CharField(max_length=200)

    class attraction_type_choices(models.TextChoices):
        roller_coaster = "RC", _("Roller Coaster")
        water_ride = "WR", _("Water Ride")
        dark_ride = "DR", _("Dark Ride")
        kid_ride = "KR", _("Kid Ride")
    attraction_type = models.CharField("Attraction Type",
                                       max_length=2,
                                       choices=attraction_type_choices.choices,
                                       default=attraction_type_choices.roller_coaster,
                                       )

    class attraction_status_choices(models.TextChoices):
        open = "OP", _("Open")
        closed = "CL", _("Closed")
        under_maintenance = "UM", _("Under Maintenance")
    attraction_status = models.CharField("Attraction Status",
                                         max_length=2,
                                         choices=attraction_status_choices.choices,
                                         default=attraction_status_choices.open,
                                         )

    capacity = models.DecimalField("Capacity", max_digits=5, decimal_places=0)
    # Assume in cm
    min_height = models.DecimalField(
        "Min Height", max_digits=3, decimal_places=2)
    # Assume in minutes
    duration = models.DecimalField("Duration", max_digits=4, decimal_places=2)
    location = models.CharField("Location", max_length=10)

    class Meta:
        db_table = 'xzz_attraction'

    def __str__(self):
        return self.attraction_name

# Order
class xzz_order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateTimeField("Order Date")
    xzz_visitor = models.ForeignKey(
        'xzz_visitor', on_delete=models.CASCADE, verbose_name="Visitor ID")

    class Meta:
        db_table = 'xzz_order'
        verbose_name = 'Xzz Order'
        verbose_name_plural = 'Xzz Orders'

    def __str__(self):
        return f"Order {self.order_id}"


# Parking
class xzz_parking(models.Model):
    # parking_id = models.AutoField(primary_key=True)
    lot = models.CharField("Lot", max_length=10)
    spot = models.FloatField("Spot")
    time_in = models.DateTimeField("Time In")
    time_out = models.DateTimeField("Time Out", null=True, blank=True)
    fee = models.DecimalField("Fee", max_digits=4, decimal_places=2)
    order = models.ForeignKey(
        'xzz_order', on_delete=models.CASCADE, verbose_name="Order ID")

    class Meta:
        db_table = 'xzz_parking'
        verbose_name = 'Xzz Parking'
        verbose_name_plural = 'Xzz Parkings'

    def __str__(self):
        return f"Parking {self.parking_id}"


# Payment
class xzz_payment(models.Model):
    # payment_id = models.AutoField(primary_key=True)

    class PaymentMethodChoices(models.TextChoices):
        CASH = 'CA', _("Cash")
        CREDIT = 'CR', _("Credit")
        DEBIT = 'DE', _("Debit")
    payment_method = models.CharField("Payment Method",
                                      max_length=15,
                                      choices=PaymentMethodChoices.choices,
                                      default=PaymentMethodChoices.CASH,)

    payment_amount = models.DecimalField(
        "Payment Amount", max_digits=8, decimal_places=2)
    name_on_card = models.CharField(
        "Name on Card", max_length=30, null=True, blank=True)
    card_number = models.CharField("Card Number", max_length=20, validators=[
                                   validate_card], null=True, blank=True)
    expiration_date = models.DateTimeField(
        "Expiration Date", null=True, blank=True)
    cvv = models.CharField("CVV", max_length=3, null=True,
                           blank=True, validators=[validate_cvv])
    order = models.ForeignKey(
        'xzz_order', on_delete=models.CASCADE, verbose_name="Order ID")

    class Meta:
        db_table = 'xzz_payment'
        verbose_name = 'Xzz Payment'
        verbose_name_plural = 'Xzz Payments'

    def __str__(self):
        return f"Payment {self.payment_id}"

    def clean(self):
        if self.payment_method == self.PaymentMethodChoices.CASH:
            if self.name_on_card or self.card_number or self.expiration_date or self.cvv:
                raise ValidationError(
                    "For cash payment, card information must be empty.")
        elif self.payment_method in (self.PaymentMethodChoices.CREDIT, self.PaymentMethodChoices.DEBIT):
            if not all([self.name_on_card, self.card_number, self.expiration_date, self.cvv]):
                raise ValidationError(
                    "For credit or debit payment, card information must be provided.")
        super().clean()


# Show
class xzz_show(models.Model):
    # show_id = models.AutoField(primary_key=True)
    show_name = models.CharField("Show Name", max_length=50)
    show_description = models.CharField("Show Description", max_length=250)

    class ShowTypeChoices(models.TextChoices):
        DRAMA = 'Drama'
        MUSICAL = 'Musical'
        COMEDY = 'Comedy'
        HORROR = 'Horror'
        ADVENTURE = 'Adventure'
    show_type = models.CharField("Show Type",
                                 max_length=15,
                                 choices=ShowTypeChoices.choices,
                                 default=ShowTypeChoices.DRAMA,)

    start_time = models.DateTimeField("Start Time")
    end_time = models.DateTimeField("End Time")

    class ShowAccessibleChoices(models.TextChoices):
        YES = 'Yes'
        NO = 'No'
    show_accessible = models.CharField("Wheelchair Accessible", max_length=3,
                                       choices=ShowAccessibleChoices.choices,
                                       default=ShowAccessibleChoices.YES,)

    show_price = models.FloatField("Show Price")

    class Meta:
        db_table = 'xzz_show'
        verbose_name = 'Xzz Show'
        verbose_name_plural = 'Xzz Shows'

    def __str__(self):
        return self.show_name


# Store
class xzz_store(models.Model):

    # store_id = models.AutoField(primary_key=True)
    store_name = models.CharField("Store Name", max_length=255)

    class CategoryChoices(models.TextChoices):
        FOOD_STALL = 'Food stall'
        ICE_CREAM_PARLOR = 'Ice cream parlor'
        RESTAURANT = 'Restaurant'
        GIFT_SHOP = 'Gift Shop'
        APPARELS = 'Apparels'
    category = models.CharField("Category", max_length=20, choices=CategoryChoices.choices,
                                default=CategoryChoices.GIFT_SHOP,)

    class Meta:
        db_table = 'xzz_store'
        verbose_name = 'Xzz Store'
        verbose_name_plural = 'Xzz Stores'

    def __str__(self):
        return self.store_name


# Ticket
class XzzTicket(models.Model):

    # ticket_id = models.AutoField(primary_key=True)

    class TicketMethodChoices(models.TextChoices):
        ONLINE = 'Online'
        ONSITE = 'Onsite'
    ticket_method = models.CharField("Ticket Method", max_length=6,
                                     choices=TicketMethodChoices.choices,
                                     default=TicketMethodChoices.ONSITE)

    visit_date = models.DateTimeField("Visit Date")
    ticket_price = models.DecimalField(
        "Ticket Price", max_digits=8, decimal_places=2)
    order = models.ForeignKey(
        'xzz_order', on_delete=models.CASCADE, verbose_name="Order ID")
    visitor = models.ForeignKey(
        'xzz_visitor', on_delete=models.CASCADE, verbose_name="Visitor ID")

    class Meta:
        db_table = 'xzz_ticket'
        verbose_name = 'Xzz Ticket'
        verbose_name_plural = 'Xzz Tickets'

    def __str__(self):
        return f"Ticket {self.ticket_id}"
