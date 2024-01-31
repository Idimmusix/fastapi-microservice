import datetime as datetime
# import passlib.hash as _hash
from sqlalchemy.schema import Column
from sqlalchemy.types import String, DateTime, Boolean, Text
from uuid import uuid4
from db.database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    id = Column(String(255), primary_key=True, index=True, default=uuid4().hex)
    email = Column(String(255), index=True, nullable=False)
    first_name = Column(String(255))
    last_name = Column(String(255))
    phone_number = Column(String(50))
    phone_country_code = Column(String(7))
    password_hash = Column(Text(255), nullable=True, index=True)
    image_url = Column(Text)
    device_id = Column(Text)
    google_id = Column(String(255), index=True)
    google_image_url = Column(Text())
    is_deleted = Column(Boolean, index = True, default=False)
    is_active = Column(Boolean, default=True, index=True)
    is_verified = Column(Boolean, default=False, index=True)
    is_superuser = Column(Boolean, default=False, index=True)
    date_created = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    date_created_db = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    last_updated = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    last_updated_db = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)

    # def verify_password(self, password: str):
    #     return _hash.sha256_crypt.verify(password, self.password_hash)
    


