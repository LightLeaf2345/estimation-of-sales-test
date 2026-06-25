import pandas as pd

sales = pd.read_csv("sales.csv")

print("2.1 List of products sold")
print(sales)
print("")

print("2.2 List of quantity sold against each product.")
print(sales.groupby(["product", "p_id"])[["qty"]].sum())
print("")

print("2.3 List of quantity and total sales against each product.")
product = pd.read_csv("products.csv")
my_sale = sales.groupby(["product", "p_id", "store"])[["qty"]].sum().reset_index()
my_sum = pd.merge(my_sale, product, on="p_id", how="left")
my_sum["total_sale"] = my_sum["qty"] * my_sum["price"]
print(my_sum)
print("")

print("2.4 List of quantity sold against each product and against each store.")
print(sales.groupby(["product", "p_id", "store"])[["qty"]].sum())
print("")

print("2.5 List of quantity sold against each Store with total turnover of the store.")
my_sum = pd.merge(sales, product, how="left", on=["p_id"])
my_sum["sales_total"] = my_sum["qty"] * my_sum["price"]
print(my_sum.groupby(["store"])[["qty", "sales_total"]].sum())
print("")

print("2.6 List of products which are not sold")
my_data = pd.merge(sales, product, on="p_id", how="right")
# print(my_data['sale_id'].isna())
my_data = my_data[my_data["sale_id"].isnull()]  # products which are not sold
print(my_data)
# print(my_data.loc[:,'product_y']) # to display only produts column
print("")

print("2.7 List of customers who have not purchased any product.")
customer=pd.read_csv("customer.csv")
my_data=pd.merge(sales,customer,on='c_id',how='right')
my_data=my_data[my_data['sale_id'].isnull()] # products which are not sold
#print(my_data)
print(my_data.loc[:,'Customer']) # to display customers who has not purchased
print("")
