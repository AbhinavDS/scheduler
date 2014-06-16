# coding: utf8
# try something like
def index():
	record = auth.user.first_name+" "+auth.user.last_name
	#form = SQLFORM(db.auth_user)
	#record = db.executesql('SELECT * FROM usertables')
	return dict(message=record )
