# -*- coding: utf-8 -*-
#auth_user
db[auth.settings.table_user_name].university.requires=IS_NOT_EMPTY()
#nitin.brain.requires=IS_NOT_EMPTY()

#Photos
db.photos.image_field.requires=IS_NOT_EMPTY()
db.photos.the_event.requires=IS_NOT_EMPTY()
