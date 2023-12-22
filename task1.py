import requests

url = 'https://s3.amazonaws.com/open-to-cors/assignment.json'
response = requests.get(url)

if response.status_code == 200:
    try:
        data = response.json()
        products_dict = data.get('products')

        if products_dict:
            
            products_list = []
            for product_id, product_info in products_dict.items():
                product = {
                    'ID': product_id,
                    'Title': product_info.get('title'),
                    'Price': product_info.get('price'),
                    'Popularity': product_info.get('popularity')
                }
                products_list.append(product)

            # Sorting products by descending popularity
            sorted_products = sorted(products_list, key=lambda x: int(x.get('Popularity', 0)), reverse=True)

            for product in sorted_products:
                print(f"ID: {product['ID']} - Title: {product['Title']} - Price: {product['Price']} - Popularity: {product['Popularity']}")
        else:
            print('No products found in the data')
    except ValueError as e:
        print('Failed to parse JSON:', e)
else:
    print('Failed to fetch data')