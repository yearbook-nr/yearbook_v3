1. Home
2. Auth
3. User home
4. Event list
5. Event album
6. *tagging people
7. *like
8. *comment
9. *student profiles
10. *contact list
6. *basic pic editing (crop, resize, etc.)
_______________________________

Models:
1. auth + university + *year + *pic + *about + username_enabled + is_admin
2. event photo table (photo to caption, event, university, date)
3. *like table
4. *comment table
5. admin user per university

Controllers & Views:
1. layout.html
2. (unlogged-in)home.html and home
3. user()
4. *user_profile.html & *user_profile()
5. event_list.html & event_list() - default user home
6. add_event.html & add_event() 
7. event.html & event() - from event_list.html
7. add_photo.html & add_photo() - from event.html
6. photo.html & photo() - *with flip-page animation
7. (unlogged-in)university_yearbook.html & university_yearbook()

*Feature to allow registration only by university admin approval
*Range of dates
