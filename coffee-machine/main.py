# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tehuanmelo <tehuanmelo@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/18 11:11:06 by tehuanmelo        #+#    #+#              #
#    Updated: 2022/09/19 12:33:28 by tehuanmelo       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import data
import time
import time
import art


def check_resources(coffee):
    if coffee:
        if data.resources['water'] < data.MENU[coffee]['ingredients']['water'] or data.resources['coffee'] < data.MENU[coffee]['ingredients']['coffee']:
            return False
    if coffee == 'latte' or coffee == 'cappuccino':
        if data.resources['milk'] < data.MENU[coffee]['ingredients']['milk']:
            return False
    return True


def make_coffee():
    message = "Making coffee "
    for i in range(4):
        os.system('clear')
        print(art.logo)
        print(art.coffee_machine)
        print(message)
        message += "."
        time.sleep(2)
    os.system('clear')
    print(art.logo)
    print(art.coffee)
    print("Enjoy your coffee!")


def reset_stock(coffee):
    for key, value in data.MENU[coffee]["ingredients"].items():
        data.resources[key] -= value
    data.profit += data.MENU[coffee]["cost"]


def check_money(coffe_cost):
    coins = input(f"Price: ${coffee_cost}\nInsert coins: e.g. 4 quarter ").split(" ")
    for key, value in data.coins.items():
        if coins[1] == key:
            return int(coins[0]) * value
    return 0


def calculate_change(money, cost):
    if money > cost:
        change = money - cost
    return round(change, 2)


def print_report():
    os.system('clear')
    print(art.logo)
    print(f"Water = {data.resources['water']}ml")
    print(f"Milk = {data.resources['milk']}ml")
    print(f"Coffee = {data.resources['water']}mg")
    print(f"Money = ${data.profit}\n")


os.system('clear')
print(art.logo)
machine_is_on = True

while machine_is_on:

    customer_coffee = input("​What would you like? (espresso/latte/cappuccino) ")
    if customer_coffee == 'off':
        os.system("clear")
        exit()
    elif customer_coffee == 'report':
        print_report()
    elif customer_coffee in data.MENU.keys():
        os.system('clear')
        print(art.logo)
        ingredients = check_resources(customer_coffee)
        if not ingredients:
            print(f"No ingredients found for {customer_coffee}")
        else:
            coffee_cost = data.MENU[customer_coffee]['cost']
            money = check_money(coffee_cost)
            if money >= coffee_cost:
                make_coffee()
                reset_stock(customer_coffee)
                change = calculate_change(money, coffee_cost)
                if change:
                    print(f"Take your change ${change}")
            else:
                os.system('clear')
                print(art.logo)
                if money > 0:
                    print(f"Not enough money\nTake your money ${money}")
                else:
                    print(f"No money iserted!")
    else:
        print("Invalid entry type it again")
