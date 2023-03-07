import subprocess
import re
command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode(errors='ignore')
profile_names = (re.findall("Profil fr alle Benutzer : (.*)\r",command_output))
if len(profile_names) != 0:
    for x in range(len(profile_names)):
        print(profile_names[x])

wifi_list = []
if len(profile_names) != 0:
    for name in profile_names:
        wifi_profile = {}
        profile_info = subprocess.run(["netsh","wlan","show","profiles",name], capture_output=True).stdout.decode(errors = 'ignore')
        if re.search("Sicherheitsschlssel   : fehlt",profile_info):
            continue
        else:
            wifi_profile["ssid"] = name
            profile_info_pass = subprocess.run(["netsh","wlan","show","profiles",name, "key=clear"], capture_output=True).stdout.decode(errors = 'ignore')
            password = re.search("Schlsselinhalt            : (.*)\r", profile_info_pass)
            if password == None:
                wifi_profile["Password"] = None
            else:
                wifi_profile["Password"] = password[1]

            wifi_list.append(wifi_profile)
for x in range(len(wifi_list)):
    print(wifi_list[x])
