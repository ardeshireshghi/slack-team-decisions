def get_404_page_html():
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
                            background-color: #3956ad;
                        }}

                        .page {{
                            height: 100vh;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            color: white;
                        }}

                        .footer {{
                            position: absolute;
                            min-height: 60px;
                            display: flex;
                            padding: 1rem 2rem;
                            color: white;
                            background-color: #3956ad;
                            bottom: 0;
                            width: 100%;
                            flex-direction: row;
                            justify-content: center;
                        }}

                        .footer__links {{
                            display: flex;
                            list-style: none;
                            gap: 1rem;
                            align-items: center;
                        }}

                        .footer__link-item a {{
                            color: white;
                            text-decoration: none;
                        }}
                    </style>
                </head>
                <body>
                    <div class="page">
                        <h1> 😕 Oops! We can not find the page you are looking for</h1>
                    </div>
                    <footer class="footer">
                        <ul class="footer__links">
                            <li class="footer__link-item"><a href="/page/privacy">Privacy Policy</a></li>
                            <li class="footer__link-item"><a href="https://github.com/ardeshireshghi/slack-team-decisions/issues">Support</a></li>
                        </ul>
                    </footer>
                </body>
            </html>
        """
