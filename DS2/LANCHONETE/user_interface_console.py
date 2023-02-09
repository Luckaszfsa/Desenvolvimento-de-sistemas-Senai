from user_interface import UserInterface


class UserInterfaceConsole:
    def __init__(self, user_interface: UserInterface) -> None:
        self.user_interface = user_interface

    def get_user_input_product_and_price(self) -> None:
        code_and_price = input(
            "Enter the code and quantity of the product to be purchased: ").split()

        result = self.user_interface.purchase(
            int(code_and_price[0]), int(code_and_price[1]))

        print(result)

        return result
