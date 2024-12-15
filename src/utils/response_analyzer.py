from typing import Dict
import re

class ResponseAnalyzer:
    @staticmethod
    def get_word_count(text: str) -> int:
        """Count words in the response."""
        return len(text.split())

    @staticmethod
    def get_key_elements(text: str) -> Dict[str, int]:
        """Analyze presence of key structural elements."""
        elements = {
            "numbered_lists": len(re.findall(r'^\d+\.', text, re.MULTILINE)),
            "bullet_points": len(re.findall(r'^\s*[-•*]', text, re.MULTILINE)),
            "paragraphs": len(re.findall(r'\n\n', text)) + 1,
            "xml_tags": len(re.findall(r'</?[^>]+>', text))
        }
        return elements

    @staticmethod
    def analyze_response(response: str) -> Dict:
        """Perform comprehensive analysis of the response."""
        return {
            "word_count": ResponseAnalyzer.get_word_count(response),
            "elements": ResponseAnalyzer.get_key_elements(response),
            "has_structure": bool(ResponseAnalyzer.get_key_elements(response)["numbered_lists"] or 
                                ResponseAnalyzer.get_key_elements(response)["bullet_points"]),
            "has_xml": bool(ResponseAnalyzer.get_key_elements(response)["xml_tags"])
        }