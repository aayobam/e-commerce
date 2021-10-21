from ecommerceapp.models import Product
from decimal import Decimal




class Cart():

    def __init__(self, request):
        """
        create a session for each user, if a user already has a session, do nothing
        but if a user doesn't have a session, then create session for the user.
        """
        self.session = request.session
        cart = self.session.get('cart-session')
        if "cart-session" not in self.session:
            cart = self.session['cart-session'] = {}
        else:
            self.cart = cart

    def add(self, product, product_qty):
        """
            This generates a session for each user, each session has a session id and session data
            the session data in this case are the products been added to the cart by the user.
        """
        product_id = product.id
        if product_id not in self.cart:
            self.cart[product_id] = {'price': str(product.price), 'qty':int(product_qty)}
            print("cart detail : ", self.cart)
        self.session.modified = True

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]["product"] = product

        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["qty"]
            yield item

    def __len__(self):
        """
            Get the cart data and count the quantity of all products in the cart.
        """
        return sum(item['qty'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item["price"]) * item["qty"] for item in self.cart.values())

    def update_product_in_cart(self, request):
        pass

    def delete_product_from_cart(self, request):
        pass
