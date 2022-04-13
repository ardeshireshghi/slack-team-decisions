def get_join_app_html(user_name):
    return f"""
            <DOCTYPE html>
            <html>
                <head>
                    <title>Slack decisions app</title>
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <meta charset="UTF-8">
                    <style>
                        body {{
                            padding: 0;
                            margin: 0;
                            font-family: sans-serif;
                        }}

                        .page {{
                            height: 100vh;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            text-align: center;
                        }}
                    </style>
                </head>
                <body>
                    <div class="page">
                        <h1>👍 Thanks "{user_name}" for choosing "Team decisions" on Slack</h1>
                    </div>
                </body>
            </html>
        """
