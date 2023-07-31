from pystyle import *
from datetime import datetime
import os
import requests
import time

class c():
    reset = '\u001b[0m'
    black = '\u001b[30m'
    green = '\u001b[32m'
    yellow = '\u001b[33m'
    blue = '\u001b[34m'
    magenta = '\u001b[35m'
    cyan = '\u001b[36m'
    white = '\u001b[37m'
    red = '\u001b[31m'
    bright_black = '\u001b[30;1m'
    bright_red = '\u001b[31;1m'
    bright_green = '\u001b[32;1m'
    bright_yellow = '\u001b[33;1m'
    bright_blue = '\u001b[34;1m'
    bright_magenta = '\u001b[35;1m'
    bright_cyan = '\u001b[36;1m'
    bright_white = '\u001b[37;1m'
    back_black = '\u001b[40m'
    back_red = '\u001b[41m'
    back_green = '\u001b[42m'
    back_yellow = '\u001b[43m'
    back_blue = '\u001b[44m'
    back_magenta = '\u001b[45m'
    back_cyan = '\u001b[46m'
    back_white = '\u001b[47m'
    back_purple = '\e[0;105m'
    bold = '\u001b[1m'
    underline = '\u001b[4m'
    reversed = '\u001b[7m'

def banner():
  print(Colorate.Vertical(Colors.white_to_red, """ 
                          
  ██████  ██▓    ▄▄▄     ▓██   ██▓▓█████  ██▀███  
▒██    ▒ ▓██▒   ▒████▄    ▒██  ██▒▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▒██░   ▒██  ▀█▄   ▒██ ██░▒███   ▓██ ░▄█ ▒
  ▒   ██▒▒██░   ░██▄▄▄▄██  ░ ▐██▓░▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒░██████▒▓█   ▓██▒ ░ ██▒▓░░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░ ▒░▓  ░▒▒   ▓▒█░  ██▒▒▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░░ ░ ▒  ░ ▒   ▒▒ ░▓██ ░▒░  ░ ░  ░  ░▒ ░ ▒░
░  ░  ░    ░ ░    ░   ▒   ▒ ▒ ░░     ░     ░░   ░ 
      ░      ░  ░     ░  ░░ ░        ░  ░   ░     
                          ░ ░                     
  """, 1))

def credits():
    print(f"""
{c.red}    [>] Slayer Token Sniffer
    [>] Version: 1.0.0
    [>] Version Date: 30/06/2023
    [>] Made By Blitz/Lightning{c.reset}
""")

clear = lambda: os.system("cls" if os.name == "nt" else "clear")

def main():
    clear()
    banner()
    credits()
    opt = input(f"""
{c.red}What Do You Want To Do?{c.reset}
[{c.red}1{c.reset}] Sniff a Token
[{c.red}2{c.reset}] Sniff an ID
""")
    if opt == "1":
        options()
    elif opt == "2":
        id_info()
    else:
        log.error(f"Invalid Option --> {opt}")
        time.sleep(3)
        main()

class log():

    def warning(message):
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        print(f"[{c.bright_yellow}{time}{c.reset}] {c.yellow}Warning{c.reset} --> {c.yellow}{message}{c.reset}")
        
    def error(message):
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        print(f"[{c.red}{time}{c.reset}] {c.red}Error{c.reset} --> {c.red}{message}{c.reset}")
        
    def success(message):
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        print(f"[{c.green}{time}{c.reset}] {c.green}Success{c.reset} --> {c.green}{message}{c.reset}")

