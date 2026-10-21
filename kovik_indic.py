"""
Kovik-Indic: Deterministic Devanagari Script Integrity & Pluralization Engine
Author: R. R. Sinha
Organization: Kovik Indic (An initiative of Kovik Enterprises)
License: MIT
"""

import unicodedata
import re

class KovikIndicValidator:
    def __init__(self):
        # Unicode range for Devanagari: U+0900 to U+097F
        self.dev_matras = set(chr(cp) for cp in range(0x093E, 0x094D))  # ा to ौ (excluding virama 094D)
        self.virama = chr(0x094D)      # ्
        self.anusvara = chr(0x0902)    # ं
        self.visarga = chr(0x0903)     # ः
        self.candrabindu = chr(0x0901) # ँ

    def validate(self, text: str):
        """
        Validates Devanagari string integrity:
        - Detects orphan matras and modifiers at token start
        - Flags dangling viramas at token end
        - Identifies illegal glyph clashes (double matras, double halant, halant+matra)
        - Detects accidental mixed-script corruption (ignoring template variables)
        """
        if not text:
            return {"valid": True, "errors": []}
            
        norm_text = unicodedata.normalize('NFC', text)
        tokens = re.findall(r'\S+|\s+', norm_text)
        errors = []
        
        for token in tokens:
            stripped = token.strip()
            if not stripped:
                continue
                
            # Mixed script token check
            has_latin = bool(re.search(r'[a-zA-Z]', stripped))
            has_dev = bool(re.search(r'[\u0900-\u097F]', stripped))
            if has_latin and has_dev:
                if not (stripped.startswith('{') and stripped.endswith('}')) and not stripped.startswith('₹'):
                    errors.append(f"Mixed script token: '{stripped}'")

            # Orphan matra or modifier at token start
            first_char = stripped[0]
            if first_char in self.dev_matras:
                errors.append(f"Orphan matra at token start: '{stripped}'")
            elif first_char in (self.anusvara, self.visarga, self.candrabindu):
                errors.append(f"Orphan modifier/anusvara at token start: '{stripped}'")
                
            # Dangling virama at token end
            if stripped.endswith(self.virama):
                errors.append(f"Dangling virama (halant) at token end: '{stripped}'")
                
            # Internal glyph clashes
            for i in range(len(stripped) - 1):
                c1, c2 = stripped[i], stripped[i+1]
                if c1 in self.dev_matras and c2 in self.dev_matras:
                    errors.append(f"Double/Conflicting matra: '{c1}{c2}' in '{stripped}'")
                elif c1 == self.anusvara and c2 == self.anusvara:
                    errors.append(f"Double anusvara clash in '{stripped}'")
                elif c1 == self.virama and c2 == self.virama:
                    errors.append(f"Double virama (halant) clash in '{stripped}'")
                elif c1 == self.virama and c2 in self.dev_matras:
                    errors.append(f"Halant + Matra clash: '{c1}{c2}' in '{stripped}'")

        return {
            "valid": len(errors) == 0,
            "errors": errors
        }

    def pluralize(self, word: str, count: int):
        """
        Applies deterministic Indic pluralization rules based on count.
        """
        if count == 1:
            return {"count": count, "pluralized": f"{count} {word}", "rule": "singular"}
        else:
            if word.endswith("ा"):
                inflected = word[:-1] + "े"
            elif word.endswith("ी"):
                inflected = word[:-1] + "ियाँ"
            else:
                inflected = word + "ों"
            return {"count": count, "pluralized": f"{count} {inflected}", "rule": "oblique/direct_plural"}


_default_engine = KovikIndicValidator()

def validate_indic_text(text: str):
    return _default_engine.validate(text)

def pluralize_indic(word: str, count: int):
    return _default_engine.pluralize(word, count)
