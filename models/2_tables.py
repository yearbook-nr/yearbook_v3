# auth
def get_current_time():
	q = request.now
	return str(q.hour) + ':' + str(q.minute) + ', ' + str(q.day) + '-' + str(q.month) + '-' + str(q.year)


auth.settings.extra_fields['auth_user'] = [
	Field('university', length=128),
	Field('batch'),
	Field('dp', type='upload'),
	Field('about', type='text')
    ]

auth.define_tables()
db.define_table('photos',
    Field('image_field',type='upload'),
    Field('caption'),
    Field('university',default=auth.user.university if auth.user is not None else None, readable=False, writable=False),
    Field('date_upload', default=get_current_time(), readable=False, writable=False),
    Field('the_event'),
    Field('about_event',type='text')
    )
