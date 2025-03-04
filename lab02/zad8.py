import re

def sylaby_counter(slowo):
    samogloski = "aeiouyAEIOUY"
    slowo = slowo.lower()
    sylaby_count = 0
    poprzedniSamogloska = False
    
    for char in slowo:
        if char in samogloski:
            if not poprzedniSamogloska:
                sylaby_count += 1
            poprzedniSamogloska = True
        else:
            poprzedniSamogloska = False
    
    if slowo.endswith("e") and sylaby_count > 1:
        sylaby_count -= 1
    
    return max(sylaby_count, 1)

def readability_score(text: str):
    zdanie = re.split(r'[.!?]', text)
    zdanie = [s.strip() for s in zdanie if s.strip()]
    slowo = text.split()
    
    if not zdanie or not slowo:
        return 0
    
    slowo_count = len(slowo)
    sentence_count = len(zdanie)
    sylaby_count = sum(sylaby_counter(slowo) for slowo in slowo)
    
    avg_slowo_na_zdanie = slowo_count / sentence_count
    avg_sylabys_per_slowo = sylaby_count / slowo_count
    
    score = avg_slowo_na_zdanie + avg_sylabys_per_slowo
    return round(score, 2)


text = "Ala ma kota ktorego kota ma, ala ! jescze new ktora, ma kota."
print(readability_score(text))