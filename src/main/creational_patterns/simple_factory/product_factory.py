from src.main.product import Product

class ProductFactory:
    """
    A simple factory class to handle the creation of Product instances.
    """

    @staticmethod
    def create_product(product_id, name, price, description, product_type='grocery'):
        """
        Factory method to create different types of products.

        :param product_id: The product's unique identifier
        :param name: The name of the product
        :param price: The price of the product
        :param description: The description of the product
        :param product_type: Type of the product (default is 'grocery')
        :return: A Product instance
        """
        if product_type == 'grocery':
            # Create and return a grocery product
            return Product(product_id, name, price, description)
        else:
            raise ValueError(f"Product type '{product_type}' not supported.")
