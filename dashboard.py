import streamlit as st

st.set_page_config(layout="wide")

# Sidebar Navigation
menu = st.sidebar.radio(
    "Navigation",
    ["Overview", "Ride Bookings", "Ride Status","Vehicles","Revenue and Rating"]
)

#Overview Page
if menu == "Overview":
    st.title("Key Performance Indicators")

   
    #Date Range
    st.image("charts/DateRange.png", caption="Date Range Overview", use_container_width=True)

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Rides", 150000 )
    col2.metric("Completed Rides", 93000.0)
    col3.metric("Ride Sucess Rate %age:", 62.00)

    col4, col5, col6 = st.columns(3)
    col4.metric("Average Wait Time", 8.46)
    col5.metric("Average Trip Duration", 30.03)
    col6.metric("Avg Ride Distance", 26.00)
   
# Rides Page

elif menu == "Ride Bookings":
    st.title("Rides Booked - Time Wise and Location Wise")

    col1, col2 = st.columns(2)
    with col1:
        st.image("charts/DailyRideBooking.png", caption="Daily Rides", use_container_width=True)
    with col2:
        st.image("charts/HourlyRides.png", caption="Hourly Distribution", use_container_width=True)

    col3, col4 = st.columns(2)
    with col3:
        st.image("charts/MonthlyRideBooking.png", caption="Monthly Rides", use_container_width=True)
    with col4:
        st.image("charts/Bookings.png", caption = "Hourly and Weekday Bookings", use_container_width = True)

    col4, col5 = st.columns(2)
    with col4:
        st.image("charts/PickupLocs.png", caption="Top 10 Pickup Locations", use_container_width=True)
    with col5:
        st.image("charts/DropLocs.png", caption="Top 10 Drop Locations", use_container_width=True)

# Revenue Page

elif menu == "Revenue and Rating":
    st.title("Revenue and Rating")

    col1, col2 = st.columns(2)
    col1.metric("Total Revenue", "₹71.72M")
    col2.metric("Revenue per Ride", "₹478.12")

    col3, col4 = st.columns(2)
    with col3:
        st.image("charts/RevenuePayment.png", caption = "Revenue By Payment Method", use_container_width=True)
    with col4:
        st.image("charts/RevenueByMonth.png", caption = "Revenue By Month", use_container_width=True)

    col4, col5 = st.columns(2)
    with col4:
        st.image("charts/RevenuePickup.png", caption = "Revenue from top 10 Pickup Locations", use_container_width=True)
    with col5:
        st.image("charts/RevenueDrop.png", caption = "Revenue from top 10 Drop Locations", use_container_width=True)
    st.title("Rating")
    col6, col7 = st.columns(2)
    col6.metric("Driver Average Rating", "4.26/5")
    col7.metric("Customer Average Rating", "4.44/5")

#Booking status Page
elif menu == "Ride Status":
    st.title("Ride Status")
    col1, col2 = st.columns(2)
    
    with col1:
         st.image("charts/status1.png", caption = "Booking Status",use_container_width=True)
         
    with col2:
        st.image("charts/StatusVehicle.png", caption = "Booking Status by Vehicle Type",use_container_width=True)

    st.title("Cancellation Status")
    st.image("charts/cancel.png" , caption = "Cancellation Status", use_container_width=True)
    st.title("Cancellation Reasons")
    col3, col4 = st.columns(2)

    with col3:
        st.image("charts/drivercancel.png", caption = "Reasons for Cancellation by Driver", use_container_width=True)
    with col4:
        st.image("charts/custcancel.png", caption = "Reasons for Cancellation by Customer", use_container_width=True)

#Vehicles Page
elif menu == "Vehicles":
    st.title("Vehicles Type")
    col1, col2 = st.columns(2)
    
    with col1:
         st.image("charts/vehicles.png", caption = "Types of Vehicles",use_container_width=True)

    st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        color: #555;
    }
    </style>
    <div class="footer">Developed by Abhijeet Kaur</div>
    """,
    unsafe_allow_html=True
)

         
    with col2:
        st.image("charts/vehicleType.png", caption = "Vehicle Types- Distance, Fare and Success Rate",use_container_width=True)
        
