from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy

book_tag = db.table(
    "book_tag", 
    db.Column('book_id', db.Integer, db.ForeignKey('book_id', primary_key=True)),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag_id', primary_key=True)),

)

class Book(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(200), nullable=False)
    author=db.Column(db.String(80), nullable=False)

    tags = db.relationship(
        'Tag',
        secondary=book_tag,
        back_populates='books',
        lazy='selectin',
    )

    def to_dict(self):
        return{
            'id': self.id,
            'title': self.title,
            'author': self.title,
            'tags': [tag.name for tag in self.tags],
        }

class Tag(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.column(db.String(50), unique=True, nullable=False)

    books = db.relationship(
        'Book',
        secondary=book_tag,
        back_populates='tags',
    )

    def to_dict(self):
        return{
            'id': self.id,
            'name': self.name,
            'book_count': len(self.books),
        }

    