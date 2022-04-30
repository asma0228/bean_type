import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image
  
# loading in the model to predict on the data
pickle_in = open('knn.pkl','rb')
classifier = pickle.load(pickle_in)
  
def welcome():
    return 'welcome all'
  
# defining the function which will make the prediction using 
# the data which the user inputs



def prediction(Area, Perimeter, MajorAxisLength, MinorAxisLength,
       AspectRation, Eccentricity, ConvexArea, Extent,
       Solidity, roundness, Compactness, ShapeFactor1, ShapeFactor2,
       ShapeFactor3, ShapeFactor4):  
   
    prediction = classifier.predict(
        [[Area, Perimeter, MajorAxisLength, MinorAxisLength,
       AspectRation, Eccentricity, ConvexArea, Extent,
       Solidity, roundness, Compactness, ShapeFactor1, ShapeFactor2,
       ShapeFactor3, ShapeFactor4]])
    print(prediction)
    return prediction
   
   
  
# this is the main function in which we define our webpage 
def main():
      # giving the webpage a title
    st.title("Bean type prediction 📈")
      
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:white;padding:13px">
    <h1 style ="color:black;text-align:center;">Bean type ML App ☘️ </h1>
    </div>
    """
      
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
      
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    
    
    Area = st.text_input("Area", "Type Here")
    Perimeter = st.text_input("Perimeter", "Type Here")
    MajorAxisLength = st.text_input("MajorAxisLength", "Type Here")
    MinorAxisLength = st.text_input("MinorAxisLength", "Type Here")
    AspectRation = st.text_input("AspectRation", "Type Here")
    Eccentricity = st.text_input("Eccentricity", "Type Here")
    ConvexArea = st.text_input("ConvexArea", "Type Here")
    Extent = st.text_input(" Extent", "Type Here")
    Solidity = st.text_input("Solidity", "Type Here")
    roundness = st.text_input("roundness", "Type Here")
    Compactness = st.text_input("Compactness", "Type Here")
    ShapeFactor1 = st.text_input("ShapeFactor1 ", "Type Here")
    ShapeFactor2 = st.text_input("ShapeFactor2", "Type Here")
    ShapeFactor3 = st.text_input("ShapeFactor3", "Type Here")
    ShapeFactor4 = st.text_input("ShapeFactor4", "Type Here")


    

    result =""
      
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result
    if st.button("Predict"):
       result = prediction(Area, Perimeter, MajorAxisLength, MinorAxisLength,
       AspectRation, Eccentricity, ConvexArea, Extent,
       Solidity, roundness, Compactness, ShapeFactor1, ShapeFactor2,
       ShapeFactor3, ShapeFactor4 )
    st.success('The bean size is {}'.format(result))
      
if __name__=='__main__':
    main()