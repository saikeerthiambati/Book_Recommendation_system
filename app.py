import streamlit as st
import pandas as pd
import base64

# ---------------- Page setup ----------------
st.set_page_config(page_title="Book Recommender", page_icon="📚")

# ---------------- Background image (custom CSS) ----------------
IMAGE_PATH = "Background.png"


def get_base64_of_image(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


img_base64 = get_base64_of_image(IMAGE_PATH)

page_bg = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/png;base64,{img_base64}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

[data-testid="stAppViewContainer"] > .main {{
    background-color: rgba(10, 12, 16, 0.92);
}}

[data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
}}

.block-container {{
    background-color: rgba(10, 12, 16, 0.92);
    border-radius: 12px;
    padding: 2rem 3rem;
    margin-top: 1rem;
}}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

st.title("📚 Book Recommendation System")
st.write("Enter a genre you like, and I'll suggest some books for you!")

# ---------------- Load data ----------------
@st.cache_data
def load_data():
    return pd.read_csv("books_small.csv")

df = load_data()

# ---------------- Sample genres (guide for user) ----------------
sample_genres = ["fantasy", "romance", "horror", "mystery", "science-fiction",
                  "thriller", "history", "biography", "poetry", "classics"]

# ---------------- Feature 3: Genre-wise book count chart ----------------
st.subheader("📊 Popular Genres Overview")

@st.cache_data
def get_genre_counts():
    counts = {}
    lower_genres = df["genres"].str.lower()
    for g in sample_genres:
        counts[g] = lower_genres.str.contains(g, na=False).sum()
    return counts

genre_counts = get_genre_counts()
st.bar_chart(genre_counts)

st.divider()

# ---------------- Feature 2: Surprise Me button ----------------
if st.button("🎲 Surprise Me!"):
    random_book = df.sample(1)
    st.info(f"How about: **{random_book['title'].values[0].title()}**?")

st.divider()

# ---------------- Feature 1: Multi-select genres ----------------
st.subheader("🔎 Find Books by Genre")
st.caption("Some popular genres you can try: " + ", ".join(sample_genres))

selected_genres = st.multiselect("Select one or more genres:", sample_genres)

num_results = st.slider("How many books do you want to see?", min_value=5, max_value=30, value=10)

if selected_genres:
    # Match books that contain ANY of the selected genres
    pattern = "|".join(selected_genres)
    filtered = df[df["genres"].str.lower().str.contains(pattern, na=False)]

    if len(filtered) == 0:
        st.warning("Sorry, no books found for the selected genres.")
    else:
        st.success(f"Found {len(filtered)} books for {', '.join(selected_genres)}. Showing top {num_results}:")
        results = filtered["title"].head(num_results)
        for title in results:
            st.write("📖", title.title())

        # ---------------- Feature 5: Download results ----------------
        csv_data = results.to_csv(index=False)
        st.download_button("⬇️ Download results as CSV", csv_data, "recommendations.csv", "text/csv")

st.divider()

# ---------------- Feature 4: Search by title ----------------
st.subheader("🔍 Search by Book Title")
search_title = st.text_input("Enter a book title to search:")

if search_title:
    title_results = df[df["title"].str.lower().str.contains(search_title.lower(), na=False)]

    if len(title_results) == 0:
        st.warning(f"No books found matching '{search_title}'.")
    else:
        st.success(f"Found {len(title_results)} matching book(s):")
        for _, row in title_results.head(10).iterrows():
            st.write(f"📖 **{row['title'].title()}**")
            st.caption(row["genres"])