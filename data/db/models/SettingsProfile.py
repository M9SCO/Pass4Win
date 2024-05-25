from sqlalchemy.orm import Mapped, mapped_column

from data.db.models.BaseModel import BaseModel


class SettingsProfile(BaseModel):
    __tablename__ = "settings_profiles"

    name: Mapped[str] = mapped_column(unique=True)
    active: Mapped[bool] = mapped_column()
    wait_seconds: Mapped[int] = mapped_column()

    path_to_gpg: Mapped[str] = mapped_column()
    path_to_external_gpg: Mapped[str] = mapped_column()
    path_to_stored_passwords: Mapped[str] = mapped_column()
