import csv


class Supportarende:
    # Beslut: Klassen representerar ett enskilt supportärende, inte CSV-filen.
    # Attributnamnen följer CSV-kolumnerna. id är ett heltal; övriga värden
    # är strängar eftersom de innehåller namn, kategorier och textstatusar.
    def __init__(
        self,
        id: int,
        kund: str,
        kategori: str,
        prioritet: str,
        status: str,
    ) -> None:
        self.id = id
        self.kund = kund
        self.kategori = kategori
        self.prioritet = prioritet
        self.status = status

    def beskrivning(self) -> str:
        """Returnera en läsbar beskrivning av supportärendet."""
        return (
            f"Ärende {self.id}: {self.kund} – {self.kategori}, "
            f"prioritet {self.prioritet}, status {self.status}."
        )


# CSV-inläsning och omvandling av id till int hör hemma utanför klassen.
with open("supportarenden.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    arenden = [
        Supportarende(
            id=int(row["id"]),
            kund=row["kund"],
            kategori=row["kategori"],
            prioritet=row["prioritet"],
            status=row["status"],
        )
        for row in reader
    ]

for arende in arenden:
    print(arende.beskrivning())
