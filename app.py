import streamlit as st
import requests
import json

def main():
    st.title("Esame API")
    url_API =st.text_input("insert API url","http://localhost:8000/predict")
    #insert the min, the max and the mean values for rdspend, administration, marketingspend: 0, 1000000, mean)
    rdspend = st.number_input("Insert R&D Spend value",0,1000000,73721)
    administration = st.number_input("Insert Administration value",0,1000000,121344)
    marketingspend = st.number_input("Insert Marketing Spend value",0,1000000,211025)

    if st.button("Predict with GET"):
        url = url_API
        url2 = f"?rdspend={rdspend}&administration={administration}&marketingspend={marketingspend}"
        link = url+url2
        st.write('"{}"'.format(link))
        response = requests.get(link)
        result = response.json()
        st.success(f"The result is: {result['prediction']}")

    if st.button("Predict with POST"):
        url = url_API
        response =requests.post(url,
                                headers={"Content-Type": "application/json"},
                                data = json.dumps({
                                                "rdspend":rdspend,
                                                "administration":administration,
                                                "marketingspend":marketingspend,
                                                })
                                )
        result =response.json()
        st.success(f"The result is: {result['prediction']}")

if __name__ == '__main__':
    main()

