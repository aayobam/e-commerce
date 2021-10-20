from django.contrib.sessions.models import Session


class Cart():

    def __init__(self, request):

        self.session = request.session
        cart = self.session.get('cart-session')
        if "cart-session" not in self.session:
            cart = self.session['cart-session'] = {}
        else:
            self.cart = cart

    def add(self, product, product_qty):
        product_id = product.id
        if product_id not in self.cart:
            self.cart[product_id] = {'price': str(product.price), 'qty':int(product_qty)}
        self.session.modified = True


    def update_product_in_cart(self, request):
        pass

    def delete_product_from_cart(self, request):
        pass
