from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from ai_core.gemini_generator import GeminiDocumentGenerator

router = APIRouter()

generator = GeminiDocumentGenerator()


class DocumentRequest(BaseModel):
    document_type: str
    parties: str
    terms: str
    dates: str


@router.post("/generate")
def generate_document(request: DocumentRequest):

    try:

        document = generator.generate_document(
            request.document_type,
            request.parties,
            request.terms,
            request.dates
        )

        return {
            "document": document
        }

    except Exception as e:

        return JSONResponse(
            status_code=500,
            content={
                "error": str(e)
            }
        )