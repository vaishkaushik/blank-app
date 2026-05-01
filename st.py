import streamlit as st

st.title("Investment Snapshot Tool")

st.write("Enter your investments (₹)")

mf = st.number_input("Mutual Funds", min_value=0)
stocks = st.number_input("Stocks", min_value=0)
gold = st.number_input("Gold", min_value=0)
crypto = st.number_input("Crypto", min_value=0)
cash = st.number_input("Cash", min_value=0)

total = mf + stocks + gold + crypto + cash

if st.button("Analyze"):
    if total == 0:
        st.warning("Please enter some values")
    else:
        st.subheader("Portfolio Breakdown")

        st.write(f"Total Investment: ₹{total}")

        st.write(f"Mutual Funds: {round(mf/total*100,2)}%")
        st.write(f"Stocks: {round(stocks/total*100,2)}%")
        st.write(f"Gold: {round(gold/total*100,2)}%")
        st.write(f"Crypto: {round(crypto/total*100,2)}%")
        st.write(f"Cash: {round(cash/total*100,2)}%")

        # Simple Risk Logic
        risk = "Low"

        if crypto/total > 0.2 or stocks/total > 0.6:
            risk = "High"
        elif stocks/total > 0.4:
            risk = "Medium"

        st.subheader(f"Risk Level: {risk}")

        # Suggestions
        if risk == "High":
            st.write("⚠️ Consider balancing with safer assets like debt or gold.")
        elif risk == "Medium":
            st.write("👍 Decent balance, can diversify more.")
        else:
            st.write("✅ Safe portfolio, but may have lower returns.")