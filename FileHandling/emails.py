def nadawca_e_maila(tresc):
    for linia in tresc.splitlines():
        if linia.startswith("From:"):
            return linia.replace("From:", "").strip()
    return "Nie znaleziono"


def odbiorca_e_maila(tresc):
    for linia in tresc.splitlines():
        if linia.startswith("To:"):
            return linia.replace("To:", "").strip()
    return "Nie znaleziono"


def email_subject(tresc):
    for linia in tresc.splitlines():
        if linia.startswith("Subject:"):
            return linia.replace("Subject:", "").strip()
    return "Nie znaleziono"


def email_body(tresc):
    # Dzielimy na dwie części po pierwszej pustej linii
    czesci = tresc.split("\n\n", 1)
    if len(czesci) > 1:
        return czesci[1].strip()
    return "Brak treści"
