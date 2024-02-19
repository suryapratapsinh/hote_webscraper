import pandas as pd
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windos NT 6.3; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
def booking():
    webpage = requests.get('https://www.booking.com/searchresults.en-gb.html?ss=Gandhinagar&ssne=Gandhinagar&ssne_untouched=Gandhinagar&efdco=1&label=gen173nr-1BCAEoggI46AdIM1gEaGyIAQGYAQm4ARfIAQzYAQHoAQGIAgGoAgO4ArG9-KYGwAIB0gIkZjdjMWNkMzEtMGYxNi00MzY5LTg5MzQtMjU4ZGE4MGI5NDEz2AIF4AIB&sid=2395d9586d4e8c565b691b883a9a2590&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=-2095816&dest_type=city&checkin=2023-11-11&checkout=2023-11-12&group_adults=2&no_rooms=1&group_children=0', headers=headers).text
    soup = BeautifulSoup(webpage, "html.parser")
    names = soup.find_all("div",class_="f6431b446c a15b38c233")
    price = soup.find_all("span",class_="f6431b446c fbfd7c1165 e84eb96b1f")
    hotel_name=[]
    hotel_prices=[]
    for i in names:
        Name = i.text
        hotel_name.append(Name)
    for i in price:
        Price = i.text
        hotel_prices.append(Price)
    df = pd.DataFrame({"hotel_Name":hotel_name ,"hotel_price":hotel_prices})
    print(df)
    df.to_csv("C:/Users/User/Desktop/hotel_dekho_booking.csv", encoding='utf-8')

def ebooking():
    webpage = requests.get('https://hotel.ebooking.com/searchresults.en-gb.html?aid=7908003&label=1cff80ab-6285-48a5-b008-560690dfe086%7C&sid=7675f8e9f951fe362051abb8fcec7c83&sb=1&src=searchresults&src_elem=sb&error_url=https%3A%2F%2Fhotel.ebooking.com%2Fsearchresults.en-gb.html%3Faid%3D7908003%26label%3D1cff80ab-6285-48a5-b008-560690dfe086%257C%26sid%3D7675f8e9f951fe362051abb8fcec7c83%26tmpl%3Dsearchresults%26checkin_month%3D8%3Bcheckin_monthday%3D22%3Bcheckin_year%3D2023%3Bcheckout_month%3D10%3Bcheckout_monthday%3D23%3Bcheckout_year%3D2023%3Bcity%3D-2095816%3Bclass_interval%3D1%3Bdest_id%3D-2095816%3Bdest_type%3Dcity%3Bfrom_sf%3D1%3Bgroup_adults%3D2%3Bgroup_children%3D0%3Blabel_click%3Dundef%3Bno_rooms%3D1%3Boffset%3D0%3Braw_dest_type%3Dcity%3Broom1%3DA%252CA%3Bsb_price_type%3Dtotal%3Bshw_aparth%3D1%3Bslp_r_match%3D0%3Bsrc%3Dsearchresults%3Bsrc_elem%3Dsb%3Bsrpvid%3D878355012fc501a8%3Bss%3DGandhinagar%3Bssb%3Dempty%3Bssne%3DGandhinagar%3Bssne_untouched%3DGandhinagar%26%26&ss=Gandhinagar&is_ski_area=0&ssne=Gandhinagar&ssne_untouched=Gandhinagar&city=-2095816&checkin_year=2023&checkin_month=11&checkin_monthday=22&checkout_year=2023&checkout_month=11&checkout_monthday=23&group_adults=2&group_children=0&no_rooms=1&from_sf=1',headers=headers).content
    soup = BeautifulSoup(webpage, "html.parser")
    names = soup.find_all("div", class_="f6431b446c a15b38c233")
    price = soup.find_all("span", class_="f6431b446c fbfd7c1165 e84eb96b1f")
    hotel_name = []
    hotel_prices = []
    for i in names:
        Name = i.text
        hotel_name.append(Name)
    for i in price:
        Price = i.text
        hotel_prices.append(Price)
    df = pd.DataFrame({"hotel_Name": hotel_name, "hotel_price": hotel_prices})
    print(df)
    df.to_csv("C:/Users/User/Desktop/hotel_dekho_ebooking.csv", encoding='utf-8')

def merge():
    # Read the two CSV files
    file1 = pd.read_csv("C:/Users/User/Desktop/hotel_dekho_booking.csv")
    file2 = pd.read_csv("C:/Users/User/Desktop/hotel_dekho_ebooking.csv")
    # Merge the two dataframes based on the 'hotel_Name' column
    merged_data = pd.merge(file1, file2, on='hotel_Name', how='inner')
    # Create a new dataframe with common hotel names and their prices
    common_hotel_prices = pd.DataFrame({'hotel_Name': merged_data['hotel_Name'],'booking': merged_data['hotel_price_x'],'hotel_ebooking': merged_data['hotel_price_y']})
    #print(common_hotel_prices)
    # Write the merged hotel names and prices to a new CSV file
    common_hotel_prices.to_csv("C:/Users/User/Desktop/Project/Project-II/scrapper/src/assets/merged_hotel_prices.csv", index=False)
    print("Merged hotel names and prices saved to 'merged_hotel_prices.csv'")

booking()
ebooking()
merge()