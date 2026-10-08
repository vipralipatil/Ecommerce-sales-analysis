# E-Commerce Sales Analysis
# Created by Viprali Liladhar Patil

products = {
    "Laptop": 5,
    "Mobile": 12,
    "Headphones": 8,
    "Smartwatch": 6
}

prices = {
    "Laptop": 50000,
    "Mobile": 20000,
    "Headphones": 3000,
    "Smartwatch": 5000
}

print("E-COMMERCE SALES ANALYSIS")
print("-------------------------")

total_sales = 0

for product in products:
    sales = products[product] * prices[product]
    total_sales += sales
    print(product, "Sales: ₹", sales)

print("-------------------------")
print("Total Sales: ₹", total_sales)
