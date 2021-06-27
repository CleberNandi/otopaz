import os
from pathlib import Path


class Desafio01:
    def __init__(self):
        self.file_input:str = os.path.join(BASE_DIR, "input.txt")
        self.file_output:str = os.path.join(BASE_DIR, "output.txt")
        self.input_list:list = self.load_input(self.file_input)
        self.ttask:int = self.get_ttask(self.input_list)
        self.umax:int = self.get_umax(self.input_list)
        self.user_list:list = self.input_list[2:]
        self.is_valid_ttask:bool = self.check_limit_ttask(self.ttask)
        self.is_valid_umax:bool = self.check_limit_umax(self.umax)
        self.servers = [0]
        
    
    def load_input(self, file_path:str)->list:
        result_input_list:list = []

        with open(self.file_input, encoding="utf-8") as file_input:
            lines = file_input.readlines()
            
            for line in lines:
                result_input_list.append(line.splitlines()[0])

        return result_input_list
    
    def save_output(self, file_output:str, output:list)->list:
        result_output:list = []

        try:
            with open(file_output, "w", encoding="utf-8") as file_out:
                for item in output:
                    file_out.write(item+"\n")
                    result_output.append(item)
        except Exception as error_output:
            print(f"Save loggin of Load balance -> Fail. Motive: {error_output}")
        
        return result_output
    
    def get_ttask(self, input_list:list)->int:
        ttask:int = None

        try:
            ttask = int(input_list[0])
        except IndexError:
            ttask = 0
        except TypeError:
            ttask = 0
        except Exception as error_ttask:
            print(f"Get ttask - Fail")
        
        return ttask
    
    def get_umax(self, input_list:list)->int:
        umax:int = None

        try:
            umax = int(input_list[1])
        except IndexError:
            umax = 0
        except TypeError:
            umax = 0
        except Exception as error_umax:
            print(f"Get umax - Fail")
        
        return umax
    
    def check_limit_ttask(self, ttask:int)->bool:
        is_limite_ttask:bool = False

        if 1 <= ttask <= 10:
            is_limite_ttask = True
        
        return is_limite_ttask

    def check_limit_umax(self, umax:int)->bool:
        is_limite_umax:bool = False

        if 1 <= umax <= 10:
            is_limite_umax = True
        
        return is_limite_umax
            
    def create_server(self):
        server_list = self.servers
        server_list.append(0)
        
        return server_list
    
    def load_balance(self)->list:
        for idx_user, user in enumerate(self.user_list):
            qt_user = int(user)

            for idx_server, server in enumerate(self.servers):
                qt_server_current = int(server)

                if qt_server_current == 0:
                    if qt_user <= self.umax:
                        self.servers[idx_server] += qt_user                        
                    else:
                        qt_user_exceeded = qt_user - self.umax
                        self.servers[idx_server] += self.umax
                        qt_user = qt_user_exceeded
                        self.create_server()
                elif qt_server_current < self.umax:
                    qt_server_free = self.umax - qt_server_current

                    if qt_server_free >= qt_user:
                        self.servers[idx_server] += qt_user
                    else:
                        qt_user_exceeded = qt_user - qt_server_free
                        self.servers[idx_server] += qt_server_free
                        qt_user = qt_user_exceeded
                        self.create_server()
                elif idx_server == len(self.servers) - 1:
                    self.create_server()
                
        print(f"Servidores existentes: {self.servers}")


BASE_DIR = Path(__file__).resolve().parent.parent

def main():
    desafio = Desafio01()

    if not desafio.is_valid_ttask:
        print(f"Limit of tasks exceeded. Closing load balance")
        exit()

    if not desafio.is_valid_umax:
        print(f"Limit of umax exceeded. Closing load balance")
        exit()
        
    desafio.load_balance()

if __name__ == "__main__":
    main()
    