# Show touch inputs from remarkable in realtime

## Setup

### Set up hostname & passwordless SSH to your remarkable:

- Get IP & password from the tablet (Menu>Settings>Help>Copyright & Licenses>Bottom of page)
- The 10. address is USB & the 192. address is usually wifi. I've ony tested over USB.
- Set up the hostname on your computer (~/.ssh/config), see below.

```
  Host remarkable
    Hostname 10.11.99.1
    User root
    IdentityFile ~/.ssh/__YOUR_PRIVATE_KEY_FILE__
```

- Set up passwordless SSH `ssh-copy-id remarkable`

### Script configuration

If you follow the steps above there should be no configuration.

## Usage

If using python3, install dependencies `pip3 install -r requirements.txt`

- Plug your remarkable into your computer.
- Run the Script `python2 script.py`
- Close the script from the terminal `CMD+C`
- Then close the plot window
