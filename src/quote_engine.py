"""A quote_engine is able to create qutoes from different files."""
from abc import ABC, abstractmethod
from typing import List
import docx
import subprocess
import pandas as pd
import regex as re
from quote_model import QuoteModel


class ImportInterface(ABC):
    """Import Interface which is used by multiple subclasses."""

    def __init__(self):
        """Initialize ImportInterface."""
        allowed_extensions = []

    @classmethod
    def can_ingest(cls, path):
        """Ingest quotes."""
        ext = path.split(".")[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes."""
        pass


class CSVImporter(ImportInterface):
    """Read files with a csv extension."""

    allowed_extensions = ["csv"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes from CSV files."""
        if not cls.can_ingest(path):
            raise Exception("cannot ingest exception")

        try:
            quotes = []
            df = pd.read_csv(path, header=0)

            for index, row in df.iterrows():
                new_quote = QuoteModel(row["body"], row["author"])
                quotes.append(new_quote)
            return quotes
        except FileNotFoundError:
            print(f"File not found: {path}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


class DocxImporter(ImportInterface):
    """Read files with a docx extension."""

    allowed_extensions = ["docx"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes from DOCX files."""
        if not cls.can_ingest(path):
            raise Exception("cannot ingest exception")
        try:
            quotes = []
            doc = docx.Document(path)

            for para in doc.paragraphs:
                if para.text.strip():
                    parts = para.text.split("-")
                    if len(parts) == 2:
                        body = parts[0].strip()
                        name = parts[1].strip()
                        new_quote = QuoteModel(body, name)
                        quotes.append(new_quote)

            return quotes
        except FileNotFoundError:
            print(f"File not found: {path}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


class PDFImporter(ImportInterface):
    """Read files with a pdf extension."""

    allowed_extensions = ["pdf"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes from TXT files."""
        if not cls.can_ingest(path):
            raise Exception("cannot ingest exception")

        try:
            pdftotext_path = r"C:\Program Files\Xpdf\bin64\pdftotext.exe"
            result = subprocess.run(
                [pdftotext_path, path, "-"],
                stdout=subprocess.PIPE,
                text=True,
                check=True,
            )
            extracted_text = result.stdout
            quote_author_pairs = re.findall(
                r'"(.*?)" - (.*?)\s*(?="|$)', extracted_text
            )

            quotes = []
            for quote, author in quote_author_pairs:
                new_quote = QuoteModel(quote, author)
                quotes.append(new_quote)
            return quotes
        except FileNotFoundError:
            print(f"File not found: {path}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


class TXTImporter(ImportInterface):
    """Read files with a txt extension."""

    allowed_extensions = ["txt"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes from TXT files."""
        if not cls.can_ingest(path):
            raise Exception("cannot ingest exception")
        try:
            quotes = []
            with open(path, "r", encoding="utf-8-sig") as file:
                for line in file:
                    quote = (line.split(" - ")[0]).replace("\n", "")
                    author = (line.split(" - ")[1]).replace("\n", "")
                    new_quote = QuoteModel(quote, author)
                    quotes.append(new_quote)
            return quotes
        except FileNotFoundError:
            print(f"File not found: {path}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
