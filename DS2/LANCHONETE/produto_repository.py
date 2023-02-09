from produto import Product


class ProductRepository:
    def __init__(self) -> None:
        self.products: Product = []

    def append(self, product: Product) -> None:
        self.products.append(product)

    def get(self, code: int) -> Product:
        for product in self.products:
            if (code == product.code):
                return product

    def check_if_product_exists(self, code: int) -> bool:
        for product in self.products:
            if (code == product.code):
                return True

        return False

    def __str__(self) -> str:
        formatText = "{0:<10} {1:<20} {2:<20}\n"
        menu = formatText.format("Code", "Name", "Price")

        for product in self.products:
            menu += formatText.format(product.code,
                                      product.description, f"$ {product.price}")

        return menu
