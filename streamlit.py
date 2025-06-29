import pandas as pd
import streamlit as st

df = pd.read_csv('lista_produtków.csv', index_col='Produkt')
df.index = df.index.str.strip().str.lower()

if 'kalorieTotal' not in st.session_state:
    st.session_state.kalorieTotal = 0
if 'białkoTotal' not in st.session_state:
    st.session_state.białkoTotal = 0
if 'tłuszczeTotal' not in st.session_state:
    st.session_state.tłuszczeTotal = 0
if 'węglowodanyTotal' not in st.session_state:
    st.session_state.węglowodanyTotal = 0
if 'listaProduktów' not in st.session_state:
    st.session_state.listaProduktów = []

# WARTOŚCI PLACEHOLDER
wartosci_placeholder = st.empty()
with wartosci_placeholder.container():
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Kalorie", st.session_state.kalorieTotal)
        col2.metric("Białko", st.session_state.białkoTotal)
        col3.metric("Tłuszcz", st.session_state.tłuszczeTotal)
        col4.metric("Węglowodany", st.session_state.węglowodanyTotal)

# IMPUTY i PRZYCISK
with st.form("dodaj_produkt_form"):
    produkt = st.text_input("\nCo dzisiaj zjadłeś? ").strip().lower()
    ilość = st.number_input("Podaj ilość (gramy)", min_value=0.0, format="%.2f")
    submit = st.form_submit_button("Dodaj")

# KALKULACJE i WARTOŚCI
if submit:
    try:
        kaloriePer100 = float(df.loc[produkt, 'Kalorie'])
        kalorieProdukt = round(kaloriePer100 * 0.01 * ilość, 2)
        st.session_state.kalorieTotal += kalorieProdukt
        
        białkoPer100 = float(df.loc[produkt, 'Białko'])
        białkoProdukt = round(białkoPer100 * 0.01 * ilość, 2)
        st.session_state.białkoTotal += białkoProdukt
        
        tłuszczePer100 = float(df.loc[produkt, 'Tłuszcze'])
        tłuszczeProdukt = round(tłuszczePer100 * 0.01 * ilość, 2)            
        st.session_state.tłuszczeTotal += tłuszczeProdukt
        
        węglowodanyPer100 = float(df.loc[produkt, 'Węglowodany'])
        węglowodanyProdukt = round(węglowodanyPer100 * 0.01 * ilość, 2)
        st.session_state.węglowodanyTotal += węglowodanyProdukt
        
        st.success(f"Dodano {ilość}g {produkt}")
    except KeyError:
        st.error("Nie ma takiego produktu w bazie")
    except ValueError:
        st.error("Niepoprawna ilość")
        
with wartosci_placeholder.container():
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Kalorie", st.session_state.kalorieTotal)
    col2.metric("Białko", st.session_state.białkoTotal)
    col3.metric("Tłuszcz", st.session_state.tłuszczeTotal) 
    col4.metric("Węglowodany", st.session_state.węglowodanyTotal)