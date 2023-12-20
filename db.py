import os
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def get_purchases(latest=False):
    if latest:
        purchases = supabase.table('purchases').select('*').order('created_at', desc=True).limit(1).single().execute()
    purchases = supabase.table('purchases').select("*").execute()
    print(purchases)
    return purchases

def get_customers(name = None, email = None):
    if name is None:
        name = ''
    if email is None:
        email = ''
    if len(name) == 0 and len(email) == 0:
        customers = supabase.table('customers').select('*').execute()
        return customers
    if len(email) > 0:
        customers = supabase.table('customers').select('*').eq("email", email).maybe_single().execute()
        return customers
    if len(name) > 0:
        customers = supabase.table('customers').select('*').eq("name", name).maybe_single().execute()
        return customers
    return None

def get_products():
    products = supabase.table('products').select('*').execute()
    print(products)
    return products

def insert_customer(purchase):
    customer = {}
    customer['name'] = purchase.supporter_name
    customer['email'] = purchase.supporter_email
    new_customer = supabase.table('customers').insert(customer).execute()
    print("Inserted...")
    print(new_customer)
    return new_customer

def insert_purchase(purchase):
    """Insert customer, product ref, notes, customer answer message"""
    order = {}
    order["customer"] = get_customers(email = purchase.supporter_email)
    order["product"] = get_products(name = purchase.data.extras[0].title)
    order["notes"] = purchase.support_note
    order["customer_message"] = purchase.data.extras[0].question_answers
    new_purchase = supabase.table('purchases').insert(order).execute()
    print(new_purchase)
    return new_purchase

if __name__ == '__main__':
    get_purchases()
    get_customers()
    get_products()