from pathlib import Path
import json

class Account:
    def __init__(self,path):
        self.path=Path(path)
        self.users=self.load_users()

    def load_users(self):
        if not self.path.exists() or self.path.stat().st_size==0:
            return{}
        return json.loads(self.path.read_text(encoding='utf-8'))
    
    def exists(self,name):
        return name in self.users
    
    def check_password(self,name,password):
        user=self.users.get(name)
        if user and user["password"]==password:
            return user
        return None

    def add_account(self,name,password):
        self.users[name]={'username':name,'password':password}
        try:
            self.path.write_text(json.dumps(self.users,indent=4),encoding='utf-8')
            return True
        except Exception:
            return False