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
# --- КОНЕЦ ЗАЩИТЫ ---


her_name = "Ника"
start_date = datetime(2025, 6, 14)  
days_together = (datetime.now() - start_date).days

# Новогодние данные
new_year_date = datetime(2026, 1, 1)
days_to_new_year = (new_year_date - datetime.now()).days

messages = [
    "Ты самое лучшее, что со мной случилось! ❤️",
    "Твоя улыбка — мой любимый свет 😘",
    "Пусть всё, о чём ты мечтаешь, становится чуть ближе каждый день 🌸"
]

reasons = [
    "За твою невероятную доброту 🌟",
    "За то, как ты смеёшься над моими шутками(редко но метко) 😂",
    "За твою красоту ❤️"
]

compliments = [
    "Ты сегодня выглядишь как принцесса! 👑",
    "Ты делаешь мой мир ярче каждый день 💖",
    "Ты умеешь делать счастливыми",
    "Ты прекрасна именно такой, какая ты есть"
]

bear_images = [
    "https://thumbs.dreamstime.com/b/cute-bear-enjoy-new-year-party-celebration-balloon-gift-watercolor-illustration-background-generative-ai-cute-bear-286326533.jpg",
    "https://static.vecteezy.com/system/resources/previews/025/504/171/large_2x/cute-polar-bear-at-a-new-years-celebration-ai-generated-photo.jpeg",
    "https://thumbs.dreamstime.com/b/group-cartoon-bears-wearing-party-hats-holding-balloons-bears-smiling-appear-to-be-celebrating-new-year-s-421552281.jpg",
    "https://thumbs.dreamstime.com/b/cute-cartoon-style-animals-celebrate-year-various-including-bears-fox-wear-party-hats-smile-holding-large-numbers-416672590.jpg",
]


page = st.sidebar.selectbox("Выбери раздел ❤️", [
    "Главная",
    "Новогоднее поздравление", 
    "Сюрприз любви",
    "Почему я тебя люблю",
    "Наши воспоминания",
    "Счётчик нашей любви",
    "Комплимент дня"
])

st.title("Милый новогодний подарок для тебя от меня 🎄💕")

if page == "Главная":
    st.write(f"Привет, {her_name}! Это приложение специально для тебя. С наступающим 2026 годом! Я люблю тебя бесконечно! 🥰")
    st.image(bear_images[0], caption="Милый медведь с подарком для тебя ❤️")  
    st.balloons()

elif page == "Новогоднее поздравление":
    st.write(f"Дорогая {her_name}, с Новым 2026 годом! 🎉 Желаю тебе море счастья, тепла и наших совместных приключений. Пусть этот год принесёт только радость, как твоя улыбка! Я так рад, что встречу его с тобой. ❤️")
    st.write(f"До Нового года осталось {days_to_new_year} дней! Давай отметим вместе? 🥂")
    st.snow()  # Анимация снега!
    
    st.subheader("Милые медведи для тебя 🐻")
    cols = st.columns(2)  # Галерея в 2 столбца
    for i, img in enumerate(bear_images):
        with cols[i % 2]:
            st.image(img, caption=f"Медведь #{i+1} желает счастья! 🎊")
    
    if st.button("Получить новогодний сюрприз"):
        st.confetti()
        st.write(random.choice(["Пусть все мечты сбудутся! 🌟", "Ты — мой лучший подарок! 🎁"]))

elif page == "Сюрприз любви":
    if st.button("Открыть сюрприз"):
        st.write(random.choice(messages))
        st.confetti()

elif page == "Почему я тебя люблю":
    st.write("Вот несколько причин (а их бесконечно много):")
    for reason in reasons:
        st.write(f"• {reason}")
    if st.button("Ещё одна причина случайно"):
        st.write(random.choice(reasons))

elif page == "Наши воспоминания":
    st.write("Наши лучшие моменты:")
    col1, col2 = st.columns(2)
    with col1:
        st.image("photo1.jpg", caption="Твой день рождения 💑")
        st.image("photo3.jpg", caption="Путешествие вместе ✈️")
    with col2:
        st.image("photo2.jpg", caption="Это напоминание о необходимости общих фото")
        

elif page == "Счётчик нашей любви":
    st.write(f"Мы вместе уже {days_together} дней! И каждый — как первый. ❤️")
    st.snow()

elif page == "Комплимент дня":
    if st.button("Получить комплимент"):
        st.write(random.choice(compliments))
        st.balloons()
