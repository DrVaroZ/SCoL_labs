from decimal import Decimal
from django.conf import settings
from car_rent.models import Car
from discounts.models import Discount


class Cart(object):

    def __init__(self, request):
        """
        Initializing cart
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

        # saving current applied discount
        self.discount_id = self.session.get('discount_id')

    def add(self, car, quantity=1, update_quantity=False):
        """
        Add car to cart and update amount
        """
        car_id = str(car.id)
        if car_id not in self.cart:
            self.cart[car_id] = {'quantity': 0,
                                 'rent_per_day': str(car.rent_per_day)}
        if update_quantity:
            self.cart[car_id]['quantity'] = quantity
        else:
            self.cart[car_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Updating cart session
        self.session[settings.CART_SESSION_ID] = self.cart
        # Cancel session "changed", to be sure that it is saved
        self.session.modified = True

    def remove(self, car):
        """
        Removing car from cart
        """
        car_id = str(car.id)
        if car_id in self.cart:
            del self.cart[car_id]
            self.save()

    def __iter__(self):
        """
        Iterating through elements in cart and getting cars from database
        """
        car_ids = self.cart.keys()
        # getting car objects and adding them to cart
        cars = Car.objects.filter(id__in=car_ids)
        for car in cars:
            self.cart[str(car.id)]['car'] = car

        for item in self.cart.values():
            item['rent_per_day'] = Decimal(item['rent_per_day'])
            item['total_price'] = item['rent_per_day'] * item['quantity']
            yield item

    def __len__(self):
        """
        Counting all elements in cart
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Counting total price of elements in cart
        """
        return sum(Decimal(item['rent_per_day']) * item['quantity'] for item in
                   self.cart.values())

    def clear(self):
        # removing cart from session
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    @property
    def discount(self):
        if self.discount_id:
            return Discount.objects.get(id=self.discount_id)
        return None

    def get_discount(self):
        if self.discount:
            return (self.discount.discount / Decimal('100')) * self.get_total_price()
        return Decimal('0')

    def get_total_price_after_discount(self):
        return self.get_total_price() - self.get_discount()
