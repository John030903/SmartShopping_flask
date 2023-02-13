from website import create_app
import requests
import json
# import streamlit as st

app = create_app()
# print("Run")
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70',}
# response = requests.get("http://127.0.0.1:5000", headers=headers)
# data = json.loads(response.content)
# st.write(data)
if __name__ == '__main__':
    app.run(debug=False,host="0.0.0.0",port="5500")
