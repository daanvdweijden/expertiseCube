import streamlit as st
import plotly.express as px
import pandas as pd



st.title('Interactive Expertise Cube')
st.header('Utrecht Data School')

with st.form('experts_from_file'):
    st.subheader('Upload experts from a file')
    file = st.file_uploader('Upload file here',['csv'])
    submit_file = st.form_submit_button('Submit')
    if submit_file:
        experts = pd.read_csv(file, sep=';')
        experts = experts.dropna()
        
        if set(['Projection of expertise',
                'Specialised knowledge',
                'Assigned status',
                'Name of Expert',
                'Community']).issubset(experts.columns):
        
            fig_file = px.scatter_3d(experts, 
                                    x='Projection of expertise', 
                                    y='Specialised knowledge', 
                                    z='Assigned status',
                                    text='Name of Expert',
                                    color='Community',
                                    range_x=[0,10],
                                    range_y=[0,10],
                                    range_z=[0,10])
            st.plotly_chart(fig_file, sharing="streamlit")
        else:
            example = pd.DataFrame({"Name of Expert"             : ['dr. Elise'], 
                                    "Projection of expertise"    : [6],
                                    "Specialised knowledge"      : [8],
                                    "Assigned status"            : [3],
                                    "Community"                  : ['Medicine']})
            st.write('Please check if your file has the correct formatting, an example with correct column names can be seen below')
            st.dataframe(example)
            
        
        

with st.form('single_expert'):
    st.subheader('Or try it out with inputting a single expert')
    nameExpert = st.text_input('Name of Expert', 'Expert')
    numberProj = st.slider('Projection', 0, 10, 5)
    numberAssi = st.slider('Assigned', 0, 10, 5)
    numberKnow = st.slider('Specialised Knowledge', 0, 10, 5)
    submit_expert = st.form_submit_button('Submit')
    if submit_expert:
        df = pd.DataFrame({"Name of Expert"             : [nameExpert], 
                           "Projection of expertise"    : [numberProj],
                           "Specialised knowledge"      : [numberKnow],
                           "Assigned status"            : [numberAssi]})
    
        
        fig = px.scatter_3d(df, 
                    x='Projection of expertise', 
                    y='Specialised knowledge', 
                    z='Assigned status',
                    text='Name of Expert',
                    range_x=[0,10],
                    range_y=[0,10],
                    range_z=[0,10])
        st.write(f"Added {nameExpert} to dataset")
        st.plotly_chart(fig, sharing="streamlit")


