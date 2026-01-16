import streamlit as st
import pandas as pd
import pickle
from datetime import datetime

st.set_page_config(
    page_title="Flight Price Prediction",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=DM+Sans:wght@400;500;700&display=swap');
    
    .stApp {
        background: linear-gradient(180deg, #e8f4fc 0%, #d0e8f7 30%, #b8dcf0 60%, #f5f9fc 100%);
        font-family: 'DM Sans', sans-serif;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }
    
    .main-header {
        text-align: center;
        padding: 2rem 0 1rem 0;
    }
    
    .main-header h1 {
        font-family: 'Poppins', sans-serif;
        font-size: 2.8rem;
        font-weight: 700;
        color: #1a5276;
        margin-bottom: 0.5rem;
        letter-spacing: -0.5px;
    }
    
    .main-header p {
        color: #5d8aa8;
        font-size: 1.1rem;
        font-weight: 400;
    }
    
    .plane-icon {
        font-size: 3rem;
        margin-bottom: 0.5rem;
    }
    
    .custom-card {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 8px 32px rgba(26, 82, 118, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.6);
        margin-bottom: 1.5rem;
    }
    
    .card-title {
        font-family: 'Poppins', sans-serif;
        font-size: 1.3rem;
        font-weight: 600;
        color: #1a5276;
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(255, 255, 255, 0.5);
        padding: 0.5rem;
        border-radius: 15px;
        border-bottom: none !important;
    }
    
    .stTabs [data-baseweb="tab-highlight"] {
        display: none !important;
    }
    
    .stTabs [data-baseweb="tab-border"] {
        display: none !important;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-family: 'Poppins', sans-serif;
        font-weight: 500;
        color: #5d8aa8;
        border-bottom: none !important;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
        color: white !important;
        border-bottom: none !important;
    }
    
    .stSelectbox > div > div,
    .stDateInput > div > div,
    .stTimeInput > div > div,
    .stNumberInput > div > div {
        background: #ffffff !important;
        border: 2px solid #d5e8f4 !important;
        border-radius: 12px !important;
        font-family: 'DM Sans', sans-serif;
    }
    
    .stSelectbox > div > div > div {
        color: #1a5276 !important;
    }
    
    .stSelectbox [data-baseweb="select"] > div {
        background: #ffffff !important;
        color: #1a5276 !important;
    }
    
    .stSelectbox svg {
        fill: #1a5276 !important;
    }
    
    .stDateInput input {
        color: #1a5276 !important;
        background: #ffffff !important;
    }
    
    .stTimeInput > div > div {
        background: #ffffff !important;
    }
    
    .stTimeInput input {
        color: #1a5276 !important;
        background: #ffffff !important;
    }
    
    .stTimeInput [data-baseweb="select"] > div,
    .stTimeInput [data-baseweb="input"] {
        background: #ffffff !important;
        color: #1a5276 !important;
    }
    
    .stNumberInput input {
        color: #1a5276 !important;
        background: #ffffff !important;
    }
    
    .stNumberInput button {
        background: #3498db !important;
        color: white !important;
        border: none !important;
    }
    
    .stNumberInput button:hover {
        background: #2980b9 !important;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(255, 255, 255, 0.5);
        padding: 0.5rem;
        border-radius: 15px;
        border-bottom: none !important;
    }
    
    .stTabs [data-baseweb="tab-highlight"] {
        display: none !important;
    }
    
    .stTabs [data-baseweb="tab-border"] {
        display: none !important;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-family: 'Poppins', sans-serif;
        font-weight: 500;
        color: #5d8aa8;
        border-bottom: none !important;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #3498db 0%, #2980b9 100%) !important;
        color: white !important;
        border-bottom: none !important;
    }
    
    .stSelectbox > div > div:focus-within,
    .stDateInput > div > div:focus-within,
    .stTimeInput > div > div:focus-within {
        border-color: #3498db !important;
        box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.15) !important;
    }
    
    .stSelectbox label, .stDateInput label, .stTimeInput label, .stSlider label, .stNumberInput label {
        font-family: 'Poppins', sans-serif;
        font-weight: 500;
        color: #2c5f7c;
        font-size: 0.9rem;
    }
    
    .stSlider > div > div > div {
        background: linear-gradient(90deg, #3498db, #2980b9);
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(52, 152, 219, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(52, 152, 219, 0.4);
    }
    
    .result-box {
        background: linear-gradient(135deg, #1a5276 0%, #2980b9 100%);
        border-radius: 16px;
        padding: 1.5rem 2rem;
        color: white;
        text-align: center;
        margin: 1rem 0;
    }
    
    .result-price {
        font-family: 'Poppins', sans-serif;
        font-size: 2.5rem;
        font-weight: 700;
    }
    
    .result-label {
        font-size: 0.9rem;
        opacity: 0.9;
        margin-bottom: 0.5rem;
    }
    
    .info-box {
        background: rgba(52, 152, 219, 0.1);
        border-left: 4px solid #3498db;
        border-radius: 0 12px 12px 0;
        padding: 1rem 1.5rem;
        margin: 1rem 0;
    }
    
    .info-box-title {
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        color: #1a5276;
        margin-bottom: 0.5rem;
    }
    
    .info-box-content {
        color: #2c5f7c;
        font-size: 0.95rem;
        line-height: 1.6;
    }
    
    .budget-card {
        background: linear-gradient(135deg, #ffffff 0%, #f5f9fc 100%);
        border-radius: 16px;
        padding: 1.5rem;
        border: 2px solid #d5e8f4;
        margin: 0.5rem 0;
        transition: all 0.3s ease;
    }
    
    .budget-card:hover {
        border-color: #3498db;
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(52, 152, 219, 0.15);
    }
    
    .budget-card-title {
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        color: #1a5276;
        font-size: 1rem;
        margin-bottom: 0.5rem;
    }
    
    .budget-card-value {
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        color: #2980b9;
        font-size: 1.3rem;
    }
    
    /* Success/Warning boxes */
    .success-box {
        background: linear-gradient(135deg, #27ae60 0%, #2ecc71 100%);
        border-radius: 12px;
        padding: 1rem 1.5rem;
        color: white;
    }
    
    .warning-box {
        background: linear-gradient(135deg, #f39c12 0%, #e67e22 100%);
        border-radius: 12px;
        padding: 1rem 1.5rem;
        color: white;
    }
    
    .cloud-decoration {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        height: 120px;
        background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1440 120'%3E%3Cpath fill='%23ffffff' fill-opacity='0.6' d='M0,64L48,69.3C96,75,192,85,288,80C384,75,480,53,576,48C672,43,768,53,864,58.7C960,64,1056,64,1152,58.7C1248,53,1344,43,1392,37.3L1440,32L1440,120L1392,120C1344,120,1248,120,1152,120C1056,120,960,120,864,120C768,120,672,120,576,120C480,120,384,120,288,120C192,120,96,120,48,120L0,120Z'%3E%3C/path%3E%3C/svg%3E") no-repeat bottom;
        background-size: cover;
        pointer-events: none;
        z-index: -1;
    }
    
    .footer {
        text-align: center;
        padding: 2rem;
        color: #5d8aa8;
        font-size: 0.9rem;
    }
    
    .footer a {
        color: #3498db;
        text-decoration: none;
    }
    
    .stSubheader, h2, h3 {
        color: #1a5276 !important;
        font-family: 'Poppins', sans-serif !important;
        font-weight: 600 !important;
    }
    
    [data-testid="stMetricValue"] {
        font-family: 'Poppins', sans-serif;
        color: #1a5276;
    }
    
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #d5e8f4, transparent);
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# LOAD MODEL & DATA
@st.cache_resource
def load_model():
    with open('rf_random.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

@st.cache_data
def load_price_data():
    """Load historical price data for Budget Finder"""
    import os
    try:
        if not os.path.exists('Data_Train.xlsx'):
            return None, "File Data_Train.xlsx not found in app directory"
        
        data = pd.read_excel('Data_Train.xlsx')
        
        # Try multiple date formats
        try:
            data['Date_of_Journey'] = pd.to_datetime(data['Date_of_Journey'], format='%d/%m/%Y')
        except:
            try:
                data['Date_of_Journey'] = pd.to_datetime(data['Date_of_Journey'], dayfirst=True)
            except:
                data['Date_of_Journey'] = pd.to_datetime(data['Date_of_Journey'])
        
        data['Journey_month'] = data['Date_of_Journey'].dt.month
        return data, None
    except Exception as e:
        return None, str(e)

price_data, data_error = load_price_data()
model = load_model()

# MAPPINGS
airline_mapping = {
    'Air Asia': 0, 'Air India': 1, 'GoAir': 2, 'IndiGo': 3,
    'Jet Airways': 4, 'Jet Airways Business': 5, 'Multiple carriers': 6,
    'Multiple carriers Premium economy': 7, 'SpiceJet': 8, 'Trujet': 9,
    'Vistara': 10, 'Vistara Premium economy': 11
}

destination_mapping = {
    'Banglore': 0, 'Cochin': 1, 'Delhi': 2,
    'Hyderabad': 3, 'Kolkata': 4, 'New Delhi': 5
}

source_cities = ['Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai']
stops_options = ['non-stop', '1 stop', '2 stops', '3 stops', '4 stops']
stops_map = {'non-stop': 0, '1 stop': 1, '2 stops': 2, '3 stops': 3, '4 stops': 4}

# Month names for display
month_names = {3: 'March', 4: 'April', 5: 'May', 6: 'June'}


st.markdown("""
<div class="main-header">
    <h1>Flight Price Prediction</h1>
    <p>Predict flight prices & find the best time to book within your budget</p>
</div>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Price Prediction", "Budget Finder"])


with tab1:
    st.subheader("Enter Flight Details")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        airline = st.selectbox('Airline', list(airline_mapping.keys()), key='pred_airline')
        source = st.selectbox('From', source_cities, key='pred_source')
        destination = st.selectbox('To', list(destination_mapping.keys()), key='pred_dest')
    
    with col2:
        journey_date = st.date_input('Journey Date', datetime.now(), key='pred_date')
        dep_time = st.time_input('Departure Time', datetime.strptime('10:00', '%H:%M').time(), key='pred_dep')
        arrival_time = st.time_input('Arrival Time', datetime.strptime('13:00', '%H:%M').time(), key='pred_arr')
    
    with col3:
        total_stops = st.selectbox('Total Stops', stops_options, key='pred_stops')
        duration_hours = st.slider('Duration (hours)', 0, 24, 2, key='pred_dur_h')
        duration_minutes = st.slider('Duration (minutes)', 0, 59, 30, key='pred_dur_m')
    
    col_btn = st.columns([1, 2, 1])
    with col_btn[1]:
        predict_btn = st.button('Predict Price', use_container_width=True, key='predict_btn')
    
    if predict_btn:
        input_data = {
            'Airline': airline_mapping[airline],
            'Destination': destination_mapping[destination],
            'Total_Stops': stops_map[total_stops],
            'Journey_day': journey_date.day,
            'Journey_month': journey_date.month,
            'Dep_Time_hour': dep_time.hour,
            'Dep_Time_minute': dep_time.minute,
            'Arrival_Time_hour': arrival_time.hour,
            'Arrival_Time_minute': arrival_time.minute,
            'Duration_hours': duration_hours,
            'Duration_mins': duration_minutes,
            'Duration_Total_mins': (duration_hours * 60) + duration_minutes
        }
        
        for city in source_cities:
            input_data[f'Source_{city}'] = 1 if source == city else 0
        
        feature_order = [
            'Airline', 'Destination', 'Total_Stops', 'Journey_day', 'Journey_month',
            'Dep_Time_hour', 'Dep_Time_minute', 'Arrival_Time_hour', 'Arrival_Time_minute',
            'Duration_hours', 'Duration_mins', 'Duration_Total_mins',
            'Source_Banglore', 'Source_Kolkata', 'Source_Delhi', 'Source_Chennai', 'Source_Mumbai'
        ]
        
        input_df = pd.DataFrame([input_data])[feature_order]
        
        try:
            prediction = model.predict(input_df)[0]
            
            st.markdown(f"""
            <div class="result-box">
                <div class="result-label">Estimated Price</div>
                <div class="result-price">₹{prediction:,.0f}</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="info-box">
                <div class="info-box-title">Flight Details</div>
                <div class="info-box-content">
                    <strong>Route:</strong> {source} → {destination}<br>
                    <strong>Airline:</strong> {airline}<br>
                    <strong>Duration:</strong> {duration_hours}h {duration_minutes}m<br>
                    <strong>Stops:</strong> {total_stops}<br>
                    <strong>Departure:</strong> {dep_time.strftime('%H:%M')} | <strong>Arrival:</strong> {arrival_time.strftime('%H:%M')}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f'Error making prediction: {str(e)}')


with tab2:
    st.subheader("Find Flights Within Your Budget")
    st.markdown('<p style="color: #1a5276; margin-bottom: 1.5rem;">Enter your budget and route to discover the best time & airline combinations that fit your wallet.</p>', unsafe_allow_html=True)
    
    available_routes_dict = {
        'Banglore': ['Delhi', 'New Delhi'],
        'Chennai': ['Kolkata'],
        'Delhi': ['Cochin'],
        'Kolkata': ['Banglore'],
        'Mumbai': ['Hyderabad']
    }
    
    col1, col2 = st.columns(2)
    
    with col1:
        budget = st.number_input(
            'Your Maximum Budget (₹)', 
            min_value=1000, 
            max_value=100000, 
            value=8000, 
            step=500,
            key='budget_input'
        )
        source_budget = st.selectbox('From', list(available_routes_dict.keys()), key='budget_source')
    
    with col2:
        available_destinations = available_routes_dict.get(source_budget, [])
        dest_budget = st.selectbox('To', available_destinations, key='budget_dest')
        preferred_stops = st.selectbox('Preferred Stops', ['Any'] + stops_options, key='budget_stops')
    
    st.markdown("""
    <div style="background: rgba(52, 152, 219, 0.1); border-radius: 8px; padding: 0.75rem 1rem; margin-bottom: 1rem;">
        <p style="color: #1a5276; margin: 0; font-size: 0.85rem;">
            <strong>Available routes:</strong> Banglore→Delhi, Banglore→New Delhi, Chennai→Kolkata, Delhi→Cochin, Kolkata→Banglore, Mumbai→Hyderabad
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col_btn2 = st.columns([1, 2, 1])
    with col_btn2[1]:
        find_btn = st.button('Find Best Options', use_container_width=True, key='find_btn')
    
    if find_btn:
        if price_data is None:
            if data_error:
                st.error(f"Could not load flight data: {data_error}")
            else:
                st.error("Could not load flight data. Please make sure Data_Train.xlsx is in the app directory.")
        elif source_budget == dest_budget:
            st.warning("Please select different cities for departure and destination.")
        elif not dest_budget:
            st.warning("Please select a destination.")
        else:
            route_data = price_data[
                (price_data['Source'] == source_budget) & 
                (price_data['Destination'] == dest_budget)
            ]
            
            if len(route_data) == 0:
                st.markdown(f"""
                <div style="background: #fff3cd; border-radius: 8px; padding: 1rem; margin: 1rem 0;">
                    <p style="color: #856404; margin: 0;"><strong>No historical data available for {source_budget} → {dest_budget}.</strong> Try a different route.</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                if preferred_stops != 'Any':
                    filtered_data = route_data[route_data['Total_Stops'] == preferred_stops]
                    if len(filtered_data) == 0:
                        filtered_data = route_data
                else:
                    filtered_data = route_data
                
                monthly_stats = filtered_data.groupby('Journey_month')['Price'].agg(['mean', 'min', 'max', 'count']).reset_index()
                
                airline_stats = filtered_data.groupby('Airline')['Price'].agg(['mean', 'min', 'count']).reset_index()
                airline_stats = airline_stats.sort_values('mean')
                
                stops_stats = filtered_data.groupby('Total_Stops')['Price'].agg(['mean', 'min']).reset_index()
                stops_stats = stops_stats.sort_values('mean')
                
                within_budget = filtered_data[filtered_data['Price'] <= budget]
                budget_percentage = (len(within_budget) / len(filtered_data)) * 100
                
                st.markdown("---")
                
                # Budget feasibility
                if budget_percentage >= 50:
                    st.markdown(f"""
                    <div class="success-box">
                        <strong>Great news!</strong> {budget_percentage:.0f}% of flights on this route are within your ₹{budget:,} budget!
                    </div>
                    """, unsafe_allow_html=True)
                elif budget_percentage >= 20:
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #3498db 0%, #2980b9 100%); border-radius: 12px; padding: 1rem 1.5rem; color: white;">
                        <strong>Good options available!</strong> {budget_percentage:.0f}% of flights fit your ₹{budget:,} budget.
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="warning-box">
                        <strong>Limited options.</strong> Only {budget_percentage:.0f}% of flights are within ₹{budget:,}. Consider increasing your budget or being flexible with dates.
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                # Recommendations
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.markdown("""
                    <div class="budget-card">
                        <div class="budget-card-title">Best Month to Travel</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    best_month = monthly_stats.loc[monthly_stats['mean'].idxmin()]
                    best_month_num = int(best_month['Journey_month'])
                    best_month_name = month_names.get(best_month_num, f'Month {best_month_num}')
                    
                    st.markdown(f"""
                    <div style="padding: 0 1rem;">
                        <div style="font-size: 1.5rem; font-weight: 700; color: #2980b9;">{best_month_name}</div>
                        <div style="color: #5d8aa8; font-size: 0.9rem;">Avg: ₹{best_month['mean']:,.0f}</div>
                        <div style="color: #27ae60; font-size: 0.85rem;">Lowest: ₹{best_month['min']:,.0f}</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    st.markdown("""
                    <div class="budget-card">
                        <div class="budget-card-title">Most Affordable Airline</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if len(airline_stats) > 0:
                        best_airline = airline_stats.iloc[0]
                        st.markdown(f"""
                        <div style="padding: 0 1rem;">
                            <div style="font-size: 1.3rem; font-weight: 700; color: #2980b9;">{best_airline['Airline']}</div>
                            <div style="color: #5d8aa8; font-size: 0.9rem;">Avg: ₹{best_airline['mean']:,.0f}</div>
                            <div style="color: #27ae60; font-size: 0.85rem;">Lowest: ₹{best_airline['min']:,.0f}</div>
                        </div>
                        """, unsafe_allow_html=True)
                
                with col3:
                    st.markdown("""
                    <div class="budget-card">
                        <div class="budget-card-title">Cheapest Stop Option</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if len(stops_stats) > 0:
                        best_stops = stops_stats.iloc[0]
                        st.markdown(f"""
                        <div style="padding: 0 1rem;">
                            <div style="font-size: 1.3rem; font-weight: 700; color: #2980b9;">{best_stops['Total_Stops']}</div>
                            <div style="color: #5d8aa8; font-size: 0.9rem;">Avg: ₹{best_stops['mean']:,.0f}</div>
                            <div style="color: #27ae60; font-size: 0.85rem;">Lowest: ₹{best_stops['min']:,.0f}</div>
                        </div>
                        """, unsafe_allow_html=True)
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                # Detailed Tips
                st.markdown(f"""
                <div class="info-box">
                    <div class="info-box-title">Smart Booking Tips for {source_budget} → {dest_budget}</div>
                    <div class="info-box-content">
                        • <strong>Best combination:</strong> Fly with {airline_stats.iloc[0]['Airline'] if len(airline_stats) > 0 else 'budget airlines'} in {best_month_name} with {stops_stats.iloc[0]['Total_Stops'] if len(stops_stats) > 0 else 'flexible stops'}<br>
                        • <strong>Price range on this route:</strong> ₹{filtered_data['Price'].min():,.0f} - ₹{filtered_data['Price'].max():,.0f}<br>
                        • <strong>Average price:</strong> ₹{filtered_data['Price'].mean():,.0f}<br>
                        • <strong>Based on:</strong> {len(filtered_data):,} historical flights
                    </div>
                </div>
                """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div class="footer">
    <p>Built with ❤️ by <strong>Damida Shu Mudita</strong></p>
    <p>Januari 2026</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="cloud-decoration"></div>', unsafe_allow_html=True)
