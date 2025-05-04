import streamlit as st
import pandas as pd
import plotly.express as px
import json
import os

st.set_page_config(page_title="Simple Finance App", page_icon="💰", layout="wide")

# --- Session State Initialization ---
category_file = "categories.json"

if "categories" not in st.session_state:
    st.session_state.categories = {"Uncategorized": []}

if os.path.exists(category_file):
    with open(category_file, "r") as f:
        st.session_state.categories = json.load(f)


# --- Helpers ---
def save_categories():
    with open(category_file, "w") as f:
        json.dump(st.session_state.categories, f)


def categorize_transactions(df):
    df["Category"] = "Uncategorized"
    for category, keywords in st.session_state.categories.items():
        if category == "Uncategorized" or not keywords:
            continue
        lowered_keywords = [kw.lower().strip() for kw in keywords]
        for idx, row in df.iterrows():
            details = row["Details"].lower().strip()
            if details in lowered_keywords:
                df.at[idx, "Category"] = category
    return df


def load_transactions(file):
    try:
        df = pd.read_csv(file)
        df.columns = [col.strip() for col in df.columns]

        expected_columns = {"Date", "Details", "Amount", "Debit/Credit"}
        if not expected_columns.issubset(set(df.columns)):
            st.error(f"CSV must include columns: {expected_columns}")
            return None

        df["Amount"] = df["Amount"].str.replace(",", "").astype(float)
        df["Date"] = pd.to_datetime(df["Date"], format="%d %b %Y", errors="coerce")
        df = df.dropna(subset=["Date"])
        return categorize_transactions(df)

    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None


def add_keyword_to_category(category, keyword):
    keyword = keyword.strip()
    if keyword and keyword not in st.session_state.categories[category]:
        st.session_state.categories[category].append(keyword)
        save_categories()
        return True
    return False


# --- App ---
def main():
    st.title("📊 Simple Finance Dashboard")
    st.sidebar.info(f"Streamlit version: {st.__version__}")

    uploaded_file = st.file_uploader("📤 Upload your transaction CSV file", type=["csv"])

    if uploaded_file is not None:
        df = load_transactions(uploaded_file)

        if df is not None:
            debits_df = df[df["Debit/Credit"].str.lower() == "debit"].copy()
            credits_df = df[df["Debit/Credit"].str.lower() == "credit"].copy()

            if debits_df.empty and credits_df.empty:
                st.warning("No valid Debit or Credit records found.")
                return

            st.session_state.debits_df = debits_df.copy()

            tab1, tab2 = st.tabs(["💸 Expenses (Debits)", "💰 Payments (Credits)"])

            # --- Expenses Tab ---
            with tab1:
                new_category = st.text_input("New Category Name")
                if st.button("➕ Add Category") and new_category:
                    if new_category not in st.session_state.categories:
                        st.session_state.categories[new_category] = []
                        save_categories()
                        st.rerun()
                    else:
                        st.warning("Category already exists!")

                st.subheader("🧾 Your Expenses")
                edited_df = st.data_editor(
                    st.session_state.debits_df[["Date", "Details", "Amount", "Category"]],
                    column_config={
                        "Date": st.column_config.DateColumn("Date", format="DD/MM/YYYY"),
                        "Amount": st.column_config.NumberColumn("Amount", format="%.2f AED"),
                        "Category": st.column_config.SelectboxColumn(
                            "Category", options=list(st.session_state.categories.keys())
                        )
                    },
                    hide_index=True,
                    use_container_width=True,
                    key="category_editor"
                )

                if st.button("✅ Apply Changes"):
                    for idx, row in edited_df.iterrows():
                        new_cat = row["Category"]
                        if new_cat != st.session_state.debits_df.at[idx, "Category"]:
                            details = row["Details"]
                            st.session_state.debits_df.at[idx, "Category"] = new_cat
                            add_keyword_to_category(new_cat, details)
                    st.success("Changes applied and keywords updated!")

                st.subheader("📊 Expense Summary")
                category_totals = st.session_state.debits_df.groupby("Category")["Amount"].sum().reset_index()
                category_totals = category_totals.sort_values("Amount", ascending=False)

                st.dataframe(
                    category_totals,
                    column_config={"Amount": st.column_config.NumberColumn("Amount", format="%.2f AED")},
                    use_container_width=True,
                    hide_index=True
                )

                fig = px.pie(
                    category_totals,
                    values="Amount",
                    names="Category",
                    title="Expenses by Category"
                )
                st.plotly_chart(fig, use_container_width=True)

            # --- Payments Tab ---
            with tab2:
                st.subheader("💵 Payment Summary")
                total_payments = credits_df["Amount"].sum()
                st.metric("Total Payments", f"{total_payments:,.2f} AED")
                st.dataframe(credits_df, use_container_width=True)


main()
