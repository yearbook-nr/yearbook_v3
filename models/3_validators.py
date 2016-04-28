# auth_user
auth.settings.table_user.university.requires=IS_IN_DB(db, 'universities.name')
#auth.settings.table_user.password.requires.insert(0, IS_STRONG(min=6, special=1))

# photos
db.photos.image.requires=IS_NOT_EMPTY()
db.photos.event_field.requires=IS_IN_DB(db, 'events.name')

# events
db.events.name.requires=IS_NOT_IN_DB(db, 'events.name')

# universities
db.universities.name.requires=IS_NOT_IN_DB(db, 'universities.name')
db.universities.email.requires=IS_EMAIL()
db.universities.address.requires=IS_NOT_EMPTY()
