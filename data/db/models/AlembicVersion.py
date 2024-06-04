from sqlalchemy.orm import Mapped, mapped_column

from data.db.models.BaseModel import Base


class AlembicVersion(Base):
    __tablename__ = "alembic_version"

    version_num: Mapped[str] = mapped_column(unique=True, primary_key=True)
