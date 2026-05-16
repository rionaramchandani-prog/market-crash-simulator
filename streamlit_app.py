import streamlit as st
import matplotlib.pyplot as plt
import random

# ---------------- PAGE SETUP ----------------

st.set_page_config(
    page_title="Volatility",
    layout="wide"
)

# ---------------- SESSION STATE ----------------

if "game_started" not in st.session_state:
    st.session_state.game_started = False

if "cash" not in st.session_state:
    st.session_state.cash = 10000

if "shares" not in st.session_state:
    st.session_state.shares = 0

if "round" not in st.session_state:
    st.session_state.round = 1

# ---------------- LANDING PAGE ----------------

if not st.session_state.game_started:

    st.markdown("# 📉 Volatility")

    st.markdown(
        "## An interactive behavioural finance experience exploring fear, herd mentality and market psychology."
    )

    st.markdown("---")

    st.markdown("## 💥 Can You Survive the Crash?")

    st.markdown("""
You are entering a financial market where panic and irrational behaviour influence investor decisions.

Protect and grow your portfolio while navigating uncertainty.
""")

    st.markdown("---")

    st.markdown("""
### 🎮 Gameplay

📈 BUY → invest during market opportunities

📉 SELL → protect yourself during panic

⏸ HOLD → wait out uncertainty

Every scenario behaves differently.
""")

    if st.button("🚀 Simulate Crash"):

        st.session_state.game_started = True

        st.rerun()

# ---------------- GAME ----------------

else:

    st.title("📉 Volatility")

    st.caption(
        "Navigate fear, irrationality and financial chaos."
    )

    # Historical scenarios

    st.sidebar.header("🕰 Historical Crash Mode")

    market_mode = st.sidebar.selectbox(
        "Choose Historical Crash",
        [
            "2008 Financial Crisis",
            "Dot-Com Bubble",
            "COVID-19 Crash",
            "Crypto Collapse"
        ]
    )

    # Scenario logic

    if market_mode == "2008 Financial Crisis":

        headline = (
            "Major banks collapse as global financial system weakens"
        )

        fear = random.randint(75,100)

        stock_price = random.randint(40,90)

        herd_sell = random.randint(70,95)

        explanation = (
            "The 2008 crisis began after risky lending and the housing market collapse weakened global banks."
        )

    elif market_mode == "Dot-Com Bubble":

        headline = (
            "Technology stocks crash after years of speculation"
        )

        fear = random.randint(55,85)

        stock_price = random.randint(60,120)

        herd_sell = random.randint(50,85)

        explanation = (
            "Investors overvalued internet companies despite weak profits."
        )

    elif market_mode == "COVID-19 Crash":

        headline = (
            "Pandemic sparks global recession fears"
        )

        fear = random.randint(70,95)

        stock_price = random.randint(50,110)

        herd_sell = random.randint(65,90)

        explanation = (
            "Lockdowns disrupted businesses and global supply chains."
        )

    else:

        headline = (
            "Crypto market loses billions during panic selling"
        )

        fear = random.randint(60,95)

        stock_price = random.randint(30,100)

        herd_sell = random.randint(60,90)

        explanation = (
            "Crypto markets are highly speculative and volatile."
        )

    # Portfolio

    portfolio = (
        st.session_state.cash +
        st.session_state.shares * stock_price
    )

    # Dashboard

    c1,c2,c3,c4,c5 = st.columns(5)

    with c1:
        st.metric(
            "💰 Cash",
            f"${st.session_state.cash}"
        )

    with c2:
        st.metric(
            "📈 Shares",
            st.session_state.shares
        )

    with c3:
        st.metric(
            "💵 Stock Price",
            f"${stock_price}"
        )

    with c4:
        st.metric(
            "🏦 Portfolio",
            f"${portfolio}"
        )

    with c5:
        st.metric(
            "🏆 Round",
            st.session_state.round
        )

    st.metric(
        "😨 Fear Level",
        f"{fear}%"
    )

    st.metric(
        "🐑 Investors Selling",
        f"{herd_sell}%"
    )

    # News

    st.subheader("📰 Market News")

    st.info(headline)

    # Education

    st.subheader("📚 Why Is This Happening?")

    st.write(explanation)

    if herd_sell > 70:

        st.info(
            "Investors are copying each other. This herd behaviour amplifies crashes."
        )

    # Trading

    st.subheader("📊 Trading")

    a,b,c = st.columns(3)

    buy=False
    sell=False
    hold=False

    with a:

        buy=st.button("📈 BUY")

        if buy:

            if st.session_state.cash>=stock_price:

                st.session_state.cash-=stock_price

                st.session_state.shares+=1

    with b:

        sell=st.button("📉 SELL")

        if sell:

            if st.session_state.shares>0:

                st.session_state.cash+=stock_price

                st.session_state.shares-=1

    with c:

        hold=st.button("⏸ HOLD")

    # Personality

    st.subheader("🧠 Investor Personality")

    personality="?"

    if buy:

        if fear>70:

            personality="Opportunistic Trader"

        else:

            personality="Aggressive Investor"

    elif sell:

        if fear>70:

            personality="Panic Investor"

        else:

            personality="Risk Averse Investor"

    elif hold:

        personality="Rational Investor"

    st.write(
        f"Investor Type: **{personality}**"
    )

    # Score

    st.subheader("🏆 Survival Score")

    score=portfolio-10000

    st.metric(
        "Performance",
        score
    )

    # Next round

    if st.button("➡️ Next Round"):

        st.session_state.round+=1

        st.rerun()

    # Graph

    prices=[100]

    for i in range(10):

        change=random.randint(
            -fear//3,
            20
        )

        prices.append(
            prices[-1]+change
        )

    fig,ax=plt.subplots(
        figsize=(10,5)
    )

    ax.plot(
        prices,
        linewidth=3
    )

    ax.set_title(
        market_mode
    )

    st.pyplot(fig)

    # Restart

    if st.button(
        "🔄 Restart"
    ):

        st.session_state.game_started=False

        st.session_state.cash=10000

        st.session_state.shares=0

        st.session_state.round=1

        st.rerun()
        