from ecommerceapp.models import Product
from decimal import Decimal
from django.shortcuts import redirect




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
    
    # Ensure the changes made were effected and updated from the backend
    def save(self):
        self.session.modified = True

    def add(self, product, product_qty):
        """
            This generates a session for each user, each session has a session id and session data
            the session data in this case are the products been added to the cart by the user.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]["qty"] = product_qty
        else:
            self.cart[product_id] = {'price': str(product.price), 'qty':int(product_qty)}
        self.save()

    def __iter__(self):
        """
        This function returns all items in the cart.
        Returns total amount of each items added.
        """
        #gets product data keys e.g price, quantity
        product_ids = self.cart.keys()

        #checks if the product exist in the database by filtering by product_ids
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        #loop through the products 1 by 1 and re-assigns them to the product.id in the cart
        for product in products:
            cart[str(product.id)]["product"] = product

        # get price and quatity of items and mutiplies price by quantity to get total price of items
        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["qty"]
            yield item

    def __len__(self):
        """
        Get the cart data and count and returns the quantity of all products in the cart.
        """
        return sum(item['qty'] for item in self.cart.values())

    def get_total_price(self):
        """
        Returns the overral cumulative price of all the products in the cart.
        """
        return sum(Decimal(item["price"]) * item["qty"] for item in self.cart.values())

    def delete(self, product):
        """
        Deletes item from session data using product_id, 
        the rest were handled at the ajax codes.
        """
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()
    
    
    def update(self, product, qty):
        """
        Updates values in sessiondata of items in the cart e.g quantity 
        and automatically calculates the price.
        """
        product_id = str(product)
        if product_id in self.cart:
            self.cart[product_id]['qty'] = qty
        self.save()

