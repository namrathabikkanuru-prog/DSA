
# linear search
1.
def linear_search(patients_list,name):
    for item in patients_list:
        if item ["name"] == name:
            return (f"name:{item["name"]}, age:{item["age"]}, disease:{item["disease"]}")
        

patients_list = [{"name":"Arjun", "age": 34, "disease": "Fever"},
{"name":"Meena","age": 22, "disease": "Flu"},
{"name":"Ravi", "age": 45, "disease": "Diabetes"},
{"name":"Sneha","age": 29, "disease": "Migraine"} ]

print (linear_search(patients_list, "Ravi"))

 



2.

def display_products(products,threshold):
    
    result = "products eligible for 10% discount\n"

    for product in products:
        name = product[0]
        price = product[1]


        if price > threshold:

            discount_price = price - (price*0.10)
            
            result+= f" - {name}: rs{discount_price}\n"
    return result 

products = [("rice 5kg",450),("olive oil",850),("cornflakes",300),("almonds 500g", 650),
            ("detergent",520),("bread", 60)]
threshold = 500
print(display_products(products,threshold))           
