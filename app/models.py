# app/models.py

from app import db

class GuestUser(db.Model):
  """
  Create a GuestUser table
  """
  # Ensures table will be named in plural and not in singular
  # as is the name of the model
  __tablename__ = 'guest_users'

  id = db.Column(db.Integer, primary_key=True)
  guest_name = db.Column(db.String(60), index=True, unique=True)
  guest_state = db.Column(db.String(60), index=True)
  is_admin = db.Column(db.Boolean, default=False)

  def __repr__(self):
    return '<GuestUser: {}>'.format(self.guest_name)
  


