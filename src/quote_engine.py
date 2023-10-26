from abc import ABC, abstractmethod
from typing import List
import docx
import subprocess
import pandas as pd
import regex as re

from quote_model import QuoteModel

class ImportInterface(ABC):

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path):
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass

class CSVImporter(ImportInterface):
    """Read files with a csv extension."""
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        df = pd.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return QuoteModel
    
class DocxImporter(ImportInterface):
    """Read files with a docx extension."""
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text.strip():
                parts = para.text.split('-')
                if len(parts) == 2:
                    quote = parts[0].strip()
                    name = parts[1].strip()
                    new_quote = QuoteModel(quote, name)
                    quotes.append(new_quote)

        return quote
    
class PDFImporter(ImportInterface):
    """Read files with a pdf extension."""
    allowed_extensions = ['pdf']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        pdftotext_path = r'C:\Program Files\Xpdf\bin64\pdftotext.exe'
        result = subprocess.run([pdftotext_path, path, '-'], stdout=subprocess.PIPE, text=True, check=True)
        extracted_text = result.stdout
        quote_author_pairs = re.findall(r'"(.*?)" - (.*?)\s*(?="|$)', extracted_text)

        quotes = []
        for quote, author in quote_author_pairs:
            new_quote = QuoteModel(quote, author)
            quotes.append(new_quote)
        return quote

class TXTImporter(ImportInterface):
    """Read files with a txt extension."""
    allowed_extensions = ['txt']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        with open(path, 'r') as file:
            for line in file:
                quote = (line.split(' - ')[0]).replace("\n", "")
                author = (line.split(' - ')[1]).replace("\n", "")
                new_quote = QuoteModel(quote,author)
                quotes.append(new_quote)
        return quotes
        