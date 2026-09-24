import os
import time

from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


class GeminiDocumentGenerator:

    def generate_document(
        self,
        document_type,
        parties,
        terms,
        dates
    ):

        prompt = f"""
You are a legal document drafting assistant.

Create a professional draft legal document.

Document Type:
{document_type}

Parties:
{parties}

Terms:
{terms}

Dates:
{dates}

Requirements:
- Use clear professional legal language.
- Include a suitable title.
- Include the parties.
- Include important terms and conditions.
- Include dates where provided.
- Use numbered sections.
- Add a signature section.
- Do not invent important personal or financial information.
- Clearly state that this is an AI-generated draft requiring human or legal review.

Return only the document text.
"""

        last_error = None

        for attempt in range(3):

            try:

                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt
                )

                return response.text

            except Exception as e:

                last_error = e

                if "503" in str(e) or "UNAVAILABLE" in str(e):

                    if attempt < 2:
                        time.sleep(5)
                        continue

                raise last_error