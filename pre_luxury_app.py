import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from datetime import datetime
import streamlit as st
from streamlit_option_menu import option_menu
import pickle
from PIL import Image
def seller_country_map(seller_country_encoded):
    country_map = {
        'Germany': 22,
        'Belgium': 8,
        'Spain': 74,
        'United States': 86,
        'United Kingdom': 85,
        'France': 19,
        'Ireland': 32,
        'Italy': 35,
        'Sweden': 76,
        'Romania': 64,
        'Cyprus': 14,
        'Monaco': 52,
        'China': 12,
        'Latvia': 41,
        'Poland': 60,
        'Finland': 18,
        'Croatia': 13,
        'Bulgaria': 10,
        'Netherlands': 55,
        'Luxembourg': 45,
        'Greece': 25,
        'Austria': 4,
        'Hong Kong': 28,
        'Portugal': 61,
        'Slovakia': 70,
        'Switzerland': 77,
        'Denmark': 16,
        'Estonia': 17,
        'Australia': 3,
        'Czech Republic': 15,
        'Japan': 36,
        'Norway': 58,
        'Hungary': 29,
        'Lithuania': 44,
        'Singapore': 69,
        'Philippines': 59,
        'Indonesia': 31,
        'Canada': 11,
        'Malta': 48,
        'Israel': 34,
        'Mexico': 50,
        'Russia': 65,
        'Slovenia': 71,
        'Malaysia': 47,
        'The Canary Islands': 80,
        'United Arab Emirates': 84,
        'Taiwan': 78,
        'South Korea': 73,
        'Brazil': 9,
        'Kazakhstan': 38,
        'Lebanon': 42,
        'Saudi Arabia': 67,
        'New Zealand': 56,
        'Albania': 0,
        'Turkey': 82,
        'Kuwait': 40,
        'Bahrain': 6,
        'Isle Of Man': 33,
        'Ukraine': 83,
        'Jersey': 37,
        'Thailand': 79,
        'Qatar': 62,
        'Liechtenstein': 43,
        'St Barthelemy': 75,
        'Guadeloupe': 26,
        'Nigeria': 57,
        'Mongolia': 53,
        'Macau': 46,
        'Andorra': 2,
        'Serbia': 68,
        'Tunisia': 81,
        'Belarus': 7,
        'Moldova': 51,
        'Algeria': 1,
        'San Marino': 66,
        'French Guiana': 20,
        'India': 30,
        'Morocco': 54,
        'South Africa': 72,
        'Georgia': 21,
        'Vietnam': 87,
        'Guernsey': 27,
        'Ghana': 23,
        'Gibraltar': 24,
        'Azerbaijan': 5,
        'Kenya': 39,
        'Martinique': 49,
        'Reunion': 63
    }
    return country_map.get(seller_country_encoded)
def product_gender_target_map(product_gender_target_binary):
     Gender_map={
          'Men':0,
          'Women':1
     }
     return Gender_map.get(product_gender_target_binary)
def product_category_map(product_category_encoded):
    Category_map={'Women Clothing':0, 'Men Clothing':1, 'Men Accessories':2,
       'Women Accessories':3, 'Men Shoes':4, 'Women Shoes':5
       }
    return Category_map.get(product_category_encoded)
def product_Season_map(product_season_encoded):
    Season_map = {
        'Autumn / Winter': 0,
        'All seasons': 1,
        'Spring / Summer': 2
    }
    return Season_map.get(product_season_encoded)

def product_condition_map(product_condition_encoded):
    Condition_map = {
        'Never worn': 0,
        'Never worn, with tag': 1,
        'Very good condition': 2,
        'Good condition': 3,
        'Fair condition': 4
    }
    return Condition_map.get(product_condition_encoded)

