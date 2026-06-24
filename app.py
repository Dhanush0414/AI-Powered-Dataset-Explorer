import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.sidebar.title("Dataset Explorer")
st.sidebar.write("Upload any CSV file")

st.title("AI-Powered Dataset Explorer")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.write(df.head())

    st.subheader("Dataset Shape")
    st.write(df.shape)

    st.subheader("Column Names")
    st.write(df.columns)

    st.subheader("Data Types")
    st.write(df.dtypes)

    st.subheader("Missing Values")
    st.write(df.isnull().sum())

    st.subheader("Statistical Summary")
    st.write(df.describe())

    st.subheader("Histogram")

    numeric_columns = df.select_dtypes(include='number').columns

    if len(numeric_columns) > 0:

        selected_column = st.selectbox(
            "Select a Numeric Column",
            numeric_columns
        )

        fig, ax = plt.subplots()

        df[selected_column].hist(ax=ax)

        st.pyplot(fig)

    st.subheader("Correlation Matrix")

    correlation = df.corr(numeric_only=True)

    st.write(correlation)

    st.subheader("Correlation Heatmap")

    fig, ax = plt.subplots(figsize=(8, 6))

    sns.heatmap(
        correlation,
        annot=True,
        cmap="coolwarm",
        ax=ax
    )

    st.pyplot(fig)

    st.subheader("Dataset Insights")

    st.write("Total Rows:", df.shape[0])
    st.write("Total Columns:", df.shape[1])
    st.write("Total Missing Values:", df.isnull().sum().sum())