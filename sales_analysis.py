import pandas as pd
# =========================
# 1. Load Data
# =========================
print("Start")

df = pd.read_excel(
    "Sales_Performance_Portfolio_Project.xlsx",
    sheet_name="Raw_Data"
)

df = df.drop_duplicates(subset=["Order_ID"])
df["Order_Date"]=pd.to_datetime(df["Order_Date"])
columns=["Employee","Department","Product","Category","Channel","City"]
df[columns] = df[columns].apply(lambda x: x.str.strip().str.title())
df["Discount"]=df["Discount"].fillna(0)
df["Hours_Worked"]=df["Hours_Worked"].fillna(df["Hours_Worked"].mean())
employee_map = (
    df.dropna(subset=["Employee"])
      .drop_duplicates(subset=["Employee_Code"])
      .set_index("Employee_Code")["Employee"]
      .to_dict()
)
df["Employee"] = df["Employee"].fillna(
    df["Employee_Code"].map(employee_map)
)
df["City"]=df["City"].fillna("Unknown")

df["order_price"]=df["Unit_Price"]*df["Quantity"]
df["discount_price"]=df["order_price"]*df["Discount"]
df["total_sales"] = df["order_price"]-df["discount_price"]
average_sales = df["total_sales"].mean()
best_employee=df.groupby ("Employee")["total_sales"].sum().sort_values()
print("Best Employee is :",best_employee.tail(1))

employee_report = df.groupby("Employee").agg(
    Total_Sales=("total_sales", "sum"),
    Average_Sales=("total_sales", "mean"),
    Orders=("Order_ID", "count"),
    Total_Hours=("Hours_Worked", "sum")
).reset_index()
employee_report = employee_report.sort_values(
    by="Total_Sales",
    ascending=False
)

employee_report["worked_hours_per_sales"]=round(
    employee_report["Total_Sales"]/employee_report["Total_Hours"])

department_report=df.groupby("Department").agg(
    Total_Sales=("total_sales","sum"),
    average_sales=("total_sales","mean"),
    orders=("Order_ID","count")
).reset_index()
department_report=department_report.sort_values(
    by="Total_Sales",
    ascending=False
)
product_report=df.groupby("Product").agg(
    Total_sales=("total_sales","sum"),
    Total_sold_qty = ("Quantity","sum"),
    total_orders=("Order_ID","count")
).reset_index()
product_report = product_report.sort_values(
    by="Total_sales",
    ascending=False
)
Category_total_sales=df.groupby("Category")["total_sales"].sum()
channel_report=df.groupby("Channel")["total_sales"].sum()
city_total_sales=df.groupby("City")["total_sales"].sum()
df["Year"]=df["Order_Date"].dt.year
df["Month"]=df["Order_Date"].dt.month
monthly_sales=df.groupby("Month")["total_sales"].sum()

best_month = monthly_sales.idxmax()
monthly_report = monthly_sales.reset_index()
print("Top City:")
print(city_total_sales.sort_values(ascending=False).head(1))

print("Top Sales Channel:")
print(channel_report.sort_values(ascending=False).head(1))


print(
    monthly_sales.sort_values(ascending=False)
)
top10_orders_in_sales=df.groupby("Order_ID")["total_sales"].max()
print(top10_orders_in_sales.nlargest(10))
df["Sales_Level"]=df["total_sales"].apply(lambda x: "High" if x > average_sales else "Normal")

df["Sales_Level"].value_counts()


with pd.ExcelWriter("Sales_Final_Report.xlsx") as writer:
    df.to_excel(writer, sheet_name="Cleaned_Data", index=False)
    employee_report.to_excel(writer, sheet_name="Employee_Analysis", index=False)
    department_report.to_excel(writer, sheet_name="Department_Analysis", index=False)
    product_report.to_excel(writer, sheet_name="Product_Analysis", index=False)
    monthly_report.to_excel(
    writer,
    sheet_name="Monthly_Analysis",
    index=False
    )
    
