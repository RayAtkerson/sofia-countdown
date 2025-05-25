import streamlit as st
import time
from datetime import datetime, timezone, timedelta

eta = datetime(2025, 6, 2, 3, 38, tzinfo=timezone.utc)  # June 1, 9:38 PM MT, I think

st.set_page_config(page_title="Flight Countdown", page_icon="✈️", layout="centered")

st.title("✈️ Sofia's Flight Countdown")
st.write("This took me longer than I was expecting I'm a big dumbass")

# --- Timer Loop ---
placeholder = st.empty()

while True:
    now = datetime.now(timezone.utc)
    remaining = eta - now

    if remaining.total_seconds() <= 0:
        placeholder.success("🎉 Your flight has landed!")
        break

    hours, rem = divmod(int(remaining.total_seconds()), 3600)
    minutes, seconds = divmod(rem, 60)

    placeholder.metric("Time Remaining", f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    time.sleep(1)
