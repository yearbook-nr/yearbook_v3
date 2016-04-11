# -*- coding: utf-8 -*-

# auth_user
db[auth.settings.table_user_name].university.requires=IS_NOT_EMPTY()

# photos
db.photos.image.requires=IS_NOT_EMPTY()
db.photos.event.requires=IS_NOT_EMPTY()

# events
db.events.name.requires=IS_NOT_EMPTY()
db.events.about.requires=IS_NOT_EMPTY()

