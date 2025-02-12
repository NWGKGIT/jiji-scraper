import requests
import pandas as pd

query = input("Search Bar: ")
num_products = int(input("Enter number of products to get: "))

base_url = "https://jiji.com.et/api_web/v1/listing"
data_list = []

scraped_count = 0
next_url = f"{base_url}?query={query}&init_page=true&page=1&webp=false&po=18.z.z.z.i&lsmid=1739390677188"

while scraped_count < num_products and next_url:
    response = requests.get(next_url)
    response.raise_for_status()
    data = response.json()

    adverts = data.get('adverts_list', {}).get('adverts', [])
    next_url = data.get('next_url')

    if not adverts:
        print("No products found")
        break

    for advert in adverts:
        if scraped_count >= num_products:
            break
        
        data_list.append({
            'product_name': advert.get('title'),
            'price': advert.get('price_title'),
            'category': advert.get('category_name'),
            'status': advert.get('status'),
            'location': advert.get('region_item_text'),
            'link': 'https://jiji.com.et' + advert.get('url')
        })
        scraped_count += 1

# Save to Excel (jiji_products.xlsx)
df = pd.DataFrame(data_list)
df.to_excel('jiji_products.xlsx', index=False)

print(f"Scraped {scraped_count} products and saved to jiji_products.xlsx")