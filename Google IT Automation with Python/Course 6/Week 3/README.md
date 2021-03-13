## Automatic Output Generation
### Course 6, Week 3

This script script is, once again, my own implementation of the solution
and is **overkill** for the purpose of finishing the assignment. However,
this script **has no dependencies** except that you have to provide your
own values for the `email_details` dictionary which contains the
parameters required for sending the email.

	# at line 25
	email_details = {
		'server'	: '<address of SMTP server>',
		'username'	: '<user account to use to send the mail>',
		'password'	: '<password to use to log in to the account>',
		'to'		: '<email address of the recipient>',
		'subject'	: '<subject line goes here>',
		'content'	: '<message body goes here>'
	}
