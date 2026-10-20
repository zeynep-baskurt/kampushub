import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Veritabanı dosya yolu (Varsayılan olarak proje klasöründe campushub.db oluşturur)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./campushub.db")

# 2. SQLite için özel bağlantı ayarı (PostgreSQL geçilirse otomatik uyum sağlar)
connect_args = {"check_same_thread": False} if "sqlite" in DATABASE_URL else {}

# 3. SQLAlchemy Motoru (Engine)
engine = create_engine(DATABASE_URL, connect_args=connect_args)

# 4. Oturum (Session) Oluşturucu
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 5. Tablo Modellerinin Türeyeceği Ana Sınıf (Base)
Base = declarative_base()

# 6. FastAPI Endpoint'lerinde veritabanı bağlantısını güvenle açıp kapatan yardımcı fonksiyon
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()