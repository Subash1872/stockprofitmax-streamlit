import streamlit as st

company_name=st.text_input("Enter Company Name","Type Here...")
amount=st.number_input("Enter Initial Amount...")
a=st.text_input("Enter Time Seperated by ,","")
b=st.text_input("Enter Prices seperated by ,","")
dates=a.split(',')
value1=b.split(',')
price=[]
for word in value1:
    if word.isdigit():
        price.append(int(word))
#st.write(dates)
#st.write(value1)
#st.write(price) 
if(st.button("Calcuate")):
#    st.write(sum(price))
    profit = 0
    shares=0
    amount_end=amount
    buy=[]
    sell=[]
    j = 0
    for i in range(1, len(price)):
        if price[i - 1] > price[i]:
            j = i
        if price[i - 1] <= price[i] and (i + 1 == len(price) or price[i] > price[i + 1]):
            profit += (price[i] - price[j])
            shares=amount_end/price[j]
            buy.append(j)
            st.write("Bought Shares:",shares)
            amount_end=shares*price[i]
            st.write("Buy on time:",dates[j])
            st.write(" Sell on time:",dates[i])
            st.write("Profit at",dates[i],":",amount_end-amount)
    st.write("Total profit earned is:",amount_end-amount)