def product_Material_map(product_material_encoded):
    # Define the mapping from materials to encoded values
    material_map = {
        'Wool': 67,
        'Cotton': 8,
        'Polyester': 39,
        'Vegan leather': 59,
        'Cotton - elasthane': 9,
        'Silk': 46,
        'Synthetic': 55,
        'Lycra': 26,
        'Viscose': 62,
        'Denim - Jeans': 12,
        'Linen': 24,
        'Polyamide': 38,
        'Velvet': 60,
        'Leather': 23,
        'Cashmere': 3,
        'Lace': 22,
        'Glitter': 19,
        'Tweed': 57,
        'Vinyl': 61,
        'Suede': 54,
        'Mongolian Lamb': 29,
        'Raccoon': 43,
        'Rabbit': 42,
        'Fur': 17,
        'Cloth': 7,
        'Mink': 28,
        'Spandex': 50,
        'Faux fur': 15,
        'Fox': 16,
        'Python': 41,
        'Shearling': 45,
        'Exotic leathers': 14,
        'Plastic': 36,
        'Beaver': 2,
        'Patent leather': 32,
        'Alligator': 0,
        'Astrakhan': 1,
        'Ostrich': 31,
        'Sponge': 51,
        'Rubber': 44,
        'Crocodile': 10,
        'Chinchilla': 6,
        'Pony-style calfskin': 40,
        'Water snake': 63,
        'Eel': 13,
        'Wood': 66,
        'Gold': 20,
        'Lizard': 25,
        'Platinum': 37,
        'Not specified': 30,
        'Steel': 52,
        'Stingray': 53,
        'Metal': 27,
        'gold and steel': 69,
        'Ceramic': 4,
        'Titanium': 56,
        'Gold plated': 21,
        'Silver': 47,
        'Pink gold': 35,
        'White gold': 64,
        'Yellow gold': 68,
        'Crystal': 11,
        'Silver Plated': 49,
        'Wicker': 65,
        'Silver Gilt': 48,
        'Glass': 18,
        'Pearl': 33,
        'Chain': 5,
        'Pearls': 34,
        'Varan': 58
    }
    
    return material_map.get(product_material_encoded)
def color_map(product_color_encoded):
    # Define the mapping from colors to encoded values
    color_to_encoded = {
        'Grey': 13,
        'Navy': 17,
        'White': 24,
        'Black': 3,
        'Beige': 1,
        'Red': 21,
        'Green': 12,
        'Blue': 4,
        'Khaki': 14,
        'Multicolour': 16,
        'Metallic': 15,
        'Turquoise': 23,
        'Yellow': 26,
        'Brown': 6,
        'Pink': 19,
        'Ecru': 10,
        'Orange': 18,
        'Burgundy': 7,
        'Purple': 20,
        'Gold': 11,
        'Anthracite': 0,
        'Camel': 8,
        'Silver': 22,
        'Charcoal': 9,
        'Bordeaux': 5,
        'White / Black': 25,
        'camel': 28,
        'Beige / Grey': 2,
        'silver/black': 29,
        'brown/black': 27
    }
    return color_to_encoded.get(product_color_encoded)

def predict_price(product_like_count, buyers_fees, seller_products_sold,
                  seller_num_products_listed, seller_num_followers, seller_pass_rate,
                  product_type_encoded, brand_name_encoded,
                  product_gender_target_binary, product_category_encoded,
                  product_season_encoded, product_condition_encoded,
                  product_material_encoded, product_color_encoded, seller_country_encoded):

    # Process and encode input features
    product_like_count_1 = int(product_like_count)
    buyers_fees_1 = int(buyers_fees)
    seller_products_sold_1 = np.log(seller_products_sold)
    seller_num_products_listed_1 = np.log(seller_num_products_listed)
    seller_num_followers_1 = np.log(int(seller_num_followers))
    seller_pass_rate_1 = np.log(int(seller_pass_rate))
    
    product_type_encoded_1 = int(product_type_encoded)
    brand_name_encoded_1 = int(brand_name_encoded)
    product_gender_target_binary_1 = product_gender_target_map(product_gender_target_binary)
    product_category_encoded_1 = product_category_map(product_category_encoded)
    product_season_encoded_1 = product_Season_map(product_season_encoded)
    product_condition_encoded_1 = product_condition_map(product_condition_encoded)
    product_material_encoded_1 = product_Material_map(product_material_encoded)
    seller_country_1 = seller_country_map(seller_country_encoded)
    product_color_encoded_1 = color_map(product_color_encoded)

    # Load the model
    with open(r"PRE_OWNED_LUXURY.pkl", "rb") as f:
        regg_model = pickle.load(f)

    # Prepare data for prediction
    user_data = np.array([[product_like_count_1, buyers_fees_1, seller_products_sold_1,
                           seller_num_products_listed_1, seller_num_followers_1, seller_pass_rate_1,
                           product_type_encoded_1, brand_name_encoded_1, product_gender_target_binary_1,
                           product_category_encoded_1, product_season_encoded_1, product_condition_encoded_1,
                           product_material_encoded_1, product_color_encoded_1, seller_country_1]])

    # Make prediction
    y_pred_1 = regg_model.predict(user_data)
    price = np.exp(y_pred_1[0])

    return round(price)




st.title("SINGAPORE RESALE FLAT PRICES PREDICTING")
st.write("")

with st.sidebar:
    select= option_menu("MAIN MENU",[ "Price Prediction", "About"])

