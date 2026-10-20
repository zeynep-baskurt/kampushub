from database import engine, Base
import models  # Modellerin import edilmesi şarttır

print("Veritabanı tabloları oluşturuluyor...")
Base.metadata.create_all(bind=engine)
print("Tablolar başarıyla oluşturuldu!")