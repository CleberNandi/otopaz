def create_server(servers, server_number):
    server_list = servers
    if len(server_list) == 0:
        server_list["S"+str(server_number)] = []
        server_list["S"+str(server_number)].append([0,0])
    
    return server_list

servers = {}
users_input = [1,3,0,1,0,1]
qt_users_total = sum(users_input)
umax = 2
qt_servers_created = 0
server_number = 1
tik = 0
create_server(servers, server_number)
print(servers)

for idx_user, user in enumerate(users_input):
    qt_user = int(user)
    idx_server = 0
    tik += 1
    for idx_server, server in enumerate(servers):        
        server_number += idx_server
        qt_server_current = servers["S"+str(server_number)][idx_user][0]
        tik_server_current = servers["S"+str(server_number)][idx_user][1]
        print(f"servers[idx_server][idx_user+1]: {servers['S'+str(server_number)][idx_user]}")
        if qt_server_current == 0:
            if qt_user <= umax:
                servers["S"+str(server_number)][idx_user][0] += qt_user
                servers["S"+str(server_number)][idx_user][1] += tik
                idx_server = 0
                
            else:
                qt_user_exceeded = qt_user - umax
                servers["S"+str(server_number)][idx_user][0] += umax
                servers["S"+str(server_number)][idx_user][1] += tik
                qt_user = qt_user_exceeded
                create_server(servers, server_number)
                print(f"Criado novo servidor")
        elif qt_server_current < umax:

            qt_server_free = umax - qt_server_current

            if qt_server_free >= qt_user:
                # create_server(servers, server_number, qt_user, tik)
                servers["S"+str(server_number)][idx_user][0] += qt_user
                servers["S"+str(server_number)][idx_user][1] += tik
            else:
                qt_user_exceeded = qt_user - qt_server_free
                servers["S"+str(server_number)][idx_user][0] += qt_server_free
                servers["S"+str(server_number)][idx_user][1] += tik
                qt_user = qt_user_exceeded
                # create_server(servers, server_number, qt_server_free, tik)
                create_server(servers, server_number)
                print(f"Criado novo servidor")
        elif idx_server == len(servers) - 1:
            create_server(servers, server_number, 0, 0)
            # create_server(servers, server_number)
            print(f"Criado novo servidor")
        

print(f"Servidores existentes: {servers}")