from faker import Faker
import pandas as pd
import numpy as np

# # Create a Faker instance
# fake = Faker()

# # Define a function to generate a row of data
# def generate_data():
#     return {
#         'supplierid':fake.id(),
#         'name': fake.name(),
#         'email': fake.email(),
#         'shareprice': fake.shareprice(),
#         'year': fake.year()
#         }

# # Generate a list of data
# data = [generate_data() for _ in range(1000)]

# # Convert the list to a DataFrame
# df = pd.DataFrame(data)

# # Print the DataFrame
# print(df)

synthetic_supp_data = Faker()

supplierName =[]
supplierId = []
supplierEmail = []
supplierSharePrice = []
supplierYear = []


recordCount: int=50000

for x in range(recordCount):
    supplierId.append(np.random.randint(1000,51000))
    supplierSharePrice.append(round(np.random.uniform(1,10000),2))
    supplierName.append(synthetic_supp_data.name())
    supplierEmail.append(synthetic_supp_data.email())
    supplierYear.append(synthetic_supp_data.year())


dfSupplier = pd.DataFrame({"supplierId":supplierId,"supplierName":supplierName,"supplierEmail":supplierEmail,"supplierSharePrice":supplierSharePrice,"supplierYear":supplierYear})

dfSupplier.to_csv("supplierdata.csv",index=False)



