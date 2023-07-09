from socketify import App, Request, Response

from socketify_app.utils.jinja_templates import JinjaTemplate
from socketify_app.resources.home import home


def run(app: App) -> None:
    """
    Creates an instance of the socketify app.
    :param app: socketify App instance.
    :return: None
    """
    # configures the templates
    app.template(JinjaTemplate("./socketify_app/templates"))

    # configures the app routes
    app.get("/", home)

    @app.on_start
    def on_start():
        """
        Application startup callback.
        """
        print("Application is starting...")

    @app.on_shutdown
    def on_shutdown():
        """
        Application shutdown callback.
        """
        print("Application is shutting down...")

    @app.on_error
    def on_error(error: Exception, res: Response, req: Request):
        """
        Application error callback.
        """
        # logs the error
        print(f"ERROR: {error}")

        # response and request can be None if the error is in an async function
        if res:
            res.write_status(500)
            res.end("Internal Server Error")
