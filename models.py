from database import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
# Define application Bases


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey('company.id'), nullable=False)
    company = relationship("Company")
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    username = Column(String(64), unique=True, nullable=False, index=True)
    password = Column(String(256), nullable=False)
    is_active = Column(Boolean, default=1)
    user_email = Column(String(120), unique=True, nullable=False)
    user_last_login = Column(DateTime)
    user_login_count = Column(Integer)
    user_fail_login_count = Column(Integer)
    user_created_on = Column(DateTime, default=datetime.now, nullable=True)
    user_changed_on = Column(DateTime, default=datetime.now, nullable=True)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return int(self.id)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        if self.last_name and self.first_name:
            return '{} {}'.format(
                self.first_name,
                self.last_name
            )


class Lead(Base):
    __tablename__ = 'leads'
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey('company.id'), nullable=False)
    company = relationship("Company")
    create_date = Column(DateTime, onupdate=datetime.now)
    modified_date = Column(DateTime, onupdate=datetime.now)
    email_addr = Column(String(255), nullable=False)
    is_verified = Column(Boolean, default=False)
    is_optout = Column(Boolean, default=False)
    is_processed = Column(Boolean, default=False)
    followup_email_sent_date = Column(DateTime)
    followup_email_receipt_id = Column(String(255), nullable=True, default='NOSTATUSID')
    followup_email_status = Column(String(20), nullable=True, default='EMAILNOTSENT')
    followup_email_delivered = Column(Boolean, default=False, nullable=True)
    followup_email_bounced = Column(Boolean, default=False, nullable=True)
    followup_email_opens = Column(Integer, default=0, nullable=True)
    followup_email_clicks = Column(Integer, default=0, nullable=True)
    followup_email_spam = Column(Boolean, default=False, nullable=True)
    followup_email_unsub = Column(Boolean, default=False, nullable=True)
    followup_email_dropped = Column(Boolean, default=False, nullable=True)
    followup_email_click_ip = Column(String(255))
    followup_email_click_device = Column(String(255))
    followup_email_open_campaign = Column(String(255), nullable=True)
    followup_email_open_ip = Column(String(255), nullable=True)
    followup_email_open_device = Column(String(255), nullable=True)
    webhook_last_updated = Column(DateTime, onupdate=datetime.now, nullable=True)
    dropped_reason = Column(String(50))
    dropped_code = Column(String(50))
    dropped_description = Column(String(255))
    bounce_error = Column(String(255))

    def __repr__(self):
        return '{}'.format(
            self.id
        )


class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    x_identifier = Column(String(255), unique=True, nullable=False)
    name = Column(String(255), unique=True, nullable=False)
    address1 = Column(String(255), nullable=False)
    address2 = Column(String(255))
    city = Column(String(255), nullable=False)
    state = Column(String(2), nullable=False)
    zip_code = Column(String(10), nullable=False)
    zip_4 = Column(String(10))
    status = Column(Boolean, default=True)
    contact_email_1 = Column(String(255), nullable=False)
    contact_email_2 = Column(String(255), nullable=False)
    alert_email = Column(String(255), nullable=False)
    reports_email = Column(String(255), nullable=False)
    phone_number = Column(String(20), nullable=False)

    def __repr__(self):
        return '{}'.format(
            self.name
        )

    def get_id(self):
        return int(self.id)
