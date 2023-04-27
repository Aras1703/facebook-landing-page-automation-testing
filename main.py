from facebook.facebook import Facebook

try:
    with Facebook() as bot:
        bot.land_first_page()
        bot.put_email()
        bot.put_password()
        bot.view_password()
        bot.press_login()
        bot.forgot_password()
        bot.create_account()
        bot.create_pages()

except Exception as e:
    if "in PATH" in str(e):
        print(
            'You are trying to run the bot from the command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows : \n'
            '   set PATH=%PATH%;C:path-to-your-folder \n'
        )
    else:
        raise