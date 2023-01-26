import webbrowser as wb

def webauto():
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s' #Path for chrome
    URLS = (
        "udemy.com",
        "btse.com",
        "stackoverflow.com",
        "github.com"
        )

    for url in URLS:
        print("opening :" + url)
        wb.get(chrome_path).open(url)

webauto()