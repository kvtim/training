from app import db


class Country(db.Model):
    __tablename__ = 'country'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Country id: {self.id}, name: {self.name}>'


class Consulate(db.Model):
    __tablename__ = 'consulate'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(200))
    email = db.Column(db.String(70))
    working_hours = db.Column(db.String(100))
    phone_number_1 = db.Column(db.String(20))
    phone_number_2 = db.Column(db.String(20))

    country_id = db.Column(db.Integer, db.ForeignKey('country.id', ondelete='CASCADE'), nullable=False)
    country = db.relationship('Country', backref=db.backref('consulates', cascade="all,delete"))

    def __repr__(self):
        return f'<Consulate id: {self.id}, address: {self.address}, email: {self.email},' \
               f' working hours: {self.working_hours}, phone number 1: {self.phone_number_1},' \
               f' phone number 2: {self.phone_number_2}, country: {self.country.name}' \
               f' country id: {self.country.id}>'

    def __eq__(self, other):
        if isinstance(other, dict):
            return (self.address == other['address'] and self.email == other['email'] and
                    self.working_hours == other['working_hours'] and
                    self.phone_number_1 == other['phone_number_1'] and
                    self.phone_number_2 == other['phone_number_2'])
        return NotImplemented


class VisaApplicationCenter(db.Model):
    __tablename__ = 'visa_application_center'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(200))
    email = db.Column(db.String(70))
    apply_working_hours_1 = db.Column(db.String(100))
    issue_working_hours_2 = db.Column(db.String(100))
    phone_number = db.Column(db.String(20))

    country_id = db.Column(db.Integer, db.ForeignKey('country.id', ondelete='CASCADE'), nullable=False)
    country = db.relationship('Country', backref=db.backref('vacs', cascade="all,delete"))

    def __repr__(self):
        return f'<Visa center id: {self.id} address: {self.address}, email: {self.email},' \
               f' working hours 1: {self.apply_working_hours_1}, working hours 2: {self.apply_working_hours_2},' \
               f' phone number: {self.phone_number}, country: {self.country.name}' \
               f' country id: {self.country.id}>'

    def __eq__(self, other):
        if isinstance(other, dict):
            return (self.address == other['address'] and self.email == other['email'] and
                    self.apply_working_hours_1 == other['apply_working_hours_1'] and
                    self.issue_working_hours_2 == other['issue_working_hours_2'] and
                    self.phone_number == other['phone_number'])
        return NotImplemented


class NewsDetails(db.Model):
    __tablename__ = 'news_details'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70))
    body = db.Column(db.String(350))
    link = db.Column(db.String(100))

    def __repr__(self):
        return f'<News details id: {self.id} title: {self.title}, body: {self.body},' \
               f' link: {self.link}>'

    def __eq__(self, other):
        if isinstance(other, dict):
            return (self.title == other['title'] and self.body == other['body'] and
                    self.link == other['link'])
        return NotImplemented


class News(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)

    country_id = db.Column(db.Integer, db.ForeignKey('country.id', ondelete='CASCADE'), nullable=False)
    country = db.relationship('Country', backref=db.backref('news', cascade="all,delete"))

    news_details_id = db.Column(db.Integer, db.ForeignKey('news_details.id', ondelete='CASCADE'), nullable=False)
    news_details = db.relationship('NewsDetails', backref=db.backref('news', cascade="all,delete"))

    def __repr__(self):
        return f'<News id: {self.id} date: {self.date}, country id: {self.country_id},' \
               f' news_details_id: {self.news_details_id}>'

    def __eq__(self, other):
        if isinstance(other, dict):
            return self.date == other['date'] and self.news_details == other['news_details']
        return NotImplemented
