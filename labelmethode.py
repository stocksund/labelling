import os
import re
import shutil
from datetime import datetime

def extract_date_from_filename(filename):
    """
    Extrahiert ein Datum im Format YYYY-MM-DD aus der Bilddatei.
    """
    match = re.search(r"(\d{4}-\d{2}-\d{2})", filename)
    if match:
        try:
            return datetime.strptime(match.group(1), "%Y-%m-%d")
        except ValueError:
            pass
    return None

def get_bbch_label(date):
    """
    Gibt das BBCH-Stadium anhand des Datums zurück.
    """
    if date < datetime(2025, 4, 1):
        return "BBCH 10-19"
    elif date < datetime(2025, 5, 1):
        return "BBCH 30-39"
    else:
        return "BBCH 50+"

def sort_images_for_training(base_folder):
    """
    Sortiert Bilder aus `base_folder` in Unterordner nach BBCH-Stadium.
    """
    for filename in os.listdir(base_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            filepath = os.path.join(base_folder, filename)
            date = extract_date_from_filename(filename)

            if not date:
                print(f"Kein Datum gefunden in: {filename}")
                continue

            bbch_label = get_bbch_label(date)
            target_dir = os.path.join(base_folder, bbch_label)

            os.makedirs(target_dir, exist_ok=True)  # Ordner erstellen, falls nicht vorhanden

            # Zieldateipfad
            target_path = os.path.join(target_dir, filename)

            # Datei verschieben
            shutil.move(filepath, target_path)
            print(f"{filename} → {bbch_label}/")

    print("\n✅ Fertig! Alle Bilder wurden gelabelt und sortiert.")

if __name__ == "__main__":
    folder = r"C:\Users\johnd\Bachelorarbeit\ba_ma_sem\trainings_data" 
    sort_images_for_training(folder)