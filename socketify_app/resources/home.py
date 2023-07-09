from socketify import Request, Response


def home(res: Response, _: Request):
    res.render("home.html", message="Hello from socketify app!")
