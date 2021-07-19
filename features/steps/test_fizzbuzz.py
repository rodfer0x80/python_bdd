from fizzbuzz.fizzbuzz_game import FizzBuzz
from behave import *

@when(u'the user enters {number}')
def step_impl(context, number):
    fb = FizzBuzz()
    context.result = fb.calculate(number)


@then(u'they should get "{expected_number}"')
def step_impl(context, expected_number):
    assert context.result == expected_number

@then(u'they should get the word "{word}"')
def step_impl(context, word):
    assert context.result == word