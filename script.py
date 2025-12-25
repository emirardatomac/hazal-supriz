import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import random

# --- Sayfa Ayarları ---
st.set_page_config(page_title="Emir & Hazal", page_icon="🚀", layout="wide")

# --- Özel CSS (Tasarım) ---
st.markdown("""
<style>
    .big-font { font-size:40px !important; color: #E91E63; text-align: center; font-weight: bold; margin-bottom: 0px;}
    .sub-font { font-size:20px !important; color: #555; text-align: center; margin-top: 0px;}
    .photo-label { text-align: center; font-weight: bold; margin-bottom: 10px; color: #E91E63; font-size: 18px; }

    /* Sekme (Tab) Tasarımları */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #fff0f5;
        border-radius: 4px 4px 0px 0px;
        color: #E91E63;
        font-weight: bold;
    }
    .stTabs [aria-selected="true"] {
        background-color: #E91E63;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# --- Başlık ---
st.markdown('<p class="big-font">Emir & Hazal ❤️</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-font">Roket Takımı\'ndan Sonsuzluğa... 🚀</p>', unsafe_allow_html=True)

# --- Müzik ---
try:
    st.audio("sarki.mp3", format='audio/mp3')
except:
    st.warning("🎵 'sarki.mp3' bulunamadı.")

# --- SEKMELER (Ana Sayfa ve Oyunlar) ---
tab1, tab2 = st.tabs(["📖 Hikayemiz", "🎮 Hazalım için oyun"])

with tab1:
    # --- FOTOĞRAF BÖLÜMÜ ---
    st.write("---")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<p class="photo-label">👶 Minik Hazal ve Emir</p>', unsafe_allow_html=True)
        try:
            img_cocukluk = Image.open('cocukluk1.jpeg')
            st.image(img_cocukluk, use_container_width=True)
        except:
            st.info("⚠️ 'cocukluk1.jpeg' bekleniyor.")

    with col2:
        st.markdown('<p class="photo-label">💑 Şimdi bizziko </p>', unsafe_allow_html=True)
        try:
            img_kapak = Image.open('kapak.jpeg')
            st.image(img_kapak, use_container_width=True)
        except:
            st.info("⚠️ 'kapak.jpeg' bekleniyor.")

    # --- CANLI SAYAÇ (JavaScript ile Saniye Saniye) ---
    st.write("---")
    st.subheader("⏳ Ateşleme Zamanı: 15 Aralık 2024")

    # Python ile statik değil, HTML/JS ile dinamik sayaç
    timer_html = """
    <div style="text-align: center; font-family: sans-serif; padding: 20px; background-color: #fff0f5; border-radius: 15px; border: 2px solid #E91E63;">
        <h3 style="color: #555;">15 Aralık 2024'ten beri yörüngedeyiz...</h3>
        <div id="clock" style="font-size: 40px; color: #E91E63; font-weight: bold;">Hesaplanıyor...</div>
        <div id="details" style="font-size: 18px; color: #333; margin-top: 10px;"></div>
    </div>

    <script>
    function updateTimer() {
        const startDate = new Date("December 15, 2024 00:00:00").getTime();
        const now = new Date().getTime();
        const distance = now - startDate;

        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        document.getElementById("clock").innerHTML = days + " Gün " + hours + " Saat " + minutes + " Dakika " + seconds + " Saniye";
        document.getElementById("details").innerHTML = "Seninle geçen her saniye yerçekimsiz ortam gibi eşsiz Bebeğim benim... ";
    }

    setInterval(updateTimer, 1000);
    updateTimer();
    </script>
    """
    components.html(timer_html, height=200)

    # --- NEDEN SEVİYORUM ---
    st.write("---")
    st.subheader("❓ Seni Neden Seviyorum?")
    if 'reason' not in st.session_state:
        st.session_state.reason = "Aviyonik sistemleri başlatmak için butona bas... 👇"

    reasons = [
        "Sivas'ın soğuğunda roket motoru gibi kalbimi ısıttığın için.",
        "Hayatımdaki en başarılı projem olduğun için.",
        "Gözlerinin içine bakınca gökyüzünü gördüğüm için.",
        "Benim en iyi takım arkadaşım ve eşim olduğun için.",
        "Sadece Hazal olduğun, sadece 'Biz' olduğun için..."
        "Eşeğim olduğun için"
        "Zebrem olduğun için"
        "bana küsemediğin için"
        "poponu ısırırım"
    ]
    if st.button("Bir Sebep Söyle ❤️"):
        st.session_state.reason = random.choice(reasons)
    st.success(f"💌 {st.session_state.reason}")

    # --- HARİTA ---
    st.write("---")
    st.subheader("📍 Seni görüp aldığım lokasyon")
    st.write("Cumhuriyet üniversitesi Mühendislik Fakültesi A Binası")

    # GÜNCELLENMİŞ KOORDİNATLAR (Plus Code: P24H+MR)
    map_data = {'lat': [39.7043], 'lon': [37.0246]}
    st.map(map_data, zoom=15)

    # --- MEKTUP ---
    st.write("---")
    st.subheader("💌 Komik bir mektup")
    with st.expander("Mektubu Okumak İçin Tıkla Ask..."):
        # Not: 'color: #333333;' ekledik. Artık yazı hep koyu renk olacak.
        st.markdown("""
        <div style="font-family: 'Georgia', serif; font-size: 18px; background-color: #fcfcfc; color: #333333; padding: 25px; border-radius: 10px; border-left: 6px solid #E91E63; line-height: 1.6;">

        <b>Canım Sevgilim,</b>
        <br><br>
        Her şey o Roket Takımı'nda, gökyüzüne ulaşmaya çalıştığımız günlerde başladı. Biz roketin irtifasını hesaplarken, kalbimin irtifasının seninle bu kadar yükseleceğini hiç hesaplamamıştım.
        <br><br>
        15 Aralık 2024'te bizim için geri sayım bitti ve asıl ateşleme gerçekleşti. O gün anladım ki, benim için en güzel hedef gökyüzü değil, senin yanınmış.
        <br><br>
        O atölyedeki yorgunluklarımız, stresimiz, Sivas'ın ayazı... Hepsi senin bir gülüşünle silinip gidiyor. Sen benim hayatımdaki en hassas sensör, en güvenilir aviyonik sistemsin. Seninle her türlübülansa göğüs gererim.
        <br><br>
        Bu site, bizim yer istasyonumuz. Anılarımız, verilerimiz ve sonsuz sevgimiz burada kayıtlı.
        İyi ki o takımdaydık, iyi ki yörüngelerimiz kesişti.
        <br><br>
        Seni çok seviyorum.
        <br><br>
        <b>- Emir</b>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.subheader("🐍 Hazalın yılan Oyunu")
    st.write("Yön tuşlarını kullanarak Kalpleri (❤️) topla!")

    # HTML/JS Snake Oyunu (Gömülü)
    snake_game_html = """
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    html, body { height: 100%; margin: 0; display: flex; justify-content: center; align-items: center; background-color: #f0f2f6; }
    canvas { border: 4px solid #E91E63; background-color: #222; box-shadow: 0px 0px 20px rgba(233, 30, 99, 0.5); border-radius: 10px; }
    </style>
    </head>
    <body>
    <canvas width="400" height="400" id="game"></canvas>
    <script>
    var canvas = document.getElementById('game');
    var context = canvas.getContext('2d');
    var grid = 16;
    var count = 0;
    var snake = { x: 160, y: 160, dx: grid, dy: 0, cells: [], maxCells: 4 };
    var apple = { x: 320, y: 320 };

    function getRandomInt(min, max) {
      return Math.floor(Math.random() * (max - min)) + min;
    }

    function loop() {
      requestAnimationFrame(loop);
      if (++count < 6) return;
      count = 0;
      context.clearRect(0,0,canvas.width,canvas.height);

      snake.x += snake.dx;
      snake.y += snake.dy;

      if (snake.x < 0) snake.x = canvas.width - grid;
      else if (snake.x >= canvas.width) snake.x = 0;
      if (snake.y < 0) snake.y = canvas.height - grid;
      else if (snake.y >= canvas.height) snake.y = 0;

      snake.cells.unshift({x: snake.x, y: snake.y});
      if (snake.cells.length > snake.maxCells) snake.cells.pop();

      // Yem Çizimi (Kalp)
      context.fillStyle = '#E91E63'; 
      context.font = "20px Arial";
      context.fillText("❤️", apple.x-2, apple.y+14);

      // Yılan Çizimi
      context.fillStyle = '#00FF00';
      snake.cells.forEach(function(cell, index) {
        context.fillRect(cell.x, cell.y, grid-1, grid-1);
        if (cell.x === apple.x && cell.y === apple.y) {
          snake.maxCells++;
          apple.x = getRandomInt(0, 25) * grid;
          apple.y = getRandomInt(0, 25) * grid;
        }
        for (var i = index + 1; i < snake.cells.length; i++) {
          if (cell.x === snake.cells[i].x && cell.y === snake.cells[i].y) {
            snake.x = 160; snake.y = 160; snake.cells = []; snake.maxCells = 4; snake.dx = grid; snake.dy = 0; apple.x = getRandomInt(0, 25) * grid; apple.y = getRandomInt(0, 25) * grid;
          }
        }
      });
    }

    document.addEventListener('keydown', function(e) {
      if (e.which === 37 && snake.dx === 0) { snake.dx = -grid; snake.dy = 0; }
      else if (e.which === 38 && snake.dy === 0) { snake.dy = -grid; snake.dx = 0; }
      else if (e.which === 39 && snake.dx === 0) { snake.dx = grid; snake.dy = 0; }
      else if (e.which === 40 && snake.dy === 0) { snake.dy = grid; snake.dx = 0; }
    });
    requestAnimationFrame(loop);
    </script>
    </body>
    </html>
    """
    components.html(snake_game_html, height=450)