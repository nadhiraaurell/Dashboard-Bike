import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')

# Helper function yang dibutuhkan untuk menyiapkan berbagai dataframe

def create_day_df(df):
    df.rename(columns={
        "instant": "no"
    }, inplace=True)

    return df

def create_hour_df(df):
    df.rename(columns={
        "intant": "no"
    }, inplace=True)

    return df 

# Load cleaned data
merged_df = pd.read_csv("https://raw.githubusercontent.com/nadhiraaurell/Dashboard-Bike/main/Dashboard/merged_df.csv")

datetime_columns = ["dteday"]
for column in datetime_columns:
    merged_df[column] = pd.to_datetime(merged_df[column])

# Filter data
min_date = merged_df["dteday"].min()
max_date = merged_df["dteday"].max()

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://raw.githubusercontent.com/nadhiraaurell/Dicoding-Streamlit/main/icon.png")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = merged_df[(merged_df["dteday"] >= str(start_date)) & 
                (merged_df["dteday"] <= str(end_date))]

# st.dataframe(main_df)

# # Menyiapkan berbagai dataframe
day_df = create_day_df(main_df)
hour_df = create_hour_df(main_df)

# JUMLAH PENYEWA DI HARI LIBUR SETIAP TAHUN (bar chart)
def create_plot():
    # Data
    day = ('2011', '2012')
    votes = (30022, 48413)

    # Membuat plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(day, votes, color='skyblue')

    # Menambahkan label dan judul
    ax.set_ylabel('Jumlah Rental', fontsize=14)
    ax.set_xlabel('Tahun', fontsize=14)
    ax.set_title('Jumlah Rental Sepeda per Tahun', fontsize=16)

    # Menampilkan plot
    st.pyplot(fig)

# Aplikasi Streamlit
def main():
    st.header('Bike Sharing Dataset :sparkles:')
    st.subheader('Jumlah Penyewa Sepeda per Tahun')

    # Memanggil fungsi untuk membuat visualisasi
    create_plot()

if __name__ == '__main__':
    main()

# Memberi penjelasan
st.write('Gambar diatas menunjukkan Bar Chart dari jumlah penyewa di hari libur per tahun.')

# JUMLAH PENYEWA DI HARI LIBUR SETIAP TAHUN (pie chart)
def main():
    st.subheader('Persentase Jumlah Penyewa Sepede per Tahun')

    # Data
    years = [2011, 2012]
    total_rentals = [30022, 48413]
    labels = [str(year) for year in years]

    # Visualisasi data
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.pie(total_rentals, labels=labels, autopct='%1.1f%%', startangle=140)
    ax.set_title('Total Penyewa di Hari Libur Setiap Tahun')
    ax.axis('equal')  

    # Menampilkan plot menggunakan Streamlit
    st.pyplot(fig)

if __name__ == '__main__':
    main()

# Memeberi penjelasan
st.write('Gambar diatas menunjukkan persentase dari jumlah penyewa di hari libur pada tahun 2011 dan 2012.')


#TOTAL JAM PENYEWA DI HARI LIBUR SETIAP BULAN(pie chart)
def main():
    st.subheader("Persentase Total Jam Penyewa di Hari Libur Setiap Bulan")

    # Data yang dibutuhkan, ganti dengan data Anda
    hour_df['total_hour'] = hour_df['casual'] + hour_df['registered']

    hasil = hour_df.groupby(['mnth', 'holiday'])['total_hour'].sum().reset_index()

    # Membuat plot pie
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.pie(hasil[hasil['holiday'] == 1]['total_hour'], labels=hasil[hasil['holiday'] == 1]['mnth'], autopct='%1.1f%%', startangle=140)
    ax.set_title('Total Jam Penyewa di Hari Libur Setiap Bulan')
    ax.axis('equal')

    # Tampilkan plot menggunakan Streamlit
    st.pyplot(fig)

if __name__ == '__main__':
    main()

# Memeberi penjelasan
st.write('Gambar diatas menunjukkan persentase dari jumlah penyewa di hari libur setiap bulan pada tahun 2011 dan 2012.')
