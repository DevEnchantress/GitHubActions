import datetime

def main():
    # Aktuelles Datum und Zeit
    heute = datetime.datetime.now()
    # Wochentage
    wochentage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
    wochentag = wochentage[heute.weekday()]
    # Formatiertes Datum
    datum = heute.strftime("%d.%m.%Y")
    # Ausgabe
    print("Hallo, schön dass du da bist.")
    print(f"Heute ist {wochentag}")
    print(datum)
    print("Hab einen schönen Tag.")

if __name__ == "__main__":
    main()
