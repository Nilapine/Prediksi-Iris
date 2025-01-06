import warnings
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np
import pandas as pd

from web_functions import train_model_DT, train_model_KNN, train_model_NBC, load_data

def app(df, x, y):
    warnings.filterwarnings('ignore')
    #st.set_option('deprecation.showPyplotGlobalUse', False)
    st.markdown('<h1 class="title">Visualisasi Prediksi Tanaman Iris</h1>', unsafe_allow_html=True)
    # if st.checkbox("Plot Decision Tree"):
    #     model, score = train_model_DT(x, y)
    #     dot_data = tree.export_graphviz(
    #         decision_tree=model, out_file=None, filled=True, rounded=True,
    #         feature_names=x.columns, class_names=['Iris-setosa','Iris-versicolor','Iris-virginica']
    #     )
    #     st.graphviz_chart(dot_data)
    # elif st.checkbox("Pairplot"):
    st.markdown("""
    <p style="text-align: justify;">
    Gambar pairplot menampilkan hubungan antar fitur numerik dalam dataset yang digunakan untuk klasifikasi dengan model Naive Bayes.<br><br>
    Visualisasi Pair plot:
    </p>
    """, 
    unsafe_allow_html=True)
    # s = sns.pairplot(df, hue="Species")
    st.pyplot(sns.pairplot(df, hue="Species"))  # type: ignore

    # Add custom CSS for expander title text color (purple)
    st.markdown("""
    <style>
        [data-testid="stExpander"]{
            color: #800080;  /* Purple text color */
        }
        .title {
            text-align: center;
            color: purple;
        }
    </style>
    """, unsafe_allow_html=True)

    # Create an expander for the explanation
    with st.expander("**Deskripsi Gambar**"):
        st.markdown("""
        Gambar di atas adalah *pair plot*, yang merupakan visualisasi dari hubungan antar variabel pada dataset *Iris*. Berikut adalah penjelasan lebih lanjut:

        1. **Dataset Iris**: Dataset ini terdiri dari tiga spesies bunga Iris—*Iris-setosa* (biru), *Iris-versicolor* (oranye), dan *Iris-virginica* (hijau)—yang diklasifikasikan berdasarkan empat fitur:
        - **SepalLengthCm**: Panjang kelopak bunga (sepal) dalam cm.
        - **SepalWidthCm**: Lebar kelopak bunga dalam cm.
        - **PetalLengthCm**: Panjang mahkota bunga (petal) dalam cm.
        - **PetalWidthCm**: Lebar mahkota bunga dalam cm.
        - **Id**: Indeks untuk identifikasi.

        2. **Distribusi diagonal**: Di sepanjang diagonal, terlihat distribusi (plot densitas atau histogram) dari masing-masing fitur secara individu. Warna-warna pada distribusi ini mewakili spesies yang berbeda.

        3. **Scatter plot non-diagonal**: Di bagian lain dari pair plot ini, terlihat plot pencar (scatter plot) yang menunjukkan hubungan antara dua fitur. Setiap titik pada scatter plot mewakili satu contoh dari dataset, dengan warnanya mencerminkan spesiesnya.

        4. **Klasifikasi visual**: Gambar ini memberikan indikasi seberapa mudah atau sulit spesies bunga dapat diklasifikasikan berdasarkan fitur tertentu. Beberapa pasangan fitur memperlihatkan pemisahan yang lebih jelas antar spesies, sedangkan beberapa pasangan lainnya menunjukkan tumpang tindih yang lebih besar.
        """)

    # Create an expander for the explanation
    with st.expander("**Manfaat Bunga Iris**"):
        st.markdown("""
        Selain cantik, bunga yang memiliki nama latin "neomarica longifolia" ini berkaitan dengan mitologi Yunani dan budaya lain. Di berbagai negara, bunga ini punya makna simbol berbeda sesuai dengan warnanya. 
        
        Tak hanya itu, ternyata bunga iris juga memiliki segudang manfaat. Salah satunya untuk memurnikan air, menjadi obat herbal, mengobati sakit tenggorokan, mengobati sembelit, perut kembung dan mual, mengobati penyakit hepatitis, luka bakar, dan mengobati radang kulit, bisul maupun digigit serangga. 
        
        Itu semua karena kandungan senyawa kimia dalam bunga iris, yakni iridin, tanin, resin, amilum, asam miristat, dan iron yang memiliki efek farmakologis. Bagian tanaman yang dimanfaatkan adalah bagian akar rimpangnya.
        """)

    # Create an expander for the explanation
    with st.expander("**Varian Bunga Iris**"):
        st.markdown("""
        Bunga iris memiliki berbagai jenis varian selain 3 yang diprediksi, terdapat juga jenis lain diantaranya yaitu :
        1. Iris Biru
        2. Iris Ungu
        3. Iris Putih
        4. Iris Louisiana
        5. Iris Jepang
        """)
