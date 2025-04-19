from behave import when, then, given
from io import StringIO
import contextlib

### Del 2 uppgift rabbat ###
def calculate_discount_pris(cart):
    total_price = 0
    discount = 0.1 # 10%
    amount_of_books = 0
    for k,v in cart.items():
        amount_of_books += v["antal"]


    for k,v in cart.items():
        total_price += v["pris"] * v["antal"]

    if amount_of_books >= 3:
        total_price -= total_price * discount

    return total_price

@when(u'användaren lägger till 2 av "Python 101" som kostar "200"')
def step_when_add_python(context):
    context.items = {
        "Python 101": {"pris": 200, "antal": 2}
    }

@when(u'användaren lägger till 3 av "Dragonball Z" som kostar "150"')
def step_when_add_dbz(context):
    new_book = {"Dragonball Z": {"pris": 150, "antal": 3}}
    context.items.update(new_book)


@then(u'totalsumman ska vara 765')
def step_then_total_price(context):
    assert calculate_discount_pris(context.items) == 765, "Incorrect total value"


### Del 2 uppgift lagerstatus ###

def buy_from_stock(stock, book, amount):
    if book not in stock.keys():
        raise ValueError("Book not in stock")
    if stock[book] > amount:
        stock[book] -= amount
        print("Boken lades i varukorgen")
        return {book: amount} # Return a new dict with the desired amount of books to purchase
    elif stock[book] == amount:
        print("Boken lades i varukorgen")
        return {book: stock.pop(book)} # Returns and remove the book from stock
    else:
        print(f"Endast {stock[book]} exemplar i lager")
        return {book: stock.pop(book)} # Returns and remove the book from stock also

@given(u'lagret innehåller "5" av "Python 101"')
def step_define_stock_and_cart(context):
    context.stock = {
        "Python 101": 5,
        "Dragonball Z": 2
    }
    context.cart = {}

@when(u'användaren försöker köpa "3" av "Python 101"')
def step_when_buy_ok_book(context):
    fake_out = StringIO()
    with contextlib.redirect_stdout(fake_out):
        context.cart = buy_from_stock(context.stock, "Python 101", 3)
    context.message_ok = fake_out.getvalue().strip()

@then(u'varukorgen ska innehålla "3" av "Python 101"')
def step_then_stock_(context):
    assert context.cart["Python 101"] == 3, "Incorrect amount of books in cart"


@then(u'ett meddelande ska visas Boken lades i varukorgen')
def step_then_show_success_message(context):
    assert context.message_ok == 'Boken lades i varukorgen', "Incorrect message"


@given(u'lagret innehåller "2" av "Dragonball Z"')
def step_given_dbz_stock(context):
    context.stock = {
        "Python 101": 5,
        "Dragonball Z": 2
    }
    context.cart = {}

@when(u'användaren försöker köpa "5" av "Dragonball Z"')
def step_when_buy_too_many_dbz(context):
    fake_out = StringIO()
    with contextlib.redirect_stdout(fake_out):
        context.cart = buy_from_stock(context.stock, "Dragonball Z", 5)
    context.message_not_ok = fake_out.getvalue().strip()

@then(u'varukorgen ska innehålla "2" av "Dragonball Z"')
def step_then_cart_contain_dbz(context):
    assert context.cart["Dragonball Z"] == 2, "Power level too low" # Should be 2 books even if we try to buy 5. stock is only 2

@then(u'ett meddelande ska visas Endast 2 exemplar i lager')
def step_then_show_information(context):
    assert context.message_not_ok == "Endast 2 exemplar i lager", "INcorrect information message"

### Del 2 uppgift inloggning krävs ###

#Copy from above function but with login requirement

def buy_from_stock_login(stock, book, amount, login=False):
    if not login:
        raise PermissionError("Du måste logga in först")
    if book not in stock.keys():
        raise ValueError("Book not in stock")
    if stock[book] > amount:
        stock[book] -= amount
        print("Boken lades i varukorgen")
        return {book: amount} # Return a new dict with the desired amount of books to purchase
    elif stock[book] == amount:
        print("Boken lades i varukorgen")
        return {book: stock.pop(book)} # Returns and remove the book from stock
    else:
        print(f"Endast {stock[book]} exemplar i lager")
        return {book: stock.pop(book)} # Returns and remove the book from stock also

@when(u'användaren försöker köpa en bok utan att vara inloggad')
def step_when_user_buy_no_login(context):
    context.stock = {"Dragonball Z": 2, "Python 101": 5}  # Define stock
    fake_out = StringIO()

    with contextlib.redirect_stdout(fake_out):  # Capture print output
        try:
            context.cart = buy_from_stock_login(context.stock, "Dragonball Z", 1, login=False)
        except PermissionError as e:
            context.error_message = str(e)  # Store exception message

@then(u'ett meddelande ska visas Du måste logga in först')
def step_then_get_error_msg(context):
    assert context.error_message == "Du måste logga in först", "Login incorrect"

### Del 2 uppgift login med credentials


def login_func(username, password):
    correct_username = 'user1'
    correct_password = 'password' # Much secure, very wow

    if username == correct_username and password == correct_password:
        return True
    else:
        return False


@when(u'en användare med användarnamn "user1" och lösenord "password"')
def step_when_try_successful_login(context):
    context.login_attempt = login_func('user1', 'password')


@then(u'inloggningen ska vara "lyckad"')
def step_then_successful_login(context):
    assert context.login_attempt is True, "Login was incorrect when it should have been"

@when(u'en användare med användarnamn "user2" och lösenord "fel"')
def step_when_try_unsuccessful_login(context):
    context.login_attempt = login_func('user2', 'fel')

@then(u'inloggningen ska vara "misslyckad"')
def step_then_login_failed(context):
    assert context.login_attempt is False, "Login was successful when it shouldnt have been"