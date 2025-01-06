import streamlit as st
from web_functions import predict_DT, predict_KNN, predict_NBC

def app(df, x, y):
    # Tambahkan CSS untuk mengubah warna latar belakang menjadi ungu dan gaya tulisan
    st.markdown(
        """
        <style>
        .main {
            background-color: #6c4891; /* Lavender */
            color: #6c4891; /* Indigo */
        }
        .title {
            text-align: center;
        }
        .centered-image {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 50%; /* Adjust width for medium size */
        }
        .result-title {
            text-align: center;
            font-size: 24x;
            font-weight: bold;
            color: #6c4891;
        }
        .result-type {
            text-align: center;
            font-size: 50px;
            font-weight: bold;
            color: #6c4891;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Judul Halaman Aplikasi
    st.markdown('<h1 class="title">Prediksi Jenis Tanaman Iris</h1>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        SepalLengthCm = st.text_input('Input Panjang Sepal (dalam cm) : ')
    with col1:
        SepalWidthCm = st.text_input('Input Lebar Sepal (dalam cm) : ')
    with col2:
        PetalLengthCm = st.text_input('Input Panjang Petal (dalam cm) : ')
    with col2:
        PetalWidthCm = st.text_input('Input Lebar Petal (dalam cm) : ')

    features = [SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]

    tipe_model = {
        "KNN": predict_KNN,
        "NBC": predict_NBC,
    }

    predict = st.radio(label="Pilih Model", options=["KNN", "NBC"])

    # Tombol Prediksi
    if st.button("Prediksi"):
        if predict == "KNN":
            prediction, score = predict_KNN(x, y, features)  # type: ignore
        else:
            prediction, score = predict_NBC(x, y, features)  # type: ignore
        
        st.markdown('<p class="result-title">Termasuk jenis bunga:</p>', unsafe_allow_html=True)

        if prediction == "Iris-setosa":
            st.markdown('<p class="result-type">IRIS SETOSA</p>', unsafe_allow_html=True)
            st.markdown('<img class="centered-image" src="https://i.etsystatic.com/20845839/r/il/86ac74/3108398608/il_fullxfull.3108398608_6l57.jpg" alt="Iris-setosa" />', unsafe_allow_html=True)
            st.markdown(
                """
                <p style='text-align: justify;'>
                Iris setosa memiliki ciri khas berupa petal (kelopak bunga) yang kecil dan pendek dengan ukuran panjang petal sekitar 1,0–1,9 cm dan lebar 0,1–0,6 cm. Sepalnya (daun pelindung) relatif panjang dibandingkan petalnya.</p>
                """,
                unsafe_allow_html=True
            )
        elif prediction == "Iris-versicolor":
            st.markdown('<p class="result-type">IRIS VERSICOLOR</p>', unsafe_allow_html=True)
            st.markdown('<img class="centered-image" src="https://www.latour-marliac.com/3033-large_default/iris-versicolor-iris-versicolore.jpg" alt="Iris-versicolor" />', unsafe_allow_html=True)
            st.markdown(
                """
                <p style='text-align: justify;'>
                Iris versicolor memiliki petal berukuran sedang, dengan panjang sekitar 3,0–5,1 cm dan lebar 1,0–1,8 cm. Warnanya cenderung ungu kebiruan dengan corak yang khas, dan biasanya tumbuh di tanah yang sedikit lebih kering dibandingkan habitat Iris setosa. Spesies ini memiliki petal berbentuk elips yang lebih lebar dibandingkan Iris setosa.</p>
                """,
                unsafe_allow_html=True
            )
        elif prediction == "Iris-virginica":
            st.markdown('<p class="result-type">IRIS VIRGINICA</p>', unsafe_allow_html=True)
            st.markdown('<img class="centered-image" src="https://daylily-phlox.eu/wp-content/uploads/2023/10/Iris-virginica-Pond-Crown-Point.jpg" alt="Iris-virginica" />', unsafe_allow_html=True)
            st.markdown(
                """
                <p style='text-align: justify;'>
                Iris virginica adalah spesies dengan petal paling besar dan lebar di antara ketiganya, dengan panjang petal mencapai 4,5–6,9 cm dan lebar 1,2–2,5 cm. Warnanya bervariasi dari biru keunguan hingga ungu pekat, dengan ujung petal yang sedikit melengkung.</p>
                """,
                unsafe_allow_html=True
            )

        st.write("Model yang digunakan memiliki tingkat akurasi ", (score * 100), "%")