if select == "Home":
    pass
    # img= Image.open(r"C:\Users\vignesh\Desktop\New folder\ResaleFlatPrices\-1x-1.jpg")
    # st.image(img)

    # st.header("HDB Flats:")

    # st.write('''The majority of Singaporeans live in public housing provided by the HDB.
    # HDB flats can be purchased either directly from the HDB as a new unit or through the resale market from existing owners.''')
    
    # st.header("Resale Process:")

    # st.write('''In the resale market, buyers purchase flats from existing flat owners, and the transactions are facilitated through the HDB resale process.
    # The process involves a series of steps, including valuation, negotiations, and the submission of necessary documents.''')
    
    # st.header("Valuation:")

    # st.write('''The HDB conducts a valuation of the flat to determine its market value. This is important for both buyers and sellers in negotiating a fair price.''')
    
    # st.header("Eligibility Criteria:")

    # st.write("Buyers and sellers in the resale market must meet certain eligibility criteria, including citizenship requirements and income ceilings.")
    
    # st.header("Resale Levy:")

    # st.write("For buyers who have previously purchased a subsidized flat from the HDB, there might be a resale levy imposed when they purchase another flat from the HDB resale market.")
    
    # st.header("Grant Schemes:")

    # st.write("There are various housing grant schemes available to eligible buyers, such as the CPF Housing Grant, which provides financial assistance for the purchase of resale flats.")
    
    # st.header("HDB Loan and Bank Loan:")

    # st.write("Buyers can choose to finance their flat purchase through an HDB loan or a bank loan. HDB loans are provided by the HDB, while bank loans are obtained from commercial banks.")
    
    # st.header("Market Trends:")

    # st.write("The resale market is influenced by various factors such as economic conditions, interest rates, and government policies. Property prices in Singapore can fluctuate based on these factors.")
    
    # st.header("Online Platforms:")

    # st.write("There are online platforms and portals where sellers can list their resale flats, and buyers can browse available options.")

