from typing import List
from quote_engine import ImportInterface, DocxImporter, CSVImporter, PDFImporter, TXTImporter
from quote_model import QuoteModel

class Ingestor(ImportInterface):
    importers = [DocxImporter, CSVImporter, PDFImporter,TXTImporter]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)

# print(Importer.parse('_data/DogQuotes/DogQuotesDOCX.docx'))
# print(Importer.parse('_data/DogQuotes/DogQuotesCSV.csv'))
# print(Importer.parse('_data/DogQuotes/DogQuotesPDF.pdf'))
# print(Importer.parse('_data/DogQuotes/DogQuotestxt.txt'))

# paths = [
#     '_data/DogQuotes/DogQuotesDOCX.docx',
#     '_data/DogQuotes/DogQuotesCSV.csv',
#     '_data/DogQuotes/DogQuotesPDF.pdf',
#     '_data/DogQuotes/DogQuotestxt.txt'
# ]

# quotes = []

# for path in paths:
#     quotes.append(Ingestor.parse(path))

# print(quotes)
