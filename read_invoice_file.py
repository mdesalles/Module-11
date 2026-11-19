import csv
cust_no_input=input("Enter a customr no: ")
total=0.0
with open("invoices.csv", "r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        if row["cust_no"]==cust_no_input.upper():
            total+=float(row["inv_total"])
    print(f"Customer Number: {cust_no_input}, Total Invoice Amount: ${total:.2f}")