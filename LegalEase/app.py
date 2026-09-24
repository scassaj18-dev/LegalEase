import streamlit as st
import requests


st.set_page_config(
    page_title="LegalEase",
    page_icon="⚖️",
    layout="wide"
)


st.title("⚖️ LegalEase")
st.subheader("AI-Powered Legal Document Generator")


st.info(
    "LegalEase creates AI-generated legal document drafts. "
    "Please review the document carefully and seek professional legal advice when appropriate."
)


document_type = st.text_input(
    "Document Type",
    placeholder="Example: Employment Contract"
)


parties = st.text_area(
    "Parties",
    placeholder="Example: ABC Technologies and John Smith"
)


terms = st.text_area(
    "Terms",
    placeholder="Example: Salary: ₹50,000; Work location: Coimbatore; Notice period: 30 days"
)


dates = st.text_input(
    "Dates",
    placeholder="Example: Effective date: 01-10-2026"
)


if st.button("Generate Document"):

    if not document_type or not parties or not terms:
        st.warning("Please fill in the required fields.")

    else:

        try:

            response = requests.post(
                "http://127.0.0.1:8000/generate",
                json={
                    "document_type": document_type,
                    "parties": parties,
                    "terms": terms,
                    "dates": dates
                }
            )

            if response.status_code == 200:

                result = response.json()["document"]

                st.success("Document generated successfully!")

                edited_document = st.text_area(
                    "Edit Document",
                    value=result,
                    height=500
                )

                st.download_button(
                    "Download TXT",
                    edited_document,
                    file_name="legalease_document.txt",
                    mime="text/plain"
                )

            else:

                st.error(
                    f"Backend error: {response.status_code}"
                )

                st.code(response.text)

        except Exception as e:

            st.error(
                f"Could not connect to FastAPI backend: {e}"
            )