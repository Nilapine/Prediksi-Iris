import streamlit as st
from web_functions import load_data  # Pastikan file ini tersedia
from Tabs import home, predict, visualise  # Pastikan file/folder Tabs tersedia

# Definisikan tab navigasi
Tabs = {
    "Home": home,
    "Prediction": predict,
    "Visualisation": visualise,
}

# Tambahkan CSS untuk latar belakang aplikasi utama, sidebar dengan desain kotak, dan header
page_bg_img = """
<style>
/* Latar belakang utama aplikasi */
[data-testid="stAppViewContainer"] {
    background-image: url("https://github.com/Nilapine/Iris/blob/main/bg.png?raw=true");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

/* Header desain */
[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
}

/* Sidebar desain kotak dengan background */
[data-testid="stSidebar"] {
    background-image: url("https://img.pikbest.com/origin/09/28/72/52MpIkbEsTXsw.jpg!w700wp");
    background-color: #6c4891;  /* Warna latar belakang sidebar */
    border-radius: 10px;  /* Menambahkan sudut melengkung pada sidebar */
    padding: 20px;  /* Menambahkan padding dalam sidebar */
    height: 100vh;  /* Sidebar memanjang penuh dari atas ke bawah */
}

/* Desain tombol menu */
.sidebar-button {
    background-color: #0078D4;  /* Warna tombol default */
    color: white;
    border: #6c4891;
    padding: 15px;
    width: 100%;
    text-align: center;
    border-radius: 8px;
    margin-bottom: 10px;
    font-size: 18px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.stButton button {
            background-color: white;
            color: w#6c4891;
            border-radius: 10px;
            hover : black;
        }

.sidebar-button:hover {
    background-color: #6c4891;  /* Warna tombol saat di-hover */
}

/* Desain tombol saat klik */
.sidebar-button-clicked {
    background-color: #6c4891 !important;  /* Warna ungu saat tombol diklik */
}

/* Styling untuk membuat menu dengan tombol kotak */
.sidebar-container {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

/* Styling untuk footer */
footer {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: #6c4891;
    color: white;
    text-align: center;
    padding: 10px 0;
    font-size: 14px;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Membuat sidebar dengan tombol menu berbentuk kotak
with st.sidebar:
    # Simpan status tombol di session_state
    if 'active_tab' not in st.session_state:
        st.session_state.active_tab = "Home" #default home

    # Tombol navigasi dengan kondisi untuk menandakan klik
    button_home = st.button("Home", key="home", help="Halaman utama", use_container_width=True)
    button_predict = st.button("Prediction", key="predict", help="Prediksi data", use_container_width=True)
    button_visualize = st.button("Visualisation", key="visualise", help="Visualisasi data", use_container_width=True)

    # Simpan tab yang dipilih di session_state
    if button_home:
        st.session_state.active_tab = "Home"
    elif button_predict:
        st.session_state.active_tab = "Prediction"
    elif button_visualize:
        st.session_state.active_tab = "Visualisation"

# Load dataset
df, x, y = load_data()

# Menambahkan logika untuk menangani status tombol yang diklik
# Mengubah tombol yang aktif dengan kelas CSS yang sesuai
for tab in Tabs.keys():
    if st.session_state.active_tab == tab:
        st.markdown(f'<style>.sidebar-button#{tab} {{ background-color: #6c4891 !important; }}</style>', unsafe_allow_html=True)

# Tampilkan page sesuai tab yang dipilih
if st.session_state.active_tab == "Home":
    Tabs["Home"].app(df, x, y)
elif st.session_state.active_tab == "Prediction":
    Tabs["Prediction"].app(df, x, y)
elif st.session_state.active_tab == "Visualisation":
    Tabs["Visualisation"].app(df, x, y)

# Footer
st.markdown('<footer>IrisPredict-2024</footer>', unsafe_allow_html=True)
