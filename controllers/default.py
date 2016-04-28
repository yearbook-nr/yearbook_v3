def index():
    if auth.user is not None:
        redirect(URL('default', 'home'))
    return dict()


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


def new_university():
    """
    creates a university with a new ADMIN user
    """
    form=SQLFORM.factory(
        Field('uni_name'),
        Field('password', type='password', readable=False),
        Field('email', requires=IS_EMAIL()),
        Field('uni_address', type='text', requires=IS_NOT_EMPTY()),
        Field('uni_message', type='text'))

    if form.process().accepted:
        db[auth.settings.table_user_name].insert(first_name='ADMIN', last_name=form.vars.name, email=form.vars.email, password=form.vars.password)
        db['universities'].insert(name=form.vars.uni_name, email=form.vars.email, address=form.vars.uni_address, message_field=form.vars.uni_message)
        redirect(URL('default', 'index'))

    elif form.errors:
        response.flash='Your form has errors.'

    return dict(form=form)


@auth.requires_login()
def home():
    user_is_admin=auth.user.is_admin
    uni_record=db(db['universities'].name == auth.user.university).select().first()
    return locals()

@auth.requires_login()
def add_event():
    user_is_admin=db(db[auth.settings.table_user_name].id == auth.user.id).select(db[auth.settings.table_user_name].is_admin)[0]['is_admin']
    form=SQLFORM(db.events).process()
    if form.accepted:
        response.flash='You have successfully added a new event'
    return locals()


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
