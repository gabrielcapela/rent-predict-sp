# Rent Predict - São Paulo

The final application is available at this [link](https://rent-predict-sp-b372d5fb9a82.herokuapp.com):

### 📊 Project Overview
This application uses Machine Learning techniques to predict the total housing cost (rent + condominium fees) of apartments in São Paulo, based on features such as location, size, number of rooms, and more.

<div align="center">
  <img width="89%" src="https://raw.githubusercontent.com/gabrielcapela/rent-predict-sp/main/images/carlos-aranda_unsplash.jpg"><br>
  <p>
    Photo by 
    <a href="https://unsplash.com/pt-br/@carlosaranda?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Carlos Aranda</a> 
    on 
    <a href="https://unsplash.com/pt-br/fotografias/arranha-ceus-durante-o-dia-qFIK_CPUwRI?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
  </p>
</div>


### 📌 Context and Objective

The real estate market can be dynamic and often lacks transparency for renters. This project aims to help users obtain a price estimate based on real data. Build a predictive model using historical property data to automatically estimate the total cost of living in São Paulo apartments.

---

### 💻 Notebooks

Click [here](https://github.com/gabrielcapela/rent-predict-sp/blob/main/explanation_notebook.ipynb) to see the complete explanatory notebook

---

### ✅ Actions (Main Steps)

- Business Understanding
- Data Understanding
- Data Preparation
- Modeling
- Evaluation
- Deployment

---

### 📊 Results

- Fully functional web application
- R² above 0.82 on validation    
- Identification of key features impacting price  
- Geospatial visualization of apartment locations  


---

### 🛠️ Technologies Used

- Python 3.x  
- Pandas & NumPy  
- Matplotlib & Seaborn   
- PyCaret
- Random Forest Regressor  
- Folium  
- Flask  
- Heroku

---

### ⚠️ Limitations

- **Data source is from 2019**: The model was trained on data collected in 2019, which may not reflect recent trends or economic changes in the São Paulo housing market.
- **Lack of external features**: The dataset does not include macroeconomic indicators, proximity to transport, or neighborhood crime rates, which could further improve prediction accuracy.
- **Limited diversity in some features**: Certain categorical variables (e.g., elevator presence or furnished status) have low variance, which might reduce their influence in the model.
- **Deployment environment**: The application is hosted on Heroku's free tier, which may result in slower initial load times due to dyno sleeping.

---

### 🔄 Next Steps

1. Refactor web interface for better usability  
2. Update the dataset with more recent data  
3. Develop a REST API for broader integration  
4. Monitor model performance over time

---

### 👤 Author

**Gabriel Capela**  
[LinkedIn](https://www.linkedin.com/in/gabrielcapela)  

### 📫 Contact

Email: gabriel.capela@ufms.br
