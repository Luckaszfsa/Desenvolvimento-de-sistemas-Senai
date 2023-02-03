from produto import Product
from produto_service import ProductService


class UserInterface:
    def __init__(self, product_service: ProductService) -> None:
        self.product_service = product_service

    def purchase(self, code: int, quantity: int) -> str:
        product = self.product_service.get_product(code)

        if (product == None):
            return "Product not found..."

        return "Total: {0}".format(self.product_service.purchase(product, quantity))
