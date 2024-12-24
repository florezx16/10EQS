Inventory report

# Low stock products
                     product_name  our_price   category  current_stock  restock_threshold last_update
3   "Yerba Mate Loose Leaf (1lb)"      12.99  beverages              5                 10  2024-11-01
7       "Chamomile Tea (30 bags)"       6.99        tea             12                 15  2024-11-05
9      "Decaf Coffee Beans (1lb)"      15.99  beverages             15                 15  2024-11-13
10           "Mint Tea (25 bags)"       7.49  beverages              0                 12  2024-10-30

# Productos without stock
            product_name  our_price   category  current_stock  restock_threshold last_update
10  "Mint Tea (25 bags)"       7.49  beverages              0                 12  2024-10-30

# latest updates
                       product_name  our_price   category  current_stock  restock_threshold last_update
2          "Masala Chai Mix (12oz)"       9.99  beverages             18                 15  2024-11-18
6            "Espresso Beans (1lb)"      16.99  beverages             22                 20  2024-11-16
8   "Matcha Green Tea Powder (4oz)"      19.99  beverages              8                  0  2024-11-17
11           "Instant Coffee (8oz)"      11.99     coffee             25                 20  2024-11-19
13          "cold brew concentrate"      13.99  beverages             19                 15  2024-11-20

# Price anaylsis
count    14.000000
mean     11.455000
std       5.061187
min       0.000000
25%       8.240000
50%      11.990000
75%      14.740000
max      19.990000
Name: our_price, dtype: float64

# Free products?
               product_name  our_price   category  current_stock  restock_threshold last_update
12  "Rooibos Tea (40 bags)"        0.0  beverages             30                 20  2024-11-08
