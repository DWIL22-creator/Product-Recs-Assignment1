from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.
print("Step 1: Products in the catalog..\n")
i = 0
for product in products:
    print(f"Product {i + 1}: {product}")
    i += 1

# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.
customer_preferences = []

response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    customer_preferences.append(preference)
    print(f"Your preference list includes: {customer_preferences}")

    response = input("Do you want to add another preference? (Y/N): ").upper()
  
# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
set_preferences = set(customer_preferences) #Elimates duplicates from the list and converts it to a set.
#print(f"Set preferences: {set_preferences}")
print()

# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []

for product in products:
    user_entry = {'name': product['name'], 'tags': set(product['tags'])}
    #if product in customer_preferences: #If the product is in the customer preference, add it to the user entry list.
    converted_products.append(user_entry)

# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    count = 0
  
    for product in product_tags:
        if  product in customer_tags:
            count+=1
    return count

# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_preferences):
    recommendations = []
    i = 0
    print("Recommended Products:\n")
    for product in products:
        countof_matches = count_matches(product['tags'], customer_preferences)
        if countof_matches > 0 and countof_matches != 0:
            i+= 1
            recommendations.append(f"{product['name']}: ({countof_matches} match(es))\n")
            print(f"- {recommendations[i-1]}")
        
    if len(recommendations) == 0:
        return "No products match your preferences."
    
    #Args:
        #products (list): A list of product dictionaries.
        #customer_tags (set): A set of tags associated with the customer.
    #Returns:
        #list: A list of products containing product names and their match counts.
    


# TODO: Step 7 - Call your function and print the results
recommend_products(converted_products, set_preferences)



# DESIGN MEMO (write below in a comment):

# 1. What core operations did you use (e.g., intersections, loops)? Why?
#The core operations I used in my code are loops, if statements, functions, lists, sets, and dictionaries.  
# I used loops to iterate through the products and customer preferences, if statements to check the matches, functions to focus on several tasks, and lists to store edit the products and cutomer preferences.
#Dictionaries allow you to store the product name and add tags to certain products. But sets are important because they eliminate dupliates in the list. For example, if a customer enters the same preference twice, the set_preferences set eliminates the duplicate.
#If I were to do this assignment again, I would've used intersection to find the matches between product tags and customer preferences to simplify the code.

# 2. How might this code change if you had 1000+ products?
#If I had 1000+ products, I would want to use a query to upload all the products via csv file and filter the data.
#Also, I think I could use lists and dictionaries again, but to make the information more readable, I would create a different list every couple of products to make it easier to read.
#But I feel like the query would be the best option.