def token_user_info():
    token = input(f"{c.red}Input Token{c.reset} -->\n")
    headers = {"authorization": token}
    halftoken = token[:len(token)//2]
    def post():
        r = requests.get("https://discord.com/api/v9/users/@me", headers = headers)
        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
            print(f"{c.red}Valid Token: {c.reset}{halftoken} **********")
            js = r.json()
            id = js["id"]
            username = js["username"]
            avatar = js["avatar"]
            discriminator = js["discriminator"]
            public_flags = js["public_flags"]
            flags = js["flags"]
            banner = js["banner"]
            accent_color = js["accent_color"]
            global_name = js["global_name"]
            avatar_decoration = js["avatar_decoration"]
            banner_color = js["banner_color"]
            mfa_enabled = js["mfa_enabled"]
            locale = js["locale"]
            premium_type = js["premium_type"]
            email = js["email"]
            verified = js["verified"]
            phone = js["phone"]
            nsfw_allowed = js["nsfw_allowed"]
            premium_usage_flags = js["premium_usage_flags"]
            linked_users = js["linked_users"]
            purchased_flags = js["purchased_flags"]
            bio = js["bio"]
            print(f"""
{c.red}[User Information]{c.reset}
ID: {id}
Name: {username}#{discriminator}
Global Name: {global_name}
MFA: {mfa_enabled}
Locale: {locale}
Email: {email}
Verified: {verified}
Premium_Type: {premium_type}
Phone: {phone}
Avatar: https://cdn.discordapp.com/avatars/{id}/{avatar}
Banner: https://cdn.discordapp.com/banners/{id}/{banner}
Accent: {accent_color}
Avatar_Decoration: {avatar_decoration}
Banner_Color: {banner_color}
Flags: {flags}
Public_Flags: {public_flags}
Purchased_Flags: {purchased_flags}
Premium_Flags: {premium_usage_flags}
NSFW: {nsfw_allowed}
Linked_Users: {linked_users}
Bio: {bio}
""")

        elif r.status_code == 429:
            log().warning(f"Ratelimited | Try Again Later")
            time.sleep(3)
            main()
        else:
            rs = requests.get("https://discord.com/api/v9/users/@me", headers = {"authorization": f"Bot {token}"})
            if rs.status_code == 200 or rs.status_code == 201 or rs.status_code == 204:
                print(f"{c.red}Valid Bot Token: {c.reset}{halftoken} **********")
                js = rs.json()
                id = js["id"]
                username = js["username"]
                avatar = js["avatar"]
                discriminator = js["discriminator"]
                public_flags = js["public_flags"]
                flags = js["flags"]
                bot = js["bot"]
                banner = js["banner"]
                accent_color = js["accent_color"]
                global_name = js["global_name"]
                avatar_decoration = js["avatar_decoration"]
                banner_color = js["banner_color"]
                mfa_enabled = js["mfa_enabled"]
                locale = js["locale"]
                premium_type = js["premium_type"]
                email = js["email"]
                verified = js["verified"]
                bio = js["bio"]
                print(f"""
{c.red}[Bot Information]{c.reset}
ID: {id}
Name: {username}#{discriminator}
Global Name: {global_name}
MFA: {mfa_enabled}
Locale: {locale}
Email: {email}
Verified: {verified}
Premium_Type: {premium_type}
Bot: {bot}
Avatar: https://cdn.discordapp.com/avatars/{id}/{avatar}
Banner: https://cdn.discordapp.com/banners/{id}/{banner}
Accent: {accent_color}
Avatar_Decoration: {avatar_decoration}
Banner_Color: {banner_color}
Flags: {flags}
Public_Flags: {public_flags}
Invite: https://discord.com/api/oauth2/authorize?client_id={id}&permissions=8&scope=bot
Bio: {bio}
""")
            elif r.status_code == 429:
                log().warning(f"Ratelimited | Try Again Later")
                time.sleep(3)
                main()
            else:
                print(f"{c.red}Invalid Token: {c.reset}{halftoken} **********")
    post()

def settings_info():
    token = input(f"{c.red}Input Token{c.reset} -->\n")
    headers = {"authorization": token}
    halftoken = token[:len(token)//2]
    def post():
        r = requests.get("https://discordapp.com/api/v9/users/@me/settings", headers = headers)
        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
            print(f"{c.red}Valid Token: {c.reset}{halftoken} **********")
            js = r.json()
            show_current_game = js["show_current_game"]
            resticted_guilds = js["restricted_guilds"]
            default_guilds_restricted = js["default_guilds_restricted"]
            inline_attachment_media = js["inline_attachment_media"]
            inline_embed_media = js["inline_embed_media"]
            gif_auto_play = js["gif_auto_play"]
            render_embeds = js["render_embeds"]
            render_reactions = js["render_reactions"]
            animate_emoji = js["animate_emoji"]
            enable_tts_command = js["enable_tts_command"]
            message_display_compact = js["message_display_compact"]
            convert_emoticons = js["convert_emoticons"]
            explicit_content_filter = js["explicit_content_filter"]
            disable_games_tab = js["disable_games_tab"]
            theme = js["theme"]
            developer_mode = js["developer_mode"]
            detect_platform_accounts = js["detect_platform_accounts"]
            status = js["status"]
            afk_timeout = js["afk_timeout"]
            timezone_offset = js["timezone_offset"]
            stream_notifications_enabled = js["stream_notifications_enabled"]
            allow_accessibility_detection = js["allow_accessibility_detection"]
            contact_sync_enabled = js["contact_sync_enabled"]
            native_phone_integration_enabled = js["native_phone_integration_enabled"]
            animate_stickers = js["animate_stickers"]
            friend_discovery_flags = js["friend_discovery_flags"]
            view_nsfw_guilds = js["view_nsfw_guilds"]
            view_nsfw_commands = js["view_nsfw_commands"]
            passwordless = js["passwordless"]
            friend_source_flags = js["friend_source_flags"]
            print(f"""
{c.red}[User Settings Information]{c.reset}
show_current_game: {show_current_game}
default_guilds_restricted: {default_guilds_restricted}
inline_attachment_media: {inline_attachment_media}
inline_embed_media: {inline_embed_media}
gif_auto_play: {gif_auto_play}
render_embeds: {render_embeds}
render_reactions: {render_reactions}
animate_emoji: {animate_emoji}
enable_tts_command: {enable_tts_command}
message_display_compact: {message_display_compact}
convert_emoticons: {convert_emoticons}
explicit_content_filter: {explicit_content_filter}
disable_games_tab: {disable_games_tab}
theme: {theme}
developer_mode: {developer_mode}
detect_platform_accounts: {detect_platform_accounts}
status: {status}
afk_timeout: {afk_timeout}
timezone_offset: {timezone_offset}
stream_notifications_enabled: {stream_notifications_enabled}
allow_accessibility_detection: {allow_accessibility_detection}
contact_sync_enabled: {contact_sync_enabled}
native_phone_integration_enabled: {native_phone_integration_enabled}
animate_stickers: {animate_stickers}
friend_discovery_flags: {friend_discovery_flags}
view_nsfw_guilds: {view_nsfw_guilds}
view_nsfw_commands: {view_nsfw_commands}
passwordless: {passwordless}
friend_source_flags: {friend_source_flags}
""")


        elif r.status_code == 429:
            log().warning(f"Ratelimited | Try Again Later")
            time.sleep(3)
            main()
        else:
            rs = requests.get("https://discord.com/api/v9/users/@me", headers = {"authorization": f"Bot {token}"})
            if rs.status_code == 200 or rs.status_code == 201 or rs.status_code == 204:
                print(f"{c.red}Valid Bot Token: {c.reset}{halftoken} **********")
                js = rs.json()
                id = js["id"]
                username = js["username"]
                avatar = js["avatar"]
                discriminator = js["discriminator"]
                public_flags = js["public_flags"]
                flags = js["flags"]
                bot = js["bot"]
                banner = js["banner"]
                accent_color = js["accent_color"]
                global_name = js["global_name"]
                avatar_decoration = js["avatar_decoration"]
                banner_color = js["banner_color"]
                mfa_enabled = js["mfa_enabled"]
                locale = js["locale"]
                premium_type = js["premium_type"]
                email = js["email"]
                verified = js["verified"]
                bio = js["bio"]
                print(f"""
{c.red}[Bot Information]{c.reset}
ID: {id}
Name: {username}#{discriminator}
Global Name: {global_name}
MFA: {mfa_enabled}
Locale: {locale}
Email: {email}
Verified: {verified}
Premium_Type: {premium_type}
Bot: {bot}
Avatar: https://cdn.discordapp.com/avatars/{id}/{avatar}
Banner: https://cdn.discordapp.com/banners/{id}/{banner}
Accent: {accent_color}
Avatar_Decoration: {avatar_decoration}
Banner_Color: {banner_color}
Flags: {flags}
Public_Flags: {public_flags}
Invite: https://discord.com/api/oauth2/authorize?client_id={id}&permissions=8&scope=bot
Bio: {bio}
""")
            elif r.status_code == 429:
                log().warning(f"Ratelimited | Try Again Later")
                time.sleep(3)
                main()
            else:
                print(f"{c.red}Invalid Token: {c.reset}{halftoken} **********")
    post()

def id_info():
    id = input(f"{c.red}Input ID{c.reset} -->\n")
    def post():
        r = requests.post("https://lookupguru.herokuapp.com/lookup", json = {"input": id})
        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
            print(f"{c.red}Valid ID: {c.reset}{id}")
            js = r.json()["data"]
            av = js["avatar"]
            av_id = av["id"]
            b = js["banner"]
            b_id = b["id"]
            created_at = js["created_at"]
            is_bot = js["is_bot"]
            username = js["username"]
            discriminator = js["discriminator"]
            print(f"""
{c.red}[ID Information]{c.reset}
ID: {id}
Name: {username}#{discriminator}
Avatar: https://cdn.discordapp.com/avatars/{id}/{av_id}
Banner: https://cdn.discordapp.com/banners/{id}/{b_id}
Created_At: {created_at}
Bot: {is_bot}
""")
        else:
            log.error("Invalid ID")
    post()

def friend_info():
    token = input(f"{c.red}Input Token{c.reset} -->\n")
    headers = {"authorization": token}
    halftoken = token[:len(token)//2]
    def post():
        r = requests.get("https://discordapp.com/api/v9/users/@me/relationships", headers = headers)
        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
            print(f"{c.red}Valid Token: {c.reset}{halftoken} **********")
            js = r.json()
            friends = []
            for f in js:
                friends.append(f"{f['user']['username']}#{f['user']['discriminator']} | {f['id']}")
            print(f"{c.red}\n[Friends Information]{c.reset}")
            print(f"{c.red}Total Friends: {c.reset}{len(js)}\n")
            for a in friends:
                print(a)
        elif r.status_code == 429:
            log().warning(f"Ratelimited | Try Again Later")
            time.sleep(3)
            main()

def guild_info():
    token = input(f"{c.red}Input Token{c.reset} -->\n")
    headers = {"authorization": token}
    halftoken = token[:len(token)//2]
    def post():
        r = requests.get("https://discordapp.com/api/v9/users/@me/guilds", headers = headers)
        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
            print(f"{c.red}Valid Token: {c.reset}{halftoken} **********")
            js = r.json()
            admin = []
            unowned = []
            for a in js:
                if int(a["permissions"]) & 0x8:
                    admin.append(f"Name: {a['name']} | ID: {a['id']} | Owned: {a['owner']} | Permissions: {a['permissions']}")
                else:
                    unowned.append(f"Name: {a['name']} | ID: {a['id']} | Owned: {a['owner']} | Permissions: {a['permissions']}")
            print(f"{c.red}\n[Guild Information]{c.reset}\n")
            print(f"{c.red}Total Guilds: {c.reset}{len(js)}\n")
            print(f"{c.red}[Admin Guilds]{c.reset}\n")
            for a in admin:
                print(a)
            print(f"\n{c.red}[Normal Guilds]{c.reset}\n")
            for a in unowned:
                print(a)
        elif r.status_code == 429:
            log().warning(f"Ratelimited | Try Again Later")
            time.sleep(3)
            main()
        else:
            rs = requests.get("https://discord.com/api/v9/users/@me", headers = {"authorization": f"Bot {token}"})
            if rs.status_code == 200 or rs.status_code == 201 or rs.status_code == 204:
                print(f"{c.red}Valid Bot Token: {c.reset}{halftoken} **********")
                js = rs.json()
                id = js["id"]
                username = js["username"]
                avatar = js["avatar"]
                discriminator = js["discriminator"]
                public_flags = js["public_flags"]
                flags = js["flags"]
                bot = js["bot"]
                banner = js["banner"]
                accent_color = js["accent_color"]
                global_name = js["global_name"]
                avatar_decoration = js["avatar_decoration"]
                banner_color = js["banner_color"]
                mfa_enabled = js["mfa_enabled"]
                locale = js["locale"]
                premium_type = js["premium_type"]
                email = js["email"]
                verified = js["verified"]
                bio = js["bio"]
                print(f"""
{c.red}[Bot Information]{c.reset}
ID: {id}
Name: {username}#{discriminator}
Global Name: {global_name}
MFA: {mfa_enabled}
Locale: {locale}
Email: {email}
Verified: {verified}
Premium_Type: {premium_type}
Bot: {bot}
Avatar: https://cdn.discordapp.com/avatars/{id}/{avatar}
Banner: https://cdn.discordapp.com/banners/{id}/{banner}
Accent: {accent_color}
Avatar_Decoration: {avatar_decoration}
Banner_Color: {banner_color}
Flags: {flags}
Public_Flags: {public_flags}
Invite: https://discord.com/api/oauth2/authorize?client_id={id}&permissions=8&scope=bot
Bio: {bio}
""")
            elif r.status_code == 429:
                log().warning(f"Ratelimited | Try Again Later")
                time.sleep(3)
                main()
            else:
                print(f"{c.red}Invalid Token: {c.reset}{halftoken} **********")
    post()

def everything():
    token = input(f"{c.red}Input Token{c.reset} -->\n")
    headers = {"authorization": token}
    halftoken = token[:len(token)//2]
    
    
    r1 = requests.get("https://discord.com/api/v9/users/@me", headers = headers)
    print(f"{c.red}Valid Token: {c.reset}{halftoken} **********")
    if r1.status_code == 200 or r1.status_code == 201 or r1.status_code == 204:
        js1 = r1.json()
        id = js1["id"]
        username = js1["username"]
        avatar = js1["avatar"]
        discriminator = js1["discriminator"]
        public_flags = js1["public_flags"]
        flags = js1["flags"]
        banner = js1["banner"]
        accent_color = js1["accent_color"]
        global_name = js1["global_name"]
        avatar_decoration = js1["avatar_decoration"]
        banner_color = js1["banner_color"]
        mfa_enabled = js1["mfa_enabled"]
        locale = js1["locale"]
        premium_type = js1["premium_type"]
        email = js1["email"]
        verified = js1["verified"]
        phone = js1["phone"]
        nsfw_allowed = js1["nsfw_allowed"]
        premium_usage_flags = js1["premium_usage_flags"]
        linked_users = js1["linked_users"]
        purchased_flags = js1["purchased_flags"]
        bio = js1["bio"]
    elif r1.status_code == 429:
            log().warning(f"Ratelimited | Try Again Later")
            time.sleep(3)
            main()
    

    r2 = requests.get("https://discordapp.com/api/v9/users/@me/settings", headers = headers)
    if r2.status_code == 200 or r2.status_code == 201 or r2.status_code == 204:
            print(f"{c.red}Valid Token: {c.reset}{halftoken} **********")
            js = r2.json()
            show_current_game = js["show_current_game"]
            resticted_guilds = js["restricted_guilds"]
            default_guilds_restricted = js["default_guilds_restricted"]
            inline_attachment_media = js["inline_attachment_media"]
            inline_embed_media = js["inline_embed_media"]
            gif_auto_play = js["gif_auto_play"]
            render_embeds = js["render_embeds"]
            render_reactions = js["render_reactions"]
            animate_emoji = js["animate_emoji"]
            enable_tts_command = js["enable_tts_command"]
            message_display_compact = js["message_display_compact"]
            convert_emoticons = js["convert_emoticons"]
            explicit_content_filter = js["explicit_content_filter"]
            disable_games_tab = js["disable_games_tab"]
            theme = js["theme"]
            developer_mode = js["developer_mode"]
            detect_platform_accounts = js["detect_platform_accounts"]
            status = js["status"]
            afk_timeout = js["afk_timeout"]
            timezone_offset = js["timezone_offset"]
            stream_notifications_enabled = js["stream_notifications_enabled"]
            allow_accessibility_detection = js["allow_accessibility_detection"]
            contact_sync_enabled = js["contact_sync_enabled"]
            native_phone_integration_enabled = js["native_phone_integration_enabled"]
            animate_stickers = js["animate_stickers"]
            friend_discovery_flags = js["friend_discovery_flags"]
            view_nsfw_guilds = js["view_nsfw_guilds"]
            view_nsfw_commands = js["view_nsfw_commands"]
            passwordless = js["passwordless"]
            friend_source_flags = js["friend_source_flags"]
            
    elif r2.status_code == 429:
            log().warning(f"Ratelimited | Try Again Later")
            time.sleep(3)
    print(f"""
{c.red}---[:Everything:]---{c.reset}
ID: {id}
Name: {username}#{discriminator}
Global Name: {global_name}
MFA: {mfa_enabled}
Locale: {locale}
Email: {email}
Verified: {verified}
Premium_Type: {premium_type}
Phone: {phone}
Avatar: https://cdn.discordapp.com/avatars/{id}/{avatar}
Banner: https://cdn.discordapp.com/banners/{id}/{banner}
Accent: {accent_color}
Avatar_Decoration: {avatar_decoration}
Banner_Color: {banner_color}
Flags: {flags}
Public_Flags: {public_flags}
Purchased_Flags: {purchased_flags}
Premium_Flags: {premium_usage_flags}
NSFW: {nsfw_allowed}
Linked_Users: {linked_users}
Bio: {bio}
show_current_game: {show_current_game}
default_guilds_restricted: {default_guilds_restricted}
inline_attachment_media: {inline_attachment_media}
inline_embed_media: {inline_embed_media}
gif_auto_play: {gif_auto_play}
render_embeds: {render_embeds}
render_reactions: {render_reactions}
animate_emoji: {animate_emoji}
enable_tts_command: {enable_tts_command}
message_display_compact: {message_display_compact}
convert_emoticons: {convert_emoticons}
explicit_content_filter: {explicit_content_filter}
disable_games_tab: {disable_games_tab}
theme: {theme}
developer_mode: {developer_mode}
detect_platform_accounts: {detect_platform_accounts}
status: {status}
afk_timeout: {afk_timeout}
timezone_offset: {timezone_offset}
stream_notifications_enabled: {stream_notifications_enabled}
allow_accessibility_detection: {allow_accessibility_detection}
contact_sync_enabled: {contact_sync_enabled}
native_phone_integration_enabled: {native_phone_integration_enabled}
animate_stickers: {animate_stickers}
friend_discovery_flags: {friend_discovery_flags}
view_nsfw_guilds: {view_nsfw_guilds}
view_nsfw_commands: {view_nsfw_commands}
passwordless: {passwordless}
friend_source_flags: {friend_source_flags}
""")

def options():
    clear()
    opt = int(input(f"""
{c.red}What Do You Want To Do?{c.reset}
[{c.red}1{c.reset}] Get General Info
[{c.red}2{c.reset}] Get Settings Info
[{c.red}3{c.reset}] Get Guild List
[{c.red}4{c.reset}] Get Friend List
[{c.red}4{c.reset}] Get Everything
"""))
    if opt == 1:
        token_user_info()
    elif opt == 2:
        settings_info()
    elif opt == 3:
        guild_info()
    elif opt == 4:
        friend_info()
    elif opt == 5:
        everything()
    else:
        log.error(f"Invalid Option --> {opt}")
        time.sleep(3)
        options()

def main():
    clear()
    banner()
    credits()
    opt = input(f"""
{c.red}What Do You Want To Do?{c.reset}
[{c.red}1{c.reset}] Sniff a Token
[{c.red}2{c.reset}] Sniff an ID
""")
    if opt == "1":
        options()
    elif opt == "2":
        id_info()
    else:
        log.error(f"Invalid Option --> {opt}")
        time.sleep(3)
        main()

if __name__ == "__main__":
    main()
