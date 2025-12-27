import streamlit as st
import random
from datetime import datetime

# --- ЗАЩИТА ПАРОЛЕМ ЧЕРЕЗ SECRETS ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("🔒 Милый новогодний подарок для моей любимой")
    st.write("Введи пароль, чтобы открыть ❤️")
    user_input = st.text_input("Пароль", type="password")
    if st.button("Войти"):
        if user_input == st.secrets["gift_password"]:
            st.session_state.authenticated = True
            st.success("Добро пожаловать, моя любовь! 🥰")
            st.rerun()
        else:
            st.error("Неверный пароль 😔")
    st.stop()

# --- ДАННЫЕ (замени на свои) ---
her_name = "Ника"  # Её имя
start_date = datetime(2025, 6, 14)  # Дата знакомства
days_together = (datetime.now() - start_date).days

new_year_date = datetime(2026, 1, 1)
days_to_new_year = (new_year_date - datetime.now()).days

messages = [
    "Ты самое лучшее, что со мной случилось! ❤️",
    "Твоя улыбка — мой любимый свет 😘",
    "Каждый день с тобой — как сказка 💕",
]

reasons = [
    "За твою невероятную доброту 🌟",
    "За то, как ты смеёшься над моими шутками 😂",
]

compliments = [
    "Ты сегодня выглядишь как принцесса! 👑",
    "Ты делаешь мой мир ярче каждый день 💖",
]

backgrounds = {
    "Главная": "https://99px.ru/sstorage/53/2014/01/mid_93854_9728.jpg",
    "Новогоднее поздравление": "https://m.media-amazon.com/images/I/71yqRuERr5L._AC_UF894,1000_QL80_.jpg",
    "Сюрприз любви": "https://img.freepik.com/premium-photo/valentines-day-pink-background-with-red-pink-hearts_280388-860.jpg",
    "Почему я тебя люблю": "https://thumbs.dreamstime.com/b/valentines-day-hearts-abstract-holiday-background-pastel-colored-heart-shaped-lights-texture-st-valentine-s-love-wedding-wallpaper-300646016.jpg",
    "Наши воспоминания": "https://thumbs.dreamstime.com/b/cute-teddy-bear-holding-heart-pink-balloons-background-plush-holds-shiny-surrounded-soft-white-creating-warm-347460194.jpg",
    "Счётчик нашей любви": "https://static.vecteezy.com/system/resources/previews/008/855/363/non_2x/rainbow-unicorn-fantasy-background-with-hearts-and-stars-holographic-illustration-in-pastel-colors-bright-multicolored-sky-vector.jpg",
    "Комплимент дня": "https://img.pikbest.com/backgrounds/20250102/romantic-valentines-day-background-with-falling-hearts_11333117.jpg!bwr800",
}

bear_images = [
    "https://99px.ru/sstorage/53/2020/10/mid_316371_785261.jpg",
    "https://media.istockphoto.com/id/171146711/photo/teddy-bear-new-years-day.jpg?s=612x612&w=0&k=20&c=bbvMtqOGMplW8UC2jFnMfhYwYb93-D8-1J7_TWXKohI=",
    "https://png.pngtree.com/thumb_back/fw800/background/20251127/pngtree-happy-new-year-celebration-with-adorable-teddy-bear-image_20621582.webp",
    "https://png.pngtree.com/thumb_back/fw800/background/20251127/pngtree-cute-teddy-bear-celebrating-new-year-with-party-hat-and-heart-image_20621595.webp",
    "https://thumbs.dreamstime.com/b/happy-new-year-cute-teddy-bear-sparkler-brown-celebrates-arrival-adorable-toy-wears-festive-yellow-party-hat-412357258.jpg",
    "https://as2.ftcdn.net/jpg/05/70/19/75/1000_F_570197574_wEDVDADjKs7FdybrfE1EpKhpbdMiO2U1.jpg",
]

page = st.sidebar.radio("Выбери раздел ❤️", [
    "Главная 🎄",
    "Новогоднее поздравление 🎉",
    "Сюрприз любви 💕",
    "Почему я тебя люблю ❤️",
    "Наши воспоминания 📸",
    "Счётчик нашей любви ⏳",
    "Комплимент дня 😘"
])

bg_url = backgrounds.get(page.split()[0], backgrounds["Главная"])  # Берем первую слово как ключ
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("{bg_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    /* Полупрозрачный оверлей для текста */
    .main > div {{
        background-color: rgba(255, 255, 255, 0.7);
        padding: 20px;
        border-radius: 15px;
        margin: 10px;
    }}
    </style>
    """, unsafe_allow_html=True)

st.title("Милый новогодний подарок для тебя от меня 🎄💕")

if page.startswith("Главная"):
    st.write(f"Привет, {her_name}! Это приложение специально для тебя. С наступающим 2026 годом! Я люблю тебя бесконечно! 🥰")
    st.image(bear_images[0], caption="Милый медведь с подарком для тебя ❤️")
    st.balloons()

elif page.startswith("Новогоднее поздравление"):
    st.write(f"Дорогая {her_name}, с Новым 2026 годом! 🎉 Желаю тебе море счастья, тепла и наших совместных приключений. Пусть этот год принесёт только радость, как твоя улыбка! Я так рад, что встречу его с тобой. ❤️")
    st.write(f"До Нового года осталось {days_to_new_year} дней! Давай отметим вместе? 🥂")
    st.snow()
    
    st.subheader("Милые медведи для тебя 🐻")
    cols = st.columns(2)
    for i, img in enumerate(bear_images):
        with cols[i % 2]:
            st.image(img, caption=f"Медведь #{i+1} желает счастья! 🎊")
    
    if st.button("Получить новогодний сюрприз"):
        st.balloons()
        st.write(random.choice(["Пусть все мечты сбудутся! 🌟", "Ты — мой лучший подарок! 🎁"]))

elif page.startswith("Сюрприз любви"):
    if st.button("Открыть сюрприз"):
        st.write(random.choice(messages))
        st.balloons()

elif page.startswith("Почему я тебя люблю"):
    st.write("Вот несколько причин (а их бесконечно много):")
    for reason in reasons:
        st.write(f"• {reason}")
    if st.button("Ещё одна причина случайно"):
        st.write(random.choice(reasons))

elif page.startswith("Наши воспоминания"):
    st.write("Наши лучшие моменты :")
    col1, col2 = st.columns(2)
    with col1:
        st.image("photo1.jpg", caption="Просто милая семейная фотка) 💑")  
        st.image("photo3.jpg", caption="Путешествие вместе ✈️")
    with col2:
        st.image("photo2.jpg", caption="Напоминание что нам нужно больше совместных фото")

elif page.startswith("Счётчик нашей любви"):
    st.write(f"Мы вместе уже {days_together} дней! И каждый — как первый. ❤️")
    st.snow()

elif page.startswith("Комплимент дня"):
    if st.button("Получить комплимент"):
        st.write(random.choice(compliments))
        st.balloons()
