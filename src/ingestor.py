"""Ingestor that is able to load quotes from different extensions (DOCX, CSV, PDF, TXT)."""
from typing import List
from quote_engine import (
    ImportInterface,
    DocxImporter,
    CSVImporter,
    PDFImporter,
    TXTImporter,
)
from quote_model import QuoteModel
import random


class Ingestor(ImportInterface):
    """Ingestor class that can import different files."""

    importers = [DocxImporter, CSVImporter, PDFImporter, TXTImporter]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes from files."""
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)
