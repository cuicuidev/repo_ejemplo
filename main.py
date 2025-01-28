import streamlit as st
import seaborn as sns

def main():
    """Esta función muestra el dataframe del iris."""
    df = sns.load_dataset("iris")
    st.dataframe(df)

if __name__ == "__main__":
    main()