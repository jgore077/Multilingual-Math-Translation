import re
from LaTeXMasker import LaTeXMasker
from TranslationModel import MBartModel



class MaskedTranslationModel:
    
    def __init__(self) -> None:
        self.maskerString= 'QZ'
        self.masker= LaTeXMasker(self.maskerString)
        self.translater= MBartModel()
        self.maskerRegexString= r'[¿\?\.,!0-9 ' + self.maskerString + r']*'
    
    def translate(self,text:str,iso639_1_from:str = None,iso639_1_to:str = 'en'):
        maskedString,maskedDict= self.masker.mask(text)
        match= re.match(self.maskerRegexString, maskedString)
        if match.group() == "" or match.group() == "¿":
            translatedString= self.translater.translate(maskedString,iso639_1_from,iso639_1_to)
            eStringMatch= re.search("[tT]he Committee recommends that the State party take all necessary measures to ensure", translatedString)
            if eStringMatch is not None:
                translatedString= self.translater.translate(text, iso639_1_from, iso639_1_to)
            return self.masker.unmask(translatedString,maskedDict)
        return text
        
        
if __name__=="__main__":
    model = MaskedTranslationModel()
    result=model.translate(r"می‌خواهم مقدار عبارت زیر را پیدا کنم: $$ 5^{133} \mod 8. $$. متوجه شدم که   هنگامی که $n$ فرد است و در غیر اینصورت برابر 1 است، که من را به این نتیجه می‌رساند که $5^{133} \mod 8 = 5$ اما نمی‌دانم چگونه این را اثبات کنم. چگونه می‌توانم اثبات کنم که این اتفاق می‌افتد (یا اگر این اتفاق نمی‌افتد، راه‌حل دیگری را پیدا کنم)؟")