import pandas as pd
import streamlit as st


st.title("EIE 2025 - Sem 4 Results")

df = pd.read_csv('result-fourth-sem.csv')

st.sidebar.title("Filter Results")
st.header("Filtered Results")

df_selection = df

#-----FORM FILTERS-----#
form = st.sidebar.form("Filter Form")
reg = sub = res = empty = []

reg = form.multiselect("Select Register Nnumber :", 
                       options = df['Register_no'].unique(), 
                       default= "71772116101"
                       )

select_all = form.checkbox("Select All Register Numbers", value = False)

sub = form.multiselect("Select Subject Code :",
                        options = ['18NHS401', '18NBS402', '18NES403', '18NPC404', '18NPC405', '18NPC406', '18NMC4Z7', '18NPC408', '18NPC409', '18NVA401',  '18NBS201', '18NBS202', '18NES203', '18NHS301', '18NBS302', '18NES303', '18NPC304', '18NPC308', '18NBS103', '18NES206', '18NPC305', '18NPC306', '18NMC3Z7'],
                        default = ["18NHS401", "18NBS402", "18NES403", "18NPC404", "18NPC405", "18NPC406", "18NMC4Z7", "18NPC408", "18NPC409", "18NVA401"]
                        )

res = form.multiselect("Select Result :",
                        options = df['Result'].unique(),
                        default = df['Result'].unique()
                        )

submit = form.form_submit_button("Apply")

print(reg, sub, res)

if submit:
    if select_all:
        df_selection = df
    elif reg:
        df_selection = df_selection.query("Register_no == @reg")
    if sub:
        df_selection = df_selection.query("Sub_code == @sub")
    if res:
        df_selection = df_selection.query("Result == @res")



st.dataframe(df_selection)
