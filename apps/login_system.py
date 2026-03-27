from core_logic import account_manager as am
from utils import user_input as ui
path=am.Account('user_data.json')

def get_password():
    pwd=ui.clean_text('Password (or [b] to go back to user name):',lower=False)
    if pwd=='b':
        return None
    return pwd
def get_username():
    unm=ui.clean_text('User Name (or [b] to go back to main menu):')
    if unm=='b':
        return None
    return unm

def log_in():
    while True:
        unm=get_username()
        if not unm:
            return None
        if not path.exists(unm):
            choice=ui.get_text_choice(f"""
> Error: Can't find '{unm}' account <
>[b] go back to main menu
>[r] to re-enter name
\n(Your choice):""",'b','r')
            if choice == 'b':
                return None
            continue
        choice=ui.get_text_choice(f"""
Are you trying to log in '{unm}' account?
>[yes]
>[no]
\n(Your choice):""",'yes','no')
        if choice == 'yes':
            while True:
                pwd=get_password()
                if not pwd:
                    break
                account=path.check_password(unm,pwd)
                if not account:
                    choice=ui.get_text_choice(f"""
> Error: Incorrect password <
>[b] go to back to user name
>[r] to re-enter password
\n(Your choice):""",'b','r')
                    if choice == 'b':
                        break
                else:
                    return account

def register():
    while True:
        unm=get_username()
        if unm == 'b':
            return None
        if path.exists(unm):
            choice=ui.get_text_choice(f"""
> Error: Duplicate username, (try log in or change the name) <
[b] to go back to main menu
[r] to change user name
\n(Your choice):""",'b','r')
            if choice == 'b':
                return None
            else:
                continue
        while True:
            pwd=get_password()
            if not pwd:
                break
            choice=ui.get_text_choice(f"""
User name:{unm}
Password:{pwd}
[yes] to register account
[rp] to change password
[rc] to recreate
\n(Your choice)""",'yes','rp','rc')
            if choice == 'rc':
                break
            elif choice == 'rp':
                continue
            if path.add_account(unm,pwd):
                return path.users[unm]
            else:
                print("> Error: Creation failed  <")
                return None


def main_menu():
    while True:
        choice=ui.get_text_choice("""
Welcome!!
[log in]
[register]
\n(Your choice):""",'log in','register')
        if choice=='log in':
            account=log_in()
            if account:
                print(f"Welcome! {account['username']}")
                return account
            else:
                choice=''
        if choice=='register':
            account=register()
            if account:
                print(f"Welcome! {account['username']}")
                return account