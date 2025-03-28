from behave import given, when, then

@given(u'varukorgen är tom')
def step_given_empty_basket(context):
    context.total_price = 0
    context.items = []
    print('basket is empty')

@when(u'användaren lägger till "Python 101" som kostar "200"')
def step_when_add_book(context):
    context.items.append('Python 101')
    context.total_price += 200
    print(context.items) # printing just for checking basket

@then(u'varukorgen ska innehålla "1" av "Python 101"')
def step_then_basket_have_book(context):
    assert len(context.items) is 1, 'Too few/many books in basket'
    print('So far basket is OK with 1 book')

@then(u'totalsumman ska vara "200"')
def step_then_check_final_basket(context):
    assert context.total_price is 200, 'Not correct total price'
    print('We made it!')

################    Scenario 2    ##############

@given(u'varukorgen innehåller 1 av "Python 101"')
def step_given_2_book(context):
    context.items = ['Python 101']
    context.total_price = 200

@when(u'användaren tar bort "Python 101"')
def step_when_remove_book(context):
    context.items.remove('Python 101')
    context.total_price -= 200

@then(u'varukorgen innehåller 0 av "Python 101"')
def step_given_check_1_book(context):
    assert context.items.count("Python 101") is 0, 'Too many books in cart'


@then(u'totalsumman ska vara 0')
def step_then_no_cost(context):
    print(f"Totalsumman is", {context.total_price})
    assert context.total_price is 0, "Total value incorrect"


################    Scenario 3    ##############

@given(u'varukorgen innehåller 1 av "Python 101" och 1 av "Data Science"')
def step_given_add_books(context):
    context.items = {
        "Python 101": 200,
        "Data Science": 200
    }
    context.total_price = sum(context.items.values())


@when(u'användaren tittar i varukorgen')
def step_when_user_check_basket(context):
    print(context.items.keys())


@then(u'varukorgen ska visa totalt 2 böcker')
def step_then_have_2_books(context):
    assert len(context.items.keys()) is 2, 'Basket items incorrect'


@then(u'totalsumman ska vara 400')
def step_then_total_price(context):
    # print(context.total_price)
    assert context.total_price == 400, 'Basket value incorrect'


################    Scenario 4    ##############


@given(u'varukorgen innehåller redan 1 av "Python 101"')
def step_given_prepare_basket(context):
    context.items = {
        "Python 101": {"pris": 200, "antal": 1}
    }


@when(u'användaren lägger till "Python 101" igen')
def step_when_add_again(context):
    if "Python 101" in context.items.keys():
        context.items["Python 101"]["antal"] +=1


@then(u'varukorgen ska innehålla 2 av "Python 101"')
def step_then_check_total_antal(context):
    assert context.items["Python 101"]["antal"] is 2, "Not correct amount of books"


################    Scenario 5    ##############

@given(u'varukorgen innehåller böcker')
def step_given_prepare_full_basket(context):
    context.items = {
        "Python 101": {"pris": 200, "antal": 1},
        "Dragonball Z": {"pris": 2000, "antal": 5}
    }


@when(u'användaren tömmer varukorgen')
def step_when_empty_basket(context):
    context.items.clear()


@then(u'varukorgen ska vara tom')
def step_then_empty_basker(context):
    assert len(context.items.keys()) == 0, "basket not empty"