elif select == "Price Prediction":
    col1,col2= st.columns(2)
    with col1:
        product_type_encoded = st.number_input("Enter the Value of product type   (Min: 0/ Max: 467")
        brand_name_encoded = st.number_input("Enter the Value of brand type   (Min: 0/ Max: 612")
        product_gender_target_binary= st.selectbox("Select the Gender Type", ['Men','Women'])
        product_category_encoded= st.selectbox("Select the Category Type", ['Women Clothing', 'Men Clothing', 'Men Accessories','Women Accessories', 'Men Shoes', 'Women Shoes'])
        product_season_encoded= st.selectbox("Select the Season Type", ['Autumn / Winter', 'All seasons', 'Spring / Summer'])
        product_condition_encoded=  st.selectbox("Select the Season Type", ['Never worn', 'Very good condition', 'Never worn, with tag','Good condition', 'Fair condition'])
    
        product_material_encoded= st.selectbox("Select the Material Type", ['Wool', 'Cotton', 'Polyester', 'Vegan leather',
    'Cotton - elasthane', 'Silk', 'Synthetic', 'Lycra', 'Viscose',
    'Denim - Jeans', 'Linen', 'Polyamide', 'Velvet', 'Leather',
    'Cashmere', 'Lace', 'Glitter', 'Tweed', 'Vinyl', 'Suede',
    'Mongolian Lamb', 'Raccoon', 'Rabbit', 'Fur', 'Cloth', 'Mink',
    'Spandex', 'Faux fur', 'Fox', 'Python', 'Shearling',
    'Exotic leathers', 'Plastic', 'Beaver', 'Patent leather',
    'Alligator', 'Astrakhan', 'Ostrich', 'Sponge', 'Rubber',
    'Crocodile', 'Chinchilla', 'Pony-style calfskin', 'Water snake',
    'Eel', 'Wood', 'Gold', 'Lizard', 'Platinum', 'Not specified',
    'Steel', 'Stingray', 'Metal', 'gold and steel', 'Ceramic',
    'Titanium', 'Gold plated', 'Silver', 'Pink gold', 'White gold',
    'Yellow gold', 'Crystal', 'Silver Plated', 'Wicker', 'Silver Gilt',
    'Glass', 'Pearl', 'Chain', 'Pearls', 'Varan'])
        product_color_encoded= st.selectbox("Select the Color Type", ['Grey', 'Navy', 'White', 'Black', 'Beige', 'Red', 'Green', 'Blue',
    'Khaki', 'Multicolour', 'Metallic', 'Turquoise', 'Yellow', 'Brown',
    'Pink', 'Ecru', 'Orange', 'Burgundy', 'Purple', 'Gold',
    'Anthracite', 'Camel', 'Silver', 'Charcoal', 'Bordeaux',
    'White / Black', 'camel', 'Beige / Grey', 'silver/black',
    'brown/black'])
        seller_country_encoded= st.selectbox("Select the Country Type", ['Germany', 'Belgium', 'Spain', 'United States', 'United Kingdom',
    'France', 'Ireland', 'Italy', 'Sweden', 'Romania', 'Cyprus',
    'Monaco', 'China', 'Latvia', 'Poland', 'Finland', 'Croatia',
    'Bulgaria', 'Netherlands', 'Luxembourg', 'Greece', 'Austria',
    'Hong Kong', 'Portugal', 'Slovakia', 'Switzerland', 'Denmark',
    'Estonia', 'Australia', 'Czech Republic', 'Japan', 'Norway',
    'Hungary', 'Lithuania', 'Singapore', 'Philippines', 'Indonesia',
    'Canada', 'Malta', 'Israel', 'Mexico', 'Russia', 'Slovenia',
    'Malaysia', 'The Canary Islands', 'United Arab Emirates', 'Taiwan',
    'South Korea', 'Brazil', 'Kazakhstan', 'Lebanon', 'Saudi Arabia',
    'New Zealand', 'Albania', 'Turkey', 'Kuwait', 'Bahrain',
    'Isle Of Man', 'Ukraine', 'Jersey', 'Thailand', 'Qatar',
    'Liechtenstein', 'St Barthelemy', 'Guadeloupe', 'Nigeria',
    'Mongolia', 'Macau', 'Andorra', 'Serbia', 'Tunisia', 'Belarus',
    'Moldova', 'Algeria', 'San Marino', 'French Guiana', 'India',
    'Morocco', 'South Africa', 'Georgia', 'Vietnam', 'Guernsey',
    'Ghana', 'Gibraltar', 'Azerbaijan', 'Kenya', 'Martinique',
    'Reunion'])
        product_like_count= st.number_input("Enter the Value of product_like_count  (Min: 0 / Max: 46")

    with col2:

        buyers_fees= st.number_input("Enter the Value of buyer_fees  (Min: 1 / Max: 365")

        seller_products_sold= st.number_input("Enter the Value of selling_products  (Min: 1 / Max: 11586")

        seller_num_products_listed= st.number_input("Enter the Value of selling_products_num_listed  (Min: 1 / Max: 39627")

        seller_num_followers= st.number_input("Enter the Value of seller_num_followers (Min: 0 / Max: 20432)")
        
        seller_pass_rate = st.number_input("Enter the Value of seller_pass_rate   (Min: 65/ Max: 101")

    button= st.button("Predict the Price", use_container_width= True)

    if button:
        pre_price= predict_price(product_like_count,  buyers_fees, 
       seller_products_sold, seller_num_products_listed,
       seller_num_followers, seller_pass_rate, product_type_encoded,
       brand_name_encoded, product_gender_target_binary,
       product_category_encoded, product_season_encoded,
       product_condition_encoded, product_material_encoded,
       product_color_encoded, seller_country_encoded)

        st.write("## :green[**The Predicted Price is :**]",pre_price)


elif select == "About":

    st.header(":blue[Data Collection and Preprocessing:]")
    st.write("Collect a dataset of resale flat transactions from the Singapore Housing and Development Board (HDB) for the years 1990 to Till Date. Preprocess the data to clean and structure it for machine learning.")

    st.header(":blue[Feature Engineering:]")
    st.write("Extract relevant features from the dataset, including town, flat type, storey range, floor area, flat model, and lease commence date. Create any additional features that may enhance prediction accuracy.")
    
    st.header(":blue[Model Selection and Training:]")
    st.write("Choose an appropriate machine learning model for regression (e.g., linear regression, decision trees, or random forests). Train the model on the historical data, using a portion of the dataset for training.")

    st.header(":blue[Model Evaluation:]")
    st.write("Evaluate the model's predictive performance using regression metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), or Root Mean Squared Error (RMSE) and R2 Score.")

    st.header(":blue[Streamlit Web Application:]")
    st.write("Develop a user-friendly web application using Streamlit that allows users to input details of a flat (town, flat type, storey range, etc.). Utilize the trained machine learning model to predict the resale price based on user inputs.")

    st.header(":blue[Deployment on Render:]")
    st.write("Deploy the Streamlit application on the Render platform to make it accessible to users over the internet.")
    
    st.header(":blue[Testing and Validation:]")
    st.write("Thoroughly test the deployed application to ensure it functions correctly and provides accurate predictions.")
