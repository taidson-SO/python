def apply_discount(price, discount):
    
    if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)):
        raise ValueError("Price and discount must be numbers.")
    
    if price < 0 or discount < 0:
        raise ValueError("Price and discount must be non-negative.")
    
    return price - (price * (discount / 100))

if __name__ == "__main__":
    try:
        print("\n" + "_-" * 25)
        product_name = input("\nEnter the product name: ")
        currency = input("Enter the currency (e.g., USD, EUR): ").strip().upper()
        price = float(input("Enter the original price: "))
        discount = float(input("Enter the discount percentage: "))
        
        final_price = apply_discount(price, discount)
        print(f"\n{'*' * 50}")
        print(f"The final price after applying a {discount}% discount is: {final_price} {currency}")
    except ValueError as e:
        print(e)

        
