from functions import get_user_input, handle_input


print("☕ Espresso: $1.50")
print("☕ Latte: $2.50")
print("☕ Cappuccino: $3.00")

print()

while True:
    user_input = get_user_input()

    if user_input == "off":
        break
    else:
        handle_input(user_input)
