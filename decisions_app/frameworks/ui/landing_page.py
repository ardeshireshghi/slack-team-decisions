def get_landing_page_html():
    return f"""
            <html>
                <head>
                    <title>Slack Decisions App</title>
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <meta charset="UTF-8">
                    <style>
                        body {{
                            padding: 0;
                            margin: 0;
                            font-family: sans-serif;
                            color: #333;
                        }}

                        .page {{
                            height: 100vh;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            text-align: center;
                            flex-direction: column;
                            max-width: 90%;
                            width: 500px;
                            margin: 0 auto;
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
                        <h1>👍 Welcome to "Team decisions" page on Slack</h1>
                        <p>"Team Decisions" is a simple Slack app which helps organising Team decisions in a given Slack channel. Teams end up having a lot of conversations in Slack threads and it is very difficult to understand the outcomes of those chats. With this app, we solve that problem by tagging a message as a decision using the Slack command `/decision [message]` and also can always view published decisions using `/decision`.</p>
                        <a href="https://slack.com/oauth/v2/authorize?scope=commands%2Cusers%3Aread%2Cchat%3Awrite&amp;user_scope=search%3Aread&amp;redirect_uri=https%3A%2F%2Fdwbr9q1gs4.execute-api.eu-west-2.amazonaws.com%2Fapi%2Fv1%2Foauth_callback&amp;client_id=25240511685.3364093289046" style="align-items:center;color:#fff;background-color:#4A154B;border:0;border-radius:56px;display:inline-flex;font-family:Lato, sans-serif;font-size:18px;font-weight:600;height:56px;justify-content:center;text-decoration:none;width:276px"><svg xmlns="http://www.w3.org/2000/svg" style="height:24px;width:24px;margin-right:12px" viewBox="0 0 122.8 122.8"><path d="M25.8 77.6c0 7.1-5.8 12.9-12.9 12.9S0 84.7 0 77.6s5.8-12.9 12.9-12.9h12.9v12.9zm6.5 0c0-7.1 5.8-12.9 12.9-12.9s12.9 5.8 12.9 12.9v32.3c0 7.1-5.8 12.9-12.9 12.9s-12.9-5.8-12.9-12.9V77.6z" fill="#e01e5a"></path><path d="M45.2 25.8c-7.1 0-12.9-5.8-12.9-12.9S38.1 0 45.2 0s12.9 5.8 12.9 12.9v12.9H45.2zm0 6.5c7.1 0 12.9 5.8 12.9 12.9s-5.8 12.9-12.9 12.9H12.9C5.8 58.1 0 52.3 0 45.2s5.8-12.9 12.9-12.9h32.3z" fill="#36c5f0"></path><path d="M97 45.2c0-7.1 5.8-12.9 12.9-12.9s12.9 5.8 12.9 12.9-5.8 12.9-12.9 12.9H97V45.2zm-6.5 0c0 7.1-5.8 12.9-12.9 12.9s-12.9-5.8-12.9-12.9V12.9C64.7 5.8 70.5 0 77.6 0s12.9 5.8 12.9 12.9v32.3z" fill="#2eb67d"></path><path d="M77.6 97c7.1 0 12.9 5.8 12.9 12.9s-5.8 12.9-12.9 12.9-12.9-5.8-12.9-12.9V97h12.9zm0-6.5c-7.1 0-12.9-5.8-12.9-12.9s5.8-12.9 12.9-12.9h32.3c7.1 0 12.9 5.8 12.9 12.9s-5.8 12.9-12.9 12.9H77.6z" fill="#ecb22e"></path></svg>Add to Slack</a>
                        <footer class="footer">
                            <ul class="footer__links">
                                <li class="footer__link-item"><a href="/page/privacy">Privacy Policy</a></li>
                                <li class="footer__link-item"><a href="https://github.com/ardeshireshghi/slack-team-decisions/issues">Support</a></li>
                            </ul>
                        </footer>
                    </div>
                </body>
            </html>
        """
