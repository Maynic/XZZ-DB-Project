from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from .validators import *

# Visitor
class xzz_visitor(models.Model):

    # visitor_id = models.AutoField(primary_key=True)
    visitor_name = models.CharField("Visitor Name", max_length=60)
    email = models.EmailField("Email", unique=True)
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

    class Meta:
        managed = True
        db_table = 'xzz_visitor'

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
        "Min Height", max_digits=5, decimal_places=2)
    # Assume in minutes
    duration = models.DecimalField("Duration", max_digits=6, decimal_places=2)
    location = models.CharField("Location", max_length=10)

    class Meta:
        managed = True
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


# class xzz_search(models.Model):
#     radio = models.CharField(max_length=100)
#     ticket_date = models.CharField(max_length=100, blank=True)
#     ticket_c = models.CharField(max_length=100, blank=True)
#     ticket_a = models.CharField(max_length=100, blank=True)
#     ticket_s = models.CharField(max_length=100, blank=True)
#     show_select = models.CharField(max_length=100, blank=True)
#     show_date = models.CharField(max_length=100, blank=True)
#     show_c = models.CharField(max_length=100, blank=True)
#     show_a = models.CharField(max_length=100, blank=True)
#     show_s = models.CharField(max_length=100, blank=True)
#     store_category = models.CharField(max_length=100, blank=True)
#     park_place = models.CharField(max_length=100, blank=True)
#     park_in_date = models.CharField(max_length=100, blank=True)
#     park_in = models.CharField(max_length=100, blank=True)
#     park_out_date = models.CharField(max_length=100, blank=True)
#     park_out = models.CharField(max_length=100, blank=True)
#
#     class Meta:
#         db_table = 'xzz_search'

# Parking
class xzz_parking(models.Model):
    # parking_id = models.AutoField(primary_key=True)
    lot = models.CharField("Lot", max_length=10)
    spot = models.DecimalField("Spot", max_digits=3, decimal_places=0)
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
        return f"Parking {self.id}"


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
class xzz_ticket(models.Model):
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
        return f"Ticket {self.id}"



class xzz_attr_visi(models.Model):
    # r_id = models.AutoField(primary_key=True)
    r_in_time = models.DateTimeField("Time In")
    visitor = models.ForeignKey('xzz_visitor', on_delete=models.CASCADE, verbose_name="Visitor ID")
    attraction = models.ForeignKey('xzz_attraction', on_delete=models.CASCADE, verbose_name="Attraction ID")

    class Meta:
        db_table = 'xzz_attr_visi'
        verbose_name = 'Xzz Attr Visi'
        verbose_name_plural = 'Xzz Attr Visis'

    def __str__(self):
        return f"Attraction Visit {self.r_id}"



class xzz_orde_show(models.Model):
    # os_id = models.AutoField(primary_key=True)
    show = models.ForeignKey('xzz_show', on_delete=models.CASCADE, verbose_name="Show ID")
    order = models.ForeignKey('xzz_order', on_delete=models.CASCADE, verbose_name="Order ID")

    class Meta:
        db_table = 'xzz_orde_show'
        verbose_name = 'Xzz Orde Show'
        verbose_name_plural = 'Xzz Orde Shows'

    def __str__(self):
        return f"Order Show {self.id}"


class xzz_orde_stor(models.Model):
    # menu_item_id = models.AutoField(primary_key=True)
    menu_item_name = models.CharField("Menu Item Name", max_length=30)
    menu_item_description = models.CharField("Menu Item Description", max_length=100)
    menu_item_unit_price = models.FloatField("Menu Item Unit Price")
    store = models.ForeignKey('xzz_store', on_delete=models.CASCADE, verbose_name="Store ID")
    order = models.ForeignKey('xzz_order', on_delete=models.CASCADE, verbose_name="Order ID")

    class Meta:
        db_table = 'xzz_orde_stor'
        verbose_name = 'Xzz Orde Stor'
        verbose_name_plural = 'Xzz Orde Stors'

    def __str__(self):
        return self.menu_item_name

class xzz_user_login(models.Model):
    visitor_name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = 'xzz_user_login'
    def __str__(self):
        return self.email
