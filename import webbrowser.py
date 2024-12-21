import webbrowser

# Replace with the path to the Microsoft Edge executable
edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"

# Register Edge as the browser
webbrowser.register("edge", None, webbrowser.BackgroundBrowser(edge_path))

# Open a URL in Edge
webbrowser.get("edge").open("https://www.example.com")
