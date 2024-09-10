from datetime import datetime


class Simulation:
    def create_user(self):
        pass

    def create_games(self):
        pass

    def start_simulation(self):
        pass



class CustomerManager:
    def customer(self):
        return []

    def authenticate_client(self, username, password):
        pass


class AdminManager:
    def admin(self):
        return []

    def authenticate_admin(self, username, password):
        pass



class LoginManager:
    def get_username(self):
        pass

    def get_password(self):
        pass

    def forget_password(self):
        pass

    def validate_account(self):
        pass



class Customer:
    def __init__(self, email, username, password, phone_number, age, address, postal_code, city):
        self.email = email
        self.username = username
        self.password = password
        self.phone_number = phone_number
        self.age = age
        self.address = address
        self.postal_code = postal_code
        self.city = city

    def sign_in(self):
        pass

    def sign_out(self):
        pass



class Admin:
    def __init__(self, id_admin, username, password):
        self.id_admin = id_admin
        self.username = username
        self.password = password

    def change_price(self, product, new_price):
        product.price = new_price

    def add_game(self, catalog, product):
        catalog.product.append(product)

    def delete_game(self, catalog, product):
        catalog.product.remove(product)

    def modify_description(self, product, new_description):
        product.description = new_description



class ProfileCustomer:
    def __init__(self):
        self.shopping_cart = []
        self.library = []

    def details_product(self, product):
        return str(product)

    def add_shoppingcart(self, product):
        self.shopping_cart.append(product)

    def purchase_product(self):
        pass
        



class Product:
    def __init__(self, id_game, name_game, description, price, genre, developer, release_date, ratings):
        self.id_game = id_game
        self.name_game = name_game
        self.description = description
        self.price = price
        self.genre = genre
        self.developer = developer
        self.release_date = release_date
        self.ratings = ratings

    def validate(self):
        
        return True



class Catalog:
    def __init__(self):
        self.product = []

    def search_product(self, product_name):
        for product in self.product:
            if product.name_game == product_name:
                return product
        return None

    def filter(self, criteria):
        pass



    def __init__(self):
        self.product = []

    def add_product(self, product):
        self.product.append(product)
        return f"Added {product.name_game} to cart."

    def delete_product(self, product):
        self.product.remove(product)
        return f"Deleted {product.name_game} from cart."

    def empty_products(self):
        self.product.clear()
        return "Cart emptied."

    def estimated_price(self):
        return sum([product.price for product in self.product])



class PurchasingManager:
    def __init__(self):
        self.vouchers = []
        self.downloads = []

    def generate_download_link(self, game):
        return f"Download link for {game.name_game}"

    def notify_customer(self):
        return "Customer notified."



class Downloads:
    def __init__(self, library, email, link_download):
        self.library = library
        self.email = email
        self.link_download = link_download

    def send_game(self):
        return f"Game sent to {self.email}"



class Voucher:
    def __init__(self, products, total_price, date, pay_method, id_number):
        self.products = products
        self.total_price = total_price
        self.date = date
        self.pay_method = pay_method
        self.id_number = id_number

    def save_purchase(self):
        return "Purchase saved."
