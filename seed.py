from database import SessionLocal
from models import Club, Event
from datetime import datetime, timedelta

def seed_database():
    db = SessionLocal()

    # Eğer veritabanında zaten veri varsa tekrar ekleme yapma
    if db.query(Club).first():
        print("Veritabanında zaten veri var. Seed atlandı.")
        db.close()
        return

    # 1. Örnek Kulüpler
    club1 = Club(name="Yazılım ve Bilişim Kulübü", description="Yazılım projeleri ve eğitimler düzenler.")
    club2 = Club(name="Doğa Sporları Kulübü", description="Trekking ve kamp etkinlikleri yapar.")
    
    db.add_all([club1, club2])
    db.commit()

    # 2. Örnek Etkinlikler
    event1 = Event(
        title="Python & FastAPI Workshop",
        description="Mikroservis mimarisine giriş workshop'u.",
        location="Mühendislik Fakültesi Amfi-1",
        capacity=50,
        event_date=datetime.utcnow() + timedelta(days=7),
        category="TECHNOLOGY",
        club_id=club1.id
    )

    event2 = Event(
        title="Kazdağları Doğa Yürüyüşü",
        description="Günübirlik trekking etkinliği.",
        location="Kazdağları",
        capacity=30,
        event_date=datetime.utcnow() + timedelta(days=14),
        category="SPORT",
        club_id=club2.id
    )

    db.add_all([event1, event2])
    db.commit()
    db.close()
    print("Örnek kulüp ve etkinlik verileri başarıyla yüklendi!")

if __name__ == "__main__":
    seed_database()
    python seed.py