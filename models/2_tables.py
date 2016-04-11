def get_current_time():
	q = request.now
	return str(q.hour) + ':' + str(q.minute) + ', ' + str(q.day) + '-' + str(q.month) + '-' + str(q.year)

# auth
auth.settings.extra_fields['auth_user'] = [
	Field('university'),
	Field('batch'),
	Field('dp', type='upload'),
	Field('about', type='text'),
	Field('is_admin', type='boolean')]
auth.define_tables()

# photos
db.define_table('photos',
		Field('image', type='upload'),
		Field('caption'),
		Field('university', default=auth.user.university if auth.user is not None else None, readable=False, writable=False),
		Field('date_of_upload', default=get_current_time(), readable=False, writable=False),
		Field('event'),
		Field('about',type='text'))

# events
db.define_table('events',
		Field('name'),
		Field('date', type='date'),
		Field('about', type='text'),
		Field('cover_pic', type='upload'))
