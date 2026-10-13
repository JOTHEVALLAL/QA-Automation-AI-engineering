"""Illustrative Kite Connect authentication flow.

DO NOT run with public or real credentials for portfolio demonstrations.
Requires the kiteconnect package and environment variables.
Never print tokens or store secrets in source control.
"""
import os

from kiteconnect import KiteConnect


def authenticate_and_check_profile():
    api_key = os.environ["KITE_API_KEY"]
    api_secret = os.environ["KITE_API_SECRET"]
    request_token = os.environ["KITE_REQUEST_TOKEN"]

    kite = KiteConnect(api_key=api_key)
    session = kite.generate_session(request_token, api_secret=api_secret)
    access_token = session["access_token"]
    kite.set_access_token(access_token)

    # Validation example: call an authenticated endpoint. The user-supplied
    # screenshots show generation, but do not establish this check was executed.
    profile = kite.profile()
    print("Authenticated profile request succeeded (demo code).")
    return {"authenticated": True, "profile_received": isinstance(profile, dict)}


if __name__ == "__main__":
    authenticate_and_check_profile()
