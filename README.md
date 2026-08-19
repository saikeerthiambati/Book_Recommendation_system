# 📚 Book Recommendation System

<<<<<<< HEAD
🔗 **Live Demo:** [bookrecommendationsystempython.streamlit.app](https://bookrecommendationsystempython.streamlit.app/)

A content-based book recommendation web app built with Python and Streamlit.

=======
A content-based book recommendation web app built with Python and Streamlit.
>>>>>>> aeb32121bc3c0a2e636b56457e8a09f73c485a93
## Features

- **Genre-based recommendations** — select one or more genres and get matching book suggestions
- **Genre overview chart** — bar chart showing how many books exist per popular genre
- **Surprise Me button** — get a random book suggestion
- **Title search** — search for a book by name and see its genres
- **Download results** — export your recommended books list as a CSV file
- Custom themed UI with a background image

## Dataset

Built using the [10,000 Books and Their Genres (standardized)](https://www.kaggle.com/datasets/michaelrussell4/10000-books-and-their-genres-standardized) dataset from Kaggle (book titles and genres sourced from GoodReads/Project Gutenberg). The dataset was trimmed to keep only the `title` and `genres` columns for faster loading.

## Tech Stack

- Python 3
- Streamlit — web UI
- Pandas — data loading and filtering

## How to Run Locally

1. Clone this repository:
   ```
   git clone https://github.com/saikeerthiambati/Book_Recommendation_system.git
   ```
2. Navigate into the project folder:
   ```
   cd Book_Recommendation_system
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the app:
   ```
   streamlit run app.py
   ```

## How It Works

The app uses **content-based filtering** — it matches books to a user's chosen genre(s) by checking whether the requested genre appears in each book's genre tags. Results can be filtered by genre selection, searched by title, or discovered randomly.

## Author

Sai Keerthi Ambati