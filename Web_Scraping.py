import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

urls = [
    "https://www.amazon.in/Redmi-Chrome-Silver-Dimensity-5000mAh/dp/B0BBFKYH4N/?_encoding=UTF8&pd_rd_w=H514T&content-id=amzn1.sym.a591f53f-b25f-40ba-9fb6-d144bc8febfb&pf_rd_p=a591f53f-b25f-40ba-9fb6-d144bc8febfb&pf_rd_r=T01XDWT5E0199MVNGWPG&pd_rd_wg=hB9tl&pd_rd_r=8a6e487b-bf78-4a3d-9cbc-b42a44f702d4&ref_=pd_gw_ci_mcx_mr_hp_atf_m",
    "https://www.amazon.in/Levis-Brilliant-Graphic-Sweatshirt-58868-0006M_M_Yellow/dp/B09BG3MH97/ref=sr_1_5?qid=1674810998&rnid=6648218031&s=apparel&sr=1-5&th=1&psc=1",
    "https://www.amazon.in/gp/product/B0B4N6JVMW/ref=s9_acss_bw_cg_Header_3a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-6&pf_rd_r=92M5EQTTZ4T96W0HB8CA&pf_rd_t=101&pf_rd_p=d6951a2f-db29-4482-9ff6-78117265abd7&pf_rd_i=1375424031",
    "https://www.amazon.in/dp/B083NFZLP9/ref=s9_acsd_al_bw_c2_x_5_t?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-3&pf_rd_r=4CWMWT4CKXHEQFQEC124&pf_rd_t=101&pf_rd_p=db784737-6953-476c-b491-cda9975ee2f4&pf_rd_i=4859477031",
    "https://www.amazon.in/gp/product/B0B4SK9VX6/ref=s9_acss_bw_cg_Desktop_3b1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-1&pf_rd_r=XKES0MPN8KJ50TCPYWW0&pf_rd_t=101&pf_rd_p=5ed03dab-06ee-4e59-b856-3dd2a0758a96&pf_rd_i=1375392031",
    "https://www.amazon.in/3M-IA260166342-Auto-Specialty-Cleaner/dp/B00S5SB3LY/ref=sr_1_4?keywords=glass+cleaner&pf_rd_i=5257474031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=47d3e9a5-e01a-4010-a2fe-7aa79e02cbae&pf_rd_r=ZQ5VGQ6W91STRP5CAF0B&pf_rd_s=merchandised-search-6&pf_rd_t=101&qid=1674812879&s=automotive&sr=1-4",
    "https://www.amazon.in/dp/B00GTJSGXE/ref=s9_acsd_al_bw_c2_x_0_t?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-4&pf_rd_r=89QN5YB3SHK0PYDG4YAD&pf_rd_t=101&pf_rd_p=afbb015b-3229-4169-a018-469abebdfaea&pf_rd_i=1350380031&th=1"
    
]

data = []

for url in urls:
    HEADERS = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'
    }
    html = requests.get(url, headers=HEADERS).text
    soup = BeautifulSoup(html,'html.parser')
    title = soup.find('span', {'id':"productTitle"}).text.strip()
    price = soup.find('span',{'class': "a-price-symbol"}).text.strip()+ soup.find('span', {'class':"a-price-whole"}).text.strip()
    if '.' in price:
        price = price[0:price.index('.')]
    category = soup.find('div', {'id': "wayfinding-breadcrumbs_feature_div"}).text.strip()
    category = category[0:category.index('\n')]  
    with open('GSTMapper.csv') as file_obj:
      
    # Create reader object by passing the file 
    # object to reader method
        reader_obj = csv.reader(file_obj)
      
    # Iterate over each row in the csv 
    # file using reader object
        for row in reader_obj:
            for cell in row:
                if cell == category:
                    gst = row[1]
    product = {"Title":title,"Price":price,"Category":category, "GST Rate Applied": gst}
    data.append(product)

df = pd.DataFrame(data)
df.to_csv('ECommerce_Scrapped.csv')
print(df)   